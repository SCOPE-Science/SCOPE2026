"""Exact fort enumerator for Cartesian products of two complete graphs.

Usage: python verify.py
Dependencies: Python 3 standard library only.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from math import comb


def direct(m, n):
    """Independent subset-by-subset check using graph adjacency."""
    adj = []
    for i in range(m):
        for j in range(n):
            a = 0
            for h in range(m):
                for k in range(n):
                    if (i == h) != (j == k):
                        a |= 1 << (h*n+k)
            adj.append(a)
    ans = Counter()
    for subset in range(1, 1 << (m*n)):
        if all((adj[u] & subset).bit_count() != 1
               for u in range(m*n) if not ((subset >> u) & 1)):
            ans[subset.bit_count()] += 1
    return ans


@lru_cache(None)
def degree_restricted(p, q, row_min, col_min):
    """Weight polynomial for labeled p-by-q zero-one matrices with min degrees."""
    f = {(p, 0, 0): Counter({0: 1})}
    for _ in range(q):
        g = defaultdict(Counter)
        for (a, b, c), pol in f.items():
            for x in range(a+1):
                for y in range(b+1):
                    for w in range(c+1):
                        num = x+y+w
                        if num < col_min:
                            continue
                        mult = comb(a,x)*comb(b,y)*comb(c,w)
                        target = (a-x,b+x-y,c+y)
                        for k,v in pol.items():
                            g[target][k+num] += mult*v
        f = g
    result = Counter()
    for (a,b,c),pol in f.items():
        if a==0 and (row_min==1 or b==0):
            result.update(pol)
    return result


def fort_polynomial(m, n):
    """Proved support-decomposition and three-status transfer computation."""
    result = Counter()
    for p in range(1,m+1):
        for q in range(1,n+1):
            row_min = 2 if q<n else 1
            col_min = 2 if p<m else 1
            mult = comb(m,p)*comb(n,q)
            for degree, v in degree_restricted(p,q,row_min,col_min).items():
                result[degree] += mult*v
    return +result


def main():
    tests = [(m,n) for m in range(1,5) for n in range(1,5)]
    tests += [(2,5),(2,6),(3,5),(3,6),(4,5)]
    candidates = 0
    for m,n in tests:
        ref = direct(m,n)
        got = fort_polynomial(m,n)
        assert got == ref, (m,n,got,ref)
        candidates += (1 << (m*n))-1
    for m,n in [(4,4),(3,4),(2,4),(3,3),(2,3)]:
        target = {(4,4):60,(3,4):54,(2,4):44,(3,3):6,(2,3):6}[(m,n)]
        degree = 4 if (m,n) in [(4,4),(3,4),(2,4)] else 3
        assert fort_polynomial(m,n)[degree] == target
    for m in range(5,9):
        for n in range(5,9):
            F = fort_polynomial(m,n)
            assert F[4] == comb(m,2)*comb(n,2)
            if m>=6 and n>=6:
                assert F[5]==0 and F[6]>0
            if m>=7 and n>=7:
                expected = comb(m,2)*comb(n,3)+comb(m,3)*comb(n,2)+6*comb(m,3)*comb(n,3)
                assert F[6]==expected, (m,n,F[6],expected)
            assert sum(F.values()) >= F[4]+F[6]
    assert fort_polynomial(5,5)[5]==120
    assert fort_polynomial(6,6)[6]==3720
    print('PASS independent direct comparisons: boards=',len(tests),'candidate subsets=',candidates)
    print('PASS boundary minimum counts on (2,3),(3,3),(2,4),(3,4),(4,4)')
    print('PASS degree-4, degree-5 gap, degree-6 formulas for 5..8 board parameters')
    print('PASS (5,5) degree-5 count 120; (6,6) degree-6 count 3720')
    for m,n in [(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)]:
        pol=fort_polynomial(m,n)
        print('sample',m,n, 'first nonzero degrees',[(k,pol[k]) for k in sorted(pol)[:8]])


if __name__=='__main__': main()
