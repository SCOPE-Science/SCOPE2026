"""Exact characteristic-two verification of the e4 six-variable gradient scheme.

Requires Python 3 and SymPy. No numerical approximations are used.
"""
import itertools
from functools import lru_cache
import sympy as s

n = 6
x = s.symbols('x1:7')
f = sum(s.prod(x[j] for j in c) for c in itertools.combinations(range(n), 4))
g = [s.Poly(s.diff(f, xi), *x, modulus=2).as_expr() for xi in x]

# The hidden projective-frame involutions preserve the gradient ideal.
for i in range(n):
    substitutions = {x[j]: x[j] + x[i] for j in range(n) if j != i}
    delta = s.Poly(s.expand(f.subs(substitutions, simultaneous=True) - f - x[i]**4), *x, modulus=2)
    assert delta.is_zero

# Exact Groebner basis over F_2, with an explicit leading-monomial
# Hilbert-series computation rather than a numerical dimension guess.
G = s.groebner(g, *x, order='grevlex', modulus=2)
lead = tuple(tuple(p.LM(order='grevlex')) for p in G.polys)
assert len(G.polys) == 49


def minimal(ms):
    ms = tuple(sorted(set(ms), key=lambda v: (sum(v), v)))
    return tuple(m for i, m in enumerate(ms)
                 if not any(all(b <= a for a, b in zip(m, ms[j]))
                            for j in range(i)))


@lru_cache(None)
def numerator(nvars, monomials):
    """Hilbert numerator over (1-t)^nvars via deletion-colon recursion."""
    if not monomials:
        return (1,)
    if any(not any(m) for m in monomials):
        return (0,)
    j = max(range(nvars), key=lambda i: sum(bool(m[i]) for m in monomials))
    deleted = minimal(tuple(m[:j] + m[j+1:] for m in monomials if m[j] == 0))
    colon = minimal(tuple(m[:j] + (max(m[j] - 1, 0),) + m[j+1:]
                          for m in monomials))
    p = numerator(nvars-1, deleted)
    q = numerator(nvars, colon)
    ans = [0] * (max(len(p)+1, len(q)+1))
    for i, c in enumerate(p):
        ans[i] += c
        ans[i+1] -= c
    for i, c in enumerate(q):
        ans[i+1] += c
    while len(ans) > 1 and ans[-1] == 0:
        ans.pop()
    return tuple(ans)


N = numerator(6, minimal(lead))
assert N == (1, 0, 0, -6, 1, 0, 15, 0, -13, -20, 35, -14, 1)
t = s.Symbol('t')
P = sum(c*t**j for j, c in enumerate(N))
assert s.cancel(P/(1-t)**6 - (
    1+4*t+10*t**2+14*t**3+12*t**4-11*t**6-10*t**7+t**8)/(1-t)**2) == 0
assert s.limit(P/(1-t)**4, t, 1) == 21
assert s.diff(s.cancel(P/(1-t)**4), t).subs(t, 1) == -14

# Degrees in which the nonreduced scheme begins to differ from its reduction.
@lru_cache(None)
def exponent_vectors(degree, numvars):
    if numvars == 1:
        return ((degree,),)
    return tuple((a,)+b for a in range(degree+1)
                 for b in exponent_vectors(degree-a, numvars-1))


def rank_mod_two(vectors):
    pivots = {}
    for v in vectors:
        while v:
            bit = v.bit_length() - 1
            if bit in pivots:
                v ^= pivots[bit]
            else:
                pivots[bit] = v
                break
    return len(pivots)


def reduced_curve_hilbert(degree):
    """Rank of degree-d restrictions to 6 star lines and 15 coordinate lines."""
    vectors = []
    for e in exponent_vectors(degree, 6):
        bits = 0
        offset = 0
        # Star line from e_i to the all-ones point: x_i=a, other x_j=b.
        for i in range(6):
            bits |= 1 << (offset + e[i])
            offset += degree + 1
        # Coordinate line (e_i,e_j): x_i=a,x_j=b, others zero.
        for i, j in itertools.combinations(range(6), 2):
            if all(e[k] == 0 for k in range(6) if k not in (i, j)):
                bits |= 1 << (offset + e[i])
            offset += degree + 1
        vectors.append(bits)
    return rank_mod_two(vectors)


expected = ((0,1,1), (1,6,6), (2,21,21), (3,50,42),
            (4,91,63), (5,132,84), (6,162,105),
            (7,182,126), (8,203,147))
for d, expected_gradient, expected_reduced in expected:
    h = sum(not any(all(a >= b for a, b in zip(e, ell)) for ell in lead)
            for e in exponent_vectors(d, 6))
    assert h == expected_gradient, (d, h)
    hr = reduced_curve_hilbert(d)
    assert hr == expected_reduced, (d, hr)

# Directly compare the full line union with the degree-four hypersurface.
A, B = s.symbols('A B')
for i, j in itertools.combinations(range(6), 2):
    z = [s.Integer(0)]*6
    z[i], z[j] = A, B
    assert s.Poly(f.subs(dict(zip(x,z)), simultaneous=True), A, B, modulus=2).is_zero
for i in range(6):
    z = [B]*6
    z[i] = A
    assert s.Poly(f.subs(dict(zip(x,z)), simultaneous=True)-B**4,
                  A, B, modulus=2).is_zero

print('VERIFY_OK')
print('Groebner_basis_size=49; Hilbert_polynomial=21*d+35')
print('Reduced_curve_Hilbert_polynomial=21*d-21; embedded_length=56')
print('Frobenius_frame_transpositions=6; line_components=21')
