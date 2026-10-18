"""Independent algebraic smoothness and zeta-polynomial checks.

Requires sympy for lexicographic Groebner bases. The checks run on
representatives of all ambient projective-coordinate orbits; the
orbit action itself is exact and exhausts the coefficient space.
"""
import sympy as sp
import verify as v

u, t = sp.symbols('u t')


def affine_quartic(mask):
    return sum(((mask >> i) & 1) * t**i for i in range(5))


def groebner_smooth(a, b, c):
    for aa, bb, cc in ((a, b, c), (v.reverse_quartic(a), v.reverse_quartic(b), v.reverse_quartic(c))):
        for A, C in ((aa, cc), (cc, aa)):
            F = affine_quartic(A) + affine_quartic(bb) * u + affine_quartic(C) * u**2
            G = sp.groebner((F, sp.diff(F, u), sp.diff(F, t)), u, t, modulus=2)
            if not (len(G.polys) == 1 and G.polys[0].as_expr() == 1):
                return False
    return True


def field_mul(a, b, m, p):
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        if (a >> m) & 1:
            a ^= p
        b >>= 1
    return out


def evaluate(mask, x, m, p):
    out = 0
    for i in range(4, -1, -1):
        out = field_mul(out, x, m, p) ^ ((mask >> i) & 1)
    return out


def points_over_extension(a, b, c, m, p):
    q = 1 << m
    out = 0
    for t0 in list(range(q)) + [None]:
        if t0 is None:
            A, B, C = (f >> 4 & 1 for f in (a, b, c))
        else:
            A, B, C = (evaluate(f, t0, m, p) for f in (a, b, c))
        out += (C == 0)
        for w in range(q):
            f = A ^ field_mul(B, w, m, p) ^ field_mul(C, field_mul(w, w, m, p), m, p)
            out += (f == 0)
    return out


def rank_from_zeta(a, b, c):
    N1, N2, N3 = (points_over_extension(a, b, c, m, p)
                  for m, p in ((1, 3), (2, 7), (3, 11)))
    S1, S2, S3 = 3 - N1, 5 - N2, 9 - N3
    a1 = -S1
    a2, r2 = divmod(S1 * S1 - S2, 2)
    assert r2 == 0
    a3, r3 = divmod(-S3 - a1 * S2 - a2 * S1, 3)
    assert r3 == 0
    L = [1, a1, a2, a3, 2 * a2, 4 * a1, 8]
    return N1, max(i for i, c0 in enumerate(L) if c0 % 2)


def main():
    unvisited = set(range(1, 32768))
    smooth_orbits = 0
    smooth_equations = 0
    while unvisited:
        i = min(unvisited)
        triple = v.unpack(i)
        orbit = {v.pack(v.transform(triple, bi, fm))
                 for bi in range(6) for fm in v.MATRICES}
        assert orbit <= unvisited
        unvisited.difference_update(orbit)
        groebner_result = groebner_smooth(*triple)
        assert groebner_result == v.smooth(*triple), triple
        if groebner_result:
            smooth_orbits += 1
            smooth_equations += len(orbit)
            assert rank_from_zeta(*triple) == (v.rational_points(*triple), v.p_rank_from_branch(triple[1]))
    assert (smooth_orbits, smooth_equations) == (294, 9216)
    print('PASS: Groebner smoothness on all projective orbits (smooth and singular).')
    print('PASS: independent finite-field zeta p-ranks on every smooth orbit.')


if __name__ == '__main__':
    main()
