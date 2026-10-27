"""Independent reproducibility checks for the Gaussian-increment-sign example.
Uses only the Python standard library; simulations do not replace the theorem's proof.
"""
import math
import random

SEED = 261023669
SAMPLE_N = 90000

def amp(t, eps):
    return 1.0 + eps * math.cos(2 * math.pi * t)

def covlag(t, lag, eps):
    if not (0.0 <= lag < 1.0):
        return 0.0
    return amp(t, eps) * amp(t + lag, eps) * (2.0 / math.pi) * math.asin(1.0 - lag)

def numerical_sigma(eps, steps=12000):
    assert steps % 2 == 0
    def f(u):
        return (1.0 + 0.5 * eps * eps * math.cos(2 * math.pi * u)) * math.asin(1.0 - u)
    h = 1.0 / steps
    s = f(0.0) + f(1.0)
    for j in range(1, steps):
        s += (4 if j % 2 else 2) * f(j * h)
    integral = s * h / 3
    return 1.0 + 0.5 * eps * eps + (4.0 / math.pi) * integral

def conditional_variance(eps, arrivals):
    # Exact variance of the partial sum given the sampled times, for the
    # explicitly Gaussian-sign-driven example (not a sampled-data variance).
    v = 0.0
    left = 0
    for i, ti in enumerate(arrivals):
        ai = amp(ti, eps)
        v += ai * ai
        while ti - arrivals[left] >= 1.0:
            left += 1
        for j in range(left, i):
            v += 2 * covlag(arrivals[j], ti - arrivals[j], eps)
    return v

def main():
    rg = random.Random(SEED)
    ts, t = [], 0.0
    for _ in range(SAMPLE_N):
        t += rg.expovariate(1.0)
        ts.append(t)
    # Unmodulated case has a closed-form answer.
    val0 = numerical_sigma(0.0)
    assert abs(val0 - (3.0 - 4.0 / math.pi)) < 1e-6, (val0, 3.0-4.0/math.pi)
    for eps in (0.0, 0.5):
        expected = numerical_sigma(eps)
        observed = conditional_variance(eps, ts) / SAMPLE_N
        assert abs(observed - expected) < 0.06, (eps, observed, expected)
        print(f'eps={eps:.1f} conditional_variance_per_sample={observed:.8f} sigma_squared={expected:.8f} difference={observed-expected:.8f}')
    # Verify mean-covariance formula analytically at deterministic test offsets.
    for u in (0.0, 0.2, 0.5, 0.8, 1.0, 1.5):
        for eps in (0.0, 0.5):
            m = sum(covlag(j/3000, u, eps) for j in range(3000)) / 3000
            formula = (1+0.5*eps*eps*math.cos(2*math.pi*u)) * (2.0/math.pi) * math.asin(max(0.0, 1.0-u))
            assert abs(m-formula) < 1e-12, (u,eps,m,formula)
    print('Finite reproducibility checks: PASS (sign-covariance means, conditional variances, exact eps=0 integral).')
if __name__ == '__main__':
    main()
