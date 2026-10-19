#!/usr/bin/env python3
"""Exact word-overlap and necklace-block DP for 5-bit binary repetitions.
Run: python3 verify.py
Standard library only; exhaustive recurrences, not solver status messages.
"""
from itertools import permutations
from collections import defaultdict

N = 5

def binary(x, n=N):
    return format(x, '0%db' % n)

def class_key(x, n=N):
    s = binary(x, n)
    return min(s[r:] + s[:r] for r in range(n))

def instance(n, power):
    words = [binary(i, n) * power for i in range(1 << n)]
    L = n * power
    cost = [[0] * len(words) for _ in words]
    for i, u in enumerate(words):
        for j, v in enumerate(words):
            if i == j: continue
            overlap = max((t for t in range(1, L) if u[-t:] == v[:t]), default=0)
            cost[i][j] = L - overlap
    clusters = defaultdict(list)
    for i in range(len(words)):
        clusters[class_key(i, n)].append(i)
    return words, cost, [clusters[k] for k in sorted(clusters)], L

def clustered_optimum(n, power):
    words, cost, clusters, L = instance(n, power)
    # Exact Hamiltonian path minima within each necklace, including all endpoints.
    internal = []
    for cluster in clusters:
        endpoints = {}
        for perm in permutations(cluster):
            v = sum(cost[x][y] for x, y in zip(perm, perm[1:]))
            key = (perm[0], perm[-1])
            if key not in endpoints or v < endpoints[key][0]:
                endpoints[key] = (v, perm)
        internal.append(endpoints)
    # Each transition visits one entire unvisited necklace. Exact subset DP.
    dp = {}
    for c, table in enumerate(internal):
        for (entry, end), (in_cost, path) in table.items():
            key = (1 << c, end)
            cand = (L + in_cost, path)
            if key not in dp or cand[0] < dp[key][0]: dp[key] = cand
    states_by_size = {}
    for taken in range(1, len(clusters)):
        states_by_size[taken] = sum(mask.bit_count() == taken for mask, _ in dp)
        following = {}
        for (mask, end), (so_far, route) in dp.items():
            if mask.bit_count() != taken:continue
            for c, table in enumerate(internal):
                if mask & (1 << c): continue
                for (entry, last), (in_cost, path) in table.items():
                    candidate = (so_far + cost[end][entry] + in_cost, route + path)
                    key = (mask | (1 << c), last)
                    if key not in following or candidate[0] < following[key][0]:
                        following[key] = candidate
        dp.update(following)
    mask = (1 << len(clusters)) - 1
    optimum, best_path = min((v for (s, _), v in dp.items() if s == mask), key=lambda v: v[0])
    assert sorted(best_path) == list(range(1 << n))
    host = words[best_path[0]]
    for i, j in zip(best_path, best_path[1:]):
        host += words[j][-cost[i][j]:]
    assert len(host) == optimum
    assert all(w in host for w in words)
    switches = sum(class_key(i, n) != class_key(j, n) for i, j in zip(best_path, best_path[1:]))
    assert switches == len(clusters) - 1
    return optimum, host, best_path, len(clusters), states_by_size

def unrestricted_optimum(n, power):
    _, cost, _, L = instance(n, power)
    size = 1 << n
    dp = {}
    for j in range(size):dp[1 << j, j] = L
    for mask in range(1, 1 << size):
        for j in range(size):
            if mask & (1 << j) and mask != 1 << j:
                earlier = mask ^ (1 << j)
                dp[mask, j] = min(dp[earlier, i] + cost[i][j]
                                  for i in range(size) if earlier & (1 << i))
    return min(dp[(1 << size) - 1, j] for j in range(size))

for n in (2, 3, 4):
    for power in (2, 3, 4):
        x, _, _, c, _ = clustered_optimum(n, power)
        y = unrestricted_optimum(n, power)
        assert x == y, (n, power, x, y)
        print('SMALL', n, power, x, 'necklaces', c)

x, host, path, classes, states = clustered_optimum(5, 3)
assert classes == 8 and x == 122
assert len(host) == 122
# For a path with B cross-necklace transitions, each other transition costs >=1,
# and every cross transition costs >=11 at power=3.
# B>=8 therefore gives a lower bound 15+(31-B)+11B >=126.
assert 15 + (31 - 8) + 11 * 8 == 126
for power in (4, 5, 8):
    optimum, new_host, new_path, _, _ = clustered_optimum(5, power)
    assert optimum == 40 * power + 2
    assert len(new_host) == 40 * power + 2
print('FIVE', x, 'necklaces', classes, 'B>=8 lower bound', 126)
print('ROUTE', ','.join(map(str,path)))
print('WITNESS', host)
print('DP_MASK_COUNTS', states)
from pathlib import Path
import json
certificate_path = Path(__file__).with_name('CERTIFICATE.json')
if certificate_path.exists():
    cert = json.loads(certificate_path.read_text(encoding='utf-8'))
    assert cert['base_length'] == 5 and cert['power'] == 3
    assert cert['minimum_length'] == x == 122
    assert cert['optimal_route'] == list(path)
    assert cert['example_host'] == host
    assert cert['conjugacy_class_count'] == classes == 8
    assert cert['nonclustered_lower_bound'] == 126
    assert cert['dp_state_histogram'] == {str(k):v for k,v in states.items()}
print('VERIFY_OK power_exponent_formula_n5_p_ge3_exact_necklace_DP_and_switch_bound')
