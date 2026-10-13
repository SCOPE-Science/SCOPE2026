from collections import Counter
from math import comb


def wheel_adj(n):
    # Rim vertices are 0,...,n-1 and the hub is n.
    adj = [set() for _ in range(n + 1)]
    hub = n
    for i in range(n):
        j = (i + 1) % n
        adj[i].add(j)
        adj[j].add(i)
        adj[i].add(hub)
        adj[hub].add(i)
    return adj


def is_connected(adj, S):
    if not S:
        return False
    seen = {next(iter(S))}
    stack = list(seen)
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v in S and v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == len(S)


def is_zero_forcing(adj, S):
    blue = set(S)
    while True:
        force = None
        for u in list(blue):
            white = [v for v in adj[u] if v not in blue]
            if len(white) == 1:
                force = white[0]
                break
        if force is None:
            return len(blue) == len(adj)
        blue.add(force)


def cycle_independent(n, R):
    return all((i + 1) % n not in R for i in R)


def cycle_connected(n, R):
    if not R:
        return False
    seen = {next(iter(R))}
    stack = list(seen)
    while stack:
        u = stack.pop()
        for v in ((u - 1) % n, (u + 1) % n):
            if v in R and v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == len(R)


def theorem_criterion(n, S):
    hub = n
    R = {v for v in S if v < n}
    if hub in S:
        return not cycle_independent(n, R)
    return len(R) >= 3 and cycle_connected(n, R)


def independent_count(n, k):
    if k == 0:
        return 1
    if k < 0 or k > n // 2:
        return 0
    return n * comb(n - k, k) // (n - k)


def formula_coefficient(n, j):
    hub_term = 0
    if 0 <= j - 1 <= n:
        hub_term = comb(n, j - 1) - independent_count(n, j - 1)
    rim_term = n if 3 <= j <= n - 1 else 0
    if j == n:
        rim_term += 1
    return hub_term + rim_term


def fibonacci(m):
    a, b = 0, 1
    for _ in range(m):
        a, b = b, a + b
    return a


subset_checks = 0
criterion_checks = 0
coefficient_checks = 0
minimum_checks = 0
total_checks = 0

for n in range(4, 12):
    adj = wheel_adj(n)
    histogram = Counter()
    for mask in range(1 << (n + 1)):
        S = {v for v in range(n + 1) if (mask >> v) & 1}
        actual = is_connected(adj, S) and is_zero_forcing(adj, S)
        predicted = theorem_criterion(n, S)
        subset_checks += 1
        criterion_checks += 1
        if actual != predicted:
            raise AssertionError((n, sorted(S), actual, predicted))
        if actual:
            histogram[len(S)] += 1

    for j in range(1, n + 2):
        expected = formula_coefficient(n, j)
        coefficient_checks += 1
        if histogram[j] != expected:
            raise AssertionError((n, j, histogram[j], expected))

    minimum_checks += 1
    if min(histogram) != 3 or histogram[3] != 2 * n:
        raise AssertionError((n, min(histogram), histogram[3]))

    total_formula = (1 << n) - (fibonacci(n - 1) + fibonacci(n + 1)) + n * (n - 3) + 1
    total_checks += 1
    if sum(histogram.values()) != total_formula:
        raise AssertionError((n, sum(histogram.values()), total_formula))

print(
    'VERIFY_OK '
    'n_range=4..11 '
    f'subset_checks={subset_checks} '
    f'criterion_checks={criterion_checks} '
    f'coefficient_checks={coefficient_checks} '
    f'minimum_checks={minimum_checks} '
    f'total_checks={total_checks} '
    'max_order=12'
)
