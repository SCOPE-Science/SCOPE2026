"""Independent numerical spot checks for a finite Fourier half-window identity.

Requires NumPy; these finite checks corroborate, but do not prove, the
statements for unbounded group orders and all masks.
"""
import itertools
import math
import random
import numpy as np


def predicted_gap_product(N, F):
    roots = np.exp(2j * np.pi * np.arange(2 * N) / (2 * N))
    E = [a for a in F if a % 2 == 0]
    O = [a for a in F if a % 2 == 1]
    r = min(len(E), len(O))
    if r == 0:
        return 1.0
    value = 0.0
    for I in itertools.combinations(E, r):
        for J in itertools.combinations(O, r):
            num = math.prod(abs(roots[a] - roots[b]) ** 2
                            for a, b in itertools.combinations(I, 2))
            num *= math.prod(abs(roots[a] - roots[b]) ** 2
                             for a, b in itertools.combinations(J, 2))
            den = math.prod(abs(roots[a] - roots[b]) ** 2
                            for a in I for b in J)
            value += num / den
    return value * (2 / N) ** (2 * r)


def check(N, F):
    F = tuple(F)
    e = sum(k % 2 == 0 for k in F)
    o = len(F) - e
    r = min(e, o)
    times = np.arange(N)
    U = np.array([
        [sum(np.exp(2j * np.pi * (l-k) * times / (2*N))) / N - (k == l)
         for l in F]
        for k in F], dtype=complex)
    U = (U + U.conj().T) / 2
    eig = np.linalg.eigvalsh(U)
    assert abs(np.trace(U)) < 2e-10
    zero_num = sum(abs(v) < 1e-9 for v in eig)
    assert zero_num == abs(e-o), (N, F, eig)
    assert np.max(abs(eig + eig[::-1])) < 2e-9
    predicted = predicted_gap_product(N, F)
    spectral = math.prod(sorted(abs(eig))[-2*r:]) if r else 1.0
    if abs(spectral) + predicted > 1e-13:
        err = abs(spectral - predicted) / max(spectral, predicted)
        assert err < 2e-7, (N, F, spectral, predicted, err)
    return predicted


def main():
    rng = random.Random(51799)
    checks = 0
    for N in range(1, 5):
        for bitmask in range(1, 1 << (2 * N)):
            F = [k for k in range(2 * N) if bitmask >> k & 1]
            check(N, F)
            checks += 1
    for N in range(5, 8):
        for _ in range(120):
            F = sorted(rng.sample(range(2*N), rng.randint(1, 2*N)))
            check(N, F)
            checks += 1
    print(f'VERIFY_OK exhaustive_n=1..4 random_n=5..7 checks={checks}')


if __name__ == '__main__':
    main()
