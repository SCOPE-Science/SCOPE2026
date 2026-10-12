"""Exact integer checks for one-circuit-hyperplane matroid toric charts.

Run: python3 check_one_circuit_matroid.py
No third-party packages are required. Finite checks supplement, not replace, the proof.
"""
from itertools import combinations
from fractions import Fraction
from math import comb


def rank(rows):
    if not rows:
        return 0
    a = [[Fraction(x) for x in row] for row in rows]
    piv = 0
    for c in range(len(a[0])):
        i = next((j for j in range(piv, len(a)) if a[j][c]), None)
        if i is None:
            continue
        a[piv], a[i] = a[i], a[piv]
        div = a[piv][c]
        a[piv] = [v / div for v in a[piv]]
        for j in range(len(a)):
            if j != piv and a[j][c]:
                mult = a[j][c]
                a[j] = [v - mult*w for v, w in zip(a[j], a[piv])]
        piv += 1
        if piv == len(a):
            break
    return piv


def main():
    total_vertices = 0
    total_facets = 0
    for n in range(6, 10):
        for k in range(3, n-2):
            H = frozenset(range(k))
            bases = [frozenset(B) for B in combinations(range(n), k)
                     if frozenset(B) != H]
            vectors = [tuple(int(i in B) for i in range(n-1)) for B in bases]
            assert rank([tuple(a-b for a,b in zip(v,vectors[0]))
                         for v in vectors[1:]]) == n-1
            # The coordinate and circuit-hyperplane inequalities support facets.
            # Original n coordinates are recovered from sum x_i=k.
            facet_tests = []
            for i in range(n):
                for c in (0,1):
                    face = [v for v,B in zip(vectors,bases) if int(i in B)==c]
                    assert len(face)>=n-1
                    assert rank([tuple(x-y for x,y in zip(v,face[0]))
                                 for v in face[1:]])==n-2
                    facet_tests.append((i,c))
            cut = [v for v,B in zip(vectors,bases) if len(B&H)==k-1]
            assert rank([tuple(x-y for x,y in zip(v,cut[0]))
                         for v in cut[1:]])==n-2
            assert len(cut)==k*(n-k)
            r1=r2=gorenstein=0
            for B in bases:
                extra=(len(B&H)==k-1)
                r=(2 if extra else 1)
                assert (n+int(extra))-(n-1)==r
                # Coordinate normals prescribe the unique canonical linear form.
                m=[1 if i in B else -1 for i in range(n)]
                exists=(sum(m)==0 and (not extra or sum(m[i] for i in H)==1))
                assert exists==(n==2*k and (not extra or k==3))
                if exists:gorenstein+=1
                if r==1:r1+=1
                else:r2+=1
            assert r2==k*(n-k)
            assert r1==comb(n,k)-1-k*(n-k)
            expect=comb(n,k)-1 if (n,k)==(6,3) else (r1 if n==2*k else 0)
            assert gorenstein==expect
            print(f'n={n} k={k}: vertices={len(bases)} facets={len(facet_tests)+1} '+
                  f'class-rank-1={r1} class-rank-2={r2} Gorenstein={gorenstein}')
            total_vertices+=len(bases)
            total_facets+=len(facet_tests)+1
    print(f'PASS: {total_vertices} torus-fixed charts, {total_facets} supporting facet checks, exact rational ranks.')

if __name__=='__main__':
    main()
