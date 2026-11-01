"""Exact standalone verification of the higher-independence complex of a 17-vertex Paley graph.

Python 3 standard library only. All face sets, matching pairs, integer incidence
and character traces are recomputed from the defining quadratic residues.
"""
from collections import Counter, defaultdict, deque
import math
import random

P = 17
Q = tuple(sorted({(a * a) % P for a in range(1, P)}))
assert Q == (1, 2, 4, 8, 9, 13, 15, 16)
ADJ = tuple(sum(1 << j for j in range(P) if (j - i) % P in Q) for i in range(P))

def verts(mask):
    return [v for v in range(P) if mask & (1 << v)]

def valid(mask):
    return all((ADJ[v] & mask).bit_count() <= 1 for v in verts(mask))

F = {mask for mask in range(1, 1 << P) if valid(mask)}
D = {k: sorted(m for m in F if m.bit_count() == k + 1) for k in range(5)}
assert tuple(len(D[k]) for k in range(5)) == (17, 136, 340, 306, 68)
assert len(F) == 867 and all(mask ^ (1 << v) in F for mask in F for v in verts(mask) if mask.bit_count() > 1)

# Verify strong-regular graph parameters, distinct vertex-pair degrees.
assert all(ADJ[v].bit_count() == 8 for v in range(P))
assert all((ADJ[u] & ADJ[v]).bit_count() == (3 if ADJ[u] & (1 << v) else 4)
           for u in range(P) for v in range(u+1, P))

def boundary_sign(big, small):
    v = next(v for v in verts(big) if not (small & (1 << v)))
    assert small == (big ^ (1 << v))
    return -1 if ((big & ((1 << v)-1)).bit_count() % 2) else 1

# Every signed integral boundary squares to zero, checked on all faces.
for big in F:
    if big.bit_count() < 3: continue
    d2 = defaultdict(int)
    for v in verts(big):
        middle = big ^ (1 << v)
        s1 = boundary_sign(big, middle)
        for w in verts(middle):
            little = middle ^ (1 << w)
            d2[little] += s1 * boundary_sign(middle, little)
    assert all(x == 0 for x in d2.values())

# Independent field ranks using exhaustive binary column reduction.
field_ranks = {}
for k in range(1, 5):
    index = {m: j for j, m in enumerate(D[k-1])}
    piv = {}
    for big in D[k]:
        col = sum(1 << index[big ^ (1 << v)] for v in verts(big))
        while col:
            lead = col.bit_length()-1
            if lead in piv:
                col ^= piv[lead]
            else:
                piv[lead] = col
                break
    field_ranks[k] = len(piv)
assert [field_ranks[k] for k in range(1,5)] == [16,120,220,68]
assert [len(D[k])-field_ranks.get(k,0)-field_ranks.get(k+1,0) for k in range(5)] == [1,0,0,18,0]

order = list(range(P))
random.Random(57).shuffle(order)
assert order == [16,10,2,12,6,13,15,4,7,5,8,3,0,14,9,11,1]
remaining = set(F)
pairs = []
for v in order:
    for low in sorted(remaining):
        high = low | (1 << v)
        if low != high and high in remaining:
            assert low in remaining
            pairs.append((low, high))
            remaining.remove(low)
            remaining.remove(high)
assert len(pairs) == 423 and Counter(m.bit_count()-1 for m in remaining) == {0:1,2:1,3:19}

# Acyclicity of the ENTIRE Forman gradient directed Hasse graph.
matched = set(pairs)
succ = defaultdict(list)
indeg = {m:0 for m in F}
for high in F:
    for v in verts(high):
        low = high ^ (1 << v)
        if not low: continue
        source,dest = (low,high) if (low,high) in matched else (high,low)
        succ[source].append(dest)
        indeg[dest] += 1
queue = deque(m for m,d in indeg.items() if d == 0)
removed = 0
while queue:
    m = queue.popleft()
    removed += 1
    for dest in succ[m]:
        indeg[dest] -= 1
        if indeg[dest] == 0:
            queue.append(dest)
assert removed == len(F), (removed,len(F))

critical_triangle = next(iter(m for m in remaining if m.bit_count() == 3))
critical_tetrahedra = sorted(m for m in remaining if m.bit_count() == 4)
up_matched_triangles = {low: high for low,high in pairs if low.bit_count() == 3}
assert len(up_matched_triangles) == 219

# Independent recursion for the signed 3->2 Morse boundary via gradient paths.
# A triangle paired with an edge is discarded. A triangle paired with a
# tetrahedron is replaced by the other signed boundary triangles of its mate.
down_triangles = {high for low,high in pairs if high.bit_count() == 3}
assert len(down_triangles) == 120
memo = {}
active = set()
def morse_coeff(triangle):
    if triangle in memo:
        return memo[triangle]
    if triangle == critical_triangle:
        return 1
    if triangle in down_triangles:
        return 0
    big = up_matched_triangles[triangle]
    assert triangle not in active, 'gradient cycle'
    active.add(triangle)
    coefficient = -sum(boundary_sign(big,other) * morse_coeff(other)
                       for other in (big ^ (1 << v) for v in verts(big)) if other != triangle)
    coefficient *= boundary_sign(big,triangle)
    active.remove(triangle)
    memo[triangle] = coefficient
    return coefficient

morse_boundary = []
for big in critical_tetrahedra:
    coefficient = sum(boundary_sign(big, big ^ (1 << v)) * morse_coeff(big ^ (1 << v))
                      for v in verts(big))
    morse_boundary.append(coefficient)
assert Counter(morse_boundary) == {0:11,1:5,-1:3}, Counter(morse_boundary)
assert math.gcd(*morse_boundary) == 1

# Independently derive the rational affine-subgroup character from signed
# alternating fixed-face trace (augmented Lefschetz number).
def character(mult, shift):
    permutation = [(mult*v+shift)%P for v in range(P)]
    assert all(bool(ADJ[v] & (1 << w)) == bool(ADJ[permutation[v]] & (1 << permutation[w]))
               for v in range(P) for w in range(v+1,P))
    trace = 0
    for mask in F:
        vv = verts(mask)
        moved = [permutation[v] for v in vv]
        if sum(1 << v for v in moved) != mask:
            continue
        inversions = sum(moved[i] > moved[j] for i in range(len(moved)) for j in range(i+1,len(moved)))
        trace += (-1)**(len(vv)-1+inversions)
    return 1-trace

rows = {}
for a in Q:
    vals = [character(a,b) for b in range(P)]
    assert len(set(vals)) == 1 if a != 1 else vals[1:] == [1]*16
    rows[a] = (vals[0], Counter(vals))
assert {a: rows[a][0] for a in Q} == {1:18,2:0,4:-2,8:0,9:0,13:-2,15:0,16:2}
assert sum(sum(value*count for value,count in counter.items()) for _,counter in rows.values()) == 0
assert (18+16)//17 == 2

print('PALEY17_IND2_INTEGRAL_MORSE_AND_AFFINE_CHARACTER_OK')
print('quadratic_residues', Q)
print('vertices', P, 'edges', sum(x.bit_count() for x in ADJ)//2, 'subsets_checked', (1 << P)-1)
print('nonempty_faces',len(F),'f_vector',tuple(len(D[k]) for k in range(5)))
print('binary_boundary_ranks',tuple(field_ranks[k] for k in range(1,5)))
print('morse_toggle_order', tuple(order))
print('morse_pairs',len(pairs),'morse_acyclic_faces',removed)
print('critical_face_dimensions',sorted(Counter(m.bit_count()-1 for m in remaining).items()))
print('critical_triangle_mask',critical_triangle,'signed_morse_boundary',morse_boundary)
print('signed_morse_boundary_gcd',math.gcd(*morse_boundary))
print('affine_group_size',len(Q)*P)
print('affine_character_by_multiplier_at_shift_0',[(a,rows[a][0]) for a in Q])
print('nonzero_translation_character',character(1,1))
print('affine_fixed_homology_dimension',0)
