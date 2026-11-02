"""Reproducible mathematical diagnostics for periodic nearest-site reset diffusion.

Run: python checker.py
Requires numpy; deterministic inputs and a fixed local random seed.
Finite checks supplement, rather than replace, the analytic proof.
"""
import math
import numpy as np


def formula(gaps, diffusion, reset_rate):
    gaps = np.asarray(gaps, dtype=float)
    q = math.sqrt(reset_rate / diffusion)
    a = q * gaps / 2
    s = np.sum(np.sinh(a))
    t = np.sum(np.tanh(a))
    return reset_rate * gaps.sum() ** 2 / (4 * s * t)


def weight(gaps, diffusion, reset_rate):
    gaps = np.asarray(gaps, dtype=float)
    a = gaps * math.sqrt(reset_rate / diffusion) / 2
    t = np.tanh(a)
    return (t + np.roll(t, 1)) / (2 * np.sum(t))


def reset_chain(gaps, diffusion, reset_rate, periods=60):
    """Independent tilted-Poisson-chain spectral-derivative calculation.

    At each reset, the free Brownian displacement has Laplace density
    q*exp(-q*abs(y))/2. Integrate over the nearest-site Voronoi cells.
    Track spatial winding in the first two displacement matrices.
    """
    g = np.array(gaps, float)
    n = len(g)
    L = sum(g)
    q = math.sqrt(reset_rate / diffusion)
    x = np.r_[0, np.cumsum(g[:-1])]
    left = x - np.roll(g, 1) / 2
    right = x + g / 2
    P, M1, M2 = (np.zeros((n, n)) for _ in range(3))

    def cdf(t):
        return 0.5 * math.exp(q * t) if t < 0 else 1 - 0.5 * math.exp(-q * t)

    for i in range(n):
        for j in range(n):
            for m in range(-periods, periods+1):
                lo = left[j] + m * L - x[i]
                hi = right[j] + m * L - x[i]
                if hi < -32/q or lo > 32/q:
                    continue
                prob = max(0.0, cdf(hi) - cdf(lo))
                disp = x[j] + m * L - x[i]
                P[i, j] += prob
                M1[i, j] += disp * prob
                M2[i, j] += disp * disp * prob
    G = reset_rate * (P - np.eye(n))
    A = G.T.copy()
    A[-1, :] = 1.0
    rhs = np.zeros(n)
    rhs[-1] = 1.0
    pi = np.linalg.solve(A, rhs)
    local_velocity = reset_rate * M1.sum(axis=1)
    velocity = pi @ local_velocity
    # Eigenvalue perturbation: G h = velocity*1 - G'(0)*1,
    # and lambda''/2 = pi (G''*1+2G' h)/2.
    B = G.copy()
    B[-1, :] = pi
    b = velocity - local_velocity
    b[-1] = 0.0
    h = np.linalg.solve(B, b)
    d_eff = 0.5 * (pi @ (reset_rate * M2.sum(axis=1)
                            + 2 * reset_rate * (M1 @ h)))
    return velocity, d_eff, pi, P


def main():
    checks = 0
    profiles = [
        ([0.2, 0.3, 0.5], 1.0, 9.0),
        ([0.1, 0.2, 0.3, 0.4], 1.0, 64.0),
        ([0.3, 0.7], 1.0, 16.0),
        ([0.1, 0.1, 0.8], 1.0, 36.0),
        ([0.2] * 5, 1.0, 9.0),
        ([0.03, 0.05, 0.22, 0.3, 0.4], 1.0, 169.0),
    ]
    for gaps, D, r in profiles:
        v, computed, pi, P = reset_chain(gaps, D, r)
        predicted = formula(gaps, D, r)
        assert abs(v) < 5e-10, (gaps, v)
        checks += 1
        assert abs(computed - predicted) < 2e-8, (gaps, computed, predicted)
        checks += 1
        assert np.max(abs(pi - weight(gaps, D, r))) < 2e-10
        checks += 1
        assert np.max(abs(P.sum(axis=1)-1)) < 2e-10
        checks += 1
    rng = np.random.default_rng(416723)
    for _ in range(100):
        n = int(rng.integers(2, 15))
        gaps = 0.1 + rng.uniform(size=n)
        gaps /= gaps.sum()
        D = 0.1 + float(rng.uniform())
        r = 0.1 + 12 * float(rng.uniform())
        x = math.sqrt(r/D)*gaps/2
        # Cauchy implies universal optimized regular-arrangement ceiling.
        lhs = np.sum(np.sinh(x)) * np.sum(np.tanh(x))
        rhs = np.sum(np.sinh(x) / np.sqrt(np.cosh(x)))**2
        assert lhs + 1e-12 >= rhs
        checks += 1
        pi = weight(gaps, D, r)
        assert all(pi > 0) and abs(sum(pi)-1) < 2e-13
        checks += 1
    # Weak-resetting coefficient and the strict fixed-rate reversal.
    uniform = [0.5, 0.5]
    unequal = [0.3, 0.7]
    for r in [0.0001, 0.0005, 0.001]:
        for g in (uniform, unequal):
            predicted_slope = sum(z**3 for z in g)/(24*sum(g))
            observed_slope = (formula(g, 1.0, r)-1.0)/r
            assert abs(predicted_slope-observed_slope) < 0.0001
            checks += 1
        assert formula(unequal, 1.0, r)>formula(uniform, 1.0, r)
        checks += 1
    # At a higher rate, the ordering can reverse.
    assert formula(unequal, 1.0, 100)<formula(uniform, 1.0, 100)
    checks += 1
    # Largest gap controls high-rate logarithmic decay.
    g = [0.2, 0.3, 0.5]
    r = 2500.0
    deff = formula(g, 1.0, r)
    asympt = r/(2*len(g))*math.exp(-max(g)*math.sqrt(r)/2)
    assert abs(deff/asympt-1)<0.02
    checks += 1
    print(f"PASS: {checks} finite checks. Independent tilted-reset-chain and closed form agree.")
    print("Example unequal gaps [0.2,0.3,0.5], D=1,r=9:",formula([.2,.3,.5],1,9))
    print("Fixed low-rate reversal, r=1:",formula(unequal,1,1),formula(uniform,1,1))
    print("High-rate regular advantage, r=100:",formula(unequal,1,100),formula(uniform,1,100))

if __name__ == '__main__':
    main()
