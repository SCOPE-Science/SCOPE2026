"""Independent finite enumerations for a co-rank-one nilpotent enumeration theorem.

Run: python verify.py
Standard library only. Finite checks corroborate but do not prove the theorem.
"""
from collections import Counter
from itertools import combinations_with_replacement
from math import comb


def is_nilpotent(mapping, n):
    """Return True precisely when all trajectories leave the domain."""
    for x in mapping:
        seen = set()
        while x in mapping:
            if x in seen:
                return False
            seen.add(x)
            x = mapping[x]
    return True


def formula(n, r):
    if n < 2 or r < 1 or r >= n:
        return 0
    v = 2 * comb(n, r + 1) * comb(n - 1, r - 1)
    assert v % (n - 1) == 0
    return v // (n - 1)


def narayana(s, k):
    if s < 1 or k < 1 or k > s:
        return 0
    numerator = comb(s, k) * comb(s, k-1)
    assert numerator % s == 0
    return numerator // s


def side_poly(s):
    if s == 0:
        return [1]
    return [narayana(s,k) for k in range(1,s+1)]


def convolution(a,b):
    ans = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            ans[i+j] += x*y
    return ans


def theoretical_by_missing(n, m):
    p = convolution(side_poly(m-1), side_poly(n-m))
    return Counter({r:v for r,v in enumerate(p,start=1) if v})


def enumerate_n(n):
    combined = Counter()
    for m in range(1, n+1):
        domain = tuple(i for i in range(1,n+1) if i != m)
        ranks = Counter()
        for image in combinations_with_replacement(range(1,n+1), n-1):
            mapping = dict(zip(domain,image))
            nil = is_nilpotent(mapping,n)
            fixed_free = all(mapping[i] != i for i in mapping)
            # This property is used only as an independently checked lemma.
            assert nil == fixed_free
            if nil:
                r = len(set(image))
                ranks[r] += 1
                assert all((i < mapping[i] <= m) if i < m
                           else (m <= mapping[i] < i) for i in domain)
        assert ranks == theoretical_by_missing(n,m), (n,m,ranks,theoretical_by_missing(n,m))
        combined.update(ranks)
    for r in range(1,n):
        assert combined[r] == formula(n,r), (n,r,combined[r],formula(n,r))
    cat = comb(2*n,n)//(n+1)
    assert sum(combined.values()) == cat
    assert combined[1] == n and combined[n-1] == 2
    return [combined[r] for r in range(1,n)]


def main():
    for n in range(2,10):
        row = enumerate_n(n)
        print(f'n={n} image-rank row={row}; total={sum(row)}')
    # Formula-only big-integer checks and Catalan convolution through 150.
    for n in range(2,151):
        row=[formula(n,r) for r in range(1,n)]
        assert sum(row) == comb(2*n,n)//(n+1)
        # Independent convolution of classical Narayana polynomials.
        ans=[0]*n
        for m in range(1,n+1):
            poly=theoretical_by_missing(n,m)
            for r,c in poly.items(): ans[r]+=c
        assert ans[1:] == row
    print('VERIFY_OK_MAXIMAL_DOMAIN_NILPOTENT_RANK_NARAYANA')


if __name__=='__main__':
    main()
