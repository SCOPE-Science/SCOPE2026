from collections import deque
from itertools import product


def reachable(n, trans, start=0):
    seen = {start}
    todo = deque([start])
    while todo:
        p = todo.popleft()
        for a in range(2):
            q = trans[a][p]
            if q not in seen:
                seen.add(q)
                todo.append(q)
    return seen


def distinguishability(n, trans, finals):
    """Exact right-language distinguishability by product reachability."""
    ans = [[False] * n for _ in range(n)]
    for p in range(n):
        for q in range(n):
            seen = {(p, q)}
            todo = deque([(p, q)])
            while todo:
                x, y = todo.popleft()
                if ((x in finals) != (y in finals)):
                    ans[p][q] = True
                    break
                for a in range(2):
                    z = (trans[a][x], trans[a][y])
                    if z not in seen:
                        seen.add(z)
                        todo.append(z)
    return ans


def semantic_alphabetic(n, trans, finals, start=0):
    dist = distinguishability(n, trans, finals)
    for p in reachable(n, trans, start):
        for a in range(2):
            pa = trans[a][p]
            paa = trans[a][pa]
            if dist[pa][paa]:
                return False
        pab = trans[1][trans[0][p]]
        pba = trans[0][trans[1][p]]
        if dist[pab][pba]:
            return False
    return True


def minimized_alphabetic(n, trans, finals, start=0):
    """Build the reachable Myhill quotient, then test literal semilattice identities."""
    dist = distinguishability(n, trans, finals)
    states = sorted(reachable(n, trans, start))
    reps = []
    cls = {}
    for p in states:
        for i, r in enumerate(reps):
            if not dist[p][r]:
                cls[p] = i
                break
        else:
            cls[p] = len(reps)
            reps.append(p)

    mt = [[0] * len(reps) for _ in range(2)]
    for i, r in enumerate(reps):
        for a in range(2):
            mt[a][i] = cls[trans[a][r]]

    for p in range(len(reps)):
        for a in range(2):
            if mt[a][mt[a][p]] != mt[a][p]:
                return False
        if mt[1][mt[0][p]] != mt[0][mt[1][p]]:
            return False
    return True


def check_small_dfas():
    total = 0
    accepted = 0
    for n in (1, 2, 3):
        subtotal = 0
        good = 0
        for t0 in product(range(n), repeat=n):
            for t1 in product(range(n), repeat=n):
                trans = (t0, t1)
                for mask in range(1 << n):
                    finals = {i for i in range(n) if (mask >> i) & 1}
                    a = semantic_alphabetic(n, trans, finals)
                    b = minimized_alphabetic(n, trans, finals)
                    if a != b:
                        raise AssertionError((n, trans, finals, a, b))
                    subtotal += 1
                    good += int(a)
        print(f"dfa n={n}: instances={subtotal}, alphabetic={good}")
        total += subtotal
        accepted += good
    print(f"dfa total: instances={total}, alphabetic={accepted}")
    return total


def graph_reachable(n, edge0, edge1, s, t):
    seen = {s}
    todo = deque([s])
    while todo:
        v = todo.popleft()
        for edges in (edge0, edge1):
            w = edges[v]
            if w is not None and w not in seen:
                seen.add(w)
                todo.append(w)
    return t in seen


def reduction_dfa(n, edge0, edge1, s, t):
    sink = n
    trans = []
    for edges in (edge0, edge1):
        row = []
        for v in range(n):
            if v == t or edges[v] is None:
                row.append(sink)
            else:
                row.append(edges[v])
        row.append(sink)
        trans.append(tuple(row))
    return n + 1, tuple(trans), {t}, s


def check_reduction():
    checked = 0
    for n in (2, 3):
        vals = list(range(n)) + [None]
        subtotal = 0
        for edge0 in product(vals, repeat=n):
            for edge1 in product(vals, repeat=n):
                for s in range(n):
                    for t in range(n):
                        if s == t:
                            continue
                        r = graph_reachable(n, edge0, edge1, s, t)
                        N, trans, finals, start = reduction_dfa(n, edge0, edge1, s, t)
                        a = semantic_alphabetic(N, trans, finals, start)
                        if a != (not r):
                            raise AssertionError((n, edge0, edge1, s, t, r, a))
                        subtotal += 1
        print(f"reduction n={n}: graph-instances={subtotal}")
        checked += subtotal
    print(f"reduction total: graph-instances={checked}")
    return checked


if __name__ == "__main__":
    d = check_small_dfas()
    g = check_reduction()
    assert d == 5898
    assert g == 24738
    print("PASS")
