#!/usr/bin/env python3
"""Complementary exact finite checks for a staggered-field Ising ring's single-flip minima.
Requires Python 3 and SymPy. A finite check is not the all-size proof.
"""
import itertools
from math import comb
import sympy as sp

PAIRS = tuple(itertools.product((-1, 1), repeat=2))


def matrix(h, parity):
    a = sp.zeros(4)
    for i, (left, spin) in enumerate(PAIRS):
        for j, (spin2, right) in enumerate(PAIRS):
            if spin == spin2 and spin*(left+right+parity*h) >= 0:
                a[i,j] = 1
    return a


def transfer_count(n, h):
    assert n >= 4 and n % 2 == 0
    return int(sp.trace((matrix(h,1)*matrix(h,-1))**(n//2)))


def brute_count(n, h):
    count = 0
    for config in itertools.product((-1,1), repeat=n):
        if all(config[i]*(config[(i-1)%n]+config[(i+1)%n]
                          +((-1)**i)*h) >= 0 for i in range(n)):
            count += 1
    return count


def defect_allowed(config, h):
    """Check the combinatorial local forbidden-word characterization."""
    d = tuple(0 if config[i] == (-1)**i else 1 for i in range(len(config)))
    n = len(d)
    if h == 0:
        return all(not (d[(i-1)%n] == d[i] == d[(i+1)%n]) for i in range(n))
    if 0 < h < 2:
        return all(not (d[i] == d[(i+1)%n] == 1) and
                   not (d[(i-1)%n] == d[i] == d[(i+1)%n] == 0)
                   for i in range(n))
    if h == 2:
        return all(not (d[i] == d[(i+1)%n] == 1) for i in range(n))
    return all(x == 0 for x in d)


def perrin(n):
    a = [3, 0, 2]
    for k in range(3,n+1):
        a.append(a[k-2]+a[k-3])
    return a[n]


def resolved_formula(n, k):
    if not ((n+2)//3 <= k <= n//2):
        return 0
    return n * comb(k, n-2*k) // k


def resolved_brute(n, h):
    counts = {}
    for config in itertools.product((-1,1), repeat=n):
        if all(config[i]*(config[(i-1)%n]+config[(i+1)%n] +
                             ((-1)**i)*h) >= 0 for i in range(n)):
            k = sum(config[i] != (-1)**i for i in range(n))
            counts[k] = counts.get(k, 0) + 1
    return counts


def lucas(n):
    a, b = 2, 1
    for i in range(n):
        a,b = b,a+b
    return a


def expected(n, name):
    m=n//2
    if name=='zero': return lucas(n)+[2,-1,-1][m%3]
    if name=='weak': return perrin(n)
    if name=='critical': return lucas(n)
    if name=='strong': return 1
    raise ValueError(name)


def main():
    cases = [('zero',sp.Rational(0)),('weak',sp.Rational(1,2)),
             ('critical',sp.Rational(2)),('strong',sp.Rational(5,2))]
    chars = {
        'zero': '(zz**2-3*zz+1)*(zz**2+zz+1)',
        'weak': 'zz*(zz**3-2*zz**2+zz-1)',
        'critical': 'zz**2*(zz**2-3*zz+1)',
        'strong': 'zz**3*(zz-1)'}
    lam=sp.Symbol('zz')
    for name,h in cases:
        p = matrix(h,1)*matrix(h,-1)
        assert sp.expand(p.charpoly(lam).as_expr() - sp.sympify(chars[name])) == 0
        for n in range(4,19,2):
            if n <= 14:
                for conf in itertools.product((-1,1), repeat=n):
                    stable=all(conf[i]*(conf[(i-1)%n]+conf[(i+1)%n]+((-1)**i)*h)>=0 for i in range(n))
                    assert stable == defect_allowed(conf,h),(name,n,conf)
            b = brute_count(n,h)
            t = transfer_count(n,h)
            f = expected(n,name)
            assert b == t == f, (name,n,b,t,f)
        print(name, 'N=4,...,18:', [expected(n,name) for n in range(4,19,2)])
    for h in (sp.Rational(1,5),sp.Rational(7,4),sp.Rational(11,4)):
        regime='weak' if h<2 else 'strong'
        for n in range(4,15,2):
            assert brute_count(n,h)==expected(n,regime)
    for n in range(4,19,2):
        got=resolved_brute(n,sp.Rational(3,4))
        exp={k:resolved_formula(n,k) for k in range((n+2)//3,n//2+1)}
        assert got==exp,(n,got,exp)
        assert sum(exp.values())==perrin(n)
    q=sp.Matrix([[0,1,0],[1,0,1],[1,0,0]])
    assert sp.factor(q.charpoly(lam).as_expr())==lam**3-lam-1
    for n in range(4,31,2):
        assert sp.trace(q**n)==perrin(n)
    print('all exact finite checks passed, including magnetization-resolved counts')

if __name__ == '__main__': main()
