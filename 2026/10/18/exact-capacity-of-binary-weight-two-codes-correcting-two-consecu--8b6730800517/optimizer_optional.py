#!/usr/bin/env python3
"""Optional exact finite optimization cross-check; requires numpy and scipy.

Run: python optimizer_optional.py [maximum_length]
The main theorem's proof and checker.py do not depend on these libraries.
"""
import itertools
import sys
from collections import defaultdict

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix


def check(n):
    sources = list(itertools.combinations(range(n), 2))
    by_output = defaultdict(list)
    for j, (i, k) in enumerate(sources):
        word = [0] * n
        word[i] = word[k] = 1
        for desc in {tuple(word[:s] + word[s+2:]) for s in range(n-1)}:
            by_output[desc].append(j)
    mat = lil_matrix((len(by_output), len(sources)), dtype=float)
    for row, index_list in enumerate(by_output.values()):
        mat[row, index_list] = 1.0
    result = milp(
        c=-np.ones(len(sources)),
        integrality=np.ones(len(sources)),
        bounds=Bounds(0, 1),
        constraints=LinearConstraint(mat.tocsr(), -np.inf, np.ones(len(by_output))),
        options={'time_limit': 25.0},
    )
    if result.status != 0 or result.fun is None or result.mip_gap > 1e-8:
        raise RuntimeError(f'Finite solve was not proved optimal for length {n}')
    optimum = round(-result.fun)
    expect = 3 * (n - 1) // 4
    assert optimum == expect, (n, optimum, expect)
    return optimum


if __name__ == '__main__':
    high = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    for length in range(3, high+1):
        check(length)
    print(f'EXACT_FINITE_OPTIMIZATION_PASS lengths=3..{high}')
