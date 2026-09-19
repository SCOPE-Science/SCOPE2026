"""Scientific checks for Rényi dependence of Gaussian magnitudes and local GPI expansions."""

import itertools
import math
import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.integrate import dblquad
from scipy.special import gamma, hyp2f1
from scipy.stats import norm


def abs_moment(a):
    return 2.0 ** (a / 2.0) * gamma((a + 1.0) / 2.0) / math.sqrt(math.pi)


def h(m, a):
    out = 1.0
    for r in range(m):
        out *= a - 2.0 * r
    return out


def gpi_bivariate_graph_series(a, b, rho, terms=30):
    return sum(h(m, a) * h(m, b) * rho ** (2 * m) / math.factorial(2 * m)
               for m in range(terms))


def folded_ratio(y, R):
    y = np.asarray(y, dtype=float)
    n = len(y)
    inv = np.linalg.inv(R)
    det = np.linalg.det(R)
    A = inv - np.eye(n)
    total = 0.0
    for s in itertools.product((-1.0, 1.0), repeat=n):
        x = np.asarray(s) * np.abs(y)
        total += det ** (-0.5) * math.exp(-0.5 * x @ A @ x)
    return total / (2.0 ** n)


def chi2_folded_quadrature(rho):
    R = np.array([[1.0, rho], [rho, 1.0]])

    def integrand(y2, y1):
        r = folded_ratio((y1, y2), R)
        return (r - 1.0) ** 2 * 4.0 * norm.pdf(y1) * norm.pdf(y2)

    value, err = dblquad(integrand, 0.0, 8.0, lambda _: 0.0, lambda _: 8.0,
                         epsabs=2e-10, epsrel=2e-9)
    return value, err


def renyi2_determinant_formula(R):
    n = R.shape[0]
    inv = np.linalg.inv(R)
    det = np.linalg.det(R)
    total = 0.0
    for u in itertools.product((-1.0, 1.0), repeat=n):
        D = np.diag(u)
        M = inv + D @ inv @ D - np.eye(n)
        if np.linalg.eigvalsh(M)[0] <= 0.0:
            return math.inf
        total += 1.0 / det / math.sqrt(np.linalg.det(M))
    return math.log(total / (2.0 ** n))


def renyi2_gauss_hermite(R, nodes=20):
    xs, ws = hermgauss(nodes)
    xs = math.sqrt(2.0) * xs
    ws = ws / math.sqrt(math.pi)
    n = R.shape[0]
    total = 0.0
    for inds in itertools.product(range(nodes), repeat=n):
        x = np.array([xs[i] for i in inds])
        w = math.prod(ws[i] for i in inds)
        r = folded_ratio(x, R)
        total += w * r * r
    return math.log(total)


def pairings(items):
    if not items:
        yield []
        return
    a = items[0]
    for j in range(1, len(items)):
        b = items[j]
        rest = items[1:j] + items[j + 1:]
        for tail in pairings(rest):
            yield [(a, b)] + tail


def wick_x1sq_x2sq_x3sq(r12, r13, r23):
    cov = np.array([[1.0, r12, r13], [r12, 1.0, r23], [r13, r23, 1.0]])
    labels = [0, 0, 1, 1, 2, 2]
    total = 0.0
    for pr in pairings(labels):
        term = 1.0
        for i, j in pr:
            term *= cov[i, j]
        total += term
    return total


def main():
    print("Bivariate normalized absolute moments: graph series versus hypergeometric formula")
    for a, b, rho in [(0.7, 3.2, 0.25), (1.3, 2.6, 0.50), (3.7, 4.4, -0.40)]:
        series = gpi_bivariate_graph_series(a, b, rho)
        exact = hyp2f1(-a / 2.0, -b / 2.0, 0.5, rho * rho)
        print(f"a={a:.1f} b={b:.1f} rho={rho:+.2f} series={series:.15f} exact={exact:.15f} error={abs(series-exact):.3e}")

    print("\nExact Wick check for alpha=(2,2,2)")
    for r12, r13, r23 in [(0.20, -0.15, 0.25), (0.35, 0.10, -0.20)]:
        wick = wick_x1sq_x2sq_x3sq(r12, r13, r23)
        formula = 1.0 + 2.0 * (r12*r12 + r13*r13 + r23*r23) + 8.0 * r12*r13*r23
        print(f"rho=({r12:+.2f},{r13:+.2f},{r23:+.2f}) wick={wick:.15f} formula={formula:.15f} error={abs(wick-formula):.3e}")

    print("\nBivariate folded-Gaussian chi-square and Renyi-2 total correlation")
    for rho in (0.10, 0.30, 0.50):
        num, err = chi2_folded_quadrature(rho)
        chi2_exact = rho**4 / (1.0-rho**4)
        d2_exact = -math.log1p(-rho**4)
        print(f"rho={rho:.2f} chi2_quad={num:.15e} chi2_exact={chi2_exact:.15e} abs_error={abs(num-chi2_exact):.3e} quad_err={err:.2e} D2={d2_exact:.15e}")

    print("\nThree-dimensional determinant formula versus tensor Gauss-Hermite integration")
    R = np.array([[1.0, 0.20, -0.15], [0.20, 1.0, 0.25], [-0.15, 0.25, 1.0]])
    det_formula = renyi2_determinant_formula(R)
    gh = renyi2_gauss_hermite(R, nodes=20)
    print(f"lambda_max={np.linalg.eigvalsh(R)[-1]:.12f} determinant_D2={det_formula:.15e} gauss_hermite_D2={gh:.15e} abs_error={abs(det_formula-gh):.3e}")

    print("\nLocal GPI coefficients")
    a = (0.8, 1.7, 3.1)
    r12, r13, r23 = 0.02, -0.03, 0.025
    q2 = 0.5 * (a[0]*a[1]*r12**2 + a[0]*a[2]*r13**2 + a[1]*a[2]*r23**2)
    q3 = a[0]*a[1]*a[2]*r12*r13*r23
    print(f"quadratic={q2:.15e} triangle_cubic={q3:.15e} sum={q2+q3:.15e}")


if __name__ == "__main__":
    main()
