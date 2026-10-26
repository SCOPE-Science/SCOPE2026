"""Exact finite-field certificate for the Galois-incidence profile of Fermat quintic lines.

Requires Python 3 standard library only.  All arithmetic is in GF(16) with
alpha^4 + alpha + 1 = 0; a projective line is a two-row RREF matrix.
"""
from collections import Counter, defaultdict
from itertools import combinations, product

REDUCTION = 0b10011  # T^4 + T + 1, irreducible over F2


def product16(x, y):
    ans = 0
    while y:
        if y & 1:
            ans ^= x
        y >>= 1
        x <<= 1
        if x & 16:
            x ^= REDUCTION
    return ans

M = [[product16(i, j) for j in range(16)] for i in range(16)]


def power(x, n):
    ans = 1
    while n:
        if n & 1:
            ans = M[ans][x]
        x = M[x][x]
        n >>= 1
    return ans

INV = [0] + [power(x, 14) for x in range(1, 16)]
assert all(M[x][INV[x]] == 1 for x in range(1, 16))


def xor_sum(xs):
    a = 0
    for v in xs:
        a ^= v
    return a


def rref(rows):
    A = [list(r) for r in rows]
    pivots = []
    h = 0
    for col in range(4):
        i = next((j for j in range(h, len(A)) if A[j][col] != 0), None)
        if i is None:
            continue
        A[h], A[i] = A[i], A[h]
        inv = INV[A[h][col]]
        A[h] = [M[inv][v] for v in A[h]]
        for j in range(len(A)):
            if j != h and A[j][col]:
                factor = A[j][col]
                A[j] = [A[j][k] ^ M[factor][A[h][k]] for k in range(4)]
        pivots.append(col)
        h += 1
        if h == len(A):
            break
    return tuple(tuple(A[i]) for i in range(h)), tuple(pivots)


def hermitian(a, b):
    return xor_sum(M[power(a[i], 4)][b[i]] for i in range(4))


def is_generator(a, b):
    return (hermitian(a, a) == 0 and hermitian(b, b) == 0
            and hermitian(a, b) == 0)


def all_generators():
    out = []
    checked = 0
    for p, q in combinations(range(4), 2):
        cols_a = [j for j in range(p + 1, 4) if j != q]
        cols_b = [j for j in range(q + 1, 4)]
        for values in product(range(16), repeat=len(cols_a) + len(cols_b)):
            checked += 1
            a, b = [0] * 4, [0] * 4
            a[p] = b[q] = 1
            for j, v in enumerate(cols_a):
                a[v] = values[j]
            for j, v in enumerate(cols_b):
                b[v] = values[j + len(cols_a)]
            if is_generator(a, b):
                out.append((tuple(a), tuple(b)))
    assert checked == 70161  # all two-planes in F16^4, each RREF exactly once
    assert len(out) == len(set(out)) == 325
    return out

lines = all_generators()
ids = {L: i for i, L in enumerate(lines)}


def sigma(L):
    Z, _ = rref([[M[x][x] for x in row] for row in L])
    return Z

frob = [ids[sigma(L)] for L in lines]
assert sorted(frob) == list(range(325))
assert all(frob[frob[frob[frob[i]]]] == i for i in range(325))

orbits, seen = [], set()
for i in range(325):
    if i in seen:
        continue
    O, j = [], i
    while j not in O:
        assert j not in seen
        O.append(j)
        seen.add(j)
        j = frob[j]
    assert j == i
    orbits.append(O)
assert len(seen) == 325
assert Counter(map(len, orbits)) == {1: 3, 2: 1, 4: 80}


def intersect(L, K):
    return len(rref(list(L) + list(K))[1]) == 3


def pivot(L):
    return tuple(next(j for j, x in enumerate(row) if x) for row in L)

roots = [a for a in range(1, 16) if power(a, 5) == 1]
assert len(roots) == 5
obvious = set()
for (i, j), (k, l) in (((0, 1), (2, 3)),
                        ((0, 2), (1, 3)),
                        ((0, 3), (1, 2))):
    for a, b in product(roots, repeat=2):
        u, v = [0] * 4, [0] * 4
        u[i], u[j], v[k], v[l] = 1, a, 1, b
        L, _ = rref((u, v))
        assert L in ids
        obvious.add(ids[L])
assert len(obvious) == 75
assert all(len(set(i in obvious for i in O)) == 1 for O in orbits)

# The two equality tests are the entire induced graph for a Frobenius 4-cycle.
# Sigma cyclically rotates the vertices. (adjacent?, opposite?) thus encodes
# respectively an independent 4-set, a matching, a 4-cycle, or a 4-clique.
shape = {(False, False): 'empty', (False, True): 'matching',
         (True, False): 'cycle4', (True, True): 'clique4'}
by_type = Counter()
by_pivot = Counter()
for O in orbits:
    L = lines[O[0]]
    p = pivot(L)
    if len(O) != 4:
        by_pivot[(p, 'orbit' + str(len(O)))] += 1
        by_type[('obvious' if O[0] in obvious else 'exceptional',
                 'orbit' + str(len(O)))] += 1
        continue
    adj = intersect(lines[O[0]], lines[O[1]])
    opp = intersect(lines[O[0]], lines[O[2]])
    signature = shape[(adj, opp)]
    by_pivot[(p, signature)] += 1
    by_type[('obvious' if O[0] in obvious else 'exceptional', signature)] += 1
    # All six pair tests must agree with the cyclic classification.
    actual = {(a, b): intersect(lines[O[a]], lines[O[b]])
              for a, b in combinations(range(4), 2)}
    for a, b in combinations(range(4), 2):
        expected = adj if (b - a) % 4 in (1, 3) else opp
        assert actual[(a, b)] == expected
    # Independent incidence check: graph-row 2x2 difference determinant.
    for exponent, corresponding in ((2, adj), (4, opp)):
        R = lines[O[0]]
        pp = pivot(R)
        qq = [i for i in range(4) if i not in pp]
        B = [[R[i][q] for q in qq] for i in range(2)]
        C = [[B[i][j] ^ power(B[i][j], exponent) for j in range(2)]
             for i in range(2)]
        singular = (M[C[0][0]][C[1][1]] ^ M[C[0][1]][C[1][0]]) == 0
        assert singular == corresponding

assert Counter(pivot(L) for L in lines) == {(0, 1): 300, (0, 2): 25}
assert by_pivot == {
    ((0, 1), 'orbit1'): 2, ((0, 1), 'orbit2'): 1,
    ((0, 1), 'empty'): 44, ((0, 1), 'matching'): 14,
    ((0, 1), 'cycle4'): 12, ((0, 1), 'clique4'): 4,
    ((0, 2), 'orbit1'): 1, ((0, 2), 'empty'): 4,
    ((0, 2), 'clique4'): 2,
}
assert by_type == {
    ('obvious', 'orbit1'): 3, ('obvious', 'empty'): 12,
    ('obvious', 'clique4'): 6,
    ('exceptional', 'orbit2'): 1,
    ('exceptional', 'empty'): 36, ('exceptional', 'matching'): 14,
    ('exceptional', 'cycle4'): 12,
}

f4_lines = [i for i in range(325) if frob[frob[i]] == i]
f2_lines = [i for i in f4_lines if frob[i] == i]
assert len(f4_lines) == 5 and len(f2_lines) == 3
P = (1, 1, 1, 1)
assert all(len(rref(list(lines[i]) + [P])[1]) == 2 for i in f4_lines)

# Precisely six rational star points outside P are centers of the six
# four-clique Frobenius orbits (the remaining rational point is P).
f2_surface_points = [tuple((n >> j) & 1 for j in range(4))
                     for n in range(1, 16) if n.bit_count() % 2 == 0]
assert len(f2_surface_points) == 7
centres = []
for O in orbits:
    if len(O) != 4 or not all(intersect(lines[O[a]], lines[O[b]])
                                    for a, b in combinations(range(4), 2)):
        continue
    possible = [Q for Q in f2_surface_points if all(
        len(rref(list(lines[i]) + [Q])[1]) == 2 for i in O)]
    assert len(possible) == 1
    centres += possible
assert len(centres) == len(set(centres)) == 6
assert set(centres) == set(f2_surface_points) - {P}

# Nontrivial independent global intersection-number check.
assert all(sum(intersect(lines[i], lines[j]) for j in range(325) if i != j)
           == 68 for i in (0, 1, 25, 100, 200, 324))

print('VERIFY_OK: 70161 planes; 325 lines = 75 obvious + 250 exceptional;')
print('  Frobenius: 3 fixed, one 2-cycle, 80 four-cycles;')
print('  obvious four-cycles: empty 12, clique 6;')
print('  exceptional four-cycles: empty 36, matching 14, cycle 12;')
print('  five F4-lines through P and six F2-centred Frobenius cliques.')
