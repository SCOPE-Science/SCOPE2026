#!/usr/bin/env python3
"""Exact-rational checks for the graph criterion for RCMC Type B positivity.

No external packages are required.  The theorem's universal proof is in RESULT.md;
these tests replay matrix identities and sample weighted connected networks.
"""
from fractions import Fraction as Q
from itertools import combinations

COUNT = 0


def check(statement, message="check failed"):
    global COUNT
    COUNT += 1
    if not statement:
        raise AssertionError(message)


def zeros(m, n):
    return [[Q(0) for _ in range(n)] for _ in range(m)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mul(a, b):
    if not a:
        return []
    if not b:
        return zeros(len(a), 0)
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def inv(a):
    n = len(a)
    z = [list(map(Q, a[i])) + [Q(int(i == j)) for j in range(n)]
         for i in range(n)]
    for j in range(n):
        i = next(i for i in range(j, n) if z[i][j])
        z[i], z[j] = z[j], z[i]
        factor = z[j][j]
        z[j] = [v / factor for v in z[j]]
        for i in range(n):
            if i != j:
                factor = z[i][j]
                z[i] = [u - factor * v for u, v in zip(z[i], z[j])]
    return [row[n:] for row in z]


def connected(n, edges):
    reached = {0}
    while True:
        nxt = reached | {v for i, j in edges for v in (i, j)
                         if i in reached or j in reached}
        if nxt == reached:
            return len(reached) == n
        reached = nxt


def safe_graph(n, edges, eliminated):
    s = set(eliminated)
    unseen = set(s)
    while unseen:
        comp = {next(iter(unseen))}
        while True:
            nxt = set(comp)
            for a, b in edges:
                if a in comp and b in s:
                    nxt.add(b)
                if b in comp and a in s:
                    nxt.add(a)
            if nxt == comp:
                break
            comp = nxt
        unseen -= comp
        boundary = set()
        for a, b in edges:
            if a in comp and b not in s:
                boundary.add(b)
            if b in comp and a not in s:
                boundary.add(a)
        if len(boundary) != 1:
            return False
    return True


def calculate(n, edges, eliminated, conductances, pi_raw):
    pi = [Q(a, sum(pi_raw)) for a in pi_raw]
    k = zeros(n, n)
    for (i, j), c in zip(edges, conductances):
        k[i][j] += Q(c) / pi[j]
        k[j][i] += Q(c) / pi[i]
    for j in range(n):
        k[j][j] = -sum(k[i][j] for i in range(n) if i != j)
    s = list(eliminated)
    t = [i for i in range(n) if i not in s]
    css = inv([[k[i][j] for j in s] for i in s])
    c = [[-sum(css[a][b] * k[s[b]][t[j]] for b in range(len(s)))
          for j in range(len(t))] for a in range(len(s))]
    omega = zeros(n, len(t))
    for a, node in enumerate(s):
        omega[node] = c[a][:]
    for j, node in enumerate(t):
        omega[node][j] = Q(1)
    omega_star = [[pi[t[i]] * omega[j][i] / pi[j] for j in range(n)]
                  for i in range(len(t))]
    m = mul(omega_star, omega)
    minv = inv(m)
    d = zeros(len(t), len(t))
    for i in range(len(t)):
        d[i][i] = 1 / sum(m[j][i] for j in range(len(t)))
    va = mul(mul(omega, d), omega_star)
    vb = mul(mul(omega, minv), omega_star)
    return pi, c, m, va, vb, t


def test(n, edges, eliminated, edge_weights, pi_raw):
    pi, c, m, va, vb, t = calculate(n, edges, eliminated, edge_weights, pi_raw)
    graph_ok = safe_graph(n, edges, eliminated)
    positive = all(x >= 0 for row in vb for x in row)
    check(positive == graph_ok, "positivity criterion")
    check((va == vb) == graph_ok, "equality of the two variants")
    check(all(x >= 0 for row in va for x in row), "Type A positivity")
    check(all(sum(va[i][j] for i in range(n)) == 1 for j in range(n)), "Type A mass")
    check(all(sum(vb[i][j] for i in range(n)) == 1 for j in range(n)), "Type B mass")
    check(mul(vb, vb) == vb, "Type B idempotence")
    check(all(sum(vb[i][j] * pi[j] for j in range(n)) == pi[i]
              for i in range(n)), "stationarity")
    if len(t) == 2:
        a, b = t
        alpha, beta = pi[a], pi[b]
        mu = sum(pi[i] for i in eliminated)
        # Exact sharp cross-terminal negativity bound.  Squaring here is safe
        # after checking that the unsquared right side is nonnegative.
        for u, v in ((a, b), (b, a)):
            alpha, beta = pi[u], pi[v]
            eta = -vb[u][v]
            check(eta >= 0, "terminal off-diagonal is nonpositive")
            base = alpha * beta
            rad = alpha * beta * (alpha + mu) * (beta + mu)
            rest = alpha * mu - 2 * eta * base
            check(rest >= 0 and rest * rest >= 4 * eta * eta * rad,
                  "sharp two-terminal bound")
        a, b = t
        # The exact weighted Gram determinant formula.
        probs = [c[j][0] * pi[a] / pi[eliminated[j]]
                 for j in range(len(eliminated))]
        first = sum(pi[i] * probs[j] for j, i in enumerate(eliminated))
        second = sum(pi[i] * probs[j]**2 for j, i in enumerate(eliminated))
        delta = pi[a] * (pi[b] + mu) - 2 * pi[a] * first + second - first**2
        check(-vb[a][b] == pi[a] * (first - second) / delta,
              "exact harmonic-moment formula")
    check(all(m[i][j] >= 0 for i in range(len(t)) for j in range(len(t))), "M positivity")
    check(all((m[i][j] == 0) == (not any(c[a][i] > 0 and c[a][j] > 0
                                              for a in range(len(c))))
              for i in range(len(t)) for j in range(len(t)) if i != j), "M support")
    if graph_ok:
        partition = []
        for terminal in t:
            group = [terminal]
            for node in eliminated:
                if c[eliminated.index(node)][t.index(terminal)] > 0:
                    group.append(node)
            partition.append(group)
        check(sorted(x for group in partition for x in group) == list(range(n)),
              "safe classes partition vertices")
        exact = zeros(n, n)
        for group in partition:
            mass = sum(pi[j] for j in group)
            for i in group:
                for j in group:
                    exact[i][j] = pi[i] / mass
        check(exact == vb == va, "mass-aggregation formula")
    else:
        check(any(vb[i][j] < 0 for i in range(n) for j in range(n)),
              "unsafe graphs admit negative output")


def main():
    edges = [(0, 1), (1, 2)]
    pi, _, _, va, vb, _ = calculate(3, edges, [1], [Q(1, 3)] * 2, [1, 1, 1])
    want = [[Q(5, 6), Q(1, 3), -Q(1, 6)],
            [Q(1, 3), Q(1, 3), Q(1, 3)],
            [-Q(1, 6), Q(1, 3), Q(5, 6)]]
    check(vb == want, "three-vertex exact witness")
    check(not safe_graph(3, edges, [1]), "three-vertex criterion")
    check(va != vb, "three-vertex variant distinction")
    check(vb[0][2] == -Q(1, 6), "sharp uniform three-node defect")
    # Connected symmetric complete bipartite graph with two terminals and m
    # eliminated vertices: each harmonic hitting probability is 1/2.
    for m in range(1, 7):
        n = m + 2
        e = [(0, s) for s in range(2, n)] + [(1, s) for s in range(2, n)]
        _, _, _, _, v, _ = calculate(n, e, list(range(2, n)),
                                     [Q(1, 2)] * len(e), [1] * n)
        check(-v[0][1] == Q(m, 2*(m+2)), "uniform sharpness")
    tested = 0
    for n in range(2, 6):
        possible = list(combinations(range(n), 2))
        limit = 1 << len(possible)
        for mask in range(1, limit):
            # All connected graphs through four nodes; a deterministic 5-node sample.
            if n == 5 and mask % 29 != 0:
                continue
            e = [ij for j, ij in enumerate(possible) if mask & (1 << j)]
            if not connected(n, e):
                continue
            for smask in range(1, (1 << n) - 1):
                s = [i for i in range(n) if smask & (1 << i)]
                w = [Q(1 + ((i * 5 + j * 3 + mask) % 3), 1 + (mask % 2))
                     for i, j in e]
                stationary = [1 + (3 * i + mask) % 5 for i in range(n)]
                test(n, e, s, w, stationary)
                tested += 1
    print(f"VERIFY_OK exact_assertions={COUNT} weighted_graph_cases={tested}")


if __name__ == '__main__':
    main()
