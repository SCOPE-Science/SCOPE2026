"""Exact finite checks for the six-cycle weak rainbow saturation construction.

No external packages. A collision pattern is a partial matching between old
and new edges, since colors are injective separately on these two sets.
At each insertion, a bad coloring exists iff such a matching hits the
old/new pair clause of every C4 containing that insertion.
"""

from itertools import combinations, permutations, product


def edge(u, v):
    return tuple(sorted((u, v)))


def construction(q, t):
    old = set(combinations(range(q), 2))
    gadgets = [tuple(range(q + 5*i, q + 5*i + 5)) for i in range(t)]
    for a, b, c, d, e in gadgets:
        cycle = (0, a, b, c, d, e, 0)
        old.update(edge(u, v) for u, v in zip(cycle, cycle[1:]))
    present = set(old)
    order = []

    def add(u, v, stage):
        uv = edge(u, v)
        if uv not in present:
            present.add(uv)
            order.append((uv, stage))

    centers = [g[2] for g in gadgets]
    for c in centers:
        add(0, c, 1)
    for c in centers:
        for x in range(1, q):
            add(c, x, 2)
    for c, f in combinations(centers, 2):
        add(c, f, 3)
    for a, b, c, d, e in gadgets:
        for w in (b, d):
            for x in range(1, q):
                add(w, x, 4)
    for a, b, c, d, e in gadgets:
        for w in (b, d):
            for s in centers:
                add(w, s, 5)
    for a, b, c, d, e in gadgets:
        for w in (b, d):
            add(0, w, 6)
    for a, b, c, d, e in gadgets:
        for w in (a, e):
            for x in range(1, q):
                add(w, x, 7)
    for u, v in combinations(range(q, q + 5*t), 2):
        add(u, v, 8)
    n = q + 5*t
    assert len(present) == n*(n-1)//2
    assert len(old) == q*(q-1)//2 + 6*t
    return n, old, order


def blocking_matching(clauses):
    """Return a matching satisfying all positive clauses, or None if UNSAT."""
    clauses = tuple(set(map(frozenset, clauses)))

    def search(todo, chosen):
        if not todo:
            return chosen
        clause = min(todo, key=len)
        if not clause:
            return None
        for o, a in sorted(clause):
            remaining = []
            for other in todo:
                if (o, a) in other:
                    continue
                remaining.append(frozenset((p, b) for p, b in other
                                           if p != o and b != a))
            answer = search(remaining, chosen + [(o, a)])
            if answer is not None:
                return answer
        return None

    return search(clauses, [])


def clauses_at(n, old, present, uv):
    """Enumerate paths directly, without using the proposed proof witnesses."""
    u, v = uv
    clauses = []
    for x in range(n):
        if x in uv or edge(u, x) not in present:
            continue
        for y in range(n):
            if y in (u, v, x):
                continue
            path = {edge(u, x), edge(x, y), edge(y, v)}
            if not path <= present:
                continue
            cycle = path | {uv}
            clauses.append(frozenset((o, a) for o in cycle & old
                                     for a in cycle - old))
    return clauses


def check(q, t):
    n, old, order = construction(q, t)
    present = set(old)
    for step, (uv, stage) in enumerate(order):
        bad = blocking_matching(clauses_at(n, old, present, uv))
        if bad is not None:
            # Independently instantiate this counterexample and enumerate cycles.
            colors = {e: i for i, e in enumerate(sorted(old))}
            colors.update({e: len(old)+i for i, (e, _) in enumerate(order)})
            for o, a in bad:
                colors[a] = colors[o]
            assert len({colors[e] for e, _ in order}) == len(order)
            assert not any(
                all(e in present for e in (edge(uv[0], x), edge(x, y), edge(y, uv[1])))
                and len({colors[e] for e in (uv, edge(uv[0], x), edge(x, y), edge(y, uv[1]))}) == 4
                for x, y in permutations(set(range(n))-set(uv), 2)
            )
            return {"q": q, "t": t, "n": n, "pass": False,
                    "step": step, "stage": stage, "edge": uv, "matching": bad}
        present.add(uv)
    return {"q": q, "t": t, "n": n, "old_edges": len(old),
            "insertions": len(order), "pass": True}


if __name__ == "__main__":
    # A collision clause and incompatible matching choices sanity-check the solver.
    assert blocking_matching([]) == []
    assert blocking_matching([set()]) is None
    assert blocking_matching([{(0, 0)}, {(0, 1)}]) is None
    assert blocking_matching([{(0, 0)}, {(1, 1)}]) is not None
    # Exhaustive independent truth-table check on all triples of 2-by-2 clauses.
    pairs = list(product(range(2), repeat=2))
    subsets = [{p for i, p in enumerate(pairs) if mask & (1 << i)}
               for mask in range(16)]
    matchings = [s for s in subsets
                 if len({o for o, a in s}) == len(s)
                 and len({a for o, a in s}) == len(s)]
    for clauses in product(subsets, repeat=3):
        expected = any(all(m & clause for clause in clauses) for m in matchings)
        assert (blocking_matching(clauses) is not None) == expected
    print("PASS: all 4096 triples of 2-by-2 collision clauses", flush=True)
    for q, t in [(5, 1), (5, 2), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (5, 4)]:
        result = check(q, t)
        print(result, flush=True)
        if q >= 5 and t >= 3:
            assert result["pass"]
    # Compare the constructed edge count to its formula and the cited bound.
    for n in [40, 100, 1000, 10000]:
        q = 5 + n % 5
        t = (n-q)//5
        count = q*(q-1)//2 + 6*t
        assert 5*count == 6*n + 5*q*(q-1)//2 - 6*q
        assert 5*count <= 6*n + 126
        # Bo--Lian--Liu Theorem 1.5 at ell=4: 4(n-16)/3 + binom(24,2).
        prior_numerator = 4*(n-16) + 3*276
        assert 3*count < prior_numerator
        print({"n": n, "construction": count,
               "prior_upper_bound": f"{prior_numerator}/3"}, flush=True)
