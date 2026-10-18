"""Exact incidence proof for blocking unions of two smooth ternary conics.

A smooth conic has four F_3 points forming a 4-arc; conversely,
through each 4-arc passes exactly one smooth F_3-conic.  Thus arcs
can serve as a complete, nonredundant parametrization of conics.
No external packages are required.
"""
from collections import Counter
from itertools import combinations, product
import json

Q = 3

def normalize(v):
    a = next(x for x in v if x)
    return tuple(x * pow(a, -1, Q) % Q for x in v)

P = sorted({normalize(p) for p in product(range(Q), repeat=3) if any(p)})
point_index = {p: i for i, p in enumerate(P)}
N = len(P)
assert N == 13
LINE = [sum(1 << i for i, p in enumerate(P) if sum(a*b for a,b in zip(l,p)) % Q == 0)
        for l in P]
assert len(set(LINE)) == 13 and all(x.bit_count() == 4 for x in LINE)
FULL = (1 << N) - 1

arcs = sorted(sum(1 << i for i in s) for s in combinations(range(N), 4)
              if all((sum(1 << i for i in s) & l).bit_count() <= 2 for l in LINE))
assert len(arcs) == 234
arc_index = {x: i for i,x in enumerate(arcs)}

pairs = set()
union_decompositions = Counter()
rows = Counter()
for i in range(len(arcs)):
    for j in range(i+1, len(arcs)):
        m, n = arcs[i], arcs[j]
        u = m | n
        if not all(u & l for l in LINE):
            continue
        pairs.add((i,j))
        union_decompositions[u] += 1
        rows[(u.bit_count(), (m & n).bit_count(), max((u & l).bit_count() for l in LINE))] += 1
assert len(pairs) == 11466

nontrivial = {(i,j) for i,j in pairs
              if all(((arcs[i]|arcs[j])&l).bit_count() < 4 for l in LINE)}
nontriv_unions = {arcs[i]|arcs[j] for i,j in nontrivial}
B6 = {u for u in nontriv_unions if u.bit_count() == 6}
B7 = {u for u in nontriv_unions if u.bit_count() == 7}
assert len(nontrivial) == 1638 and len(B6) == len(B7) == 234
assert {FULL ^ u for u in B6} == B7
assert all(union_decompositions[u] == 3 for u in B6)
assert all(union_decompositions[u] == 4 for u in B7)
assert all(all(any((u & ~(1<<i)) & l == 0 for l in LINE)
               for i in range(N) if (u>>i)&1) for u in B6)

# Check that no six-point nontrivial blocking sets were omitted.
all6 = {sum(1<<i for i in s) for s in combinations(range(N),6)
        if all(sum(1<<i for i in s)&l for l in LINE) and
        all((sum(1<<i for i in s)&l).bit_count() < 4 for l in LINE)}
assert all6 == B6

# Four explicit projectivities generate all PGL_3(F_3) of order 5616.
MATRICES = (
  ((0,1,0),(1,0,0),(0,0,1)),
  ((1,0,0),(0,0,1),(0,1,0)),
  ((1,1,0),(0,1,0),(0,0,1)),
  ((2,0,0),(0,1,0),(0,0,1)),
)
def proj(T,p):
    return normalize(tuple(sum(T[i][j]*p[j] for j in range(3)) % Q for i in range(3)))
perms = [tuple(point_index[proj(T,p)] for p in P) for T in MATRICES]
identity = tuple(range(N))
seen = {identity}
queue = [identity]
for h in queue:
    for g in perms:
        w = tuple(h[g[i]] for i in range(N))
        if w not in seen:
            seen.add(w)
            queue.append(w)
assert len(seen) == 5616, len(seen)

def perm_mask(mask, perm):
    return sum(1<<perm[i] for i in range(N) if (mask>>i)&1)
arc_perm = [[arc_index[perm_mask(mask,g)] for mask in arcs] for g in perms]

remaining = set(pairs)
orbits = []
while remaining:
    seed = min(remaining)
    orbit = {seed}
    todo = [seed]
    for a,b in todo:
        for g in arc_perm:
            v = tuple(sorted((g[a],g[b])))
            if v not in orbit:
                assert v in remaining
                orbit.add(v)
                todo.append(v)
    remaining.difference_update(orbit)
    a,b=seed
    u = arcs[a]|arcs[b]
    orbit_row = {
      "size":len(orbit),
      "conic_intersection":(arcs[a]&arcs[b]).bit_count(),
      "union_points":u.bit_count(),
      "line_intersection_spectrum":dict(sorted(Counter((u&l).bit_count() for l in LINE).items())),
      "nontrivial":all((u&l).bit_count() < 4 for l in LINE),
      "representative_arc_masks":[arcs[a],arcs[b]],
    }
    assert len(orbit) in (702,936,1404,2808,5616)
    orbits.append(orbit_row)
orbits.sort(key=lambda o:(o['union_points'],not o['nontrivial'],o['size']))
assert sorted(o['size'] for o in orbits) == [702,936,1404,2808,5616]
assert sum(o['size'] for o in orbits if o['nontrivial']) == 1638

print(json.dumps({"rational_points":N, "rational_lines":len(LINE),
 "smooth_conics":len(arcs),"all_blocking_pairs":len(pairs),
 "nontrivial_blocking_pairs":len(nontrivial),
 "six_point_unions":len(B6),"seven_point_unions":len(B7),
 "six_point_decompositions":3,"seven_point_decompositions":4,
 "complement_bijection":True,"all_projectivities":len(seen),
 "blocking_pair_orbits":orbits}, sort_keys=True,indent=2))
