"""Exact Petersen Hamilton-path rotation/Cayley verification, stdlib only.
Run: python3 verify_posa.py
"""
from itertools import combinations, permutations
from functools import lru_cache
from collections import Counter, deque

labels = tuple(combinations(range(5), 2))
index = {edge:i for i,edge in enumerate(labels)}
n = len(labels)
neighbors = tuple(tuple(j for j in range(n) if not set(labels[i]) & set(labels[j])) for i in range(n))
assert n == 10 and all(len(row)==3 for row in neighbors)

# Independent endpoint recurrence over all subsets; final endpoint t is specified.
@lru_cache(None)
def extensions(v, remaining, t):
    if not remaining:
        return int(v == t)
    return sum(extensions(w, remaining ^ (1 << w), t)
               for w in neighbors[v] if remaining & (1 << w))

# Symmetry reduces unordered endpoints to adjacent/nonadjacent representatives.
nonadjacent = extensions(0, ((1 << n)-1) ^ 1, 1)
adjacent = extensions(0, ((1 << n)-1) ^ 1, 7)
assert (nonadjacent, adjacent) == (4, 0)
assert 30*nonadjacent + 15*adjacent == 120

# Canonical reference and natural action of S_5 on 2-subsets.
base = (0, 9, 4, 2, 8, 5, 3, 7, 6, 1)
assert len(set(base)) == n
assert all(base[i+1] in neighbors[base[i]] for i in range(n-1))
canonical = lambda p: min(tuple(p), tuple(reversed(p)))

def act(s, path):
    induced = [index[tuple(sorted((s[a],s[b])))] for a,b in labels]
    return canonical(tuple(induced[x] for x in path))

S5 = tuple(permutations(range(5)))
paths = {act(g,base):g for g in S5}
assert len(paths) == 120  # trivial stabilizer, all paths covered by endpoint count

def rotations(path):
    found=set()
    for orient in (tuple(path),tuple(reversed(path))):
        end=orient[-1]
        for k in range(n-2):
            if orient[k] in neighbors[end]:
                candidate=orient[:k+1]+(end,)+tuple(reversed(orient[k+1:-1]))
                assert set(candidate)==set(path)
                found.add(canonical(candidate))
    return found

near = rotations(base)
assert len(near)==4
S = {g for g in S5 if act(g,base) in near}
assert S == {(0,2,3,4,1), (0,4,1,2,3), (0,4,2,3,1), (1,0,2,4,3)}

def compose(g,s):
    return tuple(g[s[i]] for i in range(5))
identity=tuple(range(5))
seen={identity:0}; queue=deque([identity]); histogram=Counter({0:1})
while queue:
    g=queue.popleft()
    for s in S:
        h=compose(g,s)
        if h not in seen:
            seen[h]=seen[g]+1
            histogram[seen[h]]+=1
            queue.append(h)
assert len(seen)==120 and [histogram[k] for k in range(7)]==[1,4,11,25,39,29,11]

# Every group action respects all four elementary rotations.
for g in S5:
    lhs=rotations(act(g,base))
    rhs={act(compose(g,s),base) for s in S}
    assert lhs==rhs and len(lhs)==4
# Validate the standalone certificate against the computed group action, paths,
# Cayley neighbors and graph distances; no unchecked certificate assertions.
import json
from pathlib import Path
certificate=json.loads(Path(__file__).with_name('cayley_certificate.json').read_text())
assert certificate['base_path']==list(base)
assert {tuple(s) for s in certificate['generators']}==S
assert certificate['sphere_sizes']==[histogram[k] for k in range(7)]
assert len(certificate['records'])==len(S5)
for row in certificate['records']:
    g=tuple(row['permutation'])
    assert g in seen
    assert row['path_vertex_indices']==list(act(g,base))
    assert row['distance_from_identity']==seen[g]
    assert {tuple(h) for h in row['neighbors']}=={compose(g,s) for s in S}
print('VERIFY_CERTIFICATE_OK entries=120 each_path_each_neighbor_each_distance=true')
print('VERIFY_PRIMARY_OK endpoint_fixed_nonedge=4 edge=0 paths=120 S5_regular=true')
print('VERIFY_PRIMARY_OK rotations_per_path=4 Cayley_generators=4 connected=true')
print('VERIFY_PRIMARY_OK distance_distribution=1,4,11,25,39,29,11 diameter=6')
