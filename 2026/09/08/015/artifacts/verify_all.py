"""Independent checker: K3,3-freeness, transversal counts, packing, orthogonal mates.
Reads output/artifacts/squares.json. Stdlib only. Run: python3 verify_all.py"""
import json, itertools, sys
D = json.load(open("squares.json"))
K1, K2 = D["K1"], D["K2"]
def is_latin(L):
    n=len(L)
    return all(sorted(r)==list(range(n)) for r in L) and \
           all(sorted(L[r][c] for r in range(n))==list(range(n)) for c in range(n))
def k33_patterns(L):
    n=len(L); hits=[]
    for r1,r2,r3 in itertools.permutations(range(n),3):
        for c1,c2,c3 in itertools.permutations(range(n),3):
            if L[r1][c2]==L[r2][c1] and L[r2][c3]==L[r3][c2] and L[r3][c1]==L[r1][c3]:
                hits.append(((r1,r2,r3),(c1,c2,c3)))
    return hits
def transversals(L):
    n=len(L); out=[]
    for p in itertools.permutations(range(n)):
        if len({L[r][p[r]] for r in range(n)})==n:
            out.append(tuple(p))
    return out
def check_mate(L,M):
    n=len(L)
    assert is_latin(M), "mate not latin"
    seen=set()
    for r in range(n):
        for c in range(n):
            seen.add((L[r][c],M[r][c]))
    assert len(seen)==n*n, f"not orthogonal: {len(seen)} pairs"
    # each mate symbol class must be a transversal of L
    for s in range(n):
        rows=[r for r in range(n) for c in range(n) if M[r][c]==s]
        cols=[c for r in range(n) for c in range(n) if M[r][c]==s]
        syms=[L[r][c] for r in range(n) for c in range(n) if M[r][c]==s]
        assert sorted(rows)==list(range(n)) and sorted(cols)==list(range(n)) and sorted(syms)==list(range(n)), f"mate class {s} not transversal"
for name,L in [("K1",K1),("K2",K2)]:
    assert is_latin(L), name
    h=k33_patterns(L)
    print(f"{name}: latin OK, ordered K3,3-pattern hits = {len(h)} -> K33-free = {len(h)==0}")
    T=transversals(L)
    print(f"{name}: transversal count = {len(T)}")
# packed families: cell index r*8+c, from disjoint-packing search
PACK = {
 "K1": [[0,10,22,28,33,45,55,59],[1,11,23,29,34,46,52,56],[2,8,20,30,39,43,49,61],[3,9,21,31,36,40,50,62],[4,14,18,24,35,47,53,57],[5,15,19,25,32,44,54,58],[6,12,16,26,37,41,51,63],[7,13,17,27,38,42,48,60]],
 "K2": [[0,10,20,27,38,41,55,61],[1,11,21,31,32,42,52,62],[2,13,22,28,33,43,48,63],[3,9,23,29,34,40,54,60],[4,14,18,24,37,47,51,57],[5,15,16,26,36,46,49,59],[6,12,19,25,39,45,50,56],[7,8,17,30,35,44,53,58]],
}
for name,L in [("K1",K1),("K2",K2)]:
    T=set(transversals(L))
    Tcells={frozenset((r,p[r]) for r in range(8)) for p in T}
    fam=PACK[name]
    assert len(fam)==8 and sum(fam,[]).__len__()==64 and len(set(sum(fam,[])))==64, "not a partition"
    for cells in fam:
        t=frozenset((v//8,v%8) for v in cells)
        assert t in Tcells, f"{name}: packed set {cells} not a transversal"
        syms=sorted(L[r][c] for (r,c) in t)
        assert syms==list(range(8)), f"{name}: bad symbols"
    print(f"{name}: 8-way disjoint-transversal partition VERIFIED")
    # build mate square: mate[r][c] = index of transversal class containing cell
    M=[[0]*8 for _ in range(8)]
    for i,cells in enumerate(fam):
        for v in cells: M[v//8][v%8]=i
    check_mate(L,M)
    print(f"{name}: orthogonal mate VERIFIED; mate rows:")
    for row in M: print("   ", row)
print("ALL CHECKS PASSED")
