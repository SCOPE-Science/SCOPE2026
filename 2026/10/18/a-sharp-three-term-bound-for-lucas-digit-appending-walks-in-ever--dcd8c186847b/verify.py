"""Reproduce finite checks for Lucas digit-appending walks.

The infinite result is proved analytically; these finite checks are diagnostic.
Requires only Python 3 standard library.
"""
from bisect import bisect_left

L = [2, 1]
for n in range(2, 220):
    L.append(L[-1] + L[-2])
values = sorted(set(L))
assert values[:10] == [1,2,3,4,7,11,18,29,47,76]

edge_checks = 0
triple_checks = 0
for b in range(2, 2001):
    edges = {}
    for a in values:
        lo, hi = b * a, b * (a+1)
        i = bisect_left(values, lo)
        js = []
        while i < len(values) and values[i] < hi:
            if values[i] > a:
                js.append(values[i])
            i += 1
        edges[a] = js
        edge_checks += len(js)
    for a, choices in edges.items():
        for c in choices:
            for e in edges[c]:
                triple_checks += 1
                assert not edges[e], (b,a,c,e,edges[e])
                if a >= 3:
                    x = L.index(a)
                    y = L.index(c)
                    z = L.index(e)
                    k = y-x
                    assert k >= 5 and k%2 == 1 and x%2 == 1 and x >=3 and x<k
                    assert z-y == k and b == L[k]
                    assert c-b*a == L[k-x]
                    assert e-b*c == L[x]
assert triple_checks > 0

family_checks = 0
for k in range(5, 70, 2):
    b = L[k]
    for x in range(3,k,2):
        a,c,e = L[x], L[x+k], L[x+2*k]
        assert c == b*a + L[k-x]
        assert e == b*c + a
        assert 0 < L[k-x] < b and 0 < a < b
        family_checks += 1
    assert L[2*k] == L[k]*L[k]+2
    assert L[k] < L[2*k] and 1*b == L[k]

# Direct exhaustive check of the strict ratio gap bounds at small indices.
F=[0,1]
for _ in range(2,55): F.append(F[-1]+F[-2])
ratio_cases=0
for x in range(2,25):
    for k in range(1,13):
        u_n = L[x+k]
        for ell in range(1,13):
            if ell == k: continue
            v_n = L[x+k+ell]
            # Disjoint adjacent integer base intervals for first and second edges.
            # A base must belong simultaneously to the following closed intervals.
            alo = u_n//(L[x]+1)+1
            ahi = u_n//L[x]
            blo = v_n//(u_n+1)+1
            bhi = v_n//u_n
            assert max(2,alo,blo) > min(ahi,bhi), (x,k,ell)
            ratio_cases += 1

print(f'VERIFIED edge_checks={edge_checks} triples={triple_checks} family={family_checks} gap_cases={ratio_cases}')
