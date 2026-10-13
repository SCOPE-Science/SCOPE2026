from itertools import combinations


def book(n):
    vertices = ["a", "b"] + [f"x{i}" for i in range(n)] + [f"y{i}" for i in range(n)]
    adj = {v: set() for v in vertices}

    def add(u, v):
        adj[u].add(v)
        adj[v].add(u)

    add("a", "b")
    for i in range(n):
        add("a", f"x{i}")
        add(f"x{i}", f"y{i}")
        add(f"y{i}", "b")
    return vertices, adj


def components(white, adj):
    unseen = set(white)
    result = []
    while unseen:
        root = next(iter(unseen))
        unseen.remove(root)
        stack = [root]
        comp = {root}
        while stack:
            u = stack.pop()
            for v in adj[u] & unseen:
                unseen.remove(v)
                comp.add(v)
                stack.append(v)
        result.append(comp)
    return result


def psd_closure(vertices, adj, initial):
    blue = set(initial)
    while True:
        white = set(vertices) - blue
        if not white:
            return blue
        changed = False
        for comp in components(white, adj):
            for u in list(blue):
                candidates = adj[u] & comp
                if len(candidates) == 1:
                    blue.add(next(iter(candidates)))
                    changed = True
                    break
            if changed:
                break
        if not changed:
            return blue


def is_psd_forcing(vertices, adj, initial):
    return len(psd_closure(vertices, adj, initial)) == len(vertices)


def predicted_pair(pair, n):
    pair = set(pair)
    if pair == {"a", "b"}:
        return True
    for i in range(n):
        if pair == {f"x{i}", f"y{i}"}:
            return True
    if len(pair & {"a", "b"}) == 1:
        return True
    return False


singleton_checks = 0
pair_checks = 0
orders = 0
for n in range(1, 13):
    vertices, adj = book(n)
    orders += 1
    for v in vertices:
        singleton_checks += 1
        assert not is_psd_forcing(vertices, adj, {v}), (n, v)

    good = 0
    for pair in combinations(vertices, 2):
        pair_checks += 1
        actual = is_psd_forcing(vertices, adj, pair)
        expected = predicted_pair(pair, n)
        assert actual == expected, (n, pair, actual, expected)
        good += int(actual)
    assert good == 5 * n + 1, (n, good, 5 * n + 1)

print(
    "VERIFY_OK "
    f"n_range=1..12 singleton_checks={singleton_checks} "
    f"pair_checks={pair_checks} minimum_count_checks={orders} max_order={2 * 12 + 2}"
)
