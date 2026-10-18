"""Reproducibility checks for a triangle's side-stratified inclusion-depth law.

Run: python3 checker.py. Uses only the Python standard library.
Finite checks corroborate, but do not replace, the proof in RESULT.md.
"""
import math
import random


def phi(t):
    if t <= 0.0 or t >= 1.0:
        return 0.0
    return t*(1-t)*math.log((1-t)/t)


def depth(bary):
    assert len(bary) == 3
    assert all(0 <= t <= 1 for t in bary)
    assert abs(sum(bary) - 1.0) < 1e-12
    return sum(phi(t) for t in bary)


def corner_exact(x, y):
    assert x > 0 and y > 0 and x+y < 1
    return 1 - x - y - x*y*math.log(((1-x)*(1-y))/(x*y))


def simpson(f, lo, hi, n=2000):
    assert n % 2 == 0
    step=(hi-lo)/n
    return step/3.0*(f(lo)+f(hi)+4*sum(f(lo+step*j) for j in range(1,n,2)) +2*sum(f(lo+step*j) for j in range(2,n,2)))


def inside_side_triangle(u, v, w, px, py):
    # Host vertices (0,0), (1,0), (0,1); side sample points
    # X=(u,0), Y=(1-v,v), Z=(0,w).
    c1 = (1-v-u)*py - v*(px-u)
    c2 = -(1-v)*(py-v) - (w-v)*(px-(1-v))
    c3 = u*(py-w) + w*px
    return c1 >= 0 and c2 >= 0 and c3 >= 0


def derivative(t):
    return (1-2*t)*math.log((1-t)/t)-1


def main():
    assert abs(depth((1/3,1/3,1/3)) - 2*math.log(2)/3) < 2e-15
    for x,y in [(.1,.15),(.3,.3),(.05,.64),(.47,.12),(.14,.2),(.3,.68)]:
        left=x/(1-y)
        numerical=simpson(lambda u: 1-y*u/(u-x),left,1,2000)
        exact=corner_exact(x,y)
        assert abs(exact-numerical)<5e-9,(x,y,exact,numerical)
    print('six corner integrals: pass')

    rng=random.Random(910471)
    for bary in [(1/3,1/3,1/3),(.6,.25,.15),(.8,.1,.1),(.11,.83,.06)]:
        n=180000
        count=sum(inside_side_triangle(rng.random(),rng.random(),rng.random(),bary[1],bary[2]) for _ in range(n))
        observed=count/n
        expected=depth(bary)
        assert abs(observed-expected)<0.011,(bary,observed,expected)
        print('inclusion:',bary,'observed',round(observed,6),'predicted',round(expected,6))

    # Strict Schur direction, with positive third coordinate, checked numerically.
    for k in range(1,100):
        smaller=k/1000
        for j in range(k+1,900,7):
            larger=j/1000
            if larger+smaller>=.999:
                continue
            assert derivative(larger)<derivative(smaller)+1e-11,(smaller,larger)
    print('strict Schur pairwise derivative tests: pass')

    # Integral over the normalized triangle uses density 2 on the simplex.
    n=600
    approx=simpson(lambda a: 2*(1-a)*phi(a),0,1,n)
    assert abs(3*approx-.25)<2e-5,(3*approx)
    print('spatial mean 1/4: pass')

    for q in [.1,.2,.5,.8,.9]:
        eps=1e-6
        bary=(1-eps,eps*q,eps*(1-q))
        quotient=depth(bary)/eps
        entropy=-q*math.log(q)-(1-q)*math.log(1-q)
        assert abs(quotient-entropy)<.0002,(q,quotient,entropy)
    print('directional binary-entropy vertex limits: pass')
    print('ALL CHECKS PASSED')


if __name__=='__main__':
    main()
