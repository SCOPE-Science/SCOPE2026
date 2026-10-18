"""Finite checks for boundary-jet residuals in the Hardy space.

Requires Python 3 with numpy and sympy. Run: python verify.py
This corroborates the infinite-dimensional asymptotic proof, not replaces it.
"""
import numpy as np
import sympy as sp


def moment_polynomial(m):
    h = sp.Matrix([[sp.Rational(1, a + b + 1) for b in range(m)]
                   for a in range(m)])
    c = h.inv()[:, 0]
    t = sp.Symbol('t')
    p = sp.expand(sum(c[j] * t**j for j in range(m)))
    assert h * c == sp.eye(m)[:, 0]
    assert p.subs(t, 0) == m*m
    return p


def check_case(nodes, multiplicities, degrees):
    d = sum(multiplicities)
    limit = sum(m*m for m in multiplicities)
    errs = []
    for n in degrees:
        K = n + d + 1
        indices = np.arange(K, dtype=float)
        t = indices / K
        rows = []
        scales = []
        target = []
        for z, m in zip(nodes, multiplicities):
            for ell in range(m):
                rows.append((t**ell) * z**indices / np.sqrt(K))
                scales.append(K**ell)
                target.append(1.0 if ell == 0 else 0.0)
        scaled_A = np.vstack(rows)
        scaled_b = np.array(target, dtype=complex)/np.sqrt(K)
        gram = scaled_A @ scaled_A.conj().T
        y = np.linalg.solve(gram, scaled_b)
        residual = scaled_A.conj().T @ y
        assert np.max(np.abs(scaled_A @ residual - scaled_b)) < 1e-6
        # Original constraints obtained by multiplying each scaled row by
        # the positive factor K**(ell+1/2).
        raw_target = np.array(target)
        raw_constraints = (scaled_A @ residual) * np.sqrt(K) * np.array(scales)
        assert np.max(np.abs(raw_constraints - raw_target)) < 1e-4
        leading = np.zeros(K, dtype=complex)
        for z, m in zip(nodes, multiplicities):
            p = moment_polynomial(m)
            poly_coeff = np.array([float(p.coeff(sp.Symbol('t'), j)) for j in range(m)])
            values = np.polynomial.polynomial.polyval(t, poly_coeff)
            leading += np.conj(z)**indices * values
        coeff_gap = float(np.max(np.abs(K * residual - leading)))
        rate_gap = float(abs(K*np.vdot(residual, residual).real-limit))
        errs.append((rate_gap, coeff_gap))
        print(f"degree={n:4d} K={K:4d} K*error_sq={K*np.vdot(residual,residual).real:12.8f} "
              f"rate_gap={rate_gap:10.6f} profile_gap={coeff_gap:10.6f}")
    assert errs[-1][0] < errs[0][0]
    assert errs[-1][1] < errs[0][1]
    return limit


if __name__ == '__main__':
    for m in range(1, 5):
        print(f"Legendre reproducer m={m}: {moment_polynomial(m)}")
    print('Case 1: nodes {1,-1}, multiplicities {2,3}, predicted numerator 13')
    assert check_case([1+0j, -1+0j], [2,3], [10,30,70,140,280]) == 13
    print('Case 2: nodes {1,exp(2*pi*i/3)}, multiplicities {2,1}, predicted numerator 5')
    assert check_case([1+0j, np.exp(2j*np.pi/3)], [2,1], [10,30,70,140,280]) == 5
    print('All finite consistency checks passed; these do not certify the limit.')
