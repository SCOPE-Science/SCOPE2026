from collections import deque
from itertools import combinations


def maps(n):
    a = tuple((i + 1) % n for i in range(n))
    b = tuple(0 if i == n - 1 else i for i in range(n))
    return a, b


def image(mask, f, n):
    out = 0
    for i in range(n):
        if (mask >> i) & 1:
            out |= 1 << f[i]
    return out


def distances(n):
    a, b = maps(n)
    full = (1 << n) - 1
    dist = {full: 0}
    queue = deque([full])
    while queue:
        s = queue.popleft()
        for f in (a, b):
            t = image(s, f, n)
            if t not in dist:
                dist[t] = dist[s] + 1
                queue.append(t)
    return dist


def shortest_avoidance(dist, target_mask):
    return min(d for s, d in dist.items() if s & target_mask == 0)


def target_mask(states):
    out = 0
    for i in states:
        out |= 1 << i
    return out


def check(nmax=11):
    for n in range(2, nmax + 1):
        dist = distances(n)
        for k in range(1, n):
            values = {}
            for target in combinations(range(n), k):
                values[target] = shortest_avoidance(dist, target_mask(target))
            maximum = max(values.values())
            maximizers = [t for t, d in values.items() if d == maximum]
            expected = tuple(range(n - k - 1, n - 1))
            assert maximum == k * n, (n, k, maximum, k * n)
            assert maximizers == [expected], (n, k, maximizers, expected)
            print(f"n={n:2d} k={k:2d} threshold={maximum:3d} unique={expected}")


if __name__ == "__main__":
    check()
