"""Independent forbidden-three-vertex-path enumeration and F2 boundary calculation."""
from collections import defaultdict
from itertools import combinations

# Independent edge construction: 4 vertex triangles and 6 intertriangle edges.
V = [(i, j) for i in range(4) for j in range(4) if i != j]
idx = {v: k for k, v in enumerate(V)}
E = set()
for i in range(4):
    group = [idx[(i, j)] for j in range(4) if i != j]
    for u, v in combinations(group, 2): E.add(frozenset((u, v)))
for i in range(4):
    for j in range(i+1, 4): E.add(frozenset((idx[(i,j)], idx[(j,i)])))
assert len(E) == 18

# Forbidden induced connected subgraphs have 3 vertices, possibly triangles.
forbidden = set()
for trio in combinations(range(12), 3):
    edges_inside = [e for e in E if e.issubset(trio)]
    if len(edges_inside) >= 2:
        # For 3 distinct vertices, >=2 graph edges implies connected.
        mask = sum(1 << x for x in trio)
        forbidden.add(mask)
assert len(forbidden)>0

by_dim=defaultdict(list)
for s in range(1, 1 << 12):
    if all((s & f) != f for f in forbidden):
        by_dim[s.bit_count() - 1].append(s)
assert [len(by_dim[d]) for d in range(6)] == [12,66,192,303,228,62]


def rank_gf2(columns):
    piv={}
    for c in columns:
        while c:
            lead=c.bit_length()-1
            if lead not in piv:
                piv[lead]=c
                break
            c^=piv[lead]
    return len(piv)

boundary_rank={0: 0}
for d in range(1,6):
    ind={s:i for i,s in enumerate(by_dim[d-1])}
    cols=[]
    for simplex in by_dim[d]:
        chain=0
        for v in range(12):
            if simplex&(1<<v):
                chain ^= (1 << ind[simplex^(1<<v)])
        cols.append(chain)
    boundary_rank[d]=rank_gf2(cols)
assert [boundary_rank[d] for d in range(1,6)] == [11,55,137,163,62]
betti={d:len(by_dim[d])-boundary_rank[d]-boundary_rank.get(d+1,0) for d in range(6)}
assert betti=={0:1,1:0,2:0,3:3,4:3,5:0}
print('FORBIDDEN_TRIPLES=' + str(len(forbidden)))
print('INDEPENDENT_F_VECTOR=12,66,192,303,228,62')
print('MOD2_BOUNDARY_RANKS=11,55,137,163,62')
print('MOD2_BETTI=1,0,0,3,3,0')
print('INDEPENDENT_MOD2_VERIFICATION_PASS')
