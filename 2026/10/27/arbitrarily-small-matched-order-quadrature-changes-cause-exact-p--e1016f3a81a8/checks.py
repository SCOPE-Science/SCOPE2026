#!/usr/bin/env python3
"""Exact-rational checks of the one-node HJB quadrature-dynamics formulas."""
from fractions import Fraction as Q


def left_phi(x):
    assert 0 < x < 1
    return x


def right_phi(x):
    assert 1 < x < 2
    return 2 - x


def f0_at_nodes(x, center):
    # Locally f_0=2+(x-center)^2; a fixed smooth extension exists.
    return 2 + (x - center) ** 2


def b1_at_left_nodes(x):
    # Locally b_1=2-4(x-1/2)^2; zero throughout the right cell.
    return 2 - 4 * (x - Q(1, 2)) ** 2


def assemble(e):
    half = Q(1, 2)
    left = [half-e, half+e]
    right = [Q(3, 2)-e, Q(3, 2)+e]
    assert all(0 < x < 1 for x in left)
    assert all(1 < x < 2 for x in right)
    qf0 = sum((f0_at_nodes(x, half)*left_phi(x) for x in left), Q(0)) / 2
    qf0 += sum((f0_at_nodes(x, Q(3, 2))*right_phi(x) for x in right), Q(0)) / 2
    qb1 = sum((b1_at_left_nodes(x)*left_phi(x) for x in left), Q(0)) / 2
    return qf0, qb1


def nonlinear_residual(a, t):
    return 2*(a-1)-t + (1-2*t)*max(a-1,Q(0))


def residual_step(a, t):
    return a - nonlinear_residual(a,t) / (3 if a > 1 else 2)


def nonresidual_step(a,t):
    return (1-t/Q(3)) if a > 1 else (1+t/Q(2))


def test(e):
    t=e*e
    assert Q(0)<e<Q(1,16)
    f0,b1=assemble(e)
    assert (f0,b1)==(2+t,1-2*t), (f0,b1)
    lo,hi=1-t/Q(3),1+t/Q(2)
    assert lo<1<hi
    assert nonresidual_step(lo,t)==hi
    assert nonresidual_step(hi,t)==lo
    assert hi-lo==Q(5,6)*t
    assert nonlinear_residual(lo,t)==-Q(5,3)*t
    assert 2*(lo-1)==-Q(2,3)*t
    assert nonlinear_residual(hi,t)==t/Q(2)-t*t
    assert 3*(hi-1)==Q(3,2)*t
    fixed=1 + t/(3-2*t)
    assert nonlinear_residual(fixed,t)==0
    assert residual_step(fixed,t)==fixed
    ratio=Q(2,3)*t
    for a in (Q(-10),Q(0),Q(1,2),Q(1),Q(5,4),Q(17)):
        cur=residual_step(a,t)
        assert cur>1
        for _ in range(5):
            nxt=residual_step(cur,t)
            assert nxt-fixed==ratio*(cur-fixed)
            cur=nxt
    # Matched assembly: f0=2, b1=1, both policy roots equal 1.
    assert Q(2)/2==Q(3)/3==1
    return f0,b1,lo,hi,ratio


def main():
    for e in [Q(1,2**k) for k in range(5,13)]:
        print('eps=',e,'data/cycle/rate=',test(e))
    print('PASS: 8 rational offsets; exact quadrature, cycles, nonlinear residual, contraction, matching case')


if __name__=='__main__':
    main()
