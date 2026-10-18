#!/usr/bin/env python3
"""Independent exact finite checks of even-semiprime cyclotomic node census.

Uses only the Python standard library; no floating-point arithmetic.
"""
from itertools import product
from math import factorial, comb


def weak_compositions(total, slots):
    if slots == 1:
        yield (total,)
    else:
        for n in range(total + 1):
            for r in weak_compositions(total-n, slots-1):
                yield (n,) + r


def formula_nodes(p, N):
    assert p % 2 == 1 and p >= 3
    numerator = 0
    for k in range(-N // p - 1, N // p + 2):
        remaining = N - p * abs(k)
        if remaining < 0 or remaining % 2:
            continue
        for amounts in weak_compositions(remaining // 2, p):
            denom = 1
            for a in amounts:
                denom *= factorial(a) * factorial(a + abs(k))
            numerator += factorial(N) // denom
    assert numerator % (2*p) == 0
    return numerator // (2*p)


def orbit_formula(p, N):
    value=0
    for k in range(N//p+1):
        rem=N-p*k
        if rem%2: continue
        a=rem//2
        fixed=1 if a%p==0 else 0
        term=(comb(a+p-1,p-1)+(p-1)*fixed)
        assert term%p==0
        value+=term//p
    return value


def brute_nodes(p, N):
    # root codes 0...p-1 mean +zeta^j; p...2p-1 mean -zeta^j.
    # Every projective node has a unique representative with first root 1.
    count = 0
    rational = 0
    orbit_types = set()
    for codes in product(range(2*p), repeat=N-1):
        d = [0] * p
        d[0] = 1
        for v in codes:
            if v < p:
                d[v] += 1
            else:
                d[v-p] -= 1
        if min(d) != max(d):
            continue
        count += 1
        multiplicities=[0]*(2*p)
        multiplicities[0]=1
        for v in codes: multiplicities[v]+=1
        orbit=[]
        for shift in range(p):
            for flip in range(2):
                v=[0]*(2*p)
                for j in range(p):
                    for sign in range(2):
                        v[(sign^flip)*p+(j+shift)%p]=multiplicities[sign*p+j]
                orbit.append(tuple(v))
        orbit_types.add(min(orbit))
        # Galois fixed by any nontrivial group element iff all ratios are +/-1.
        if all(v in (0,p) for v in codes):
            rational += 1
    return count, rational, len(orbit_types)


def main():
    for p, Ns in ((3, (5,6,7,8)), (5, (5,6))):
        for N in Ns:
            formula = formula_nodes(p,N)
            brute, rat, orbit_count = brute_nodes(p,N)
            assert orbit_count == orbit_formula(p,N), (p,N,orbit_count,orbit_formula(p,N))
            assert formula == brute, (p,N,formula,brute)
            target_rat = comb(N,N//2)//2 if N%2==0 else 0
            assert rat == target_rat, (p,N,rat,target_rat)
            assert (brute-rat) % (p-1) == 0
            print('p=%d N=%d geometric_nodes=%d rational_nodes=%d degree_%d_closed_nodes=%d S_N_orbits=%d' %
                  (p,N,brute,rat,p-1,(brute-rat)//(p-1),orbit_count))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
