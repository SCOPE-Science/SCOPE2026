"""Exact finite checks for graph-edge averaging hulls and generating radii.

Standard-library checks of the support-function formula are exhaustive over
all simple graphs on 2--5 labeled vertices and a deterministic finite set of
integer-valued dual functionals. These checks supplement, not replace,
the all-dimensional proof.
"""
from itertools import combinations, product
from fractions import Fraction


def allowed_signs(n, edges):
    return [s for s in product((-1, 1), repeat=n)
            if any(s[i] == s[j] for i, j in edges)]


def bipartite(n, edges):
    neighbors = [[] for _ in range(n)]
    for i, j in edges:
        neighbors[i].append(j)
        neighbors[j].append(i)
    color = [0] * n
    for root in range(n):
        if color[root]:
            continue
        color[root] = 1
        queue = [root]
        for u in queue:
            for v in neighbors[u]:
                if color[v] == color[u]:
                    return False
                if color[v] == 0:
                    color[v] = -color[u]
                    queue.append(v)
    return True


def predicted_support(a, n, edges):
    s = [1 if x >= 0 else -1 for x in a]
    total = sum(abs(x) for x in a)
    if any(s[i] == s[j] for i, j in edges):
        return total
    active = {v for e in edges for v in e}
    return total - 2 * min(abs(a[v]) for v in active)


def main():
    graph_count = 0
    cases = 0
    for n in range(2, 6):
        pairs = list(combinations(range(n), 2))
        # All nonempty simple graphs on n labelled vertices.
        for mask in range(1, 1 << len(pairs)):
            edges = [e for j, e in enumerate(pairs) if (mask >> j) & 1]
            active = {v for e in edges for v in e}
            signs = allowed_signs(n, edges)
            assert signs
            radius = Fraction(1, 1) if not bipartite(n, edges) else Fraction(len(active)-2, len(active))
            assert 0 <= radius <= 1
            # Check both universal lower bound and an explicit sharp dual witness
            # on all vertices of the dual l_1-ball, including every proper coloring.
            # The proof establishes all dual vectors; tests check a rich exact grid.
            test_a = []
            if n <= 4:
                test_a = list(product((-2, -1, 0, 1, 2), repeat=n))
            else:
                test_a = [tuple(((i * (2*v+3) + v*v) % 7)-3 for v in range(n)) for i in range(83)]
                test_a.extend(product((-1, 1), repeat=n))
            for a in test_a:
                if not any(a):
                    continue
                h = max(sum(ai*si for ai,si in zip(a,s)) for s in signs)
                assert h == predicted_support(a, n, edges), (n, edges, a, h)
                assert Fraction(h, sum(abs(x) for x in a)) >= radius, (n, edges, a, h, radius)
                cases += 1
            if bipartite(n, edges):
                neighbors = [[] for _ in range(n)]
                for u, v in edges:
                    neighbors[u].append(v)
                    neighbors[v].append(u)
                c = [0] * n
                for root in range(n):
                    if c[root] != 0:
                        continue
                    c[root] = 1
                    queue = [root]
                    for u in queue:
                        for v in neighbors[u]:
                            if c[v] == 0:
                                c[v] = -c[u]
                                queue.append(v)
                witness = [c[v] if v in active else 0 for v in range(n)]
                h = max(sum(witness[v]*s[v] for v in range(n)) for s in signs)
                assert Fraction(h, len(active)) == radius
            graph_count += 1
        print(f"n={n}: all nonempty labeled simple graphs checked",flush=True)
    print(f"PASS: {graph_count} graphs, {cases} exact support inequalities, and all bipartite sharp witnesses")


if __name__ == '__main__':
    main()
