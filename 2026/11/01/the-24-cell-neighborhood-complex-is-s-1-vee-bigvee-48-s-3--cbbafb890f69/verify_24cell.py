"""Exact verifier for the open-neighborhood complex of the 24-cell graph.
Requires only Python 3.9+ standard library. All coordinates and arithmetic are integers.
"""
from collections import Counter, deque
from itertools import combinations, product

V = []
for a,b in combinations(range(4), 2):
    for s,t in product((-1,1), repeat=2):
        x=[0]*4; x[a]=s; x[b]=t; V.append(tuple(x))
assert len(V)==len(set(V))==24
N=[]
for x in V:
    N.append(tuple(j for j,y in enumerate(V) if sum(x[k]*y[k] for k in range(4))==1))
assert all(len(z)==8 for z in N)
assert sum(len(n) for n in N)//2==96
F=set()
for n in N:
    for sub in range(1,1<<8):
        mask=0
        for k in range(8):
            if sub>>k&1:mask|=1<<n[k]
        F.add(mask)
expected={0:24,1:264,2:960,3:1608,4:1344,5:672,6:192,7:24}
assert dict(Counter(f.bit_count()-1 for f in F))==expected
assert len(F)==5088

# Fixed, explicit pivot order. Each pivot pairs all currently-unpaired
# sigma with sigma U {pivot}, ordered deterministically.
PIVOTS=(5,18,22,15,7,14,23,21,6,19,13,16,8,0,9,11,3,17,2,1,20,12,4,10)
remaining=set(F); pairs=[]
ordered=sorted(F,key=lambda f:(f.bit_count(),f))
for pivot in PIVOTS:
    b=1<<pivot
    for face in ordered:
        if face&b: continue
        upper=face|b
        if face in remaining and upper in remaining:
            remaining.remove(face);remaining.remove(upper)
            pairs.append((face,upper))
assert len(pairs)==2519
assert Counter(f.bit_count()-1 for f in remaining)=={0:1,1:1,3:48},Counter(f.bit_count()-1 for f in remaining)

# Verify every reversed matched Hasse edge defines an acyclic directed graph.
matched=set(pairs)
faces=sorted(F)
id_of={f:i for i,f in enumerate(faces)}
indeg=[0]*len(faces)
out=[[] for _ in faces]
incidences=0
for upper in faces:
    if upper.bit_count()==1:continue
    for bit in range(24):
        if not upper>>bit&1:continue
        lower=upper^(1<<bit)
        assert lower in F
        # Matched lower->upper; unmatched upper->lower.
        a,b=(lower,upper) if (lower,upper) in matched else (upper,lower)
        ai=id_of[a];bi=id_of[b]
        out[ai].append(bi);indeg[bi]+=1;incidences+=1
queue=deque(i for i,x in enumerate(indeg) if not x)
removed=0
while queue:
    i=queue.popleft();removed+=1
    for j in out[i]:
        indeg[j]-=1
        if indeg[j]==0:queue.append(j)
assert removed==len(F),('cyclic',removed,len(F))
chi=sum((-1)**d*c for d,c in expected.items())
assert chi==-48
print('VERTICES',len(V),'EDGES',96,'NEIGHBORHOOD_SIZES',set(map(len,N)))
print('F_VECTOR',expected)
print('MATCHED_PAIRS',len(pairs),'CRITICAL',dict(Counter(f.bit_count()-1 for f in remaining)))
print('ORIENTED_HASSE_EDGES',incidences,'DAG_NODES_PROCESSED',removed)
print('EULER_CHARACTERISTIC',chi)
print('HOMOTOPY_TYPE S^1 wedge 48 copies S^3')
print('VERIFY_OK')
