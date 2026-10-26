#!/usr/bin/env python3
"""Self-contained brute-force checks of the stated rook-graph dissociation formulas.
No external dependencies or precomputed enumerators are used.
"""
from collections import Counter
from math import factorial


def predicted(p, q):
    fac = factorial
    diss, maximal = Counter(), Counter()
    component_profiles = Counter()
    for a in range(p+1):
        for b in range(p//2+1):
            for c in range(min(p,q)+1):
                u = p - a - 2*b - c
                v = q - 2*a - b - c
                if u < 0 or v < 0:
                    continue
                count = fac(p)*fac(q)//(fac(u)*fac(v)*fac(a)*fac(b)*fac(c)*2**(a+b))
                # Division exact, since every component's labelled exponential structure is counted.
                assert fac(p)*fac(q) % (fac(u)*fac(v)*fac(a)*fac(b)*fac(c)*2**(a+b)) == 0
                k = 2*(a+b)+c
                diss[k] += count
                if (c == 0 and (u == 0 or v == 0)) or (c > 0 and u == v == 0):
                    maximal[k] += count
                component_profiles[(a,b,c,u,v)] = count
    return diss, maximal, component_profiles


def brute(p, q):
    n = p*q
    adj = [0]*n
    for r in range(p):
        for c in range(q):
            i = r*q+c
            adj[i] = sum(1<<j for j in range(n) if j!=i and (j//q == r or j%q==c))
    iss = bytearray(1<<n)
    diss, maximal = Counter(), Counter()
    for mask in range(1<<n):
        ok=True
        cand=mask
        while cand:
            bit = cand & -cand
            i = bit.bit_length()-1
            if (adj[i] & mask).bit_count()>1:
                ok=False; break
            cand ^= bit
        if ok:
            iss[mask]=1
            diss[mask.bit_count()] += 1
    for mask in range(1<<n):
        if not iss[mask]: continue
        # A downward-closed family: non-maximal iff some one-vertex extension exists.
        omitted = ((1<<n)-1)^mask
        is_max=True
        while omitted:
            bit=omitted & -omitted
            if iss[mask|bit]:
                is_max=False; break
            omitted ^= bit
        if is_max:
            maximal[mask.bit_count()] += 1
    return diss, maximal


def lower_maximal_formula(p,q):
    return p if p%2 == 0 or p==q else p+1


def maximum_formula(p,q):
    return min(2*p, 2*(p+q)//3)


def run():
    total_subsets = 0
    pairs = [(2,q) for q in range(2,7)] + [(3,q) for q in range(3,7)] + [(4,4),(4,5)]
    for p,q in pairs:
        expected, max_expected, _ = predicted(p,q)
        actual, max_actual = brute(p,q)
        assert actual == expected, ('all sets', p, q, actual, expected)
        assert max_actual == max_expected, ('maximal sets', p, q, max_actual, max_expected)
        assert max(expected) == maximum_formula(p,q), ('max size',p,q)
        assert min(max_expected) == lower_maximal_formula(p,q), ('lower maximal size',p,q)
        assert max(max_expected) == max(expected), ('maximal max', p,q)
        assert sum(expected.values()) == sum(actual.values())
        total_subsets += 2**(p*q)
        print(f'R_{{{p},{q}}} all={dict(sorted(actual.items()))}; maximal={dict(sorted(max_actual.items()))}')
    for p in range(2,32):
        for q in range(p, 2*p+8):
            expected, mx, _ = predicted(p,q)
            assert min(mx) == lower_maximal_formula(p,q),(p,q,'lower',min(mx))
            assert max(expected) == maximum_formula(p,q),(p,q,'upper',max(expected))
    print('BRUTE_FORCE_ALL_PASS',len(pairs),'boards',total_subsets,'vertex subsets')
    print('ARITHMETIC_PROFILES_ALL_PASS',sum(p+8 for p in range(2,32)),'additional pairs')

if __name__ == '__main__':
    run()
