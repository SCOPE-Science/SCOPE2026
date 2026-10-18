"""Independent small-case verification of a rank-two preconditional enumeration.
Run: python3 verify_rank_two_preconditionals.py (Python standard library)."""
from itertools import product


def lattice(k):
    n = k + 2
    top = n - 1
    def le(x, y):
        return x == y or x == 0 or y == top
    def meet(x, y):
        if le(x, y): return x
        if le(y, x): return y
        return 0
    def join(x, y):
        if le(x, y): return y
        if le(y, x): return x
        return top
    return n, top, le, meet, join


def is_preconditional(op, k):
    n, top, le, meet, _ = lattice(k)
    for a in range(n):
        if not le(op[top][a], a): return False # axiom 1
        for b in range(n):
            if not le(meet(a, b), op[a][b]): return False # axiom 2
            if not le(op[a][b], op[a][meet(a, b)]): return False # axiom 3
            for c in range(n):
                if not le(op[a][meet(b, c)], op[a][b]): return False # axiom 4
                inner = op[meet(a, b)][c]
                if not le(op[a][inner], inner): return False # axiom 5
    return True


def run(k):
    n, top, le, meet, join = lattice(k)
    # Only use axioms 1--4 to reduce the unbounded search to row candidates.
    # The original fifth axiom is then checked directly on every table.
    pairs = {}
    for a in range(1, top):
        pairs[a] = [(u,v) for u in range(n) for v in range(n)
                    if le(u,v) and le(a,v)]
    outcome = [0] * n
    induced = 0
    for t in range(n):
        for selections in product(*(pairs[a] for a in range(1, top))):
            rows = [[t] * n]
            for a, (u, v) in enumerate(selections, start=1):
                rows.append([v if meet(a,b) == a else u for b in range(n)])
            rows.append(list(range(n)))
            if is_preconditional(rows, k):
                outcome[t] += 1
                neg = [rows[a][0] for a in range(n)]
                if (all(le(neg[y],neg[x]) for x in range(n) for y in range(n)
                        if le(x,y)) and all(rows[a][b] == join(neg[a],meet(a,b))
                                          for a in range(n) for b in range(n))):
                    induced += 1
    expected = [2**k] + [2 * (3 ** (k-1))] * k + [(k+3)**k]
    predicted_induced = 1 + k * (2**k) + (k+2)**k
    print('k=',k,'axiom5-complete counts by bottom value=',outcome,
          'induced=',induced,'total=',sum(outcome))
    assert outcome == expected, (outcome,expected)
    assert induced == predicted_induced, (induced,predicted_induced)

if __name__ == '__main__':
    for k in (2,3,4): run(k)
    print('ALL CHECKS PASSED')
