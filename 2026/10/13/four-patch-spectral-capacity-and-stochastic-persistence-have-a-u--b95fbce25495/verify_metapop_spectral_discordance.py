"""Exact finite certificates for spectral-vs-extinction-time rankings.

Standard-library only. Every polynomial has integer coefficients in ascending
powers of the colonization rate. Determinants use the Leibniz permutation sum
organized by row and column-subset dynamic programming.
"""
from fractions import Fraction
from itertools import combinations, permutations

PAW = ((0, 1), (0, 2), (0, 3), (1, 2))
CYCLE = ((0, 1), (1, 2), (2, 3), (0, 3))
STAR = ((0, 1), (0, 2), (0, 3))
PATH = ((0, 1), (1, 2), (2, 3))


def canon(poly):
    p = list(poly)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def add(a, b):
    z = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        z[i] += x
    for i, x in enumerate(b):
        z[i] += x
    return canon(z)


def neg(a):
    return tuple(-v for v in a)


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    z = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                z[i + j] += x * y
    return canon(z)


def mul_const(a, k):
    return canon(tuple(k * t for t in a))


def polynomial(descending):
    return canon(tuple(reversed(descending)))


def eval_poly(p, t):
    out = 0
    for a in reversed(p):
        out = out * t + a
    return out


def determinant(mat):
    """Exact polynomial determinant by signed permutation subset DP."""
    n = len(mat)
    dp = {0: (1,)}
    for i in range(n):
        ndp = {}
        for used, coeff in dp.items():
            for j in range(n):
                if used & (1 << j):
                    continue
                term = mat[i][j]
                if not any(term):
                    continue
                prod = mul(coeff, term)
                if (used >> (j + 1)).bit_count() % 2:
                    prod = neg(prod)
                target = used | (1 << j)
                ndp[target] = add(ndp.get(target, (0,)), prod)
        dp = ndp
    return dp[(1 << n) - 1]


def image(state, perm):
    return sum(1 << perm[i] for i in range(4) if state & (1 << i))


def states_and_generator(edges):
    e = {tuple(sorted(v)) for v in edges}
    automorphisms = []
    for perm in permutations(range(4)):
        if {tuple(sorted((perm[a], perm[b]))) for a, b in e} == e:
            automorphisms.append(perm)
    unseen = set(range(1, 16))
    orbits = []
    while unseen:
        state = min(unseen)
        orbit = frozenset(image(state, p) for p in automorphisms)
        assert orbit <= unseen
        unseen.difference_update(orbit)
        orbits.append(tuple(sorted(orbit)))
    index = {s: j for j, orb in enumerate(orbits) for s in orb}
    neighbors = [set() for _ in range(4)]
    for a, b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)

    def transition_by_orbit(state):
        total = {}  # off-diagonal rates indexed by target state (including 0)
        for v in range(4):
            if state & (1 << v):
                target = state ^ (1 << v)
                rate = (1,)
            else:
                target = state | (1 << v)
                rate = (0, sum(bool(state & (1 << u)) for u in neighbors[v]))
            if rate == (0, 0):
                continue
            k = index[target] if target else -1
            total[k] = add(total.get(k, (0,)), rate)
        return total

    n = len(orbits)
    Q = [[(0,) for _ in range(n)] for _ in range(n)]
    for i, orb in enumerate(orbits):
        t = transition_by_orbit(orb[0])
        for state in orb[1:]:
            assert transition_by_orbit(state) == t, 'Orbit lumping not exact'
        for dest, rate in t.items():
            Q[i][i] = add(Q[i][i], rate)
            if dest >= 0:
                Q[i][dest] = sub(Q[i][dest], rate)
    return Q, index[15], len(orbits)


def charpoly(edges):
    e = set(tuple(sorted(q)) for q in edges)
    mat = []
    for i in range(4):
        mat.append([])
        for j in range(4):
            mat[-1].append((0, 1) if i == j else ((-1,) if tuple(sorted((i, j))) in e else (0,)))
    return determinant(mat)


# Exact continuous-time absorption-time formulas, from Cramer's rule.
# Numerators/denominators are in the common per-graph normalization, not
# determinants themselves (which may have common polynomial factors).
F = {
    'paw': (
        polynomial([324, 2556, 9919, 25760, 48131, 65654, 65563, 46968, 22806, 6696, 900]),
        mul_const(polynomial([162, 806, 1857, 2618, 2412, 1416, 480, 72]), 6),
        PAW,
    ),
    'cycle': (
        polynomial([8, 24, 42, 61, 25]),
        mul_const(polynomial([5, 3]), 4),
        CYCLE,
    ),
    'star': (
        polynomial([9, 60, 193, 439, 554, 331, 75]),
        mul_const(mul(mul(polynomial([1, 1]), polynomial([3, 2])), polynomial([4, 3])), 6),
        STAR,
    ),
    'path': (
        polynomial([12, 100, 427, 1280, 2628, 3527, 2961, 1424, 300]),
        mul_const(mul(polynomial([4, 9, 6]), polynomial([12, 31, 32, 12])), 2),
        PATH,
    ),
}

# Check each rational function against the generator with exact polynomial
# determinants; equality as polynomials proves equality for every rate.
checked = {}
for name, (numerator, denominator, edges) in F.items():
    Q, idx, count = states_and_generator(edges)
    den = determinant(Q)
    replace = [[(1,) if j == idx else entry for j, entry in enumerate(row)] for row in Q]
    num = determinant(replace)
    assert mul(num, denominator) == mul(numerator, den), f'{name}: formula mismatch'
    assert eval_poly(den, Fraction(1, 1)) != 0
    checked[name] = (numerator, denominator)

# Forest/tree case: the star has larger eigenvalue and also a strictly longer
# mean time to extinction for every rate > 0.
Nstar, Dstar = checked['star']
Npath, Dpath = checked['path']
startree_num = polynomial([324, 2595, 8941, 17676, 22477, 19319, 11195, 4032, 684])
startree_den = mul_const(
    mul(mul(mul(mul(polynomial([1, 1]), polynomial([3, 2])), polynomial([4, 3])),
            polynomial([4, 9, 6])), polynomial([12, 31, 32, 12])), 6
)
assert mul(sub(mul(Nstar, Dpath), mul(Npath, Dstar)), startree_den) == mul(
    mul((0, 0, 1), startree_num), mul(Dstar, Dpath)
)
assert all(c > 0 for c in startree_num)

# Four-edge unicyclic case: cycle minus paw is exactly x^2*P/(positive D).
Np, Dp = checked['paw']
Nc, Dc = checked['cycle']
P = polynomial([648, 3504, 8486, 10624, 4144, -7529, -13801, -10608, -4176, -684])
D = mul_const(mul(polynomial([5, 3]),
                  polynomial([162, 806, 1857, 2618, 2412, 1416, 480, 72])), 12)
assert mul(sub(mul(Nc, Dp), mul(Np, Dc)), D) == mul(mul((0, 0, 1), P), mul(Dc, Dp))
assert list(P[:5]) == [-684, -4176, -10608, -13801, -7529]
assert all(y > 0 for y in P[5:])
# Descartes: one sign change, hence exactly one positive root. Opposite end
# signs prove existence. Rational sign isolation gives a reproducible interval.
assert eval_poly(P, Fraction(1079524, 1000000)) < 0
assert eval_poly(P, Fraction(1079525, 1000000)) > 0
assert eval_poly(P, 0) < 0 and P[-1] > 0

# Exact absorption-time comparison at two rates: verifies the direction.
def at(name, rate):
    n, d = checked[name]
    return Fraction(eval_poly(n, rate), eval_poly(d, rate))

assert at('paw', 1) == Fraction(295277, 58938)
assert at('cycle', 1) == Fraction(5, 1)
assert at('paw', 2) == Fraction(1182381, 99812)
assert at('cycle', 2) == Fraction(635, 52)
assert at('cycle', 2) - at('paw', 2) == Fraction(237101, 648778)

# Independent exact full-state linear equations at two test rates, using
# standard Fraction Gaussian elimination (no orbit quotient).
def full_state_tau(edges, rate):
    M = 15
    mat = [[Fraction(0) for _ in range(M + 1)] for _ in range(M)]
    neighbors = [set() for _ in range(4)]
    for a, b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)
    for s in range(1, 16):
        i = s - 1
        mat[i][-1] = Fraction(1)
        for v in range(4):
            if s & (1 << v):
                target, eventrate = s ^ (1 << v), Fraction(1)
            else:
                target = s | (1 << v)
                eventrate = rate * sum(bool(s & (1 << u)) for u in neighbors[v])
            if not eventrate:
                continue
            mat[i][i] += eventrate
            if target:
                mat[i][target - 1] -= eventrate
    for j in range(M):
        pivot = next(k for k in range(j, M) if mat[k][j] != 0)
        mat[j], mat[pivot] = mat[pivot], mat[j]
        div = mat[j][j]
        mat[j] = [t / div for t in mat[j]]
        for k in range(M):
            if k == j or not mat[k][j]:
                continue
            fac = mat[k][j]
            mat[k] = [a - fac * b for a, b in zip(mat[k], mat[j])]
    return mat[-1][-1]

for name, (_, _, edges) in F.items():
    for rate in (Fraction(1, 2), Fraction(1), Fraction(2)):
        assert full_state_tau(edges, rate) == at(name, rate)

# Characteristic polynomial checks are independent of numerical eigenvalues.
assert charpoly(PAW) == polynomial([1, 0, -4, -2, 1])  # (x+1)(x^3-x^2-3x+1)
assert charpoly(CYCLE) == polynomial([1, 0, -4, 0, 0])  # (x^2-4)x^2
assert charpoly(STAR) == polynomial([1, 0, -3, 0, 0])
assert charpoly(PATH) == polynomial([1, 0, -3, 0, 1])

# All connected simple graph types up to 4 vertices, per edge stratum.
# Canonical adjacency-edge bit strings remove vertex relabelings exactly.
def edge_signature(n, edges, perm):
    es = set(tuple(sorted((perm[u], perm[v]))) for u, v in edges)
    return tuple(int((u, v) in es) for u in range(n) for v in range(u + 1, n))

def canonical(n, edges):
    return min(edge_signature(n, edges, p) for p in permutations(range(n)))

def connected(n, edges):
    vis = {0}
    while True:
        nxt = vis | {v for u, v in edges if u in vis} | {u for u, v in edges if v in vis}
        if nxt == vis:
            return len(vis) == n
        vis = nxt

class_counts = {}
for n in range(2, 5):
    all_e = tuple(combinations(range(n), 2))
    for m in range(n - 1, len(all_e) + 1):
        classes = set()
        for es in combinations(all_e, m):
            if connected(n, es):
                classes.add(canonical(n, es))
        class_counts[(n, m)] = len(classes)
assert class_counts == {
    (2, 1): 1,
    (3, 2): 1, (3, 3): 1,
    (4, 3): 2, (4, 4): 2, (4, 5): 1, (4, 6): 1,
}
print('VERIFY_OK')
print('connected_unlabeled_types', class_counts)
print('lumped_state_counts', {name: states_and_generator(graph)[2] for name, (_, _, graph) in F.items()})
print('unique_positive_root_interval', '1.079524 < rate < 1.079525')
print('rate_2_cycle_minus_paw', at('cycle', 2) - at('paw', 2))
