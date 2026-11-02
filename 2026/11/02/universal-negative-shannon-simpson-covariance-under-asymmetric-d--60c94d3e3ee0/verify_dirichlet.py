"""Exact finite checks for the Shannon--Simpson Dirichlet covariance formula.

Uses only the Python standard library.  The analytical theorem in RESULT.md
is not inferred from this finite verification.
"""
from fractions import Fraction as F
from itertools import product


def harmonic(n):
    return sum((F(1, j) for j in range(1, int(n) + 1)), F(0))


def cov_weighted(alphas, psis):
    A = sum(alphas)
    weights = [a / A for a in alphas]
    mean_a = sum((w * a for w, a in zip(weights, alphas)), F(0))
    mean_p = sum((w * p for w, p in zip(weights, psis)), F(0))
    return sum((w * (a - mean_a) * (p - mean_p)
                for w, a, p in zip(weights, alphas, psis)), F(0))


def formula(alphas, psis):
    A = sum(alphas)
    Q = sum((a*a for a in alphas), F(0))
    V = cov_weighted(alphas, psis)
    return -((A*A-Q)/ (A+1) + 2*A*V)/(A*(A+1)*(A+2))


def independent_mixed_moment(alphas):
    # Integer Dirichlet parameters: psi(k+1) = H_k - EulerGamma.
    # Every EulerGamma term cancels in the covariance.
    A = sum(alphas)
    H_mean = harmonic(A) - sum((a*harmonic(a) for a in alphas), F(0))/A
    G_mean = sum((a*(a+1) for a in alphas), F(0))/(A*(A+1))
    HG = F(0)
    for i, ai in enumerate(alphas):
        for j, aj in enumerate(alphas):
            if i == j:
                weight = ai*(ai+1)*(ai+2)/ (A*(A+1)*(A+2))
                shift = harmonic(ai+2)
            else:
                weight = ai*aj*(aj+1)/ (A*(A+1)*(A+2))
                shift = harmonic(ai)
            HG += weight*(harmonic(A+2)-shift)
    return HG-H_mean*G_mean


def run():
    checked = 0
    for m in range(2, 6):
        for aa in product(range(1, 6), repeat=m):
            alphas = [F(x) for x in aa]
            psis = [harmonic(x) for x in aa]
            cv = formula(alphas, psis)
            direct = independent_mixed_moment(alphas)
            assert cv == direct, (aa,cv,direct)
            assert cv < 0, (aa,cv)
            if len(set(aa)) == 1:
                t = alphas[0]
                A = sum(alphas)
                assert cv == -(m-1)*t/((A+1)**2*(A+2))
            checked += 1
    assert checked == sum(5**m for m in range(2, 6))
    # At total concentration 2: exact half-integer psi difference is 2/3.
    a = [F(1, 2), F(3, 2)]
    assert formula(a, [F(0), F(2, 3)]) == -F(1, 24)
    assert formula([F(1), F(1)], [F(1), F(1)]) == -F(1, 36)
    print(f'PASS: {checked} exact independent mixed-moment comparisons;')
    print('PASS: strict sign, symmetric case and two fixed-total asymmetry examples.')


if __name__ == '__main__':
    run()
