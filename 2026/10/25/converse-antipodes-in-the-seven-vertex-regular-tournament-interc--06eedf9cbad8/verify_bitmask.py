"""Exact finite verification for the 7-player regular-tournament triangle-flip graph.
Run with Python 3.10+; no third-party dependencies.
"""
from collections import Counter, deque
from itertools import combinations, permutations
from hashlib import sha256

N = 7
PAIRS = list(combinations(range(N), 2))
POS = {p: k for k, p in enumerate(PAIRS)}
FULL = (1 << len(PAIRS)) - 1
TRIANGLES = [(POS[i,j], POS[i,k], POS[j,k]) for i,j,k in combinations(range(N),3)]
ROWPLUS = [sum(1 << POS[i,j] for j in range(i+1,N)) for i in range(N)]
ROWMINUS = [tuple(POS[j,i] for j in range(i)) for i in range(N)]

def regular(mask):
    return all((mask & ROWPLUS[i]).bit_count() + sum(not ((mask >> b) & 1) for b in ROWMINUS[i]) == 3 for i in range(N))

V = [m for m in range(1 << 21) if regular(m)]
assert len(V) == 2640
INDEX = set(V)
ADJ = {}
for mask in V:
    nbr = []
    for a,b,c in TRIANGLES:
        # i<j<k: i->j, j->k, k->i, or the converse.
        p = ((mask >> a)&1, (mask >> b)&1, (mask >> c)&1)
        if p in ((1,0,1),(0,1,0)):
            other = mask ^ ((1<<a)|(1<<b)|(1<<c))
            assert other in INDEX
            nbr.append(other)
    assert len(nbr) == 14 and len(set(nbr)) == 14
    ADJ[mask] = tuple(nbr)
assert sum(map(len, ADJ.values())) == 36960
assert all(u in ADJ[v] for u,ne in ADJ.items() for v in ne)

def bfs(root):
    dist = {root:0}; queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in ADJ[u]:
            if v not in dist:
                dist[v] = dist[u]+1; queue.append(v)
    assert len(dist)==2640
    return dist

# Exhaustive orbit generation from the permutation group on seven labels.
REMAP = []
for p in permutations(range(N)):
    mp=[]; flip=0
    for bit,(i,j) in enumerate(PAIRS):
        pi,pj = p[i],p[j]
        new_bit=POS[min(pi,pj), max(pi,pj)]
        mp.append(new_bit)
        if pi>pj: flip |= 1 << new_bit
    REMAP.append((tuple(mp),flip))

def images(mask):
    result=set()
    for p,flip in REMAP:
        x=flip
        for i,j in enumerate(p):
            if mask & (1<<i):x ^= 1<<j
        result.add(x)
    return result

seen=set(); summary=[]
for root in V:
    if root in seen: continue
    orb=images(root); assert orb <= INDEX and not (orb&seen)
    seen |= orb
    d=bfs(root)
    hist=Counter(d.values()); shell=tuple(hist[i] for i in range(max(hist)+1))
    four=Counter()
    for s in combinations(range(N),4):
        t=0
        for a,b,c in combinations(s,3):
            i,j,k=POS[a,b],POS[a,c],POS[b,c]
            if ((root>>i)&1,(root>>j)&1,(root>>k)&1) in ((1,0,1),(0,1,0)):t+=1
        four[t]+=1
    antipodes=[x for x in d if d[x]==max(d.values())]
    opposite=root^FULL
    summary.append((len(orb),shell,tuple(four[k] for k in range(3)),d[opposite],len(antipodes),opposite in antipodes))
assert len(seen)==2640 and len(summary)==3
summary.sort()
EXPECTED=[
(240,(1,14,91,343,749,871,476,92,3),(0,14,21),7,3,False),
(720,(1,14,91,336,721,822,485,147,22,1),(7,0,28),9,1,True),
(1680,(1,14,91,340,739,853,483,113,6),(3,8,24),7,6,False)]
assert summary == EXPECTED, (summary,EXPECTED)
encoded_vertices=b''.join(m.to_bytes(3,'little') for m in V)
encoded_edges=b''.join(u.to_bytes(3,'little')+v.to_bytes(3,'little') for u in V for v in sorted(ADJ[u]) if u<v)
print('vertices=2640 edges=18480 degree=14 components=1 radius=8 diameter=9')
print('sorted_vertex_masks_sha256='+sha256(encoded_vertices).hexdigest())
print('sorted_edge_pairs_sha256='+sha256(encoded_edges).hexdigest())
for row in summary:print('class='+repr(row))
print('PASS')
