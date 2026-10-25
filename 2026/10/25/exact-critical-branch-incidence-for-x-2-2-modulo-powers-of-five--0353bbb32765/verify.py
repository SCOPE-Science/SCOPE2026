"""Independent finite checks for the quadratic Dickson map modulo powers of five.

Usage: python verify.py
Python standard library only. Enumeration is a check, not a universal proof.
"""
from collections import Counter, deque


def layer(x, root, modulus, k):
    d = (x - root) % modulus
    if d == 0:
        return k, 0
    t = 0
    while d % 5 == 0:
        d //= 5
        t += 1
    character = 1 if d % 5 in (1, 4) else -1
    return t, character


def verify_level(k):
    modulus = 5 ** k
    succ = [(x * x - 2) % modulus for x in range(modulus)]
    incoming = [[] for _ in range(modulus)]
    indegree = [0] * modulus
    for x, y in enumerate(succ):
        incoming[y].append(x)
        indegree[y] += 1

    # Peel all noncycle vertices without using any theoretical period formula.
    active = indegree[:]
    queue = deque(x for x, degree in enumerate(active) if degree == 0)
    while queue:
        x = queue.popleft()
        y = succ[x]
        active[y] -= 1
        if active[y] == 0:
            queue.append(y)

    cycles = []
    component = [-1] * modulus
    depth = [-1] * modulus
    for x in range(modulus):
        if active[x] == 0 or component[x] != -1:
            continue
        c = len(cycles)
        vertices = []
        y = x
        while component[y] == -1:
            component[y] = c
            depth[y] = 0
            vertices.append(y)
            y = succ[y]
        assert y == x
        cycles.append(vertices)

    queue = deque(x for cycle in cycles for x in cycle)
    while queue:
        x = queue.popleft()
        for pred in incoming[x]:
            if depth[pred] != -1:
                continue
            depth[pred] = depth[x] + 1
            component[pred] = component[x]
            queue.append(pred)

    assert all(d != -1 for d in depth)
    assert len(cycles) == 3 * k - 1
    assert Counter(depth) == Counter({
        0: 2 * 5 ** (k - 1),
        1: 2 * 5 ** (k - 1),
        2: 5 ** (k - 1),
    })
    for x, d in enumerate(depth):
        assert d == ({2: 0, 4: 0, 1: 1, 3: 1, 0: 2}[x % 5])
        if d == 2 or (d == 1 and x % 5 == 1):
            assert len(incoming[x]) == 0

    seen_layers = Counter()
    critical_vertices = 0
    for c, cycle in enumerate(cycles):
        x0 = cycle[0]
        root = 2 if x0 % 5 == 2 else -1
        t, character = layer(x0, root, modulus, k)
        key = (root, t, character if t < k and root == 2 else 0)
        seen_layers[key] += 1
        if t == k:
            assert len(cycle) == 1 and x0 == root % modulus
        else:
            expected_period = (2 if root == 2 else 4) * 5 ** (k - t - 1)
            assert len(cycle) == expected_period, (k, x0, len(cycle), expected_period)

        for y in cycle:
            assert layer(y, root, modulus, k) == (t, character) if root == 2 else layer(y, root, modulus, k)[0] == t
            assert len(incoming[y]) == 2
            tails = [w for w in incoming[y] if depth[w] == 1]
            assert len(tails) == 1
            w = tails[0]
            actual_leaves = sum(depth[z] == 2 for z in incoming[w])
            if root == -1:
                expected_leaves = 0
            elif t == k:
                expected_leaves = 5 ** (k // 2)
            elif t % 2 == 0 and character == 1:
                expected_leaves = 2 * 5 ** (t // 2)
            else:
                expected_leaves = 0
            assert actual_leaves == expected_leaves, (k, y, actual_leaves, expected_leaves)
            critical_vertices += int(actual_leaves > 0)

        expected_component_size = sum(1 for x in range(modulus) if component[x] == c)
        count_leaves = sum(len([z for z in incoming[w] if depth[z] == 2])
                           for y in cycle for w in incoming[y] if depth[w] == 1)
        assert expected_component_size == 2 * len(cycle) + count_leaves

    assert seen_layers[(2, k, 0)] == 1
    assert seen_layers[(-1, k, 0)] == 1
    for t in range(1, k):
        assert seen_layers[(2, t, 1)] == 1
        assert seen_layers[(2, t, -1)] == 1
        assert seen_layers[(-1, t, 0)] == 1
    assert sum(seen_layers.values()) == len(cycles)
    return len(cycles), critical_vertices


def main():
    components = 0
    critical = 0
    for k in range(1, 8):
        nc, nb = verify_level(k)
        components += nc
        critical += nb
    print(f"VERIFY_OK: 97655 distinct residue states across k=1..7; "
          f"{components} exact cycles; {critical} cycle vertices with depth-two leaves; "
          "all tails, periods and component sizes")


if __name__ == '__main__':
    main()
