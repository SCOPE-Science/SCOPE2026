"""Reproduce exact proper conflict-free colouring claims for Mobius ladders.

Uses the standard library only.  A characteristic polynomial is computed
exactly by the Faddeev-LeVerrier identities, not fitted to sample counts.
"""
from itertools import permutations, product
from collections import defaultdict

COLORS = tuple(range(4))
COL = tuple(permutations(COLORS, 2))


def swap(p):
    return p[1], p[0]


def adjacent(a, b):
    return a[0] != b[0] and a[1] != b[1]


def locally_valid(a, b, c):
    return (adjacent(a, b) and adjacent(b, c)
            and not (a[0] == c[0] == b[1])
            and not (a[1] == c[1] == b[0]))


STATES = tuple((a, b) for a in COL for b in COL if adjacent(a, b))
INDEX = {s: i for i, s in enumerate(STATES)}

def swap_state(s):
    return swap(s[0]), swap(s[1])


ORBIT_REPS = tuple(sorted(set(min(s, swap_state(s)) for s in STATES)))


def transfer_edges():
    edges = []
    for a, b in STATES:
        i = INDEX[(a, b)]
        for c in COL:
            if locally_valid(a, b, c):
                edges.append((i, INDEX[(b, c)]))
    return tuple(edges)


EDGES = transfer_edges()
NEXT = [[] for _ in STATES]
for _i, _j in EDGES:
    NEXT[_i].append(_j)
EDGE_SET = {(STATES[i], STATES[j]) for i, j in EDGES}


def transfer_blocks():
    # On each orbit span, e_rep +/- e_swap(rep) is an eigenvector of row exchange.
    plus = []
    minus = []
    for u in ORBIT_REPS:
        prow = []
        mrow = []
        for v in ORBIT_REPS:
            x = int((u, v) in EDGE_SET)
            y = int((u, swap_state(v)) in EDGE_SET)
            prow.append(x + y)
            mrow.append(x - y)
        plus.append(prow)
        minus.append(mrow)
    return plus, minus


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_pow(a, k):
    z = [1]
    for _ in range(k):
        z = poly_mul(z, a)
    return z


def characteristic_polynomial(a):
    """Monic coefficients descending, via Faddeev-LeVerrier over Z."""
    n = len(a)
    m = [[int(i == j) for j in range(n)] for i in range(n)]
    coeff = [1]
    sparse = [[(j, x) for j, x in enumerate(row) if x] for row in a]
    for k in range(1, n + 1):
        nxt = [[0] * n for _ in range(n)]
        for i, row in enumerate(sparse):
            for j, val in row:
                old = m[j]
                dest = nxt[i]
                for h, x in enumerate(old):
                    if x:
                        dest[h] += val * x
        tr = sum(nxt[i][i] for i in range(n))
        assert tr % k == 0, (k, tr)
        c = -(tr // k)
        coeff.append(c)
        for i in range(n):
            nxt[i][i] += c
        m = nxt
    return coeff


def expected_charpoly_plus():
    # Polynomials in ascending order, then reversed.
    p = [1]
    for factor, power in (
        ([-1, 1], 3),
        ([-2, 0, -1, 1], 2),
        ([4, -6, -4, 1], 1),
        ([4, -2, 6, 3, 1], 3),
    ):
        p = poly_mul(p, poly_pow(factor, power))
    p = [0] * 18 + p
    return p[::-1]


def expected_charpoly_minus():
    p = [1]
    for factor, power in (
        ([-2, 1], 1),
        ([-1, 1], 3),
        ([1, 1], 2),
        ([2, 1, 1], 3),
    ):
        p = poly_mul(p, poly_pow(factor, power))
    p = [0] * 30 + p
    return p[::-1]


def trace_power(mat, n):
    # Explicit row-by-row multiplication against a sparse matrix.
    k = len(mat)
    edges = [[(j, x) for j, x in enumerate(row) if x]
             for row in mat]
    x = [[int(i == j) for j in range(k)] for i in range(k)]
    for _ in range(n):
        y = [[0] * k for _ in range(k)]
        for i, row in enumerate(x):
            dest = y[i]
            for j, val in enumerate(row):
                if val:
                    for h, weight in edges[j]:
                        dest[h] += val * weight
        x = y
    return sum(x[i][i] for i in range(k))


def graph_neighbours(m, twisted):
    n = 2 * m
    out = [set() for _ in range(n)]
    def edge(u, v):
        out[u].add(v)
        out[v].add(u)
    for i in range(m):
        edge(i, m+i)
        if i < m-1:
            edge(i, i+1)
            edge(m+i, m+i+1)
    if twisted:
        edge(m-1, m)
        edge(2*m-1, 0)
    else:
        edge(m-1, 0)
        edge(2*m-1, m)
    assert all(len(row) == 3 for row in out)
    return out


def is_valid_colouring(colors, nbr):
    for v, ns in enumerate(nbr):
        if any(colors[v] == colors[w] for w in ns):
            return False
        found_unique = any(sum(colors[w] == colors[x] for x in ns) == 1
                           for w in ns)
        if not found_unique:
            return False
    return True


def explicit_four_colouring(m):
    a, b, c, d = (0, 1), (1, 0), (2, 3), (3, 2)
    q, r = divmod(m, 3)
    assert q >= 1
    cols = [a, b, c] * q
    if r == 1:
        cols += [d]
    if r == 2:
        cols += [a, c]
    return tuple(x[0] for x in cols) + tuple(x[1] for x in cols)


def direct_count(m, k, twisted):
    nbr = graph_neighbours(m, twisted)
    return sum(is_valid_colouring(col, nbr)
               for col in product(range(k), repeat=2*m))


def cyclic_trace_count(m, twisted):
    # Counts closed/row-exchanged m-step walks in the 84-state transfer.
    total = 0
    for u in STATES:
        start = INDEX[u]
        dp = {start: 1}
        for _ in range(m):
            nxt = defaultdict(int)
            for x, weight in dp.items():
                for j in NEXT[x]:
                    nxt[j] += weight
            dp = nxt
        total += dp.get(INDEX[swap_state(u) if twisted else u], 0)
    return total


def lucas_at(m):
    a, b = 2, -1
    for _ in range(m):
        a, b = b, -b - 2*a
    return a


def main():
    assert len(STATES) == 84
    assert len(ORBIT_REPS) == 42
    assert len(EDGES) == 384
    plus, minus = transfer_blocks()
    pc = characteristic_polynomial(plus)
    mc = characteristic_polynomial(minus)
    assert pc == expected_charpoly_plus()
    assert mc == expected_charpoly_minus()
    print('EXACT_42x42_CHARACTERISTIC_POLYNOMIALS_OK')

    # The fixed four-symbol pattern gives a direct witness for every length.
    for m in range(3, 301):
        w = explicit_four_colouring(m)
        assert is_valid_colouring(w, graph_neighbours(m, True))
        assert is_valid_colouring(w, graph_neighbours(m, False))
    print('BOTH_BOUNDARY_4_COLOUR_WITNESSES_OK 298')

    # Independent brute force: the graph is built from its edge definition.
    for m in (3, 4):
        for twist in (False, True):
            assert direct_count(m, 4, twist) == cyclic_trace_count(m, twist)
            assert direct_count(m, 3, twist) == (12 if (not twist and m % 3 == 0) else 0)
    print('DIRECT_GRAPH_BRUTE_FORCE_COUNTS_OK 4')

    # Check exact twist correction against transfer counts, independently of
    # the characteristic-polynomial computation above.
    for m in range(3, 31):
        cylinder = cyclic_trace_count(m, False)
        mobius = cyclic_trace_count(m, True)
        difference = 2 ** (m + 1) + 6 + 4 * ((-1) ** m) + 6 * lucas_at(m)
        assert cylinder - mobius == difference
        assert mobius > 0
    print('TWIST_TRACE_AND_LUCAS_CORRECTION_OK 28')
    print('COUNTS_MOBIUS_3_TO_7', [cyclic_trace_count(m, True) for m in range(3, 8)])
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
