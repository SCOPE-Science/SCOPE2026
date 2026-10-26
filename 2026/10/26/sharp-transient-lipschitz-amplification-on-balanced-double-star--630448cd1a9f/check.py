"""Independent finite-dimensional checks of the balanced-double-star heat formula.

Requires Python 3, NumPy, SciPy.  A finite computation supplements the proof;
it does not certify all degrees or positive times.
"""
import math
import numpy as np
from scipy.linalg import expm


def formula(d, t):
    delta = math.sqrt(d*d + 6*d + 1)
    lo = (d + 3 - delta) / 2
    hi = (d + 3 + delta) / 2
    alpha = (hi + 2*d - 2) / delta
    return alpha*math.exp(-lo*t) - (alpha-1)*math.exp(-hi*t)


def edge_matrix(d):
    # Leaves -> left hub; left hub -> right hub; right hub -> leaves.
    vertices = 2*d + 2
    edges = 2*d + 1
    B = np.zeros((edges, vertices))
    for j in range(d):
        B[j, j] = -1
        B[j, d] = 1
    B[d, d] = -1
    B[d, d+1] = 1
    for j in range(d):
        B[d+1+j, d+1] = -1
        B[d+1+j, d+2+j] = 1
    return B


def run():
    cases = 0
    error = 0.0
    for d in [1,2,3,4,5,7,10,15,20]:
        B = edge_matrix(d)
        L = B.T @ B
        M = B @ B.T
        for t in [0.0001, .01, .07, .21, .43, 1., 3.]:
            E = expm(-t*M)
            E_v = expm(-t*L)
            mismatch = np.max(np.abs(B @ E_v - E @ B))
            assert mismatch < 3e-12, (d, t, mismatch)
            central = np.sum(np.abs(E[d]))
            peak_row = np.max(np.sum(np.abs(E), axis=1))
            predicted = formula(d, t)
            err = max(abs(central-predicted), abs(peak_row-predicted))
            error = max(error, err)
            assert err < 2e-11, (d, t, err)
            assert np.min(E[d]) > -2e-13, (d, t)
            cases += 1
        delta = math.sqrt(d*d+6*d+1)
        lo = (d+3-delta)/2
        hi = (d+3+delta)/2
        A = (hi+2*d-2)/delta
        if d >= 2:
            tstar = math.log(hi*(A-1)/(lo*A))/delta
            eps = min(tstar/3, .05)
            assert formula(d,tstar) > max(formula(d,tstar-eps), formula(d,tstar+eps))
    print('CHECK_OK cases=', cases, 'max_abs_error=', f'{error:.3e}')
    for d in (2, 3, 10, 100, 1000):
        delta = math.sqrt(d*d+6*d+1)
        lo = (d+3-delta)/2
        hi = (d+3+delta)/2
        A = (hi+2*d-2)/delta
        tstar = math.log(hi*(A-1)/(lo*A))/delta
        print('d=',d,'time=',format(tstar,'.12g'),'max=',format(formula(d,tstar),'.12g'))

if __name__ == '__main__':
    run()
