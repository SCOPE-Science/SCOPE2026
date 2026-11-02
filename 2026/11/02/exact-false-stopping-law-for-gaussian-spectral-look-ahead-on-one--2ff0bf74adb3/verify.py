"""Reproducible finite checks for the one-spike Gaussian QB indicator law.

Requires Python 3, NumPy, and SciPy. These are numerical checks, not a
replacement for the all-dimensional proof in RESULT.md.
"""
import math
import numpy as np
from scipy.special import betainc


def false_stop_probability(N, b, d, q, threshold):
    assert N >= 1 and 1 <= b <= N + 1 and 0 < d < 1 and q >= 0
    if threshold <= d:
        return 0.0
    if threshold >= 1:
        return 1.0
    if b == N + 1:
        return 0.0
    odds = (d ** (4*q+2)) * (threshold**2-d**2) / (1-threshold**2)
    return float(betainc(b/2, (N+1-b)/2, odds/(1+odds)))


def sample_indicator(N, b, d, q, omega):
    assert omega.shape == (N+1, b)
    tail = d ** (2*q+1)
    filtered = omega.copy()
    filtered[1:, :] *= tail
    Q, _ = np.linalg.qr(filtered, mode='reduced')
    # Compute ||Q.T @ diag(1,d,...,d)||_2 without forming the large matrix.
    weighted = Q.T.copy()
    weighted[:, 1:] *= d
    direct_sq = float(np.linalg.norm(weighted, ord=2)**2)
    e1_sq = float(np.dot(Q[0, :], Q[0, :]))
    projected_sq = d*d + (1-d*d)*e1_sq
    assert abs(direct_sq-projected_sq) < 2e-12
    # Unfiltered Haar subspace: S = ||P_span(omega)e1||^2.
    U, _ = np.linalg.qr(omega, mode='reduced')
    S = float(np.dot(U[0, :], U[0, :]))
    a = d**(4*q+2)
    transformed_sq = d*d+(1-d*d)*S/(S+a*(1-S))
    assert abs(direct_sq-transformed_sq) < 2e-11
    return math.sqrt(direct_sq)


def main():
    rng = np.random.default_rng(260706758)
    checks = 0
    for N, b, d, q in [(1,1,0.55,0),(7,1,0.13,0),
                       (20,4,0.65,0),(40,5,0.22,1),
                       (60,10,0.38,2),(80,12,0.1,0),
                       (40,40,0.7,0)]:
        for _ in range(75):
            sample_indicator(N,b,d,q,rng.standard_normal((N+1,b)))
            checks += 2

    # Probability monotonicity: more nested Gaussian columns cannot make
    # the spectral norm smaller. All finite beta-CDF evaluations agree.
    for N, d, q, threshold in [(7,0.3,0,0.6), (24,0.25,1,0.7),
                               (41,0.5,0,0.8)]:
        ps = [false_stop_probability(N,b,d,q,threshold)
              for b in range(1,N+2)]
        for j in range(len(ps)-1):
            assert ps[j] > ps[j+1]
            checks += 1
        assert 0 < ps[0] < 1 and ps[-1] == 0
        checks += 1

    # Independent Monte Carlo using the chi-square ratio implied by the
    # Haar projection; compare empirical event frequency against exact CDF.
    for N,b,d,q,threshold in [(300,8,.2,0,.6),(300,8,.2,0,.7),
                               (200,6,.2,0,.6),(170,5,.32,1,.9)]:
        draws = 70000
        z = rng.chisquare(b, size=draws)
        v = rng.chisquare(N+1-b, size=draws)
        s = z/(z+d**(4*q+2)*v)
        observed = float(np.mean(d*d+(1-d*d)*s <= threshold**2))
        predicted = false_stop_probability(N,b,d,q,threshold)
        bound = 6*math.sqrt(max(predicted*(1-predicted),1e-5)/draws)+0.001
        assert abs(observed-predicted) < bound, (observed,predicted,bound)
        checks += 1

    # The sharp dimension-dependent example: despite ||E||_2=1 and best
    # rank-one approximation error .1, the look-ahead statistic is under
    # .5 with probability greater than 98% for 16 Gaussian columns.
    p = false_stop_probability(10000,16,0.1,0,0.5)
    assert abs(p-0.9897679877478459) < 5e-13
    checks += 1

    # Critical scaling for a fixed sketch width, checked only as a finite
    # asymptotic diagnostic; the distributional limit is proved on paper.
    b=8
    for alpha in [0.3,0.5,0.8]:
        vals=[]
        for N in [300,3000,30000]:
            d=N**(-alpha)
            vals.append(false_stop_probability(N,b,d,0,0.5))
        if alpha < .5:
            assert vals[-1] > vals[0]
        elif alpha > .5:
            assert vals[-1] < vals[0]
        checks += 1

    print(f'PASS: {checks} deterministic and seeded numerical checks')
    print(f'Example false-stop probability: {p:.12f}')
    print('All-dimensional correctness rests on the analytic proof, not simulations.')


if __name__ == '__main__':
    main()
