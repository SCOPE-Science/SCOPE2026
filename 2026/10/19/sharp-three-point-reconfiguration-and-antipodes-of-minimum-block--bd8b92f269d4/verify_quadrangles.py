"""Independent generation of Fano subplanes from projective quadrangles.

Run with Python 3.10+.  No packages or external inputs are needed.
"""
import hashlib
import json
from itertools import combinations
from collections import Counter, deque

M=((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))
INV=(0,1,3,2)

def dot(a,b):
    return M[a[0]][b[0]] ^ M[a[1]][b[1]] ^ M[a[2]][b[2]]

def cross(a,b):
    return (M[a[1]][b[2]] ^ M[a[2]][b[1]],
            M[a[2]][b[0]] ^ M[a[0]][b[2]],
            M[a[0]][b[1]] ^ M[a[1]][b[0]])

def normalize(a):
    first=next(x for x in a if x)
    return tuple(M[x][INV[first]] for x in a)

points=[(1,a,b) for a in range(4) for b in range(4)]
points += [(0,1,b) for b in range(4)] + [(0,0,1)]
assert len(points)==21 and len(set(points))==21
index={p:i for i,p in enumerate(points)}

B=set()
for ids in combinations(range(21),4):
    a,b,c,d=(points[i] for i in ids)
    if any(dot(cross(points[i],points[j]),points[k])==0
           for i,j,k in combinations(ids,3)):
        continue
    e=normalize(cross(cross(a,b),cross(c,d)))
    f=normalize(cross(cross(a,c),cross(b,d)))
    g=normalize(cross(cross(a,d),cross(b,c)))
    seven=(*ids,index[e],index[f],index[g])
    assert len(set(seven))==7
    B.add(frozenset(seven))
assert len(B)==360

# Sort by the geometric incidence mask. This is independent of the indexing
# used in the other enumerator; convert to its lexicographic projective basis.
basis=sorted(points)
index2={p:i for i,p in enumerate(basis)}
masks=sorted(sum(1<<index2[points[i]] for i in b) for b in B)
certificate=''.join(f'{m:06x}\n' for m in masks).encode('ascii')

# Independent switch graph built by symmetric-difference Hamming distance six.
rows=[set() for _ in masks]
for i,j in combinations(range(360),2):
    if (masks[i]^masks[j]).bit_count()==6:
        rows[i].add(j);rows[j].add(i)
assert {len(x) for x in rows}=={56}
assert sum(map(len,rows))//2==10080
report=Counter()
for i in range(360):
    dist={i:0}
    fringe=[i]
    while fringe:
        nxt=[]
        for u in fringe:
            for v in rows[u]:
                if v not in dist:
                    dist[v]=dist[u]+1
                    nxt.append(v)
        fringe=nxt
    assert len(dist)==360
    assert Counter(dist.values())=={0:1,1:56,2:287,3:16}
    for j in range(i+1,360):
        report[((masks[i]&masks[j]).bit_count(),dist[j])]+=1
assert report=={(0,3):2880,(1,2):7560,(2,2):30240,(3,2):13860,(4,1):10080}
print(json.dumps({
    'method':'quadrangle completion via projective cross products',
    'total_subplanes':len(masks),
    'neighbor_degree':56,
    'switching_edges':10080,
    'distance_layers_per_subplane':[1,56,287,16],
    'intersection_distance_histogram':sorted((list(k),v) for k,v in report.items()),
    'certificate_sha256':hashlib.sha256(certificate).hexdigest()
},sort_keys=True,separators=(',',':')))
