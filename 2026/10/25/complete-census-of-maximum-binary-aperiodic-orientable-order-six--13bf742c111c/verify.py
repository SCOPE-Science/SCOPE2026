#!/usr/bin/env python3
"""Independent exact census of maximal binary reversal-distinguishing 6-windows.

Run: python3 verify.py. Python 3 standard library only.
The first algorithm scans literal words; the second uses a 28-bit
reversal-orbit automaton and memoized optimal-path recurrence.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product

N = 6
L = 26

def reverse_int(w, width=N):
    v = 0
    for _ in range(width):
        v = (v << 1) | (w & 1)
        w >>= 1
    return v

orbit_index = [-1] * 64
orbit_count = 0
for w in range(64):
    rw = reverse_int(w)
    if rw != w and orbit_index[w] == -1:
        orbit_index[w] = orbit_index[rw] = orbit_count
        orbit_count += 1
assert orbit_count == 28
assert sorted(set(orbit_index)) == [-1] + list(range(28))

@lru_cache(None)
def remaining(vertex, seen):
    best = 0
    for bit in (0, 1):
        six = (vertex << 1) | bit
        index = orbit_index[six]
        if index >= 0 and not (seen >> index) & 1:
            best = max(best, 1 + remaining(six & 31, seen | (1 << index)))
    return best

def optimal_extensions(s, vertex, seen, remaining_edges):
    if remaining_edges == 0:
        yield s
        return
    for bit in (0, 1):
        six = (vertex << 1) | bit
        index = orbit_index[six]
        if index >= 0 and not (seen >> index) & 1:
            newmask = seen | (1 << index)
            if remaining(six & 31, newmask) == remaining_edges - 1:
                yield from optimal_extensions(s + str(bit), six & 31, newmask, remaining_edges - 1)

start_depth = {format(v, '05b'): remaining(v, 0) for v in range(32)}
assert max(start_depth.values()) == 21
optimal_dp = set()
for prefix, longest in start_depth.items():
    if longest == 21:
        optimal_dp.update(optimal_extensions(prefix, int(prefix, 2), 0, 21))
assert len(optimal_dp) == 22

# Literal-word exhaustive extension: no graph orbit indexing or DP used.
visited_count_by_length = defaultdict(int)
optimal_brute = set()

def brute(w, seen):
    if len(w) >= N:
        visited_count_by_length[len(w)] += 1
    if len(w) == L:
        optimal_brute.add(w)
        return
    for c in '01':
        ext = w + c
        if len(ext) < N:
            brute(ext, seen)
            continue
        sub = ext[-N:]
        rev = sub[::-1]
        if sub == rev or sub in seen or rev in seen:
            continue
        brute(ext, seen | {sub, rev})

for start in map(''.join, product('01', repeat=N-1)):
    brute(start, set())
assert optimal_brute == optimal_dp
assert visited_count_by_length[26] == 22
assert visited_count_by_length[25] == 108
assert visited_count_by_length[6] == 56

def complement(s):
    return s.translate(str.maketrans('01', '10'))

def transformations(s):
    return {s, s[::-1], complement(s), complement(s[::-1])}

orbits = defaultdict(set)
for w in sorted(optimal_dp):
    orbits[min(transformations(w))].add(w)
assert sorted(map(len, orbits.values())) == [2, 4, 4, 4, 4, 4]
assert len(orbits) == 6
assert all(w.startswith('00000') and w.endswith('11111') or
           w.startswith('11111') and w.endswith('00000') for w in optimal_dp)
assert len([w for w in optimal_dp if w.startswith('00000')]) == 11
assert len([w for w in optimal_dp if w.startswith('11111')]) == 11
print('ORIENTABLE_ORDER6_PASS best_length=26 total_maxima=22 orbits=6')
print('optimal_prefix_depths_first_bit_zero:', ' '.join(f'{v:05b}:{remaining(v,0)}' for v in range(16)))
print('states=', remaining.cache_info().currsize, 'raw_prefixes=', sum(visited_count_by_length.values()))
print('orbits:', ' '.join(f'{k}:{len(v)}' for k, v in sorted(orbits.items())))
