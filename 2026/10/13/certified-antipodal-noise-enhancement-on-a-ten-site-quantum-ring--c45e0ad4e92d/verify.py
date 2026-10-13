#!/usr/bin/env python3
"""Exact-integer residual certificate for a ten-site quantum-ring transport witness."""
import json
from pathlib import Path


def check():
    c = json.loads((Path(__file__).parent / 'certificate.json').read_text(encoding='utf-8'))
    assert (c['n'], c['trap_site'], c['initial_site'], c['mu_num'],
            c['mu_den'], c['kappa'], c['gamma_den'], c['scale']) == (
                10, 0, 5, 1, 1000, 30, 5, 10**14)
    assert len(c['cases']) == 2
    n = 10
    scale = c['scale']
    exact = {}
    for entry in c['cases']:
        gamma_num = entry['gamma_num']
        assert gamma_num in (0, 1) and gamma_num not in exact
        u, v = entry['real'], entry['imag']
        assert len(u) == len(v) == n
        assert all(len(row) == n and all(type(k) is int for k in row) for row in u + v)
        residual_sum = 0
        for i in range(n):
            for j in range(n):
                coefficient = 2 + 30000 * (int(i == 0) + int(j == 0))
                coefficient += 400 * gamma_num * int(i != j)
                commutator_real = sum(u[(i + s) % n][j] for s in (-1, 1))
                commutator_real -= sum(u[i][(j + s) % n] for s in (-1, 1))
                commutator_imag = sum(v[(i + s) % n][j] for s in (-1, 1))
                commutator_imag -= sum(v[i][(j + s) % n] for s in (-1, 1))
                residual_real = coefficient*u[i][j] - 1000*commutator_imag
                residual_real -= 1000*scale*int(i == 5 and j == 5)
                residual_imag = coefficient*v[i][j] + 1000*commutator_real
                residual_sum += abs(residual_real) + abs(residual_imag)
        exact[gamma_num] = (u[0][0], residual_sum)
    assert exact[0] == (1430222719987, 244156), exact[0]
    assert exact[1] == (1453306925594, 187408), exact[1]
    # Hilbert-Schmidt coercivity: ||M^{-1}|| <= 1/(2*mu) = 500.
    # Rate eta = 2*kappa*Re(X_00) = 60*Re(X_00).
    # The residual absolute-entry sum gives an exact error <= 30*S/scale.
    u0, s0 = exact[0]
    u1, s1 = exact[1]
    gap_num = 60*(u1-u0) - 30*(s0+s1)
    assert gap_num == 1385039389500 and gap_num > 0
    # The bound is therefore exactly 0.013850393895.
    assert gap_num*10**8 > 1385039*scale  # gap > 0.01385039
    print('VERIFY_OK n=10 cases=2 residuals=%d,%d gap_lower=%d/%d' %
          (s0, s1, gap_num, scale))

if __name__ == '__main__':
    check()
