"""Finite corroboration of the dyadic four-point uncertainty gap.

Run with: python verify.py
Requires numpy; uses floating point for sampled Fourier values only.
All-size conclusions require the accompanying analytic proof.
"""
import itertools
import random
import numpy as np


def test_signal(N, sites, coeffs):
    arr = np.zeros(N, dtype=np.complex128)
    arr[list(sites)] = coeffs
    spectrum = np.fft.fft(arr)
    supp = int(np.count_nonzero(np.abs(spectrum) > 1e-7))
    is_order_four_coset = ({(sites[0] + j * (N // 4)) % N for j in range(4)} == set(sites))
    assert supp >= N // 4, (N, sites, coeffs, supp)
    if supp < 3 * N // 8:
        assert supp == N // 4 and is_order_four_coset, (N, sites, coeffs, supp)
    return supp


def main():
    trials = 0
    rng = random.Random(20261015)
    alphabet = [1, -1, 1j, -1j]
    N = 8
    for sites in itertools.combinations(range(N), 4):
        for coeffs in itertools.product(alphabet, repeat=4):
            test_signal(N, sites, coeffs)
            trials += 1
    for N in (16, 32, 64, 128):
        for _ in range(1200):
            sites = tuple(sorted(rng.sample(range(N), 4)))
            coeffs = tuple(rng.choice(alphabet) for _ in range(4))
            test_signal(N, sites, coeffs)
            trials += 1
    for N in (8, 16, 32, 64, 128, 256):
        h = N // 8
        sites = (0, h, N // 2, N // 2 + h)
        assert test_signal(N, sites, (1, 1, 1, 1)) == 3 * N // 8
        trials += 1
        sites = (0, N // 4, N // 2, 3 * N // 4)
        assert test_signal(N, sites, (1, 1, 1, 1)) == N // 4
        trials += 1
    print('VERIFY_OK', trials, 'finite sampled comparisons')


if __name__ == '__main__':
    main()
