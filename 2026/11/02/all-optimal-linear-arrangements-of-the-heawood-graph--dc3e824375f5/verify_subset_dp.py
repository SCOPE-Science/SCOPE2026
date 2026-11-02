#!/usr/bin/env python3
"""Independent exhaustive subset-DP proof check for Heawood optimal linear arrangements.
Public mathematical artifact: no dependencies outside the Python standard library.
"""
N = 14
FULL = (1 << N) - 1
# Cyclic difference-set representation of the Fano-plane incidence graph.
EDGES = tuple((p, 7 + (p + d) % 7) for p in range(7) for d in (0, 1, 3))
assert len(EDGES) == 21 and len(set(EDGES)) == 21
adj = [0] * N
for x, y in EDGES:
    adj[x] |= 1 << y
    adj[y] |= 1 << x
assert all(a.bit_count() == 3 for a in adj)
assert all((adj[x]&adj[y]).bit_count()==1 for x in range(7) for y in range(x+1,7))
assert all((adj[x]&adj[y]).bit_count()==1 for x in range(7,14) for y in range(x+1,14))

bound = [0] * (1 << N)
minimum_by_size = [10**9] * (N + 1)
number_min_sets = [0] * (N + 1)
for s in range(1 << N):
    if s:
        bit = s & -s
        v = bit.bit_length() - 1
        rest = s ^ bit
        bound[s] = bound[rest] + 3 - 2 * (adj[v] & rest).bit_count()
    k = s.bit_count()
    if bound[s] < minimum_by_size[k]:
        minimum_by_size[k] = bound[s]
        number_min_sets[k] = 1
    elif bound[s] == minimum_by_size[k]:
        number_min_sets[k] += 1

EXPECTED_PROFILE = (0,3,4,5,6,7,6,7,6,7,6,5,4,3,0)
assert tuple(minimum_by_size) == EXPECTED_PROFILE
assert number_min_sets[6] == number_min_sets[8] == 28
assert number_min_sets[7] == 168

# Exact minimum-linear-arrangement dynamic program over every subset, not a
# search over the conjectured structural family.
inf = 10**12
cost = [inf] * (1 << N)
ways = [0] * (1 << N)
cost[0] = 0
ways[0] = 1
for s in range(1, 1 << N):
    bs = bound[s]
    t = s
    best = inf
    ct = 0
    while t:
        bit = t & -t
        pre = s ^ bit
        z = cost[pre] + bs
        if z < best:
            best, ct = z, ways[pre]
        elif z == best:
            ct += ways[pre]
        t ^= bit
    cost[s], ways[s] = best, ct
assert sum(minimum_by_size) == 69
assert cost[FULL] == 69
assert ways[FULL] == 1548288

# Independently count the chains of individual boundary minimizers.
chains = [0] * (1 << N)
chains[0] = 1
for s in range(1, 1 << N):
    if bound[s] != minimum_by_size[s.bit_count()]:
        continue
    t = s
    while t:
        bit = t & -t
        chains[s] += chains[s ^ bit]
        t ^= bit
assert chains[FULL] == ways[FULL]

print('EXHAUSTIVE_HEAWOOD_SUBSET_DP_PASS')
print('subsets=16384 minLA=69 optimal_orders=1548288')
print('profile=' + ','.join(map(str,minimum_by_size)))
print('minimizer_counts=' + ','.join(map(str,number_min_sets)))
