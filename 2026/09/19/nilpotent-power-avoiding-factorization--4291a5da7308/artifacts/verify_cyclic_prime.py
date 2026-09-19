"""Exact verifier for the cyclic prime-power formula in RESULT.md."""

from math import gcd

PRIMES = (2, 3, 5, 7, 11)


def phi(n):
    if n == 0:
        return 0
    r = n
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            r -= r // p
        p += 1
    if x > 1:
        r -= r // x
    return r


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def multiplicative_order(a, n):
    if n == 1:
        return 1
    assert gcd(a, n) == 1
    x = a % n
    r = 1
    while x != 1:
        x = (x * a) % n
        r += 1
    return r


def closed_formula(p, n):
    a = 0
    m = n
    while m % p == 0:
        a += 1
        m //= p

    if a % 2 == 0:
        A = p * (p**a - 1) // (p + 1)
        eps = 1
    else:
        A = (p ** (a + 1) - 1) // (p + 1)
        eps = 0

    coprime = 0
    if eps:
        for d in divisors(m):
            r = multiplicative_order(p, d)
            coprime += (phi(d) // r) * (r // 2)

    return m * A + coprime


def exact_functional_graph_alpha(p, n):
    """Maximum independent set for x -> p*x on the additive group Z/nZ."""
    nxt = [(p * x) % n for x in range(n)]
    rev = [[] for _ in range(n)]
    for x, y in enumerate(nxt):
        if x != y:
            rev[y].append(x)

    state = [0] * n
    cycles = []

    for start in range(n):
        if state[start]:
            continue
        path = []
        pos = {}
        x = start
        while state[x] == 0 and x not in pos:
            pos[x] = len(path)
            path.append(x)
            x = nxt[x]
        if x in pos:
            cyc = path[pos[x]:]
            cycles.append(cyc)
        for v in path:
            state[v] = 1

    cycle_vertices = {v for cyc in cycles for v in cyc}

    def tree_dp(v):
        take = 1
        skip = 0
        for u in rev[v]:
            if u in cycle_vertices:
                continue
            u_take, u_skip = tree_dp(u)
            take += u_skip
            skip += max(u_take, u_skip)
        return take, skip

    total = 0
    for cyc in cycles:
        r = len(cyc)
        dp = [tree_dp(v) for v in cyc]

        if r == 1:
            # A loop forbids its vertex.
            total += dp[0][1]
            continue

        # Maximum weighted independent set on a cycle.
        def path_best(indices, first_taken):
            neg = -10**18
            skip_prev = 0
            take_prev = neg
            for j, idx in enumerate(indices):
                take_w, skip_w = dp[idx]
                if j == 0:
                    if first_taken:
                        take_prev, skip_prev = take_w, neg
                    else:
                        take_prev, skip_prev = neg, skip_w
                    continue
                new_take = skip_prev + take_w
                new_skip = max(skip_prev, take_prev) + skip_w
                take_prev, skip_prev = new_take, new_skip
            return take_prev, skip_prev

        take_end, skip_end = path_best(range(r), False)
        best_first_skip = max(take_end, skip_end)

        take_end, skip_end = path_best(range(r), True)
        # If the first cycle vertex is taken, the last must be skipped.
        best_first_take = skip_end
        total += max(best_first_skip, best_first_take)

    return total


def main():
    checked = 0
    for p in PRIMES:
        for n in range(1, 121):
            exact = exact_functional_graph_alpha(p, n)
            formula = closed_formula(p, n)
            if exact != formula:
                raise AssertionError((p, n, exact, formula))
            checked += 1

    print(f"verified {checked} cyclic prime-power-map cases")
    print(f"s_2(C_20) = {closed_formula(2, 20)}")


if __name__ == "__main__":
    main()
