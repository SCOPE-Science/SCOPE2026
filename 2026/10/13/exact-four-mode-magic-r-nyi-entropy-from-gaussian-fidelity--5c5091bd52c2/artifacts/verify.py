#!/usr/bin/env python3
import math


def gamma_apply(vec, mode, kind):
    """Apply a Jordan--Wigner Majorana on one of eight physical fermion modes."""
    out = [0j] * len(vec)
    for idx, amp in enumerate(vec):
        if amp == 0:
            continue
        parity = (idx & ((1 << mode) - 1)).bit_count() & 1
        z = -1 if parity else 1
        bit = (idx >> mode) & 1
        j = idx ^ (1 << mode)
        phase = z if kind == 0 else z * (1j if bit == 0 else -1j)
        out[j] += phase * amp
    return out


def paired_majorana(vec, i):
    """Apply gamma_i on copy 1 and gamma_i on copy 2 for i=0,...,7."""
    mode = i // 2
    kind = i % 2
    v = gamma_apply(vec, 4 + mode, kind)
    return gamma_apply(v, mode, kind)


def balanced_rotation(vec, i):
    c = math.cos(math.pi / 8)
    s = math.sin(math.pi / 8)
    gv = paired_majorana(vec, i)
    return [c * a + s * b for a, b in zip(vec, gv)]


def purity_direct(p):
    q = 1 - p
    psi = [0j] * 16
    psi[0] = math.sqrt(p)
    psi[15] = math.sqrt(q)

    two_copy = [0j] * 256
    for a, x in enumerate(psi):
        for b, y in enumerate(psi):
            two_copy[a + (b << 4)] = x * y

    for i in range(8):
        two_copy = balanced_rotation(two_copy, i)

    rho = [[0j] * 16 for _ in range(16)]
    for a in range(16):
        for b in range(16):
            rho[a][b] = sum(
                two_copy[a + (c << 4)] * two_copy[b + (c << 4)].conjugate()
                for c in range(16)
            )
    return sum(abs(rho[a][b]) ** 2 for a in range(16) for b in range(16))


def formula(p):
    t = p * (1 - p)
    return 1 - 3 * t + 1.5 * t * t


for p in [0.5, 0.6, 0.8, 1.0]:
    direct = purity_direct(p)
    expected = formula(p)
    print(p, direct, expected, abs(direct - expected))
    assert abs(direct - expected) < 1e-12

assert abs(formula(0.5) - 11 / 32) < 1e-15
assert all(formula(0.5) <= formula(0.5 + k / 1000) + 1e-15 for k in range(501))
print("VERIFY_OK")
