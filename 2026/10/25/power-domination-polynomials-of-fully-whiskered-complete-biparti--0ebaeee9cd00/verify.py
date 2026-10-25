"""Independent adjacency-rule verification of the bipartite one-leaf-corona enumeration."""
from collections import Counter
from math import comb


def p_add(*series):
    result = Counter()
    for coeff in series:
        for k, v in coeff.items():
            result[k] += v
    return {k: v for k, v in result.items() if v}


def p_mul(a, b):
    result = Counter()
    for i, x in a.items():
        for j, y in b.items():
            result[i+j] += x*y
    return dict(result)


def p_sub(a, b):
    return {k: a.get(k, 0)-b.get(k, 0) for k in a.keys() | b.keys() if a.get(k, 0) != b.get(k, 0)}


def one_plus(n):
    return {k: comb(n, k) for k in range(n+1)}


def touched(n):
    # Every private pair contributes a nonempty subset of size one or two.
    a = {0: 1}
    for _ in range(n):
        a = p_mul(a, {1: 2, 2: 1})
    return a


def closed_polynomial(p, q):
    def f(n): return p_sub(one_plus(2*n), one_plus(n))
    def a(n): return p_sub(touched(n), {n: 1})
    def b(n): return {k: n*v for k, v in p_sub(touched(n-1), {n-1: 1}).items()}
    def c(n): return {n-1: n, n: 1}
    return p_add(
        p_mul(f(p), f(q)),
        p_mul(a(p), one_plus(q)),
        p_mul(b(p), p_sub(one_plus(q), {0: 1})),
        p_mul(a(q), one_plus(p)),
        p_mul(b(q), p_sub(one_plus(p), {0: 1})),
        p_mul(c(p), c(q)),
    )


def adjacency(p, q):
    n = p + q
    graph = [set() for _ in range(2*n)]
    for i in range(p):
        for j in range(p, n):
            graph[i].add(j)
            graph[j].add(i)
    for i in range(n):
        graph[i].add(n+i)
        graph[n+i].add(i)
    return graph


def power_dominates(graph, selected):
    seen = set(selected)
    for v in selected:
        seen.update(graph[v])
    while True:
        if len(seen) == len(graph):
            return True
        new = set()
        for v in seen:
            remaining = graph[v] - seen
            if len(remaining) == 1:
                new.update(remaining)
        if not new:
            return False
        seen |= new


def exhaustive(p, q):
    g = adjacency(p, q)
    distribution = Counter()
    for bits in range(1 << len(g)):
        selected = {v for v in range(len(g)) if bits & (1 << v)}
        if power_dominates(g, selected):
            distribution[len(selected)] += 1
    return dict(distribution)


def minimum_count(p, q):
    if p == q == 2:
        return 22
    if min(p, q) == 2:
        return 4*max(p, q)+3
    return p*q


def main():
    cases = [(2,2), (2,3), (2,4), (2,5), (3,3), (3,4), (3,5), (4,4)]
    total_subsets = 0
    for p, q in cases:
        exact = exhaustive(p, q)
        closed = closed_polynomial(p, q)
        assert exact == closed, (p, q, exact, closed)
        assert min(exact) == 2, (p, q, min(exact))
        assert exact[2] == minimum_count(p, q), (p, q, exact[2])
        assert sum(exact.values()) == sum(closed.values())
        total_subsets += 1 << (2*(p+q))
        print(f"K_{{{p},{q}}} corona K_1: size={2*(p+q)}, subsets={1 << (2*(p+q))}, success={sum(exact.values())}, min_count={exact[2]}, MATCH")
    for p in range(2, 21):
        for q in range(2, 21):
            poly = closed_polynomial(p, q)
            assert min(poly) == 2 and poly[2] == minimum_count(p, q)
            assert all(v > 0 for v in poly.values())
    print(f"VERIFY_OK: {len(cases)} graphs; {total_subsets} exhaustively checked subsets; 361 symbolic parameter pairs")


if __name__ == "__main__":
    main()
