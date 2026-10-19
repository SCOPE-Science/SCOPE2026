"""Independent LCF-graph and perfect-matching DP verification.

Usage: python3 verify_lcf.py
No external packages are required.
"""
from itertools import combinations

N = 18
LCF = [5, 7, -7, 7, -7, -5]*3
edges = set()
for i in range(N):
    edges.add(tuple(sorted((i, (i+1) % N))))
    edges.add(tuple(sorted((i, (i+LCF[i]) % N))))
assert len(edges) == 27
nbr = [{i} for i in range(N)]
for a, b in edges:
    nbr[a].add(b)
    nbr[b].add(a)
assert all(len(x) == 4 for x in nbr)

def dominant(vertices):
    covered = set()
    for u in vertices:
        covered.update(nbr[u])
    return len(covered) == N


def shift(A, B):
    """Existence of an injective old-to-new guard assignment via bitset DP."""
    choices = [{j for j, b in enumerate(B) if b in nbr[a]} for a in A]
    reachable = {0}
    for row in choices:
        reachable = {mask | (1 << j) for mask in reachable for j in row
                     if not mask & (1 << j)}
        if not reachable:
            return False
    return bool(reachable)

for k in (4, 5, 6):
    states = [C for C in combinations(range(N), k) if dominant(C)]
    expected = {4: 0, 5: 18, 6: 423}[k]
    assert len(states) == expected
    if k == 4:
        continue
    reach = [set() for _ in states]
    for i, A in enumerate(states):
        for j, B in enumerate(states):
            if shift(A, B):
                reach[i].add(j)
    defects = []
    attack_counts = []
    for i, A in enumerate(states):
        failures = set()
        for v in range(N):
            if v in A:
                continue
            options = sum(1 for j in reach[i] if v in states[j])
            attack_counts.append(options)
            if not options:
                failures.add(v)
        defects.append(failures)
    if k == 5:
        assert sum(map(len, reach)) == 234
        assert len(attack_counts) == 234
        assert all(len(d) == 1 for d in defects)
        assert set().union(*defects) == set(range(N))
        assert len({next(iter(d)) for d in defects}) == 18
        print('LCF_FIVE_OK configurations=18 one_fatal_attack_each=18')
    else:
        assert sum(map(len, reach)) == 72891
        assert len(attack_counts) == 5076
        assert all(not d for d in defects)
        assert (min(attack_counts), max(attack_counts)) == (25, 81)
        print('LCF_SIX_OK configurations=423 no_fatal_attacks=5076 options=25..81')
print('LCF_COMPLETE_OK ordinary=5 m_eternal=6')
print('VERIFY_OK')
