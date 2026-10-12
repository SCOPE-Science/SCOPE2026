#!/usr/bin/env python3
from itertools import combinations


def graph_edges(m, n, t):
    return tuple((i, j) for i in range(m) for j in range(n)
                 if not (i == j and i < t))


def maximal_matchings(m, n, t):
    edge_set = set(graph_edges(m, n, t))
    out = []

    def rec(a, used_b, matching):
        if a == m:
            used_a = {x for x, _ in matching}
            ua = [x for x in range(m) if x not in used_a]
            ub = [y for y in range(n) if y not in used_b]
            if all((x, y) not in edge_set for x in ua for y in ub):
                out.append(tuple(matching))
            return
        rec(a + 1, used_b, matching)
        for b in range(n):
            if b not in used_b and (a, b) in edge_set:
                used_b.add(b)
                matching.append((a, b))
                rec(a + 1, used_b, matching)
                matching.pop()
                used_b.remove(b)

    rec(0, set(), [])
    return out


def predicted_eis(m, n, t):
    return m - 1 if m == n and t >= 3 else m


def verify_case(m, n, t):
    edges = graph_edges(m, n, t)
    matchings = maximal_matchings(m, n, t)
    assert edges
    local = {}
    for e in edges:
        sizes = [len(M) for M in matchings if e in M]
        assert sizes, (m, n, t, e, 'edge is in no maximal matching')
        local[e] = min(sizes)
    actual = max(local.values())
    assert actual == predicted_eis(m, n, t), (m, n, t, actual, predicted_eis(m, n, t))

    # The proof's stronger assertions.
    if m < n:
        assert set(len(M) for M in matchings) == {m}, (m, n, t)
        assert set(local.values()) == {m}, (m, n, t)
    elif t >= 3:
        assert set(local.values()) == {m - 1}, (m, n, t, local)
    else:
        # At least one forcing edge needs a perfect maximal matching.
        assert max(local.values()) == m, (m, n, t, local)

    return len(edges), len(matchings)


def main():
    parameter_cases = 0
    edge_checks = 0
    maximal_matching_checks = 0
    for m in range(2, 7):
        for n in range(m, 7):
            for t in range(m + 1):
                ecount, mcount = verify_case(m, n, t)
                parameter_cases += 1
                edge_checks += ecount
                maximal_matching_checks += mcount
    print(
        'ALL CHECKS PASSED; '
        f'parameter_cases={parameter_cases}; '
        f'edge_checks={edge_checks}; '
        f'maximal_matchings={maximal_matching_checks}; '
        'range=2<=m<=n<=6; 0<=t<=m'
    )


if __name__ == '__main__':
    main()
