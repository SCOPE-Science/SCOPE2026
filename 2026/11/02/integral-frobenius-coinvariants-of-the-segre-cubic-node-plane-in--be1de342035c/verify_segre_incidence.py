"""Exact integral verification of the 10-node/15-plane Segre incidence theorem.

Requires Python 3.10+ and SymPy >= 1.12.  No external data or network.
The algebraic-geometric identification of the nodes and planes is justified
in the associated mathematical proof and is not inferred from this program.
"""
from itertools import combinations, permutations
from math import prod
from sympy import Matrix, eye, zeros
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form
from sympy.polys.domains import ZZ

V = tuple(range(6))
NODES = sorted(tuple(t) for t in combinations(V, 3) if 0 in t)


def matchings(remaining):
    if not remaining:
        yield ()
        return
    a = remaining[0]
    for j in range(1, len(remaining)):
        b = remaining[j]
        rest = remaining[1:j] + remaining[j+1:]
        for m in matchings(rest):
            yield tuple(sorted(((a, b),) + m))


PLANES = sorted(set(matchings(V)))
assert len(NODES) == 10 and len(PLANES) == 15
INC = Matrix(10, 15, lambda i, j: int(all(len(set(p) & set(NODES[i])) == 1 for p in PLANES[j])))


def normal_node(indices):
    x = set(indices)
    return tuple(sorted(x if 0 in x else set(V) - x))


def node_action(g):
    return tuple(NODES.index(normal_node(g[k] for k in t)) for t in NODES)


def plane_action(g):
    return tuple(PLANES.index(tuple(sorted(tuple(sorted((g[a], g[b]))) for a, b in m))) for m in PLANES)


def perm_matrix(action):
    out = zeros(len(action), len(action))
    for i, j in enumerate(action):
        out[j, i] = 1
    return out


def mod2_rank(mat):
    a = [[int(mat[i, j]) & 1 for j in range(mat.cols)] for i in range(mat.rows)]
    rank = 0
    for j in range(mat.cols):
        pivot = next((i for i in range(rank, mat.rows) if a[i][j]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for i in range(mat.rows):
            if i != rank and a[i][j]:
                a[i] = [x ^ y for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == mat.rows:
            break
    return rank


def invariant_factors(mat):
    d = smith_normal_form(mat, domain=ZZ)
    return tuple(abs(int(d[i, i])) for i in range(min(d.rows, d.cols)) if abs(int(d[i, i])) > 1)


def cycle_representative(parts):
    g = list(V)
    pos = 0
    for length in parts:
        for k in range(length):
            g[pos+k] = pos + (k+1) % length
        pos += length
    assert pos == 6
    return tuple(g)


def partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    if maximum is None:
        maximum = n
    for k in range(min(n, maximum), 0, -1):
        for remaining in partitions(n-k, k):
            yield (k,) + remaining


assert (INC * INC.T) == (4*eye(10) + 2*Matrix.ones(10, 10))
assert all(sum(INC.row(i)) == 6 for i in range(10))
assert all(sum(INC.col(j)) == 4 for j in range(15))
assert mod2_rank(INC) == 5
certificate = (0, 1, 2, 3, 4, 5, 6, 7, 9, 12)
assert INC[:, list(certificate)].det() == 64
assert invariant_factors(INC) == (2, 2, 2, 2, 4)
# Separate HNF test: the full integral image has index 2^6.
assert abs(int(hermite_normal_form(INC).det())) == 64

# Node triple indicators map to F_2^6 / <all-ones>.  The maps have
# full quotient dimension, and each plane is sent to zero mod 2.
indicator = Matrix(6, 10, lambda i, j: int(i in NODES[j]))
assert all(int((indicator*INC)[i, j]) % 2 == 0 for i in range(6) for j in range(15))
assert mod2_rank(indicator) == 5
assert mod2_rank(indicator.row_join(Matrix.ones(6, 1))) == 6

# All 720 S_6 permutations preserve the geometric incidence relation.
for g in permutations(V):
    A = perm_matrix(node_action(g))
    B = perm_matrix(plane_action(g))
    assert A * INC == INC * B
    # Triple-indicator map equivariance in the quotient by the all-ones vector:
    for t_index, new_index in enumerate(node_action(g)):
        old_t = NODES[t_index]
        gg = [int(i in [g[t] for t in old_t]) for i in V]
        new_t = [int(i in NODES[new_index]) for i in V]
        diff = [x ^ y for x, y in zip(gg, new_t)]
        assert diff == [0]*6 or diff == [1]*6

print('INCIDENCE_OK: 10 nodes, 15 planes, 720 S6 equivariances, Smith 2^4 + 4, minor 64')
print('CYCLE_TYPE | INVARIANT_FACTORS | CYCLIC_ORDER_4 | N_CYCLES | EVEN_CYCLES_ONLY')
for typ in partitions(6):
    g = cycle_representative(typ)
    n_cyc = len(typ)
    delta = int(any(k % 2 for k in typ))
    predicted = (2,)*(n_cyc - delta - 1) + (4,)
    action = perm_matrix(node_action(g))
    matrix = INC.row_join(action-eye(10))
    got = invariant_factors(matrix)
    assert got == predicted, (typ, got, predicted)
    assert abs(int(hermite_normal_form(matrix).det())) == prod(predicted)
    assert mod2_rank(matrix) == 10 - (n_cyc-delta)
    print(f'{typ} | {got} | 4 | {n_cyc} | {delta == 0}')
print('VERIFY_OK: all 11 Galois cycle types match the uniform formula')
