"""Self-contained finite verifier for a Roman edge optimum-exchange classification.
Python 3.10+ standard library only. Run: python verify_gp.py
"""
import json
from collections import Counter, deque
from itertools import combinations
from pathlib import Path

DATA = json.loads(Path(__file__).with_name('CERTIFICATE.json').read_text('utf-8'))
EDGES = sorted({tuple(sorted(pair)) for i in range(8) for pair in
                ((i, (i+1)%8), (i, i+8), (i+8, 8+(i+3)%8))})
assert len(EDGES) == 24 and EDGES == [tuple(e) for e in DATA['edge_order_gp']]
ALL = (1 << 24) - 1
COVER = [sum(1 << j for j, f in enumerate(EDGES) if set(e)&set(f))
         for e in EDGES]

# For any fixed set of label-2 edges, the unique cheapest completion puts a
# label 1 precisely on those other edges not meeting any label-2 edge.
# A solution cheaper than 12 has at most five label-2 edges.
best = 24
states = []
for size in range(6):
    for chosen in combinations(range(24), size):
        two_mask = sum(1 << j for j in chosen)
        protected = 0
        for j in chosen:
            protected |= COVER[j]
        ones = ALL ^ protected
        cost = 2*size + ones.bit_count()
        if cost < best:
            best, states = cost, []
        if cost == best:
            states.append((two_mask, ones))
assert best == 11 and len(states) == 72
assert all(one.bit_count() == 1 and two.bit_count() == 5 for two, one in states)
expected = [
    (sum(1 << x for x in s['two_edges']), 1 << s['one_edge'])
    for s in DATA['states']
]
assert states == expected
lookup = {pair: k for k, pair in enumerate(states)}
assert len(lookup) == 72

# Legal operation: replace exactly one doubly occupied edge by another;
# the forced single-occupied edge is recalculated, and weight stays optimal.
adjacency = [set() for _ in states]
for i, (twos, ones) in enumerate(states):
    selected = [j for j in range(24) if twos & (1 << j)]
    for departing in selected:
        for arriving in range(24):
            if twos & (1 << arriving):
                continue
            nxt = twos ^ (1 << departing) ^ (1 << arriving)
            protected = 0
            for j in range(24):
                if nxt & (1 << j):
                    protected |= COVER[j]
            ones_next = ALL ^ protected
            destination = lookup.get((nxt, ones_next))
            if destination is not None:
                adjacency[i].add(destination)
assert all(i in adjacency[j] for i, arr in enumerate(adjacency) for j in arr)
edges = sorted((i,j) for i, arr in enumerate(adjacency) for j in arr if i < j)
assert edges == [tuple(pair) for pair in DATA['exchange_edges']]
assert len(edges) == 96
assert all(states[i][1] != states[j][1] for i,j in edges)
assert Counter(map(len, adjacency)) == {4:24, 2:48}
branches = {i for i, arr in enumerate(adjacency) if len(arr) == 4}
mids = {i for i, arr in enumerate(adjacency) if len(arr) == 2}
assert len(branches) == 24 and len(mids) == 48
assert all(adjacency[i] <= branches for i in mids)
assert all(adjacency[i] <= mids for i in branches)

# The finite certificate supplies an explicit bijection from the 24 degree-4
# states onto the 24 original edges. Verify the 48 intermediate vertices
# correspond bijectively to unordered pairs of incident original edges.
branch_map = dict(DATA['branch_state_to_line_edge'])
assert set(branch_map) == branches and set(branch_map.values()) == set(range(24))
contracted = set()
for mid in mids:
    a,b = sorted(branch_map[z] for z in adjacency[mid])
    assert a != b
    assert (a,b) not in contracted
    contracted.add((a,b))
line_edges = {(i,j) for i in range(24) for j in range(i+1,24)
              if set(EDGES[i])&set(EDGES[j])}
assert contracted == line_edges and len(contracted) == 48

# Exact metric check, with a second explicit proof of the claimed diameter.
eccentricities = []
witness_start_distance = None
for s in range(72):
    d = [-1]*72
    d[s] = 0
    q = deque([s])
    while q:
        v = q.popleft()
        for w in adjacency[v]:
            if d[w] < 0:
                d[w] = d[v] + 1
                q.append(w)
    assert -1 not in d
    if s == DATA['witness_distance_8'][0]:
        witness_start_distance = d[DATA['witness_distance_8'][-1]]
    eccentricities.append(max(d))
assert Counter(eccentricities) == {8:72}
witness = DATA['witness_distance_8']
assert len(witness) == 9 and all(b in adjacency[a] for a,b in zip(witness,witness[1:]))
assert witness_start_distance == 8
print('GP check PASS: 24 original edges; edge Roman minimum 11; 72 optima (5 double, 1 single)')
print('Exchange graph PASS: 96 links, 24 degree-four and 48 degree-two states')
print('Line-graph subdivision PASS: exact explicit 24-edge bijection and all 48 incidence pairs')
print('Distances PASS: connected, radius 8, diameter 8, all 72 eccentricities 8')
