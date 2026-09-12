"""Exact evaluators for binary pairwise MAP: integer optimum (2^n) and SA1/local-polytope
optimum via half-integral enumeration (3^n) with closed-form min-coupling per edge.

Correctness of the LP value rests on the classical half-integrality theorem:
the local-polytope relaxation of binary pairwise MAP always admits a
half-integral optimal solution (roof duality; Hammer-Hansen-Simeone 1984;
see also Rother-Kolmogorov-Lempitsky-Szummer 2007, QPBO). Given singleton
marginals p, each edge decouples: min over couplings of Ber(p_i)xBer(p_j)
marginals, a 1-D LP in t = b(0,0) over [max(0,p+q-1), min(p,q)].
Hence LP opt = min over p in {0,1/2,1}^n of (unary part + per-edge min-coupling).
All arithmetic in Fractions: exact.
"""
from fractions import Fraction as F
import itertools


def min_coupling(p, q, th):
    """th = ((00,01),(10,11)) Fractions. p=P(Xi=1), q=P(Xj=1).
    t = P(00); P(01)=(1-p)-t; P(10)=(1-q)-t; P(11)=p+q-1+t.
    Bounds: lo=max(0,1-p-q), hi=min(1-p,1-q)."""
    lo = max(F(0), 1 - p - q)
    hi = min(1 - p, 1 - q)
    assert lo <= hi
    s = th[0][0] + th[1][1] - th[0][1] - th[1][0]
    t = lo if s > 0 else hi
    return (th[0][0] * t + th[0][1] * ((1 - p) - t) + th[1][0] * ((1 - q) - t)
            + th[1][1] * (p + q - 1 + t)), t


def lp_exact(n, edges, unary, pair):
    """Returns (best_value, best_p, best_t_dict). unary[i]=(u0,u1); pair[k]=2x2."""
    halves = [F(0), F(1, 2), F(1)]
    best = None
    best_p = best_t = None
    for ps in itertools.product(halves, repeat=n):
        val = sum(u[0] * (1 - p) + u[1] * p for u, p in zip(unary, ps))
        ts = []
        for k, (i, j) in enumerate(edges):
            c, t = min_coupling(ps[i], ps[j], pair[k])
            val += c
            ts.append(t)
        if best is None or val < best:
            best, best_p, best_t = val, ps, ts
    return best, best_p, best_t


def int_exact(n, edges, unary, pair):
    """Returns (best_value, best_x)."""
    best = None
    best_x = None
    for xs in itertools.product([0, 1], repeat=n):
        val = sum(u[x] for u, x in zip(unary, xs))
        for k, (i, j) in enumerate(edges):
            val += pair[k][xs[i]][xs[j]]
        if best is None or val < best:
            best, best_x = val, xs
    return best, best_x


def lp_primal_point(n, edges, unary, pair, ps, ts):
    """Build explicit primal feasible distributions from (p, t) solution."""
    b_i = [(1 - p, p) for p in ps]
    b_ij = []
    for (i, j), t in zip(edges, ts):
        p, q = ps[i], ps[j]
        b_ij.append(((t, (1 - p) - t), ((1 - q) - t, p + q - 1 + t)))
    return b_i, b_ij


def check_primal_feasible(n, edges, b_i, b_ij):
    """Verify nonnegativity, normalization, marginal agreement. Returns (ok, msg)."""
    for i, (a, b) in enumerate(b_i):
        if a < 0 or b < 0 or a + b != 1:
            return False, f"node {i} bad singleton {a},{b}"
    for k, ((i, j), ((t00, t01), (t10, t11))) in enumerate(zip(edges, b_ij)):
        if min(t00, t01, t10, t11) < 0:
            return False, f"edge {k} negative entry"
        if t00 + t01 + t10 + t11 != 1:
            return False, f"edge {k} not normalized"
        if (t00 + t01, t10 + t11) != (b_i[i][0], b_i[i][1]):
            return False, f"edge {k} margin-i mismatch"
        if (t00 + t10, t01 + t11) != (b_j(j, b_i)[0], b_j(j, b_i)[1]):
            return False, f"edge {k} margin-j mismatch"
    return True, "feasible"


def b_j(j, b_i):
    return b_i[j]


def primal_value(edges, unary, pair, b_i, b_ij):
    v = sum(u[0] * a + u[1] * b for u, (a, b) in zip(unary, b_i))
    for k, ((t00, t01), (t10, t11)) in enumerate(b_ij):
        th = pair[k]
        v += th[0][0] * t00 + th[0][1] * t01 + th[1][0] * t10 + th[1][1] * t11
    return v
