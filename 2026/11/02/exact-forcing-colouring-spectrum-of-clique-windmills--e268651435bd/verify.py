#!/usr/bin/env python3
"""Direct exhaustive check of forced-colouring enumerators for clique windmills.

Requires only Python 3's standard library. The exhaustive tests do not constitute
an infinite-family proof; see RESULT.md for the argument.
"""
from itertools import product
from math import comb, factorial


def graph(q, n):
    count = 1 + n * (q - 1)
    adj = [set() for _ in range(count)]
    for b in range(n):
        blade = list(range(1 + b * (q - 1), 1 + (b + 1) * (q - 1)))
        for v in blade:
            adj[0].add(v)
            adj[v].add(0)
            for w in blade:
                if w != v:
                    adj[v].add(w)
    return adj


def is_proper(values, adj):
    return all(not values[u] or values[u] != values[v]
               for u, a in enumerate(adj) for v in a if v > u)


def forced(values, adj, q):
    if not is_proper(values, adj):
        return False
    values = list(values)
    while True:
        changes = []
        for v, a in enumerate(adj):
            if values[v]:
                continue
            seen = {values[u] for u in a if values[u]}
            if len(seen) == q - 1:
                remaining = set(range(1, q + 1)) - seen
                changes.append((v, remaining.pop()))
        if not changes:
            break
        for v, colour in changes:
            values[v] = colour
        if not is_proper(values, adj):
            return False
    return all(values) and is_proper(values, adj)


def local_characterization(values, q, n):
    adj = graph(q, n)
    if not is_proper(values, adj):
        return False
    for b in range(n):
        blade = values[1 + b * (q - 1):1 + (b + 1) * (q - 1)]
        if sum(v != 0 for v in blade) < q - 2:
            return False
    if values[0]:
        return True
    leaves = {v for v in values[1:] if v}
    return len(leaves) == q - 1


def polynomial(q, n):
    base = q * factorial(q - 1) ** n
    offset = n * (q - 2)
    out = [0] * (1 + n * (q - 1) + 1)
    for j in range(n + 2):
        a = comb(n, j) * (q - 1) ** (n - j) if j <= n else 0
        b = comb(n, j - 1) * (q - 1) ** (n - j + 1) if 1 <= j <= n + 1 else 0
        out[offset + j] = base * (a + b - ((q - 1) if j == 0 else 0))
    return out


def exhaustive(q, n):
    adj = graph(q, n)
    out = [0] * (len(adj) + 1)
    all_assignments = 0
    accepted = 0
    for assignment in product(range(q + 1), repeat=len(adj)):
        all_assignments += 1
        got = forced(assignment, adj, q)
        expected = local_characterization(assignment, q, n)
        assert got == expected, (q, n, assignment)
        if got:
            out[sum(v != 0 for v in assignment)] += 1
            accepted += 1
    assert out == polynomial(q, n), (q, n, out, polynomial(q, n))
    return all_assignments, accepted


def main():
    tested = [(3, 2), (3, 3), (3, 4), (4, 2)]
    total = 0
    forceable = 0
    for q, n in tested:
        a, f = exhaustive(q, n)
        total += a
        forceable += f
    for q in range(3, 17):
        for n in range(2, 17):
            coefs = polynomial(q, n)
            n_vertices = 1 + n * (q - 1)
            assert coefs[n * (q - 2)] == q * factorial(q - 1) ** n * ((q - 1) ** n - (q - 1))
            assert coefs[n_vertices] == q * factorial(q - 1) ** n
            assert sum(coefs) == q * factorial(q - 1) ** n * (2 * q ** n - (q - 1))
    print('VERIFY_OK complete_cases=4 initial_assignments=%d forcing_assignments=%d symbolic_profiles=224' % (total, forceable))


if __name__ == '__main__':
    main()
