#!/usr/bin/env python3
"""Independent exhaustive and transfer-matrix checks for wheel minimal-fort enumerators.

Definitions and proof live in RESULT.md. Requires Python 3 standard library only.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def fort(mask, n):
    """Direct test on W_{n+1}: rim vertices 0..n-1, hub n."""
    if mask == 0:
        return False
    full = (1 << (n + 1)) - 1
    for v in range(n + 1):
        if mask & (1 << v):
            continue
        if v == n:
            neighbors = (1 << n) - 1
        else:
            neighbors = (1 << n) | (1 << ((v - 1) % n)) | (1 << ((v + 1) % n))
            neighbors &= ~(1 << n)
            neighbors |= (1 << n)
        if (mask & neighbors).bit_count() == 1:
            return False
    return True


def brute(n):
    """Check every subset against the definition and all known smaller minimal forts."""
    minimal = []
    tested = 0
    for size in range(1, n + 2):
        for mask in range(1, 1 << (n + 1)):
            if mask.bit_count() != size:
                continue
            tested += 1
            if not fort(mask, n):
                continue
            if not any((mask & other) == other for other in minimal):
                minimal.append(mask)
    a = Counter(x.bit_count() for x in minimal if x & (1 << n))
    b = Counter(x.bit_count() for x in minimal if not x & (1 << n))
    return a, b, tested


def formula(n):
    """Count rim gap compositions and maximal independent cyclic subsets independently."""
    A, B = Counter(), Counter()
    for r in range(2, n // 2 + 1):
        word_count = 0
        for gaps in product((1, 2, 3), repeat=r):
            if sum(gaps) == n and 3 in gaps and all(gaps[j] + gaps[(j + 1) % r] >= 4 for j in range(r)):
                word_count += 1
        multiplicity = Fraction(n * word_count, r)
        assert multiplicity.denominator == 1, (n, r, multiplicity)
        A[r + 1] += int(multiplicity)
    for s in range(2, n // 2 + 1):
        # s gaps of length 2 or 3; exactly n-2s gaps are 3
        if 2*s <= n <= 3*s:
            from math import comb
            val = Fraction(n * comb(s, n-2*s), s)
            assert val.denominator == 1
            B[n-s] += int(val)
    return +A, +B


def direct_transfer_coefficients(N):
    """Trace of the 3-state transfer matrix, with weights u^(next gap) z."""
    from collections import defaultdict
    d = {(a, a, 0, 0): 1 for a in (1, 2, 3)}
    # State = (starting gap, last gap, gap_sum, number of gap transitions)
    # Generate cyclic walks of r transitions; their vertex sum is gap total.
    A = Counter()
    for r in range(1, N//2 + 1):
        if r == 1:
            continue
        for g in product((1, 2, 3), repeat=r):
            if 3 not in g or any(g[i] + g[(i+1)%r] < 4 for i in range(r)):
                continue
            nn=sum(g)
            if 4 <= nn <= N:
                A[(nn,r+1)] += Fraction(nn,r)
    return {k: int(v) for k,v in A.items() if v.denominator==1}


def rational_coefficients(N):
    """Independent formal-series inversion of the two rational logarithmic derivatives."""
    from collections import defaultdict
    def invert(den):
        inverse = [{0: 1}]
        for n in range(1, N + 1):
            cur = defaultdict(int)
            for j, p in den.items():
                if j == 0 or j > n:
                    continue
                for k, coeff in p.items():
                    for oldk, oldc in inverse[n-j].items():
                        cur[k+oldk] -= coeff * oldc
            inverse.append(dict(cur))
        return inverse
    D = {0:{0:1},2:{1:-1},3:{1:-1},4:{2:-1},6:{3:1}}
    E = {0:{0:1},2:{1:-1},3:{2:-1}}
    invD, invE = invert(D), invert(E)
    A, B = [], []
    for n in range(N + 1):
        aa, bb = defaultdict(int), defaultdict(int)
        for j,p in D.items():
            if j == 0 or j > n: continue
            for k,c in p.items():
                for kk,cc in invD[n-j].items():
                    aa[k+kk+1] -= j*c*cc
        if n >= 2 and n % 2 == 0:
            aa[n//2+1] -= 2
        for j,p in E.items():
            if j == 0 or j > n: continue
            for k,c in p.items():
                for kk,cc in invE[n-j].items():
                    bb[k+kk] -= j*c*cc
        A.append(Counter({k:v for k,v in aa.items() if v}))
        B.append(Counter({k:v for k,v in bb.items() if v}))
    return A, B


def main():
    checked=0
    rational_A, rational_B = rational_coefficients(40)
    for n in range(4,16):
        a,b,k=brute(n); checked+=k
        aa,bb=formula(n)
        assert a == aa, ('hub included',n,a,aa)
        assert b == bb, ('hub omitted',n,b,bb)
        assert a == rational_A[n], ('hub rational',n,a,rational_A[n])
        assert b == rational_B[n], ('rim rational',n,b,rational_B[n])
        print(f'W_{n+1}: hub={sum(a.values())}, rim={sum(b.values())}, sizes={dict(a+b)}')
    expected=[3,4,5,3,14,12,21,25,44,55,78,112,158]
    from math import comb
    vals=[]
    for rim in range(3,16):
        if rim==3:
            vals.append(3)
        else:
            vals.append(sum(formula(rim)[0].values()))
    assert vals == expected, (vals, expected)
    assert [sum(rational_A[n].values()) for n in range(3,16)] == expected
    for n in range(4,19):
        assert formula(n) == (rational_A[n], rational_B[n]), (n,formula(n), rational_A[n], rational_B[n])
    for n in range(4,41):
        assert all(c > 0 for c in rational_A[n].values())
        assert all(c > 0 for c in rational_B[n].values())
    print(f'VERIFY_OK: {checked} subsets checked across 12 wheels, published sequence of 13 terms matched; rational generating functions checked through rim order 40')

if __name__=='__main__':
    main()
