from collections import defaultdict
from itertools import combinations


def theta(lengths):
    g = defaultdict(set)
    nxt = 2
    for L in lengths:
        prev = 0
        for _ in range(1, L):
            x = nxt
            nxt += 1
            g[prev].add(x)
            g[x].add(prev)
            prev = x
        g[prev].add(1)
        g[1].add(prev)
    return {v: set(g[v]) for v in range(nxt)}


def square(g):
    h = {v: set() for v in g}
    for v in g:
        d1 = set(g[v])
        d2 = set()
        for x in d1:
            d2.update(g[x])
        h[v] = (d1 | d2) - {v}
    return h


def colorable(h, k):
    vertices = list(h)
    color = {}

    def rec():
        if len(color) == len(vertices):
            return True
        uncolored = [v for v in vertices if v not in color]
        v = max(
            uncolored,
            key=lambda x: (
                len({color[y] for y in h[x] if y in color}),
                len(h[x]),
            ),
        )
        used = {color[y] for y in h[v] if y in color}
        for c in range(k):
            if c not in used:
                color[v] = c
                if rec():
                    return True
                del color[v]
        return False

    return rec()


def predicted(a, b, c):
    if (a, b, c) == (2, 2, 3):
        return 6
    five = (
        (a, b, c) in {(2, 2, 2), (2, 2, 6), (1, 2, 3), (1, 2, 4), (1, 3, 4)}
        or (a, b) == (2, 3)
        or (a, b) == (1, 4)
    )
    return 5 if five else 4


def exact_chi(h):
    for k in (4, 5, 6):
        if colorable(h, k):
            return k
    raise AssertionError("unexpected chromatic number above 6")

checked = 0
by_chi = {4: 0, 5: 0, 6: 0}
for a in range(1, 11):
    for b in range(max(a, 2), 11):
        for c in range(b, 11):
            h = square(theta((a, b, c)))
            got = exact_chi(h)
            want = predicted(a, b, c)
            if got != want:
                raise AssertionError(((a, b, c), got, want))
            checked += 1
            by_chi[got] += 1

# Four-color two-state transfer table. A path of L edges corresponds to L-1 transitions.
colors = range(4)
states = [(x, y) for x in colors for y in colors if x != y]
idx = {s: i for i, s in enumerate(states)}
adj = [[False] * len(states) for _ in states]
for i, (x, y) in enumerate(states):
    for z in colors:
        if z not in (x, y):
            adj[i][idx[(y, z)]] = True


def step(reach):
    out = [False] * len(states)
    for i, yes in enumerate(reach):
        if yes:
            for j, edge in enumerate(adj[i]):
                if edge:
                    out[j] = True
    return out

reach = [False] * len(states)
reach[idx[(0, 1)]] = True
counts = {1: 1}
for L in range(2, 8):
    reach = step(reach)
    counts[L] = sum(reach)
assert counts == {1: 1, 2: 2, 3: 4, 4: 7, 5: 10, 6: 11, 7: 12}
reach = step(reach)
assert sum(reach) == 12

# The exceptional six-color theta has diameter two, so its square is K6.
h = square(theta((2, 2, 3)))
assert len(h) == 6 and all(len(h[v]) == 5 for v in h)

print(f"exact_theta_instances_checked={checked}")
print("chromatic_counts=" + ",".join(f"{k}:{by_chi[k]}" for k in sorted(by_chi)))
print("four_color_state_counts=" + ",".join(f"L{L}:{counts[L]}" for L in sorted(counts)))
print("theta_2_2_3_square=K6")
print("status=PASS")
