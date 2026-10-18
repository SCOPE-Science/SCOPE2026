#!/usr/bin/env python3
"""Exact finite certificate for the 2-independence complex of GP(10,3).

Run: python3 verify_desargues_ind2.py
Requires only the Python 3 standard library.  Every face and every
face-poset cover is reconstructed from the displayed graph definition.
"""
from collections import Counter, deque

N = 10
NV = 20
EDGES = set()
for i in range(N):
    EDGES.add(tuple(sorted((i, (i+1)%N))))
    EDGES.add((i, N+i))
    EDGES.add(tuple(sorted((N+i, N+(i+3)%N))))
assert len(EDGES) == 30
ADJ = [0]*NV
for u,v in EDGES:
    ADJ[u] |= 1<<v
    ADJ[v] |= 1<<u
assert all(a.bit_count()==3 for a in ADJ)


def is_face(mask):
    # All components have size <=2 iff induced maximum degree is <=1.
    remaining=mask
    while remaining:
        b=remaining&-remaining
        v=b.bit_length()-1
        if (ADJ[v]&mask).bit_count()>1:
            return False
        remaining ^= b
    return True

# Independent exhaustive global enumeration: each nonempty bit mask is tested.
FACES = {mask for mask in range(1, 1<<NV) if is_face(mask)}
assert len(FACES)==62048, len(FACES)
assert all(((mask ^ (mask&-mask)) in FACES or mask.bit_count()==1) for mask in FACES)

# Second enumeration from the empty set via incremental admissible adjunction.
current = {0}
for v in range(NV):
    bit=1<<v
    extensions={s|bit for s in current if (ADJ[v]&s).bit_count()<=1
                and all((ADJ[x]&s).bit_count()==0 for x in range(NV) if (ADJ[v]&s)&(1<<x))}
    current |= extensions
assert current == (FACES | {0})

F_VECTOR = Counter(mask.bit_count()-1 for mask in FACES)
EXPECTED = {0:20,1:190,2:1080,3:3985,4:9784,5:15910,
            6:16600,7:10390,8:3460,9:564,10:60,11:5}
assert dict(F_VECTOR) == EXPECTED, F_VECTOR
assert sum((-1)**d*c for d,c in F_VECTOR.items())==-40

# Deterministic lexicographic toggle matching: even indices first, then odd.
ORDER = list(range(0,NV,2))+list(range(1,NV,2))
active=set(FACES)
matched=[]
for v in ORDER:
    bit=1<<v
    for s in sorted((x for x in active if not x&bit)):
        t=s|bit
        if t in active:
            assert s in active
            active.remove(s)
            active.remove(t)
            matched.append((s,t))
CRITICAL=Counter(mask.bit_count()-1 for mask in active)
assert CRITICAL == {0:1,7:41}, CRITICAL
assert len(matched)==31003
assert len(matched)*2+len(active)==len(FACES)
assert all(t==s|(t&-t) or (t^s).bit_count()==1 for s,t in matched)

# Directed Hasse graph (each codimension-one cover points downward except
# matched covers, which point upward).  Full graph topological sort is an
# exact acyclicity check, not a sampling or a gradient-path bound.
faces=sorted(FACES)
pos={s:i for i,s in enumerate(faces)}
matching_edges={(s,t) for s,t in matched}
indeg=[0]*len(faces)
out=[[] for _ in faces]
covers=0
for upper in faces:
    remaining=upper
    upper_ix=pos[upper]
    while remaining:
        b=remaining&-remaining
        lower=upper^b
        remaining ^=b
        if not lower:
            continue  # empty face is outside nonempty face poset
        lower_ix=pos[lower]
        if (lower,upper) in matching_edges:
            src,dst=lower_ix,upper_ix
        else:
            src,dst=upper_ix,lower_ix
        out[src].append(dst)
        indeg[dst]+=1
        covers+=1
assert covers==400780-20, covers
queue=deque(i for i,d in enumerate(indeg) if d==0)
visited=0
while queue:
    i=queue.popleft()
    visited+=1
    for j in out[i]:
        indeg[j]-=1
        if indeg[j]==0:
            queue.append(j)
assert visited == len(faces), (visited,len(faces))

print('graph: GP(10,3), 20 vertices, 30 edges, all degree 3')
print('faces (nonempty):',len(FACES))
print('f-vector:',','.join(str(F_VECTOR[d]) for d in range(12)))
print('Euler characteristic:',sum((-1)**d*c for d,c in F_VECTOR.items()))
print('vertex matching order:',','.join(map(str,ORDER)))
print('matching pairs:',len(matched))
print('critical cells:',dict(sorted(CRITICAL.items())))
print('directed covers:',covers)
print('acyclicity topological sort:',visited,'of',len(faces),'faces')
print('homotopy conclusion: 41 copies of S^7 wedged at a point')
print('PASS')
