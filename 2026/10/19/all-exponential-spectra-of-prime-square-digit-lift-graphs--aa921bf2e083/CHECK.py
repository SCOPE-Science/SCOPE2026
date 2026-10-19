#!/usr/bin/env python3
"""Exact cyclotomic checks for prime-square digit-lift Fourier spectra.
No floating-point arithmetic or external packages are required.
"""
from itertools import combinations, product
from math import isqrt
from collections import Counter


def points(p, h):
    return {(r + p*s, r + p*h[r]) for r in range(p) for s in range(p)}


def cyclotomic_zero(p, exponents):
    # A sum of p^2-th roots vanishes iff coefficient multiplicities
    # are constant along every congruence class modulo p.
    counts = Counter(e % (p*p) for e in exponents)
    return all(len({counts[r + p*t] for t in range(p)}) == 1
               for r in range(p))


def mask_zero(p, h, u, v):
    return cyclotomic_zero(p, [u*x + v*y for x,y in points(p,h)])


def predicted_zero(p, u, v):
    return ((u % p) != 0 or
            ((v % p) == 0 and ((u+v)//p) % p != 0))


def spectral_pair(p, h, spectrum):
    return len(spectrum) == p*p and all(mask_zero(p,h,(u1-u2)%(p*p),(v1-v2)%(p*p))
                                       for (u1,v1),(u2,v2) in combinations(spectrum,2))


def spectrum(p, c, funcs):
    return {(a+p*funcs[a][t], c[a]+p*((t-funcs[a][t])%p))
            for a in range(p) for t in range(p)}


def is_prime(n):
    return n >= 2 and all(n%d for d in range(2,isqrt(n)+1))


def run():
    import random
    rng = random.Random(260816)
    tests=0
    for p in (2,3,5,7):
        assert is_prime(p)
        hs = [tuple(0 for _ in range(p)), tuple((r**p-r)//p % p for r in range(p)),
              tuple(r*r%p for r in range(p)),tuple(rng.randrange(p) for _ in range(p))]
        zeros = 0
        for h in dict.fromkeys(hs):
            assert len(points(p,h)) == p*p
            for u,v in product(range(p*p), repeat=2):
                actual=mask_zero(p,h,u,v)
                expect=predicted_zero(p,u,v)
                assert actual == expect, (p,h,u,v,actual,expect)
                tests += 1
                if actual: zeros += 1
            c=tuple(rng.randrange(p) for _ in range(p))
            f=tuple(tuple(rng.randrange(p) for _ in range(p)) for _ in range(p))
            sp=spectrum(p,c,f)
            assert spectral_pair(p,h,sp)
            tests += len(sp)*(len(sp)-1)//2
        print(f'p={p}: Fourier mask agrees at every frequency for {len(dict.fromkeys(hs))} graphs; generated bases orthogonal')
    # Exhaustively enumerate all 4-point spectra in the 16-element dual group.
    p=2
    allfreq=list(product(range(p*p),repeat=2))
    for h in product(range(p), repeat=p):
        actual={frozenset(B) for B in combinations(allfreq,p*p)
                if spectral_pair(p,h,B)}
        expected={frozenset(spectrum(p,c,funcs))
                  for c in product(range(p),repeat=p)
                  for values in product(range(p),repeat=p*p)
                  for funcs in [tuple(tuple(values[a*p+t] for t in range(p)) for a in range(p))]}
        assert actual == expected and len(actual)==p**(p*p+p), (p,h,len(actual),len(expected))
        tests += len(actual)
    print('p=2: all 1,820 four-frequency subsets classified for each of the 4 graph lifts; 64 spectra per graph')
    print(f'TOTAL exact checks (frequencies, orthogonal pairs, and small spectra): {tests}')
    print('PASS')

if __name__=='__main__':
    run()
