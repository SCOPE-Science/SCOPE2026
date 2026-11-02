#!/usr/bin/env python3
"""Independent finite checks for a closed rank enumerator of partial graph isomorphisms.

Only Python's standard library is used. The second algorithm enumerates individual
partial injections and checks adjacency in both directions; it does not use the
induced-subgraph type classification from the proof.
"""
from itertools import combinations, permutations, product
from math import comb, factorial


def formula(m, s):
    assert m >= 1 and s >= 1
    out = [0] * (m * s + 2)
    out[0] = 1
    for j in range(1, s + 2):
        embeddings = m * comb(s + 1, j) if j >= 2 else m * s + 1
        out[j] += factorial(j) * embeddings ** 2
    for cs in product(range(m + 1), repeat=s):
        c = sum(cs)
        if not 2 <= c <= m:
            continue
        support = sum((j + 1) * count for j, count in enumerate(cs))
        ways = factorial(m) // factorial(m - c)
        aut = 1
        for j, count in enumerate(cs, start=1):
            ways *= comb(s, j) ** count
            aut *= factorial(j) ** count * factorial(count)
        ways //= 1  # numerator and denominator processed below
        for count in cs:
            ways //= factorial(count)
        contribution = ways * ways * aut
        out[support] += contribution
        out[support + 1] += contribution
    return out


def direct(m, s):
    n = m * s + 1
    edge = {(min(0,v),max(0,v)) for v in range(1,n)}
    for i in range(m):
        blade = range(i*s+1,(i+1)*s+1)
        edge.update((u,v) for u,v in combinations(blade,2))
    def adj(u,v):
        return (min(u,v),max(u,v)) in edge
    counts = [0] * (n + 1)
    vertices = range(n)
    for k in range(n + 1):
        subs = list(combinations(vertices,k))
        for u in subs:
            for v in subs:
                for image in permutations(v):
                    ok = True
                    for a in range(k):
                        for b in range(a+1,k):
                            if adj(u[a],u[b]) != adj(image[a],image[b]):
                                ok=False; break
                        if not ok: break
                    if ok: counts[k] += 1
    return counts


def dclass_count(m,s):
    return 2*comb(m+s,s)-s


def tests():
    for m,s in [(1,1),(1,3),(2,1),(3,1),(2,2),(3,2),(2,3)]:
        expected=formula(m,s)
        actual=direct(m,s)
        assert expected==actual,(m,s,expected,actual)
        assert expected[0]==1
        assert expected[1]==(m*s+1)**2
        assert expected[2]==2*((m*comb(s+1,2))**2+(comb(m,2)*s*s)**2) if m*s+1>=2 else True
        print(f"EXHAUSTIVE_OK m={m} s={s} degree={m*s+1} total={sum(actual)} ranks={actual}")
    for m in range(1,8):
        for s in range(1,7):
            out=formula(m,s)
            assert out[0]==1 and out[1]==(m*s+1)**2
            assert out[-1]==(factorial(s)**m*factorial(m) if m>=2 else factorial(s+1))
            assert len(out)==m*s+2
            assert dclass_count(m,s)>0
    print('FORMULA_BOUNDARY_OK 42 parameter pairs')
    print('VERIFY_OK')

if __name__=='__main__': tests()
