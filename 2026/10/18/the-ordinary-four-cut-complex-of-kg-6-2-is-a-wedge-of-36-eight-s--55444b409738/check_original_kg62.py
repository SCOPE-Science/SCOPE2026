"""Independent face enumeration for the ordinary four-cut complex of KG(6,2)."""
from collections import Counter
from itertools import combinations
from math import comb

verts = tuple((1 << a) | (1 << b) for a,b in combinations(range(6), 2))
n = len(verts)
edge = {(a,b) for a,b in combinations(range(n),2) if verts[a] & verts[b] == 0}

def is_connected(q):
    seen={q[0]}
    while True:
        new = seen | {v for v in q if v not in seen and any((min(v,w),max(v,w)) in edge for w in seen)}
        if new == seen:
            return len(seen) == len(q)
        seen = new

disconnected = [tuple(q) for q in combinations(range(n),4) if not is_connected(q)]
assert len(disconnected)==615
universe = (1 << n)-1
all_cut_faces=set()
for q in disconnected:
    cut_facet = universe ^ sum(1 << j for j in q)
    s = cut_facet
    while True:
        all_cut_faces.add(s)
        if s == 0:
            break
        s = (s-1) & cut_facet
f=Counter(x.bit_count() for x in all_cut_faces)
assert [f[k] for k in range(12)] == [1,15,105,455,1365,3003,5005,6435,6435,4935,2511,615]
assert max(f)==11
assert all(f[k] == comb(n,k) for k in range(9))
euler = sum((-1 if k%2==0 else 1)*v for k,v in f.items())
assert euler == 36
print('ORIGINAL_OK', 'faces='+str(len(all_cut_faces)), 'facets='+str(len(disconnected)),
      'full_7_skeleton=yes', 'reduced_euler='+str(euler))
