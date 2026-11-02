"""Exact checks for the facet transition theorem, using rational arithmetic.

Finite tests only; the dimension-uniform proof is in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import comb


def analytic(n, t):
    t = Fraction(t)
    assert n >= 4 and t > 0
    if t >= n-1:
        return 2**(n-1)
    weights = [Fraction(1)] * (n-1) + [t]
    a = 0
    b = 0
    for signs in product((-1, 1), repeat=n-1):
        s = sum(signs)
        if abs(s) < t:
            a += 1
    for signs in product((-1, 1), repeat=n-2):
        s = sum(signs)
        if abs(s+t) < 1:
            b += 2*(n-1)
    c = 0
    for signs in product((-1, 1), repeat=n-1):
        if sum(signs) == t:
            c += 2
    return a + b + c


def closed(n, t):
    t = Fraction(t)
    assert n >= 4 and t > 0
    if t >= n - 1:
        return 2**(n-1)
    if n % 2 == 0:
        h = (n-2)//2
        for j in range(h+1):
            critical=2*j+1
            if t == critical:
                return 2*sum(comb(2*h+1,h+r) for r in range(1,j+2))
            if 2*j-1 < t < 2*j+1:
                return (2*sum(comb(2*h+1,h+r) for r in range(1,j+1))
                        +2*(2*h+1)*comb(2*h,h-j))
    else:
        h=(n-1)//2
        for j in range(h):
            if 2*j < t < 2*j+2:
                return (comb(2*h,h) + 2*sum(comb(2*h,h+r) for r in range(1,j+1))
                        +4*h*comb(2*h-1,h-1-j))
            if t == 2*j+2:
                return (comb(2*h,h)
                        +2*sum(comb(2*h,h+r) for r in range(1,j+2)))
    raise AssertionError((n,t))


def brute(n, t):
    weights = [Fraction(1)]*(n-1) + [Fraction(t)]
    V = set()
    for free in range(n):
        fixed=[i for i in range(n) if i != free]
        for signs in product((-1, 1), repeat=n-1):
            x=[Fraction(0)]*n
            for i,s in zip(fixed, signs):
                x[i]=weights[i]*s
            x[free]=-sum(x)
            if abs(x[free]) <= weights[free]:
                V.add(tuple(x))
    if t < n-1:
        # A facet of the primal space has one edge-molecule vertex per
        # tight edge inequality of its exposing Lipschitz potential.
        nonsimplicial=sum(sum(abs(x[i]) == weights[i] for i in range(n))==n for x in V)
    else:
        nonsimplicial=0
    return len(V), nonsimplicial


def critical_nonsimplicial(n,t):
    t=Fraction(t)
    if t >= n-1 or t <= 0 or t.denominator!=1 or (int(t)-(n-1))%2:
        return 0
    return 2*comb(n-1,(n-1+int(t))//2)


def main():
    tests=0
    for n in range(4,12):
        ts=set(Fraction(k, 4) for k in range(1,4*(n+1)+1))
        ts.update(Fraction(k,3) for k in range(1,3*(n+1)+1))
        for t in sorted(ts):
            a, c = analytic(n,t), closed(n,t)
            b, ns = brute(n,t)
            assert a==b==c and ns==critical_nonsimplicial(n,t), (n,t,a,b,c,ns)
            tests+=1
        if n % 2 == 0:
            t=Fraction(1)
            assert closed(n,t) == comb(n,n//2)
            assert closed(n,Fraction(3,4)) == (n//2)*comb(n,n//2)
            assert closed(n,Fraction(5,4)) == (n//2)*comb(n,n//2)
            global_max=(n//2)*comb(n,n//2)
        else:
            global_max=n*comb(n-1,(n-1)//2)
            assert closed(n,Fraction(1)) == global_max
        assert max(closed(n,Fraction(k,10)) for k in range(1,10*(n+1))) == global_max
    print(f'VERIFY_OK exact_rational_grid_cases={tests} dimensions=4..11; independent vertex enumeration, sign-count formula, closed binomial formula, maxima')

if __name__=='__main__':
    main()
