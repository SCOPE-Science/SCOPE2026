from itertools import combinations_with_replacement
from collections import Counter, defaultdict
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

# Generator order and metabelian Hall basis from the cited construction.
ORDER = ["x5", "x1", "x2", "x3", "x4"]
RANK = {x: i for i, x in enumerate(ORDER)}

BASIS = [("g", x) for x in ORDER]
for weight in (2, 3, 4):
    tail_len = weight - 2
    for a in ORDER:
        for b in ORDER:
            if RANK[a] <= RANK[b]:
                continue
            allowed = [x for x in ORDER if RANK[x] >= RANK[b]]
            for tail in combinations_with_replacement(allowed, tail_len):
                BASIS.append(("c", a, b, tail))
INDEX = {b: i for i, b in enumerate(BASIS)}


def add(v, w):
    out = dict(v)
    for k, c in w.items():
        out[k] = out.get(k, 0) + c
        if out[k] == 0:
            del out[k]
    return out


def scale(v, n):
    return {k: n * c for k, c in v.items() if n * c}


def gen(x, c=1):
    return {("g", x): c}


def bracket_token_gen(tok, g):
    # Normal form for [tok,g] in the class-4 free metabelian quotient.
    if tok[0] == "g":
        a = tok[1]
        if a == g:
            return {}
        if RANK[a] > RANK[g]:
            return {("c", a, g, ()): 1}
        return {("c", g, a, ()): -1}

    a, b, tail = tok[1], tok[2], tok[3]
    weight = 2 + len(tail)
    if weight >= 4:
        return {}

    new_tail = list(tail) + [g]
    if all(RANK[x] >= RANK[b] for x in new_tail):
        return {("c", a, b, tuple(sorted(new_tail, key=RANK.get))): 1}

    # Only g can lie below b.  Jacobi gives
    # [[a,b],g] = [[a,g],b] - [[b,g],a].
    def append_tail(v, seq):
        cur = v
        for h in seq:
            nxt = defaultdict(int)
            for t, c in cur.items():
                for u, d in bracket_token_gen(t, h).items():
                    nxt[u] += c * d
            cur = {t: c for t, c in nxt.items() if c}
        return cur

    v1 = append_tail(bracket_token_gen(("g", a), g), [b])
    v2 = append_tail(bracket_token_gen(("g", b), g), [a])
    core = add(v1, scale(v2, -1))
    return append_tail(core, list(tail))


def bracket_vec_gen(v, g):
    out = defaultdict(int)
    for tok, c in v.items():
        for u, d in bracket_token_gen(tok, g).items():
            out[u] += c * d
    return {k: c for k, c in out.items() if c}


def nested(names):
    v = gen(names[0])
    for g in names[1:]:
        v = bracket_vec_gen(v, g)
    return v


def eq(v, w):
    return add(v, scale(w, -1)) == {}


# Structural checks on the normal-form bracket.
for a in ORDER:
    for b in ORDER:
        for c in ORDER:
            jac = add(
                add(bracket_vec_gen(nested([a, b]), c), bracket_vec_gen(nested([b, c]), a)),
                bracket_vec_gen(nested([c, a]), b),
            )
            assert jac == {}, ("Jacobi", a, b, c, jac)
for tok in BASIS:
    weight = 1 if tok[0] == "g" else 2 + len(tok[3])
    if tok[0] == "c" and weight <= 2:
        for g in ORDER:
            for h in ORDER:
                lhs = bracket_vec_gen(bracket_vec_gen({tok: 1}, g), h)
                rhs = bracket_vec_gen(bracket_vec_gen({tok: 1}, h), g)
                assert eq(lhs, rhs), ("tail symmetry", tok, g, h)

# N=1 notation from the paper.
t = nested(["x4", "x5"])
c = {i: bracket_vec_gen(t, f"x{i}") for i in (1, 2, 3)}
u = {i: bracket_vec_gen(c[i], f"x{i}") for i in (1, 2, 3)}

r = {}
r[1] = add(add(gen("x1", 4), scale(c[3], 2)), c[2])
r[2] = add(add(gen("x2", 16), scale(c[3], 4)), scale(c[1], -1))
r[3] = add(add(gen("x3", 64), scale(c[2], -4)), scale(c[1], -2))

# Reproduce the six displayed relations (3.5) exactly.
b12 = nested(["x1", "x2"])
b13 = nested(["x1", "x3"])
b23 = nested(["x2", "x3"])
expected = {
    (1, "x2"): add(scale(b12, 4), u[2]),
    (1, "x3"): add(scale(b13, 4), scale(u[3], 2)),
    (2, "x1"): add(scale(b12, -16), scale(u[1], -1)),
    (2, "x3"): add(scale(b23, 16), scale(u[3], 4)),
    (3, "x1"): add(scale(b13, -64), scale(u[1], -2)),
    (3, "x2"): add(scale(b23, -64), scale(u[2], -4)),
}
for key, want in expected.items():
    i, x = key
    got = bracket_vec_gen(r[i], x)
    # Relation (iii) kills every mixed weight-4 Hall term; (3.5) is displayed
    # in the quotient after imposing that relation.
    reduced = {}
    for tok, coeff in got.items():
        weight = 1 if tok[0] == "g" else 2 + len(tok[3])
        if tok[0] == "c" and weight == 4 and tok not in {next(iter(u[j])) for j in (1,2,3)}:
            continue
        reduced[tok] = coeff
    assert eq(reduced, want), ("relation 3.5", key, reduced, want)

# Additive presentation: close r_i under all generator brackets through weight 4,
# kill all weight-4 Hall basis elements except u_1,u_2,u_3, and impose (iv).
relations = []
for i in (1, 2, 3):
    relations.append(r[i])
    frontier = [r[i]]
    for _depth in range(1, 4):
        new_frontier = []
        for v in frontier:
            for g in ORDER:
                w = bracket_vec_gen(v, g)
                if w:
                    relations.append(w)
                    new_frontier.append(w)
        frontier = new_frontier

u_tokens = {next(iter(u[i])) for i in (1, 2, 3)}
for tok in BASIS:
    weight = 1 if tok[0] == "g" else 2 + len(tok[3])
    if tok[0] == "c" and weight == 4 and tok not in u_tokens:
        relations.append({tok: 1})
relations.append(add(u[1], scale(u[3], -16)))
relations.append(add(u[2], scale(u[3], -4)))
relations.append(scale(u[3], 64))

M = sp.zeros(len(relations), len(BASIS))
for i, rel in enumerate(relations):
    for tok, coeff in rel.items():
        M[i, INDEX[tok]] = coeff

S = smith_normal_form(M, domain=ZZ)
diag = []
for i in range(min(S.rows, S.cols)):
    d = int(S[i, i])
    if d:
        diag.append(abs(d))

counts = Counter(d for d in diag if d > 1)
expected_counts = Counter({2: 1, 4: 22, 8: 1, 16: 15, 64: 7, 256: 3})
assert len(BASIS) == 160
assert len(relations) == 483
assert len(diag) == 155
assert len(BASIS) - len(diag) == 5
assert counts == expected_counts, (counts, expected_counts)
assert sum((d.bit_length() - 1) * m for d, m in counts.items()) == 174

# Independent modular Gaussian-elimination checks on the original presentation matrix.
def rank_mod_p(matrix, p):
    a = [[int(matrix[i,j]) % p for j in range(matrix.cols)] for i in range(matrix.rows)]
    row = 0
    for col in range(matrix.cols):
        pivot = next((r for r in range(row, len(a)) if a[r][col] % p), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][col], -1, p)
        a[row] = [(x * inv) % p for x in a[row]]
        for r in range(len(a)):
            if r != row and a[r][col] % p:
                f = a[r][col] % p
                a[r] = [(a[r][j] - f * a[row][j]) % p for j in range(matrix.cols)]
        row += 1
        if row == len(a):
            break
    return row

assert rank_mod_p(M, 2) == 106
assert rank_mod_p(M, 3) == 155

print("HALL_BASIS_COUNTS", {w: sum(1 for b in BASIS if (1 if b[0] == "g" else 2 + len(b[3])) == w) for w in range(1, 5)})
print("RELATION_ROWS", len(relations))
print("SMITH_NONZERO", len(diag))
print("FREE_RANK", len(BASIS) - len(diag))
print("TORSION_INVARIANTS", dict(sorted(counts.items())))
print("TORSION_ORDER_EXPONENT_2", 174)
print("CHECK_OK")
