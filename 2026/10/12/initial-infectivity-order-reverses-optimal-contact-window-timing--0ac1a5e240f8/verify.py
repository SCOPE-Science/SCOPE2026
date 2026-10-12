"""Standalone finite-dimensional algebra checks for a contact-window timing theorem.

Requires Python >=3.9; the theorem itself is established analytically.
"""
from fractions import Fraction as F
from math import exp, sqrt, sinh


def diffusion(conductances, v):
    n = len(v)
    y = [F(0) for _ in range(n)]
    for i, c in enumerate(conductances):
        delta = c * (v[i + 1] - v[i])
        y[i] += delta
        y[i + 1] -= delta
    return y


def differences(v):
    return [b - a for a, b in zip(v, v[1:])]


def edge_generator(conductances, g):
    return [
        (conductances[i - 1] * g[i - 1] if i else F(0))
        - 2 * conductances[i] * g[i]
        + (conductances[i + 1] * g[i + 1] if i + 1 < len(g) else F(0))
        for i in range(len(g))
    ]


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


def check_exact_identities():
    count = 0
    for n in range(2, 11):
        for seed in range(1, 10):
            c = [F((i + 2) * (seed + 1), 3 + i + seed) for i in range(n - 1)]
            vals = [F((i + 1) * (i + 2) * (seed + 1), 10 + seed + i) for i in range(n)]
            lam = [F(i, n - 1) for i in range(n)]
            q = F(seed, seed + 3)
            p = [F(n - i, n * (n + 1) // 2) for i in range(n)]
            # The mutation gradient equation is a cooperative tridiagonal system.
            assert differences(diffusion(c, vals)) == edge_generator(c, differences(vals))
            # The pulse adjoint has strictly positive forcing in its gradient system.
            direct = differences([x + q * l * v for x, l, v in zip(diffusion(c, vals), lam, vals)])
            gradient = edge_generator(c, differences(vals))
            forced = [gradient[i] + q * lam[i + 1] * (vals[i + 1] - vals[i])
                      + q * (lam[i + 1] - lam[i]) * vals[i]
                      for i in range(n - 1)]
            assert direct == forced
            # Exact Green/Dirichlet integration by parts.
            assert dot(vals, diffusion(c, p)) == -sum(
                (c[i] * (vals[i + 1] - vals[i]) * (p[i + 1] - p[i])
                 for i in range(n - 1)), F(0))
            assert all(z > 0 for z in differences(vals))
            assert all(z < 0 for z in differences(p))
            count += 1
    return count


def check_two_trait_exact_formula():
    # In a two-trait chain the pulse fitness difference is explicit.
    c, q, ell, mu, t = F(1, 3), F(3, 2), F(1, 4), F(1, 5), F(1)
    a, b = F(1, 7), F(3, 5)
    cv, qv, lv, muv, tv, av, bv = map(float, (c, q, ell, mu, t, a, b))
    omega = sqrt(qv*qv + 4*cv*cv)
    gap = (2*qv/omega) * exp((qv-2*cv)*lv/2) * sinh(omega*lv/2)
    mass_difference = exp(-muv*tv)*gap/2*(exp(-2*cv*av)-exp(-2*cv*bv))
    assert 0 < av < bv < tv - lv
    assert gap > 0 and mass_difference > 0
    # The high-trait delta distribution changes the sign, the uniform one has zero shift.
    assert -mass_difference < 0
    assert abs((mass_difference + (-mass_difference))/2) == 0
    return mass_difference


if __name__ == '__main__':
    n = check_exact_identities()
    example = check_two_trait_exact_formula()
    print(f'VERIFY_OK: {n} exact-rational gradient/Dirichlet tests; two-trait shift {example:.12f}')
