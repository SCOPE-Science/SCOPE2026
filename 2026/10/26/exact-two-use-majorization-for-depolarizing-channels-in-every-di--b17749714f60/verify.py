"""Independent finite checks of a two-use depolarizing majorization theorem.

Requires Python 3 and NumPy. Finite examples are not the analytic proof.
"""
from fractions import Fraction as F
import numpy as np


def exact_gram_check(amplitudes):
    # If amplitudes are rational and sum of squares is one, the matrix
    # identity has exact rational entries.
    v = [F(k) for k in amplitudes]
    assert sum(x*x for x in v) == 1
    d = len(v)
    left = [[int(i == j) + v[i]*v[j] - (2*v[i]*v[i] if i == j else 0)
             for j in range(d)] for i in range(d)]
    right = [[F(0) for j in range(d)] for i in range(d)]
    for i in range(d):
        for j in range(i+1, d):
            z = [F(0)]*d
            z[i], z[j] = v[j], v[i]
            for k in range(d):
                for m in range(d):
                    right[k][m] += z[k]*z[m]
    assert left == right


def sample_spectrum(d, p, lam):
    a, b = 1-p, p/d
    diag = np.diag(lam)
    X = b*b*np.eye(d*d) + a*b*(np.kron(diag, np.eye(d))
                                      + np.kron(np.eye(d), diag))
    psi = np.zeros(d*d)
    psi[np.arange(d)*(d+1)] = np.sqrt(lam)
    X += a*a*np.outer(psi, psi)
    alpha = a+b
    ref = np.sort([alpha*alpha]+[alpha*b]*(2*(d-1))
                  +[b*b]*((d-1)**2))[::-1]
    return np.linalg.eigvalsh(X)[::-1], ref


def main():
    exact_gram_check([F(3,5), F(4,5)])
    exact_gram_check([F(1,3), F(2,3), F(2,3)])
    exact_gram_check([F(1,5), F(2,5), F(2,5), F(4,5)])
    rng = np.random.default_rng(20261022)
    count = 0
    worst = -1.0
    for d in (2, 3, 4, 5, 7):
        pc = d*d/(d*d-1)
        for p in (0.0, 0.02, .37, .91, 1., (1.+pc)/2., pc):
            for _ in range(30):
                lam = rng.dirichlet(np.ones(d)*rng.uniform(.2, 3.0))
                x, y = sample_spectrum(d, p, lam)
                defect = float(np.max(np.cumsum(x)-np.cumsum(y)))
                assert abs(np.sum(x)-1) < 1e-11
                assert np.min(x) > -1e-11
                assert defect < 1e-11, (d, p, lam, defect)
                worst = max(worst, defect)
                count += 1
    print('exact rational Gram identities: PASS (d=2,3,4)')
    print(f'numerical pure-state majorization examples: PASS ({count})')
    print(f'largest observed numerical Lorenz defect: {worst:.3g}')
    print('The all-dimension, all-input proof is in RESULT.md, not this finite test.')


if __name__ == '__main__':
    main()
