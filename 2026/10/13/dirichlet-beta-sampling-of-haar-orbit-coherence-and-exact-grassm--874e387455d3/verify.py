"""Reproducibility checks for Dirichlet-Beta Haar-orbit coherence formulas.

Uses NumPy for seeded Haar-unitary simulation. Simulation corroborates but cannot prove the analytic formulas.
"""
import math
import numpy as np


def mean_coherence(d, k):
    if not (isinstance(d, int) and isinstance(k, int) and d >= 2 and 1 <= k < d):
        raise ValueError("Require integers d>=2 and 1<=k<d")
    return math.exp(math.log(d-1)-math.log(k)+math.lgamma(1.5)
                    +math.lgamma(d-1)-math.lgamma(d-.5)
                    +math.lgamma(k+.5)+math.lgamma(d-k+.5)
                    -math.lgamma(k)-math.lgamma(d-k))


def haar(d, rng):
    z = rng.normal(size=(d,d)) + 1j*rng.normal(size=(d,d))
    q,r = np.linalg.qr(z)
    diag = np.diag(r)
    return q * (diag / np.abs(diag))[None, :]


def main():
    expected_pi_ratios = {(4,2): 9/20, (5,2): 9/14, (6,3): 25/42}
    for (d,k), ratio in expected_pi_ratios.items():
        assert abs(mean_coherence(d,k)/math.pi-ratio) < 1e-12
    for d in range(2,16):
        assert abs(mean_coherence(d,1)-math.pi*(d-1)/4) < 1e-10
        assert abs(mean_coherence(d,d-1)-math.pi/4) < 1e-10
        for k in range(1,d):
            second = (d-k)/(k*d*(d*d-1))
            from_beta = (1/k**2) * (k*(d-k)/(d*(d+1))) / (d-1)
            assert abs(second-from_beta) < 1e-14
    rng = np.random.default_rng(17291)
    cases = [(2,1),(3,1),(4,2),(5,2),(6,3),(8,3),(9,8)]
    for d,k in cases:
        sample = []
        spectrum = np.diag([1/k]*k + [0]*(d-k))
        for _ in range(3000):
            u=haar(d,rng)
            a=u@spectrum@u.conj().T
            sample.append(float(np.sum(np.abs(a)) - np.sum(np.abs(np.diag(a)))))
        got = float(np.mean(sample))
        expected = mean_coherence(d,k)
        assert abs(got-expected) < 0.07, (d,k,got,expected)
    print('VERIFY_OK endpoints=passed gamma_cases=3 second_moments=passed Haar_samples=21000')

if __name__ == '__main__':
    main()
