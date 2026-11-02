"""Exact finite-factor and microscopic checks for the 3-state Greenberg-Hastings
rule on crown graphs. Requires only Python 3 standard library.
Run: python3 verify_crown_gh3.py
"""
from itertools import product
from collections import Counter
from math import factorial

TYPES = tuple(product(range(3), repeat=2))
PROFILES = tuple(product(range(3), repeat=9))
INDEX = {v: k for k, v in enumerate(PROFILES)}

def pair_map(c):
    # c is the per-matched-pair type-count vector clipped at 2.
    num_b1 = min(2, sum(c[3*a + 1] for a in range(3)))
    num_a1 = min(2, sum(c[3 + b] for b in range(3)))
    mapping = {}
    for j, (a, b) in enumerate(TYPES):
        if c[j] == 0:
            continue
        new_a = (a + 1) % 3 if a else int(num_b1 > int(b == 1))
        new_b = (b + 1) % 3 if b else int(num_a1 > int(a == 1))
        mapping[j] = 3 * new_a + new_b
    return mapping

def advance(c, f):
    out = [0] * 9
    for typ, dest in f.items():
        out[dest] = min(2, out[dest] + c[typ])
    return tuple(out)

NEXT = []
MAPS = []
for c in PROFILES:
    f = pair_map(c)
    MAPS.append(f)
    NEXT.append(INDEX[advance(c, f)])

# Find all cyclic signatures and exact first entry times of the 9-trit factor.
info = {}  # profile ID -> (entry time, signature-period, cycle representative)
cycles = {}
for start in range(len(PROFILES)):
    if start in info:
        continue
    local = {}
    path = []
    u = start
    while u not in info and u not in local:
        local[u] = len(path)
        path.append(u)
        u = NEXT[u]
    if u in local:
        cut = local[u]
        cyc = path[cut:]
        key = min(cyc)
        cycles[key] = tuple(cyc)
        for v in cyc:
            info[v] = (0, len(cyc), key)
        path = path[:cut]
    for v in reversed(path):
        t, pp, key = info[NEXT[v]]
        info[v] = (t + 1, pp, key)
assert len(info) == 3 ** 9

# Exact lifting: transport each occupied paired color-type through a
# recurrent profile cycle; its return is a permutation, not necessarily id.
true_period = {}
cycle_kinds = Counter()
for key, cyc in cycles.items():
    support = tuple(i for i, x in enumerate(PROFILES[cyc[0]]) if x)
    transport = {i: i for i in support}
    for state in cyc:
        f = MAPS[state]
        transport = {i: f[x] for i, x in transport.items()}
    assert set(transport.values()) == set(support)
    order = 1
    perm = dict(transport)
    while any(perm[i] != i for i in support):
        perm = {i: transport[perm[i]] for i in support}
        order += 1
        assert order <= 9
    period = len(cyc) * order
    true_period[key] = period
    cycle_kinds[(len(cyc), order, period)] += 1

by_p = Counter()
by_t = Counter()
rare = {6: [], 10: []}
for i, (entry, macro_p, key) in info.items():
    p = true_period[key]
    by_p[p] += 1
    by_t[entry] += 1
    if p in rare:
        rare[p].append((i, entry))
assert max(by_t) == 6, by_t
assert set(by_p) == {1, 3, 4, 6, 10}, by_p
assert {p: len(v) for p, v in rare.items()} == {6: 50, 10: 6}
assert all(sum(PROFILES[i]) == 3 and max(PROFILES[i]) == 1 for i, _ in rare[6])
assert all(sum(PROFILES[i]) == 5 and max(PROFILES[i]) == 1 for i, _ in rare[10])
assert Counter(t for i, t in rare[6]) == Counter({0: 2, 1: 14, 2: 24, 3: 10})
assert Counter(t for i, t in rare[10]) == Counter({0: 2, 1: 2, 2: 2})
# Two periodic signatures, n! labelled assignments per signature, p phases.
assert 2 * factorial(3) // 6 == 2
assert 2 * factorial(5) // 10 == 24

# A reachable six-step initial signature with a type of multiplicity >=2.
six = [PROFILES[i] for i, (t, _, _) in info.items()
       if t == 6 and sum(PROFILES[i]) == 5 and 2 in PROFILES[i]]
assert six
print('FACTOR_SIGNATURES', len(PROFILES))
print('FACTOR_CYCLES', len(cycles))
print('FACTOR_CYCLE_TYPES', sorted((str(k), v) for k, v in cycle_kinds.items()))
print('SIGNATURE_PERIOD_BASINS', sorted(by_p.items()))
print('SIGNATURE_ENTRY_TIMES', sorted(by_t.items()))
print('EXCEPTIONAL_6_SIGNATURE_ENTRY', sorted(Counter(t for _,t in rare[6]).items()))
print('EXCEPTIONAL_10_SIGNATURE_ENTRY', sorted(Counter(t for _,t in rare[10]).items()))
print('SIX_STEP_PROFILE', six[0])

# Independent vertex-level dynamics (not using the profile update functions).
def successor(x, n, cca=False):
    a = [x // (3**i) % 3 for i in range(n)]
    b = [x // (3**(n+i)) % 3 for i in range(n)]
    tot_a = [a.count(i) for i in range(3)]
    tot_b = [b.count(i) for i in range(3)]
    y = 0
    for i in range(n):
        va, vb = a[i], b[i]
        if cca:
            wa = (va + 1) % 3 if tot_b[(va+1)%3] > int(vb == (va+1)%3) else va
            wb = (vb + 1) % 3 if tot_a[(vb+1)%3] > int(va == (vb+1)%3) else vb
        else:
            wa = (va + 1) % 3 if va else int(tot_b[1] > int(vb == 1))
            wb = (vb + 1) % 3 if vb else int(tot_a[1] > int(va == 1))
        y += wa*(3**i) + wb*(3**(n+i))
    return y

def full_census(n, cca=False):
    count = 3**(2*n)
    trans = [successor(s, n, cca) for s in range(count)]
    entry = [-1]*count
    period = [0]*count
    for start in range(count):
        if entry[start] != -1:
            continue
        path = []; seen = {}; u = start
        while entry[u] == -1 and u not in seen:
            seen[u] = len(path)
            path.append(u)
            u = trans[u]
        if u in seen:
            k = seen[u]
            p = len(path)-k
            for v in path[k:]:
                entry[v] = 0; period[v] = p
            path = path[:k]
        for v in path[::-1]:
            entry[v] = entry[trans[v]] + 1
            period[v] = period[trans[v]]
    return entry, period

expected = {
    1: ({1}, 2),
    2: ({1}, 3),
    3: ({1,3,6}, 5),
    4: ({1,3,4}, 5),
    5: ({1,3,4,10}, 6),
    6: ({1,3,4}, 6),
}
for n in range(1,7):
    entry, period = full_census(n)
    assert set(period) == expected[n][0], (n, set(period))
    assert max(entry) == expected[n][1], (n, max(entry))
    orbit_counts = {p: sum(1 for t,k in zip(entry, period) if t==0 and k==p)//p for p in sorted(set(period))}
    if n == 3:
        assert orbit_counts[6] == 2
        assert Counter(t for t,k in zip(entry,period) if k==6) == {0:12,1:84,2:144,3:60}
    if n == 5:
        assert orbit_counts[10] == 24
        assert Counter(t for t,k in zip(entry,period) if k==10) == {0:240,1:240,2:240}
        _, cca_period = full_census(5, cca=True)
        assert sum(k==10 for k in cca_period) == 720
        assert all((x==10)==(y==10) for x,y in zip(period,cca_period))
        print('CROWN5_CCA_GHM_IDENTICAL_TEN_BASINS', 720)
    print('MICRO', n, 'states', 3**(2*n), 'periods', sorted(set(period)),
          'max_entry', max(entry), 'orbits', sorted(orbit_counts.items()))
print('CROWN_GHM3_VERIFY_OK')
