"""Obstruction certificate for lane-973 target.

Part A (numeric): verifies the shuffle/symmetric-part identity
    sym(S_k(omega)) = x^{otimes k}/k!, k=2,3,
on a random piecewise-linear BV path by exact segment-sum iterated integrals.
Part B (exact, sympy): for a given set of <=4 atom increments, builds the
evaluation matrix on the 6-dim space P_{<=2}(R^2), exhibits an exact nonzero
quadratic vanishing at all atoms, and certifies E[p(Z)^2] > 0 exactly via the
Gaussian moment Gram matrix (so no positive-weight quadrature on these points
can match Gaussian moments through degree 4, hence no degree-5 cubature).
"""
import itertools
import numpy as np
import sympy as sp


def signature_levels(segments, k):
    """Exact level-k signature of a piecewise-linear path (constant velocity
    per segment) via Chen's identity. segments: list of 2-vectors (steps)."""
    S = [np.eye(1).reshape(1)] + [np.zeros((2,) * j) for j in range(1, k + 1)]
    for v in segments:
        v = np.asarray(v, dtype=float)
        # exp(v) truncated: v^{otimes j}/j!
        E = [np.ones((1,)).reshape(tuple()) for _ in range(k + 1)]
        E[0] = 1.0
        pw = np.ones(tuple())
        fact = 1
        for j in range(1, k + 1):
            fact *= j
            pw = np.tensordot(pw, v, axes=0)
            E[j] = pw / fact
        N = [None] * (k + 1)
        for j in range(k + 1):
            tot = np.zeros((2,) * j)
            for i in range(j + 1):
                tot = tot + np.tensordot(S[i].reshape((2,) * i),
                                         np.asarray(E[j - i]).reshape((2,) * (j - i)),
                                         axes=0)
            N[j] = tot
        S = N
    return S


def symmetrize(T):
    k = T.ndim
    fact = 1
    for j in range(1, k + 1):
        fact *= j
    out = np.zeros_like(T)
    for s in itertools.permutations(range(k)):
        out = out + np.transpose(T, axes=s)
    return out / float(fact)


def part_a():
    rng = np.random.default_rng(0)
    steps = [rng.normal(size=2) for _ in range(5)]
    x = sum(steps)
    for k in (2, 3):
        S = signature_levels(steps, k)[k]
        lhs = symmetrize(S)
        rhs = x.copy()
        for _ in range(k - 1):
            rhs = np.tensordot(rhs, x, axes=0)
        rhs = rhs / float(np.prod(range(1, k + 1)))
        assert np.allclose(lhs, rhs, atol=1e-9), f"shuffle check failed at k={k}"
        print(f"Part A: sym(S_{k}) = x^otimes{k}/{k}!  maxerr="
              f"{np.max(np.abs(lhs - rhs)):.2e}")
    print("Part A: VERIFY_OK")


MONOMIALS = [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)]


def gauss_moment(a, b):
    """Exact E[X^a Y^b] for (X,Y) ~ N(0,I_2): (a-1)!!(b-1)!! if a,b even else 0."""
    if a % 2 or b % 2:
        return sp.Integer(0)

    def df(n):
        r = sp.Integer(1)
        for j in range(n - 1, 0, -2):
            r *= j
        return r
    return df(a) * df(b)


def gram_matrix():
    G = sp.zeros(6)
    for i, (a1, b1) in enumerate(MONOMIALS):
        for j, (a2, b2) in enumerate(MONOMIALS):
            G[i, j] = gauss_moment(a1 + a2, b1 + b2)
    return G


def certify(points, name):
    """points: list of (x, y) increments (rational-friendly). Exhibits vanishing
    quadratic and certifies E[p^2] > 0 exactly."""
    M = sp.Matrix([[sp.Rational(px) ** a * sp.Rational(py) ** b
                    for (a, b) in MONOMIALS] for (px, py) in points])
    ns = M.nullspace()
    assert ns, "no vanishing quadratic (unexpected: rank full)"
    c = ns[0]
    G = gram_matrix()
    val = (c.T * G * c)[0]
    assert val > 0, "Gaussian second moment not positive"
    terms = " + ".join(f"({c[i]})*x^{MONOMIALS[i][0]}y^{MONOMIALS[i][1]}" for i in range(6))
    print(f"Part B [{name}]: npoints={len(points)}, eval-rank={M.rank()}, "
          f"nulldim={len(ns)}, E[p(Z)^2] = {val} > 0")
    print(f"  vanishing quadric coeffs (1,x,y,x^2,xy,y^2): {list(c)}")
    return val


if __name__ == "__main__":
    part_a()
    print("Gaussian moment Gram matrix G =\n", gram_matrix())
    certify([(1, 1), (1, -1), (-1, 1), (-1, -1)], "isotropic-4")
    certify([(sp.Rational(1, 2), sp.Rational(1, 3)),
             (sp.Rational(-2), 1), (0, sp.Rational(3, 2)), (1, 1)], "generic-4")
    certify([(1, 0), (0, 1), (-1, -1)], "three-points")
    print("Part B: VERIFY_OK")
