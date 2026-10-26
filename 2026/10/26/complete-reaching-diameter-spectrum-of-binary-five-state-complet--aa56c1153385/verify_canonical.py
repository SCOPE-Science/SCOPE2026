#!/usr/bin/env python3
"""Independent exhaustive census of normalized five-state cyclic-defect-one automata."""
from collections import Counter
from itertools import product
Q = range(5)
a = (1, 2, 3, 4, 0)
FULL = 31

def image(mask, transition):
    answer = 0
    for state in Q:
        if (mask >> state) & 1:
            answer |= 1 << transition[state]
    return answer

def reach_distances(b):
    distances = {FULL: 0}
    frontier = {FULL}
    depth = 0
    while frontier:
        depth += 1
        new_frontier = set()
        for subset in frontier:
            for transition in (a, b):
                result = image(subset, transition)
                if result not in distances:
                    distances[result] = depth
                    new_frontier.add(result)
        frontier = new_frontier
    return distances

def cyclic_relabel(b, k):
    return tuple((b[(i-k) % 5] + k) % 5 for i in Q)

canonical = {}
frequencies = Counter()
size_maxima = [Counter() for _ in range(5)]
number_of_maps = 0
for b in product(Q, repeat=5):
    if len(set(b)) != 4:
        continue
    number_of_maps += 1
    distances = reach_distances(b)
    assert len(distances) == 31
    radius = max(distances.values())
    frequencies[radius] += 1
    for k in (1,2,3,4):
        size_maxima[k][max(v for s,v in distances.items() if s.bit_count() == k)] += 1
    representative = min(cyclic_relabel(b, k) for k in Q)
    if representative in canonical:
        assert canonical[representative] == radius
    canonical[representative] = radius

expected = {7:30,8:100,9:195,10:175,11:245,12:170,13:100,
            14:100,15:25,16:25,17:20,18:10,20:5}
assert frequencies == Counter(expected)
assert number_of_maps == 1200
assert len(canonical) == 240
assert len([k for k,v in canonical.items() if v == 20]) == 1
assert [k for k,v in canonical.items() if v == 20] == [(0,1,2,3,0)]
assert set(size_maxima[4]) == {5}
assert max(size_maxima[1]) == 20 and max(size_maxima[2]) == 15
assert max(size_maxima[3]) == 10
print('normalized_rank_four_maps', number_of_maps)
print('all_subsets_reached', True)
print('normalized_reaching_diameters', sorted(frequencies.items()))
print('isomorphism_classes', len(canonical))
print('class_diameters', sorted(Counter(canonical.values()).items()))
print('size_conditioned_maxima', {k:max(size_maxima[k]) for k in (1,2,3,4)})
print('unique_extremal_representative', (0,1,2,3,0))
print('VERIFY_OK')
