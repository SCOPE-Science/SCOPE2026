"""Exhaustive exact checker for optimal independent domination of the 30-vertex duad-syntheme graph.

Python 3 standard library only. Every one of the 2^15 duad selections is processed.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations

U = tuple(range(6))
DUADS = list(combinations(U, 2))


def matchings(vertices):
    if not vertices:
        yield ()
        return
    first = vertices[0]
    for other in vertices[1:]:
        for rest in matchings(tuple(v for v in vertices[1:] if v != other)):
            yield tuple(sorted(((first, other),) + rest))


SYNTHEMES = sorted(matchings(U))
assert len(DUADS) == len(SYNTHEMES) == 15
DUAD_INDEX = {e: i for i, e in enumerate(DUADS)}
SYN_INDEX = {s: i for i, s in enumerate(SYNTHEMES)}
SYNTHEME_MASKS = [sum(1 << DUAD_INDEX[e] for e in s) for s in SYNTHEMES]
assert all(sum(1 for m in SYNTHEME_MASKS if m & (1 << i)) == 3 for i in range(15))

valid_by_duad_count = defaultdict(list)
minimum_sets = set()
minimum_size = 31
for duad_mask in range(1 << 15):
    allowed = [j for j, m in enumerate(SYNTHEME_MASKS) if not (m & duad_mask)]
    covered = 0
    for j in allowed:
        covered |= SYNTHEME_MASKS[j]
    if (covered | duad_mask) != (1 << 15) - 1:
        continue
    size = duad_mask.bit_count() + len(allowed)
    valid_by_duad_count[duad_mask.bit_count()].append(size)
    independent_set = duad_mask | sum(1 << (15 + j) for j in allowed)
    if size < minimum_size:
        minimum_size = size
        minimum_sets = set()
    if size == minimum_size:
        minimum_sets.add(independent_set)

assert sum(map(len, valid_by_duad_count.values())) == 3264
assert minimum_size == 9 and len(minimum_sets) == 90
assert Counter((s & ((1 << 15) - 1)).bit_count() for s in minimum_sets) == {4: 45, 5: 45}


def duad_mask_is_four_cycle(mask):
    if mask.bit_count() != 4:
        return False
    chosen = [DUADS[i] for i in range(15) if mask & (1 << i)]
    degree = Counter(v for edge in chosen for v in edge)
    if len(degree) != 4 or set(degree.values()) != {2}:
        return False
    graph = {v: set() for v in degree}
    for a, b in chosen:
        graph[a].add(b)
        graph[b].add(a)
    seen = {min(graph)}
    stack = list(seen)
    for a in stack:
        for b in graph[a]:
            if b not in seen:
                seen.add(b)
                stack.append(b)
    return len(seen) == 4


class_a = {s for s in minimum_sets if (s & ((1 << 15) - 1)).bit_count() == 4}
class_b = minimum_sets - class_a
assert len(class_a) == len(class_b) == 45
paired = set()
for a in class_a:
    da = a & ((1 << 15) - 1)
    assert duad_mask_is_four_cycle(da)
    used = {v for i, edge in enumerate(DUADS) if da & (1 << i) for v in edge}
    remaining_duad = tuple(sorted(set(U) - used))
    db = da | (1 << DUAD_INDEX[remaining_duad])
    allowed_b = [j for j, m in enumerate(SYNTHEME_MASKS) if not (m & db)]
    b = db | sum(1 << (15 + j) for j in allowed_b)
    assert b in class_b
    assert (a ^ b).bit_count() == 2
    paired.add((a, b))
assert len(paired) == 45 and {b for _, b in paired} == class_b

adjacent = [[] for _ in range(30)]
for i, mask in enumerate(SYNTHEME_MASKS):
    for e in range(15):
        if mask & (1 << e):
            adjacent[e].append(15 + i)
            adjacent[15 + i].append(e)

exchange_edges = set()
slide_edges = set()
for s in minimum_sets:
    for deleted in range(30):
        if not (s & (1 << deleted)):
            continue
        for added in range(30):
            if s & (1 << added):
                continue
            candidate = s ^ (1 << deleted) ^ (1 << added)
            if candidate in minimum_sets:
                ordered = tuple(sorted((s, candidate)))
                exchange_edges.add(ordered)
                if added in adjacent[deleted]:
                    slide_edges.add(ordered)
assert len(exchange_edges) == len(slide_edges) == 45
assert exchange_edges == {tuple(sorted(edge)) for edge in paired}
assert Counter(x for edge in exchange_edges for x in edge) == {s: 1 for s in minimum_sets}

# Every four-cycle on the six labels is a single S_6-orbit.
reference = next(iter(class_a))
images = set()
for p in permutations(U):
    dmap = [DUAD_INDEX[tuple(sorted(p[x] for x in e))] for e in DUADS]
    smap = [SYN_INDEX[tuple(sorted(tuple(sorted(p[x] for x in e)) for e in syn))]
            for syn in SYNTHEMES]
    transformed = sum(1 << dmap[i] for i in range(15) if reference & (1 << i))
    transformed |= sum(1 << (15 + smap[i]) for i in range(15) if reference & (1 << (15 + i)))
    images.add(transformed)
assert images == class_a

print("MODEL duads_synthemes_K6")
print("vertices 30; incidence_edges 45; independent_dominating_sets 3264")
print("minimum_size 9; minimum_count 90; S6_orbit_sizes 45,45")
print("four_duad_optima 45; five_duad_optima 45")
print("classification every four-duad optimum is a C4 in K6")
print("classification every five-duad optimum is the paired C4 plus complementary duad")
print("token_jump_exchange_edges 45; token_slide_exchange_edges 45")
print("exchange_components 45 copies of K2; every vertex degree 1")
print("duad_count:valid_subsets:minimum_size:count_of_size_9")
for k in range(16):
    values = valid_by_duad_count.get(k, [])
    print(f"{k}:{len(values)}:{min(values) if values else '-'}:{values.count(9)}")
print("VERIFY_OK")
