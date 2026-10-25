#!/usr/bin/env python3
"""Numerically check the first NPT boundary for a spin-1 pure-biquadratic dimer.

Requires NumPy and SciPy. This finite computation is a sanity check only; it is not
used as a proof of the asymptotic statement.
"""
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq

S = np.array([1.0, -1.0, 1.0]) / np.sqrt(3.0)
D = np.diag([2.0, 0.0, -2.0])
P = np.outer(S, S)

def npt_block_margins(x, eps):
    A = D - 3.0 * eps * P
    G = expm(-x * A)
    # Exact 2x2 partial-transpose blocks; positive iff each margin <= 0.
    return (abs(G[0, 2]) - 1.0,
            abs(G[0, 1]) - np.exp(-x),
            abs(G[1, 2]) - np.exp(x))

def first_crossing(eps, block=0):
    hi = max(30.0, 2.0 * np.log(1.0 / eps) + 5.0)
    grid = np.linspace(0.0, hi, 20000)
    vals = [npt_block_margins(x, eps)[block] for x in grid]
    for i in range(1, len(grid)):
        if vals[i-1] <= 0.0 < vals[i]:
            return brentq(lambda x: npt_block_margins(x, eps)[block], grid[i-1], grid[i])
    raise RuntimeError("crossing not bracketed")

if __name__ == '__main__':
    print('eps, x_ac, 0.5*log(4/eps), difference, other_block_crossings')
    for eps in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6):
        x = first_crossing(eps, 0)
        pred = 0.5 * np.log(4.0 / eps)
        others = [first_crossing(eps, j) for j in (1, 2)]
        print(f'{eps:.0e}, {x:.12f}, {pred:.12f}, {x-pred:.3e}, '
              f'{others[0]:.12f};{others[1]:.12f}')
