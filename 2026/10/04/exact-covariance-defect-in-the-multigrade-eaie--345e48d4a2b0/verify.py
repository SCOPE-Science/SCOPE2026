from fractions import Fraction
from itertools import product


def additive_game(d, zeta):
    vals = {}
    for mu in product(*[range(di + 1) for di in d]):
        total = Fraction(0)
        for j, mj in enumerate(mu):
            for q in range(1, mj + 1):
                total += zeta.get((j, q), Fraction(0))
        vals[mu] = total
    return vals


def eaie(d, vals):
    n = len(d)
    zero = tuple(0 for _ in d)
    assert vals[zero] == 0
    delta = {}
    for j, dj in enumerate(d):
        for k in range(1, dj + 1):
            a = [0] * n
            b = [0] * n
            a[j] = k
            b[j] = k - 1
            delta[(j, k)] = vals[tuple(a)] - vals[tuple(b)]
    top = tuple(d)
    balance = (vals[top] - sum(delta[(j, d[j])] for j in range(n))) / n
    return {jk: delta[jk] + balance for jk in delta}


def add_expr(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, Fraction(0)) + value
        if out[key] == 0:
            del out[key]
    return out


def scale_expr(a, c):
    return {k: c * v for k, v in a.items() if c * v}


def formal_defect(d):
    n = len(d)
    lower = {}
    for j, dj in enumerate(d):
        for q in range(1, dj):
            lower[(j, q)] = Fraction(1, n)
    # Reconstruct the EAIE shift coefficient by coefficient.
    top_shift = {(j, q): Fraction(1) for j, dj in enumerate(d) for q in range(1, dj + 1)}
    top_steps = {(j, dj): Fraction(1) for j, dj in enumerate(d)}
    balance_shift = scale_expr(add_expr(top_shift, scale_expr(top_steps, -1)), Fraction(1, n))
    assert balance_shift == lower
    for j, dj in enumerate(d):
        for k in range(1, dj + 1):
            step = {(j, k): Fraction(1)}
            total = add_expr(step, balance_shift)
            required = step
            defect = add_expr(total, scale_expr(required, -1))
            assert defect == lower
    return lower


# Minimal exact counterexample: d=(2,1), U=0, zeta_(1,1)=1.
d = (2, 1)
zeta = {(0, 1): Fraction(1)}
H = additive_game(d, zeta)
Psi = eaie(d, H)
assert Psi[(0, 1)] == Fraction(3, 2)
assert Psi[(0, 2)] == Fraction(1, 2)
assert Psi[(1, 1)] == Fraction(1, 2)
assert {k: Psi[k] - zeta.get(k, 0) for k in Psi} == {
    (0, 1): Fraction(1, 2),
    (0, 2): Fraction(1, 2),
    (1, 1): Fraction(1, 2),
}

# Coefficient-level transcription checks for representative multigrade domains.
for d in [(2, 1), (2, 2), (3, 1, 2)]:
    defect = formal_defect(d)
    assert defect

# Binary-grade domains have no lower-grade term and hence no covariance defect.
assert formal_defect((1, 1, 1)) == {}

print('VERIFY_OK')
