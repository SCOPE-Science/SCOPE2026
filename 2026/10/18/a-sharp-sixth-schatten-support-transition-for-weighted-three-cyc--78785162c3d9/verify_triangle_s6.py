#!/usr/bin/env python3
"""Reproducible finite checks for the weighted three-cycle sixth Schatten moment.

This script checks finite arithmetic identities; the analytic proof of the
continuous optimization is independent of these diagnostics.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt

Z = (F(0), F(0))
ONE = (F(1), F(0))
I = (F(0), F(1))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def star(a):
    return (a[0], -a[1])


def mm(A, B):
    n = len(A)
    return [[sum_gauss(mul(A[i][k], B[k][j]) for k in range(n))
             for j in range(n)] for i in range(n)]


def sum_gauss(items):
    out = Z
    for x in items:
        out = add(out, x)
    return out


def sixth_trace(weights, t, phase):
    n = 3
    u = 1-t
    z = ONE if phase == 0 else I
    iz = star(z)
    S = [[F(0) for _ in range(n)] for _ in range(n)]
    for j, w in enumerate(weights):
        S[(j+1) % n][j] = F(w)
    A = [[add(mul((t, F(0)), mul(z, (S[i][j], F(0)))),
              mul((u, F(0)), mul(iz, (S[j][i], F(0)))))
          for j in range(n)] for i in range(n)]
    Ast = [[star(A[j][i]) for j in range(n)] for i in range(n)]
    H = mm(Ast, A)
    H3 = mm(mm(H, H), H)
    ans = sum_gauss(H3[i][i] for i in range(n))
    assert ans[1] == 0, ans
    return ans[0]


def polynomial(weights, t, phase):
    u = 1-t
    squares = [F(w*w) for w in weights]
    e1 = sum(squares)
    e2 = sum(squares[i]*squares[j] for i in range(3) for j in range(i+1,3))
    e3 = squares[0]*squares[1]*squares[2]
    c = t**6+u**6
    a = 3*(t*t+u*u)*(t*t-u*u)**2
    osc = F(1) if phase == 0 else F(-1)
    b = 3*c+6*t**3*u**3*osc
    return c*e1**3-a*e1*e2+b*e3


def face_min(t):
    u = 1-t
    c = t**6+u**6
    a = 3*(t*t+u*u)*(t*t-u*u)**2
    b = 3*c+6*t**3*u**3
    return min(c-a/F(3)+b/F(27),c-a/F(4))


def main():
    patterns = [(0,0,0),(1,0,0),(1,1,0),(1,1,1),
                (1,2,3),(2,3,4),(5,3,1)]
    ts = [F(0),F(1,6),F(1,4),F(2,5),F(1,2),F(3,4),F(1)]
    checked = 0
    for w,t,phase in product(patterns,ts,[0,1]):
        assert sixth_trace(w,t,phase) == polynomial(w,t,phase), (w,t,phase)
        checked += 1
    # The exact Schur inequality includes both equality families.
    for i in range(49):
        for j in range(49-i):
            x,y,z = F(i,48), F(j,48), F(48-i-j,48)
            e2=x*y+y*z+z*x
            assert 4*e2-9*x*y*z<=1
            if 4*e2-9*x*y*z==1:
                assert sorted([x,y,z]) in [[F(0),F(1,2),F(1,2)],
                                            [F(1,3)]*3]
    # Exhaustive rational-simplex diagnostics: grid minimum matches theorem.
    tested = 0
    for t in ts:
        u=1-t
        c=t**6+u**6
        a=3*(t*t+u*u)*(t*t-u*u)**2
        b=3*c+6*t**3*u**3
        bound=face_min(t)
        equals=False
        for i in range(49):
            for j in range(49-i):
                x,y,z=F(i,48),F(j,48),F(48-i-j,48)
                e2=x*y+y*z+z*x
                val=c-a*e2+b*x*y*z
                assert val>=bound,(t,i,j,val,bound)
                equals |= val==bound
                tested += 1
        assert equals
    qcrit=(3*sqrt(5)-5)/4
    rho=(1-sqrt(1-4*qcrit*qcrit))/(2*qcrit)
    tcrit=rho/(1+rho)
    assert 0.3597<tcrit<0.3598
    print('TRIANGLE_SIXTH_MOMENT_EXACT_CHECK_OK',
          'identities=',checked,'simplex_grid=',tested,
          'transition_t=',round(tcrit,12))


if __name__=='__main__':
    main()
