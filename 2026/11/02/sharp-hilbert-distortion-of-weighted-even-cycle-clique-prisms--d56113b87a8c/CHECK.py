"""Reproduce finite checks for the weighted cyclic-clique metric distortion formula.

Requires Python 3, NumPy and SciPy for the independent linear-program checks.
The infinite theorem is proved analytically; finite samples are corroboration only.
"""
import math
import numpy as np
from scipy.optimize import linprog


def predicted_squared(m, lam):
    c = math.sin(math.pi / (2 * m)) ** 2
    return (m + lam) ** 2 * c / (1 + c * lam * lam)


def direct_pair_checks():
    count = 0
    for m in range(2, 81):
        x = math.pi / (2 * m)
        den = math.sin(x)
        for lam in (0.01, 0.1, 0.25, 0.5, 0.75, 1.0):
            D2 = predicted_squared(m, lam)
            for k in range(m + 1):
                for cross in (0, 1):
                    if k == 0 and not cross:
                        continue
                    d = k + cross * lam
                    sq = D2 * ((math.sin(k * x) / den) ** 2 + cross * lam * lam)
                    assert sq + 1e-9 >= d * d, (m, lam, k, cross, 'lower', sq, d*d)
                    assert sq <= D2 * d*d + 1e-9, (m, lam, k, cross, 'upper', sq, D2*d*d)
                    count += 1
            assert abs(D2 * (1 / den**2 + lam**2) - (m + lam)**2) < 1e-8
    return count


def independent_lp(n, lam):
    """Solve all translation/layer-exchange invariant squared-distance constraints.

    Conditional negativity of a squared Euclidean distance matrix is a
    finite set of independent Fourier-sign inequalities.  Both lower and
    upper pairwise distortion inequalities are imposed on every pair type.
    """
    m = n // 2
    orbits = []
    multiplicities = []
    for layer_diff in (0, 1):
        for k in range(m + 1):
            if layer_diff == 0 and k == 0:
                continue
            orbits.append((layer_diff, k))
            multiplicities.append(1 if k in (0, m) else 2)
    count = len(orbits)
    inequalities = []
    bounds = []
    for j in range(n):
        for sign in (1, -1):
            if j == 0 and sign == 1:
                continue
            inequalities.append([multiplicities[a] * math.cos(2 * math.pi * j * k / n)
                                 * (1 if b == 0 else sign)
                                 for a, (b, k) in enumerate(orbits)] + [0.0])
            bounds.append(0.0)
    for a, (layer_diff, k) in enumerate(orbits):
        metric = k + layer_diff * lam
        row = [0.] * (count+1)
        row[a] = -1.
        inequalities.append(row)
        bounds.append(-metric * metric)
        row = [0.] * (count+1)
        row[a] = 1.
        row[-1] = -metric * metric
        inequalities.append(row)
        bounds.append(0.)
    obj = [0.] * count + [1.]
    res = linprog(obj, A_ub=inequalities, b_ub=bounds,
                  bounds=[(None, None)] * count + [(1., None)], method='highs')
    assert res.success, (n, lam, res.message)
    return res.fun


def main():
    count = direct_pair_checks()
    tested = 0
    max_error = 0.0
    for n in (4, 6, 8, 10, 12, 16, 20):
        for lam in (0.01, 0.1, 0.25, 0.5, 0.75, 1.0):
            solved = independent_lp(n, lam)
            formula = predicted_squared(n//2, lam)
            err = abs(solved - formula)
            max_error = max(max_error, err)
            assert err < 2.e-6, (n, lam, solved, formula)
            tested += 1
    print('CHECK_OK finite_pair_inequalities=', count,
          'independent_Fourier_LP_cases=', tested,
          'maximum_absolute_LP_error=', f'{max_error:.3g}')


if __name__ == '__main__':
    main()
