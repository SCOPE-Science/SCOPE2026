#!/usr/bin/env python3
"""Independent exact edge-color recursion and alternating-cycle switch verifier."""
from collections import Counter, deque

# Build the generalized Petersen graph with separately ordered outer, spoke,
# and inner edges. This enumeration does not use perfect matchings.
arc = []
for i in range(8):
    arc.append(tuple(sorted((i, (i+1) % 8))))
for i in range(8):
    arc.append((i, i+8))
for i in range(8):
    arc.append(tuple(sorted((i+8, ((i+3) % 8)+8))))
assert len(arc) == 24 and len(set(arc)) == 24
incident = [[j for j, e in enumerate(arc) if v in e] for v in range(16)]
assert all(len(x) == 3 for x in incident)
assignment = [-1] * 24
used = [0] * 16
states = []

def edge_backtrack(left):
    if left == 0:
        assert all(used[v] == 7 for v in range(16))
        states.append(tuple(assignment))
        return
    candidates = []
    for ei, (u, v) in enumerate(arc):
        if assignment[ei] != -1:
            continue
        colors = [c for c in range(3) if not (used[u] | used[v]) & (1 << c)]
        if not colors:
            return
        candidates.append((len(colors), ei, u, v, colors))
    _, ei, u, v, colors = min(candidates)
    for c in colors:
        assignment[ei] = c
        used[u] |= 1 << c
        used[v] |= 1 << c
        edge_backtrack(left - 1)
        used[u] ^= 1 << c
        used[v] ^= 1 << c
        assignment[ei] = -1

edge_backtrack(24)
states = sorted(states)
assert len(states) == 120 and len(set(states)) == 120
state_id = {s: k for k, s in enumerate(states)}

# Two-colour edge-induced subgraphs decompose into alternating cycles.
# Construct components by direct traversal on the edge-incidence graph.
def moves(s):
    choices = set()
    for x, y in ((0, 1), (0, 2), (1, 2)):
        remaining = {j for j, color in enumerate(s) if color == x or color == y}
        while remaining:
            initial = remaining.pop()
            pending = [initial]
            component = {initial}
            while pending:
                ei = pending.pop()
                for v in arc[ei]:
                    for ej in incident[v]:
                        if ej in remaining:
                            remaining.remove(ej)
                            pending.append(ej)
                            component.add(ej)
            vertices = {v for ei in component for v in arc[ei]}
            assert all(sum(ei in component for ei in incident[v]) == 2 for v in vertices)
            assert len(component) == len(vertices)
            t = list(s)
            for ei in component:
                t[ei] = y if s[ei] == x else x
            choices.add(state_id[tuple(t)])
    return choices

neighborhood = [moves(s) for s in states]
assert all(i in neighborhood[j] for j, row in enumerate(neighborhood) for i in row)
assert sum(len(x) for x in neighborhood) // 2 == 342

# Every component is determined by a complete search. This does not borrow
# matching-based component information from any other program.
def traverse(root, allowed=None):
    distance = {root: 0}
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in neighborhood[u]:
            if allowed is not None and v not in allowed:
                continue
            if v not in distance:
                distance[v] = distance[u] + 1
                queue.append(v)
    return distance

unused = set(range(len(states)))
components = []
while unused:
    found = set(traverse(next(iter(unused))))
    unused -= found
    components.append(found)
components.sort(key=len)
assert tuple(map(len, components)) == (24, 96)
short, long = components
assert Counter(len(neighborhood[v]) for v in short) == {4: 18, 6: 6}
assert Counter(len(neighborhood[v]) for v in long) == {6: 96}
assert sum(len(neighborhood[v]) for v in short) // 2 == 54
assert sum(len(neighborhood[v]) for v in long) // 2 == 288

profile = {}
for component in components:
    rows = Counter()
    for root in component:
        dist = traverse(root)
        assert len(dist) == len(component)
        cnt = Counter(dist.values())
        rows[tuple(cnt.get(i, 0) for i in range(max(cnt) + 1))] += 1
    profile[len(component)] = rows
assert profile == {24: Counter({(1, 4, 15, 4): 18, (1, 6, 15, 2): 6}),
                   96: Counter({(1, 6, 27, 42, 20): 96})}

# Separate parity tests; an attempted 2-coloring of the 24-state component
# encounters a same-parity edge, whereas the 96-state component succeeds.
def two_colour(component):
    root = next(iter(component))
    parity = {root: 0}
    todo = deque([root])
    while todo:
        u = todo.popleft()
        for v in neighborhood[u]:
            if v not in parity:
                parity[v] = 1 - parity[u]
                todo.append(v)
            elif parity[v] == parity[u]:
                return False
    assert len(parity) == len(component)
    return True

assert not two_colour(short)
assert two_colour(long)

# All colourings in the 96-state component have two bichromatic cycles of
# six and ten edges for each colour-pair. There is no switch connecting it
# to the twenty-four-state component with its 8/8 or Hamiltonian factors.
def factor_cycle_lengths(s, x, y):
    remaining = {i for i, c in enumerate(s) if c in (x, y)}
    lens = []
    while remaining:
        root = remaining.pop()
        todo = [root]
        count = 0
        while todo:
            i = todo.pop()
            count += 1
            for v in arc[i]:
                for j in incident[v]:
                    if j in remaining:
                        remaining.remove(j)
                        todo.append(j)
        lens.append(count)
    return tuple(sorted(lens))

def signature(s):
    return tuple(sorted(factor_cycle_lengths(s, i, j) for i, j in
                        ((0, 1), (0, 2), (1, 2))))

assert Counter(signature(states[v]) for v in long) == {
    ((6, 10), (6, 10), (6, 10)): 96}
assert Counter(signature(states[v]) for v in short) == {
    ((8, 8), (16,), (16,)): 18,
    ((8, 8), (8, 8), (8, 8)): 6}

# A visible short odd cycle in the smaller component is certified directly.
def find_odd_cycle(component):
    for target_length in (5, 7):
        for root in sorted(component):
            def rec(path):
                if len(path) == target_length:
                    return path[:] if root in neighborhood[path[-1]] else None
                for nxt in sorted(neighborhood[path[-1]]):
                    if nxt != root and nxt not in path and nxt in component:
                        found = rec(path + [nxt])
                        if found:
                            return found
                return None
            found = rec([root])
            if found:
                return found
    return None

odd = find_odd_cycle(short)
assert odd and len(odd) == 5
assert all(not any(v in neighborhood[u] and w in neighborhood[v] for w in neighborhood[u])
           for u in short for v in neighborhood[u])
assert all(odd[(i+1) % len(odd)] in neighborhood[odd[i]] for i in range(len(odd)))
print('EDGE_BACKTRACK_120_COLORINGS_342_SWITCH_EDGES_PASS')
print('INDEPENDENT_TWO_COMPONENTS_24_96_FULL_METRICS_PASS')
print('FACTOR_SIGNATURE_AND_BIPARTITE_CONTRAST_PASS')
print('EXPLICIT_ODD_CYCLE_LENGTH', len(odd))
