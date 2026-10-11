#!/usr/bin/env python3
"""Finite exact root-of-unity pattern checks and direct cyclic/product-group DFTs."""
from fractions import Fraction
from itertools import product
from math import gcd, lcm, pi
from random import Random
import cmath


def atom(scale=1, turn=0):
    return (Fraction(scale), Fraction(turn) % 1)


def mul(a, b):
    return (a[0] * b[0], (a[1] + b[1]) % 1)


def inv(a):
    return (1 / a[0], (-a[1]) % 1)


def power(a, k):
    return (a[0] ** k, (a[1] * k) % 1)


def complex_value(a):
    return float(a[0]) * cmath.exp(2j * pi * float(a[1]))


def in_coset(r, alpha, m):
    v = mul(r, inv(alpha))
    return v[0] == 1 and (v[1] * m).denominator == 1


def closed_case(alpha, m):
    return power(alpha, m * m) == atom()


def cyclic_orbits(N, step):
    unseen = set(range(N))
    answer = []
    while unseen:
        start = min(unseen)
        C = []
        x = start
        while x in unseen:
            unseen.remove(x)
            C.append(x)
            x = (x + step) % N
        assert x == start
        answer.append(C)
    return answer


def admissible(C, labels, alpha, m):
    present = [x for x in C if x in labels]
    t = len(present)
    if t <= m - 2:
        return True
    if t == m - 1:
        return not closed_case(alpha, m)
    prod = power(alpha, m)
    for x in C:
        prod = mul(prod, atom(1, Fraction(labels[x], m)))
    return prod == atom()


def construct(orbits, successor, labels, alpha):
    """Build nonzero coefficient vector realizing a prescribed valid labeled pattern."""
    result = {}
    for C in orbits:
        m = len(C)
        assert admissible(C, labels, alpha, m)
        r = {x:mul(alpha, atom(1, Fraction(labels[x], m)))
             for x in C if x in labels}
        missing = [x for x in C if x not in labels]
        for x in missing[:-1]:
            r[x] = atom(7)
        if missing:
            prod_r = atom()
            for x in C:
                if x != missing[-1]:
                    prod_r = mul(prod_r, r[x])
            r[missing[-1]] = inv(prod_r)
        assert all(in_coset(r[x], alpha, m) == (x in labels) for x in C)
        prod_r = atom()
        for x in C:
            prod_r = mul(prod_r, r[x])
        assert prod_r == atom()
        result[C[0]] = atom()
        for x in C[:-1]:
            result[successor(x)] = mul(result[x], r[x])
        assert result[successor(C[-1])] == result[C[0]]
    return result


def verify_direct(orbits, successor, labels, alpha, freqs):
    f = construct(orbits, successor, labels, alpha)
    # The window c*delta_0+d*delta_a is chosen so alpha=-conj(c)/conj(d).
    c = 1 + 0j
    d = -1 / complex_value((alpha[0], (-alpha[1]) % 1))
    m = len(orbits[0])
    h = len(orbits)
    for C in orbits:
        for x in C:
            r = mul(f[successor(x)], inv(f[x]))
            if x in labels:
                assert r == mul(alpha, atom(1, Fraction(labels[x], m)))
            else:
                assert not in_coset(r, alpha, m)
            observed = set()
            expected = set()
            for frequency, angle, root_index in freqs:
                if x in labels and root_index == labels[x]:
                    expected.add(frequency)
                z = complex_value(f[x]) * c.conjugate() + (
                    complex_value(f[successor(x)]) * d.conjugate()
                    * cmath.exp(-2j * pi * float(angle)))
                if abs(z) < 1e-9 * max(abs(complex_value(f[x]) * c.conjugate()),
                                       abs(complex_value(f[successor(x)]) * d.conjugate())):
                    observed.add(frequency)
            assert observed == expected, (x, labels, observed, expected)
            assert len(observed) == (h if x in labels else 0)


def test_cyclic():
    checked = 0
    checked_direct = 0
    exact_counts = 0
    for N in range(2, 8):
        for step in range(1, N):
            m = N // gcd(N, step)
            h = N // m
            C = cyclic_orbits(N, step)
            alpha_values = [atom(), atom(2), atom(1, Fraction(1, m * m)),
                            atom(1, Fraction(1, m * m * m))]
            fqs = [(k, Fraction(k * step, N) % 1,
                    (k * (step // gcd(N, step))) % m)
                   for k in range(N)]
            for alpha in alpha_values:
                if N <= 5:
                    patterns = product(range(-1, m), repeat=N)
                else:
                    rng = Random(22 + 100 * N + step)
                    patterns = ([rng.randrange(-1, m) for _ in range(N)]
                                for _ in range(220))
                admissible_number = 0
                for count, pat in enumerate(patterns):
                    labels = {x:q for x,q in enumerate(pat) if q >= 0}
                    ok = all(admissible(c, labels, alpha, m) for c in C)
                    checked += 1
                    if ok:
                        admissible_number += 1
                        f = construct(C, lambda x:(x+step)%N, labels, alpha)
                        assert all(x in f and f[x][0] != 0 for x in range(N))
                        if N<=4 or count%23==0:
                            verify_direct(C,lambda x:(x+step)%N,labels,alpha,fqs)
                            checked_direct += 1
                if N <= 5:
                    count_cycle = ((m + 1)**m - 2*m**m + m**(m-1)) if closed_case(alpha,m) else ((m+1)**m-m**m)
                    assert admissible_number == count_cycle ** h, (N,step,alpha,admissible_number,count_cycle**h)
                    exact_counts += 1
    return checked,checked_direct,exact_counts


def test_product_groups():
    rng = Random(42)
    checked = 0
    for u,v in [(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)]:
        points = list(product(range(u),range(v)))
        for a in points[1:]:
            if a == (0,0):continue
            m = lcm(u//gcd(u,a[0]), v//gcd(v,a[1]))
            h = u*v//m
            unseen = set(points)
            cycles=[]
            def successor(x): return ((x[0]+a[0])%u,(x[1]+a[1])%v)
            while unseen:
                start=min(unseen)
                orbit=[]; x=start
                while x in unseen:
                    unseen.remove(x);orbit.append(x);x=successor(x)
                assert x==start and len(orbit)==m
                cycles.append(orbit)
            assert len(cycles)==h
            freqs = [((k,l),Fraction(k*a[0],u)+Fraction(l*a[1],v),
                      (m*(Fraction(k*a[0],u)+Fraction(l*a[1],v)))%m)
                     for k,l in points]
            assert all(isinstance(label,int) or label.denominator==1 for _,_,label in freqs)
            for alpha in [atom(),atom(2),atom(1,Fraction(1,m*m))]:
                for _ in range(10):
                    labels = {x:rng.randrange(m) for x in points if rng.randrange(4) != 0}
                    # Force an all-good cycle into the admissible character-product class.
                    for C in cycles:
                        if len([x for x in C if x in labels]) == m and closed_case(alpha,m):
                            prod_r=power(alpha,m)
                            for x in C[:-1]:
                                prod_r=mul(prod_r,atom(1,Fraction(labels[x],m)))
                            need=inv(prod_r)
                            assert need[0]==1 and (need[1]*m).denominator==1
                            labels[C[-1]]=int((need[1]*m)%m)
                    if all(admissible(C,labels,alpha,m) for C in cycles):
                        verify_direct(cycles,successor,labels,alpha,freqs)
                        checked+=1
    return checked


def main():
    # Verify local pattern-count identities for every small step order.
    for m in range(2, 24):
        a=sum(__import__('math').comb(m,t)*m**t for t in range(m-1))
        assert a+m**(m-1)==(m+1)**m-2*m**m+m**(m-1)
        assert a+m*m**(m-1)==(m+1)**m-m**m
    observed,direct,counts=test_cyclic()
    group_direct=test_product_groups()
    print('VERIFY_OK',f'cyclic_labeled_cases={observed}',f'cyclic_direct_DFT={direct}',
          f'exhaustive_cardinality_cases={counts}',f'product_group_direct_DFT={group_direct}',
          'exact_root_cosets=PASS', 'holonomy=PASS','pattern_count=PASS')

if __name__=='__main__':main()
