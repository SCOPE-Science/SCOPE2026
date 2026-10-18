"""Exact rational checks for the polynomial modulo skew-map periodic-point theorem.

Run: python3 verify.py
All orbit coordinates and coefficients are fractions; no floating-point orbits.
"""
from fractions import Fraction as F
from itertools import product
from math import floor
from sympy import symbols, simplify, mobius, divisors, series


def frac(t):
    return t - t.numerator // t.denominator


def scalar_fixed_points(m, phase):
    """All solutions of v = {m*v+phase}, for positive integer m."""
    ans = []
    lo = phase.numerator // phase.denominator - 1
    for k in range(lo, lo + m + 3):
        x = (F(k) - phase) / F(m - 1)
        if 0 <= x < 1:
            ans.append(x)
    assert len(ans) == m - 1 and len(set(ans)) == len(ans)
    return ans


def scalar_base_periodic_points(e, r, n):
    """Enumerate all possible digit words of a rational noninteger beta map."""
    # Within 1<e<2 and 0<r<=2-e, there are only digit 0 and 1 branches.
    assert F(1)<e<F(2) and 0<r<=2-e
    roots = set()
    for w in product((0, 1), repeat=n):
        offset = F(0)
        for k in w:
            offset = e * offset + r - k
        z = -offset / (e**n - 1)
        if not (0 <= z < 1):
            continue
        t = z
        ok = True
        for k in w:
            q = e*t+r
            if q.numerator // q.denominator != k:
                ok = False
                break
            t = frac(q)
        if ok:
            assert t == z
            roots.add(z)
    return sorted(roots)


def map_step(x, y, z, a, c, e, b, d, r, gamma=2):
    return frac(a*x+b*y**gamma), frac(c*y+d*z**gamma), frac(e*z+r)


def orbit(p, n, params):
    ans = [p]
    for _ in range(n):
        ans.append(map_step(*ans[-1], *params))
    return ans


def complete_periodic_set(n, params, max_points=30000):
    a,c,e,b,d,r = params
    z0s = scalar_base_periodic_points(e,r,n)
    all_roots = set()
    for z0 in z0s:
        zorb = [z0]
        for j in range(n):
            zorb.append(frac(e*zorb[-1]+r))
        assert zorb[-1] == z0
        sy = sum((c ** (n-1-j)*d*zorb[j]**2 for j in range(n)),F(0))
        for y0 in scalar_fixed_points(c**n, sy):
            yorb=[y0]
            for j in range(n):
                yorb.append(frac(c*yorb[-1]+d*zorb[j]**2))
            assert yorb[-1] == y0
            sx = sum((a**(n-1-j)*b*yorb[j]**2 for j in range(n)),F(0))
            for x0 in scalar_fixed_points(a**n,sx):
                p=(x0,y0,z0)
                assert p not in all_roots
                all_roots.add(p)
                assert orbit(p,n,params)[-1] == p
                if len(all_roots)>max_points:
                    raise RuntimeError('unexpectedly many roots')
    assert len(all_roots)==(a**n-1)*(c**n-1)*len(z0s)
    return len(z0s), len(all_roots)


def main():
    # The source paper's example uses gains 2, 3, 1.7; here the additive input is fixed.
    params=(2,3,F(17,10),F(-1,5),F(6,5),F(1,5))
    print('Noninteger base, exact rational all-orbit checks:')
    for n in range(1,5):
        q,p=complete_periodic_set(n,params)
        print('period',n,'base fixed points',q,'three-dimensional fixed points',p)
    t,a,c,e=symbols('t a c e')
    rational = ((1-a*c*t)*(1-a*e*t)*(1-c*e*t)*(1-t))/((1-a*c*e*t)*(1-a*t)*(1-c*t)*(1-e*t))
    # Rational identity by logarithmic derivative: t*zeta'/zeta = Sum P_n t^n.
    lhs=simplify(t * rational.diff(t) / rational)
    rhs=sum(sign*k*t/(1-k*t) for sign,k in [
        (+1,a*c*e),(-1,a*c),(-1,a*e),(-1,c*e),(+1,a),(+1,c),(+1,e),(-1,F(1))])
    assert simplify(lhs-rhs)==0
    for A,C,E in [(2,3,2),(2,2,2),(3,4,5)]:
        for n in range(1,14):
            pn=(A**n-1)*(C**n-1)*(E**n-1)
            primitive = sum(int(mobius(d))*(A**(n//d)-1)*(C**(n//d)-1)*(E**(n//d)-1) for d in divisors(n))
            assert primitive>=0 and primitive % n==0
            assert (pn==sum(sum(int(mobius(k))*(A**(j//k)-1)*(C**(j//k)-1)*(E**(j//k)-1) for k in divisors(j)) for j in divisors(n)))
    # Test sharp strict/closed boundaries and the golden-ratio transition,
    # with exact rational parameters on both sides of the transition.
    tested = 0
    for E in (F(6,5), F(3,2), F(8,5), F(17,10), F(9,5)):
        lower = (1+E-E*E)/(E+1)
        upper = 1/(E+1)
        possible = (F(1,100), F(1,20), F(1,10), F(1,5),
                    F(3,10), lower, upper, (upper+lower)/2, 2-E)
        for R in possible:
            if not (0<R<=2-E):
                continue
            n1=len(scalar_base_periodic_points(E,R,1))
            n2=len(scalar_base_periodic_points(E,R,2))
            predicted = 2 if lower<R<=upper else 0
            assert n1==0 and n2==predicted, (E,R,n1,n2,predicted)
            tested+=1
    assert tested>=20
    print('Sharp phase boundaries:', tested, 'exact-rational configurations passed.')
    print('Symbolic zeta identity and 39 exact primitive-orbit integrality checks passed.')
    print('PASS')


if __name__ == '__main__':
    main()
