#!/usr/bin/env python3
import cmath
import math


def bell_quantities(x, D, aligned):
    s = math.sqrt(1.0 + D * D)
    y = x * s
    r = math.exp(x) * math.cosh(y)
    a = 1.0 / (2.0 * (1.0 + r))
    b = r / (2.0 * (1.0 + r))
    nu = math.exp(x) * math.sinh(y) / (2.0 * (1.0 + r))
    if not aligned:
        nu /= s
    q = (b + nu, a, a, b - nu)
    return s, y, q


def average_from_q(q):
    q0, q1, q2, q3 = q
    assert abs(q1 - q2) < 1e-14
    a = q1
    return q0 * q0 + q3 * q3 + (2.0 / 3.0) * q0 * q3 + (4.0 / 3.0) * a * a


def aligned_formula(x, D):
    s = math.sqrt(1.0 + D * D)
    y = x * s
    den = 3.0 * (1.0 + math.exp(x) * math.cosh(y)) ** 2
    return (1.0 + math.exp(2.0 * x) * (3.0 * math.cosh(y) ** 2 - 1.0)) / den


def source_formula(x, D):
    s = math.sqrt(1.0 + D * D)
    y = x * s
    den = 6.0 * s * s * (1.0 + math.exp(x) * math.cosh(y)) ** 2
    num = 2.0 * s * s + math.exp(2.0 * x) * (
        (2.0 * s * s - 1.0) + (2.0 * s * s + 1.0) * math.cosh(2.0 * y)
    )
    return num / den


def gain_formula(x, D):
    s = math.sqrt(1.0 + D * D)
    y = x * s
    den = 3.0 * s * s * (1.0 + math.exp(x) * math.cosh(y)) ** 2
    return math.exp(2.0 * x) * math.sinh(y) ** 2 * D * D / den


def logical_state(theta, phi):
    return (0j, cmath.exp(1j * phi) * math.sin(theta / 2.0), math.cos(theta / 2.0), 0j)


def pauli_apply(index, bit, amp0, amp1):
    if index == 0:
        return amp0, amp1
    if index == 1:
        return amp1, amp0
    if index == 2:
        return -1j * amp1, 1j * amp0
    if index == 3:
        return amp0, -amp1
    raise ValueError(index)


def kron_pauli_state(i, j, psi):
    out = [0j] * 4
    for a in (0, 1):
        for b in (0, 1):
            amp = psi[2 * a + b]
            if amp == 0:
                continue
            va = [0j, 0j]
            va[a] = 1.0
            vb = [0j, 0j]
            vb[b] = 1.0
            aa = pauli_apply(i, a, va[0], va[1])
            bb = pauli_apply(j, b, vb[0], vb[1])
            for ap in (0, 1):
                for bp in (0, 1):
                    out[2 * ap + bp] += amp * aa[ap] * bb[bp]
    return tuple(out)


def overlap_sq(psi, phi):
    z = sum(psi[k].conjugate() * phi[k] for k in range(4))
    return (z.real * z.real + z.imag * z.imag)


def quadrature_average(x, D, n_z=36, n_phi=72):
    _, _, q = bell_quantities(x, D, True)
    total = 0.0
    for iz in range(n_z):
        z = -1.0 + (2.0 * iz + 1.0) / n_z
        theta = math.acos(z)
        for ip in range(n_phi):
            phi = 2.0 * math.pi * (ip + 0.5) / n_phi
            psi = logical_state(theta, phi)
            fidelity = 0.0
            for i in range(4):
                for j in range(4):
                    transformed = kron_pauli_state(i, j, psi)
                    fidelity += q[i] * q[j] * overlap_sq(psi, transformed)
            total += fidelity
    return total / (n_z * n_phi)


def main():
    grid = [
        (-1.3, -2.0), (-1.3, -0.7), (-1.3, 0.4), (-1.3, 1.9),
        (-0.4, -2.3), (-0.4, -0.8), (-0.4, 0.6), (-0.4, 2.1),
        (0.2, -2.2), (0.2, -0.5), (0.2, 0.9), (0.2, 2.4),
        (0.9, -1.8), (0.9, -0.6), (0.9, 0.5), (0.9, 1.7),
        (1.5, -1.4), (1.5, -0.3), (1.5, 0.8), (1.5, 1.5),
    ]
    source_count = 0
    gain_count = 0
    for x, D in grid:
        _, _, q_un = bell_quantities(x, D, False)
        f_un = average_from_q(q_un)
        f_src = source_formula(x, D)
        assert abs(f_un - f_src) < 2e-12, (x, D, f_un, f_src)
        source_count += 1

        _, _, q_al = bell_quantities(x, D, True)
        f_al = average_from_q(q_al)
        assert abs(f_al - aligned_formula(x, D)) < 2e-12
        assert abs((f_al - f_un) - gain_formula(x, D)) < 2e-12
        if x != 0.0 and D != 0.0:
            assert f_al > f_un
        gain_count += 1

    quad_cases = [(1.0, 0.7), (-1.0, 2.0), (0.4, 3.0), (-0.3, -1.2)]
    for x, D in quad_cases:
        qv = quadrature_average(x, D)
        assert abs(qv - aligned_formula(x, D)) < 4e-4, (x, D, qv, aligned_formula(x, D))

    limit_count = 0
    for x in (-0.8, 0.8):
        D = 18.0
        fa = aligned_formula(x, D)
        fz = source_formula(x, D)
        assert abs(fa - 1.0) < 2e-5, (x, fa)
        assert abs(fz - 2.0 / 3.0) < 2e-3, (x, fz)
        limit_count += 1

    print(
        f"VERIFY_OK source_formula={source_count} gain_identity={gain_count} "
        f"quadrature={len(quad_cases)} limits={limit_count}"
    )


if __name__ == '__main__':
    main()
