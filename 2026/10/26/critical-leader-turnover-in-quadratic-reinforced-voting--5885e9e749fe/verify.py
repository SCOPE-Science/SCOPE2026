#!/usr/bin/env python3
"""Finite checks for formulas used in a reinforced-voting leader theorem.

These checks do not establish the asymptotic probability-one statements;
those follow from the analytic proof in RESULT.md.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial, exp, lgamma, log, sqrt, ceil


def occupancies(n):
    c = Counter()
    for vote in product(range(n), repeat=n):
        x = [0] * n
        for v in vote:
            x[v] += 1
        c[tuple(x)] += 1
    return c


def second_factorial(n, j):
    if 2*j > n:
        return Fraction(0)
    ways = factorial(n) // (factorial(j)**2 * factorial(n - 2*j))
    return (Fraction(n*(n-1)*ways, n**(2*j))
            * Fraction(n-2, n)**(n-2*j))


def check_occupancy():
    checks = 0
    for n in range(2, 6):
        states = occupancies(n)
        assert sum(states.values()) == n**n
        for j in range(n + 1):
            got1 = Fraction(sum(w * sum(z == j for z in x)
                                for x, w in states.items()), n**n)
            want1 = Fraction(n * comb(n, j), n**j) * Fraction(n-1, n)**(n-j)
            assert got1 == want1, (n,j,'mean')
            got2 = Fraction(sum(w * (sum(z == j for z in x))
                                * (sum(z == j for z in x)-1)
                                for x,w in states.items()), n**n)
            assert got2 == second_factorial(n,j), (n,j,'factorial')
            checks += 2
        for x in states:
            assert sum(z*z for z in x) == n + 2*sum(z*(z-1)//2 for z in x)
            checks += 1
    print('Exact uniform-occupancy identity checks:', checks)


def check_round2():
    for n in [2,3,4]:
        states = occupancies(n)
        total = Fraction(0)
        for x, w in states.items():
            M = max(x)
            a = [i for i,v in enumerate(x) if v==M]
            b = [i for i,v in enumerate(x) if v==M-1]
            if not b:
                continue
            Q = sum(v*v for v in x)
            conditional = Fraction(0)
            for y, ways in states.items():
                if max(y[i] for i in b) <= max(y[i] for i in a):
                    continue
                prod = Fraction(1)
                for i in range(n):
                    if y[i]:
                        prod *= Fraction(x[i]**2, Q)**y[i]
                conditional += ways * prod
            total += Fraction(w, n**n) * conditional
        assert 0 <= total <= 1
        print(f'Exact strict-turnover probability for n={n}: {total} ({float(total):.8g})')


def poisson_tail(lam, k):
    assert k>=0 and lam>0
    p=exp(-lam + k*log(lam)-lgamma(k+1))
    tail=p
    steps=0
    while True:
        k+=1
        p *= lam/k
        tail+=p
        steps+=1
        if p < max(1e-308, tail*1e-13) and k>lam:
            break
        if steps>200000:
            raise RuntimeError('Poisson series tail did not converge')
    return min(1.0,tail)


def check_tail_geometry():
    for m in [100,200,400]:
        for r in [1,m,m*m]:
            mu=m*m/2
            nu=(m-1)**2/2
            L=log(r)+log(m)/4
            threshold=ceil(mu+sqrt(2*mu*L))
            p_top=poisson_tail(mu,threshold)
            p_low=poisson_tail(nu,threshold)
            s=ceil(r*m/log(m))
            assert 0<=p_top<=1 and 0<=p_low<=1
            assert p_low>0
            union_upper=min(1.0,r*p_top)
            no_low=exp(s*log(1-p_low)) if p_low<1 else 0
            assert 0<=union_upper<=1 and 0<=no_low<=1
            print(f'm={m:3d}, top group={r:7d}, lower group={s:9d}, '
                  f'union(top)≤{union_upper:.4g}, no lower exceed≤{no_low:.4g}')

if __name__=='__main__':
    check_occupancy()
    check_round2()
    check_tail_geometry()
    print('Finite verification completed; infinite limit uses the written proof.')
