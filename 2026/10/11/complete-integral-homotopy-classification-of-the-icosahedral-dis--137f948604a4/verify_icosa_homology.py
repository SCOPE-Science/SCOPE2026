"""Independent exhaustive face and mod-2 boundary-rank crosscheck.
Run: python3 verify_icosa_homology.py (standard library only).
"""
from itertools import combinations
from collections import deque
V=tuple(range(12)); E=set()
for i in range(5):
    for a,b in ((0,1+i),(11,6+i),(1+i,1+(i+1)%5),
                (6+i,6+(i+1)%5),(1+i,6+i),(1+i,6+(i-1)%5)):
        E.add(frozenset((a,b)))
assert len(E)==30
neighbors={v:{w for w in V if frozenset((v,w)) in E} for v in V}
distances={}
for start in V:
    ds={start:0}
    Q=deque([start])
    while Q:
        v=Q.popleft()
        for w in neighbors[v]:
            if w not in ds:
                ds[w]=ds[v]+1;Q.append(w)
    distances[start]=ds

def check(D):
    faces=set()
    for v in V:
        neighborhood=tuple(w for w in V if distances[v][w] in D)
        for k in range(1,len(neighborhood)+1):
            faces.update(combinations(neighborhood,k))
    layers={k:sorted(s for s in faces if len(s)==k) for k in range(1,13)}
    ranks={1:0}
    for k in range(2,13):
        positions={s:i for i,s in enumerate(layers[k-1])}
        basis={}
        for simplex in layers[k]:
            column=0
            for facet in combinations(simplex,k-1):
                column ^= 1 << positions[facet]
            while column:
                j=column.bit_length()-1
                if j in basis:column ^= basis[j]
                else:
                    basis[j]=column
                    break
        ranks[k]=len(basis)
    betti={k-1:len(layers[k])-ranks.get(k,0)-ranks.get(k+1,0)-(k==1)
           for k in range(1,13)}
    return len(faces), {k:b for k,b in betti.items() if b}

EXPECTED={
 1:(12,{0:11}),2:(264,{2:23}),3:(446,{2:1}),4:(264,{2:23}),
 5:(446,{2:1}),6:(3366,{4:1}),7:(4094,{10:1}),8:(12,{0:11}),
 9:(18,{0:5}),10:(446,{2:1}),11:(1006,{2:6,3:21}),
 12:(446,{2:1}),13:(1006,{2:6,3:21}),14:(4094,{10:1}),15:(4095,{})}
for mask in range(1,16):
    D=tuple(i for i in range(4) if mask>>i & 1)
    observed=check(D)
    assert observed==EXPECTED[mask], (D,observed,EXPECTED[mask])
    print('D',D,'independent face count and F2 reduced Betti ranks',observed)
print('ICOSAHEDRAL_DISTANCE_HOMOLOGY_PASS')
