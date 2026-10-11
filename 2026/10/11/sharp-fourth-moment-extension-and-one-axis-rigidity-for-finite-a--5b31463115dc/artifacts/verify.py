"""Independent finite checks for the union-of-transverse-subgroups fourth-moment bound.

Run: python artifacts/verify.py. Only Python 3 and NumPy are required.
Finite numerical tests corroborate the proof; they do not establish the universal result.
"""
import itertools
import math
import numpy as np


def group_elements(moduli):
    return list(itertools.product(*(range(m) for m in moduli)))


def char_table(moduli):
    elements = group_elements(moduli)
    q = len(elements)
    T = np.empty((q, q), dtype=complex)
    for i, k in enumerate(elements):
        for j, x in enumerate(elements):
            T[i, j] = np.exp(2j * np.pi * sum(k[t] * x[t] / moduli[t]
                                                   for t in range(len(moduli))))
    return elements, T


def ratio(c, a, b, T):
    # a,b are length-q vectors, with a[0]=b[0]=0: center counted once.
    A = T @ a
    B = T @ b
    X = c + A[:, None] + B[None, :]
    energy = abs(c)**2 + np.vdot(a, a).real + np.vdot(b, b).real
    return np.mean(abs(X)**4) / energy**2


def check_group(moduli, seed):
    rng = np.random.default_rng(seed)
    elements, T = char_table(moduli)
    q = len(elements)
    ntests = 400
    for _ in range(ntests):
        a = rng.normal(size=q) + 1j * rng.normal(size=q)
        b = rng.normal(size=q) + 1j * rng.normal(size=q)
        a[0] = 0
        b[0] = 0
        c = complex(*rng.normal(size=2))
        R = ratio(c, a, b, T)
        assert R <= q + 1e-8, (moduli, R, q)
    for k in range(q):
        a = np.conjugate(T[k, :]).copy()
        c = a[0]
        a[0] = 0
        b = np.zeros(q, dtype=complex)
        R = ratio(c, a, b, T)
        assert abs(R - q) < 1e-8, (moduli, R)
        R2 = ratio(c, b, a, T)
        assert abs(R2 - q) < 1e-8, (moduli, R2)
    print(f"PASS group {moduli}, order {q}: {ntests} complex inputs; {2*q} exact-line extremizers")


def check_centered_moments():
    rng = np.random.default_rng(840531)
    for q in range(5, 18):
        K = q - 2 + 1/(q - 1)
        g = math.sqrt(K - 1)
        for _ in range(300):
            z = rng.normal(size=q) + 1j*rng.normal(size=q)
            z -= np.mean(z)
            u = np.mean(abs(z)**2)
            fourth = np.mean(abs(z)**4)
            third = np.mean(z*abs(z)**2)
            assert fourth <= K*u*u+1e-9
            assert abs(third) <= g*u**1.5+1e-9
        x = np.full(q, -1.0, dtype=complex)
        x[0] = q-1
        x /= np.sqrt(np.mean(abs(x)**2))
        assert abs(np.mean(abs(x)**4) - K) < 1e-9
        assert abs(abs(np.mean(x*abs(x)**2)) - g) < 1e-9
    print("PASS centered complex-moment tests, orders 5..17: 3900 random, 13 sharp examples")


def check_low_order_obstruction():
    _, T = char_table((3,))
    a = np.ones(3, dtype=complex); b = a.copy()
    a[0] = b[0] = 0
    R = ratio(1, a, b, T)
    assert abs(R - 77/25) < 1e-10, R
    print("PASS order-three obstruction: exact ratio 77/25 > 3")


if __name__ == '__main__':
    check_centered_moments()
    for k, m in enumerate([(5,), (6,), (7,), (8,), (9,), (10,), (11,), (2, 3), (2, 2, 2), (3, 3), (2, 5)]):
        check_group(m, 7100 + k)
    check_low_order_obstruction()
    print("ALL CHECKS PASSED")
