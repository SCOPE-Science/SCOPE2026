"""Direct finite-state and asymptotic checks for a slow-site zero-range gas.

Standard library only. Run: python3 verify_stationary.py
"""
from fractions import Fraction as F
from itertools import product
from math import ceil, comb, erf, exp, gamma, lgamma, log, pi, sqrt


def compositions(n, k):
    if k == 1:
        yield (n,)
        return
    for j in range(n + 1):
        for tail in compositions(n - j, k - 1):
            yield (j,) + tail


def exact_stationary_linear(N, weights):
    L = len(weights)
    states = list(compositions(N, L))
    pos = {s: j for j, s in enumerate(states)}
    d = len(states)
    mat = [[F(0) for _ in range(d + 1)] for _ in range(d)]
    for j, state in enumerate(states):
        for i in range(L):
            if not state[i]:
                continue
            rate = F(1, L - 1) / weights[i]
            for target in range(L):
                if target == i:
                    continue
                nxt = list(state)
                nxt[i] -= 1
                nxt[target] += 1
                p = pos[tuple(nxt)]
                mat[p][j] += rate
                mat[j][j] -= rate
    mat[-1][:d] = [F(1)] * d
    mat[-1][-1] = F(1)
    # Solve the stationary generator without using the product-form equations.
    for c in range(d):
        pivot = next(row for row in range(c, d) if mat[row][c])
        mat[c], mat[pivot] = mat[pivot], mat[c]
        a = mat[c][c]
        for q in range(c, d + 1):
            mat[c][q] /= a
        for row in range(d):
            if row != c and mat[row][c]:
                a = mat[row][c]
                for q in range(c, d + 1):
                    mat[row][q] -= a * mat[c][q]
    actual = [mat[j][-1] for j in range(d)]
    unnorm = []
    for s in states:
        p = F(1)
        for i, n in enumerate(s):
            p *= weights[i] ** n
        unnorm.append(p)
    Z = sum(unnorm)
    expected = [p / Z for p in unnorm]
    assert actual == expected
    return len(states)


def exact_hub_marginal(N, weights, M):
    r = len(weights) - M
    for s in range(N + 1):
        mass = F(0)
        for h in compositions(s, r):
            p = F(comb(N - s + M - 1, M - 1))
            for k, n in enumerate(h):
                p *= weights[k] ** n
            mass += p
        brute = F(0)
        for state in compositions(N, len(weights)):
            if sum(state[:r]) != s:
                continue
            p = F(1)
            for k, n in enumerate(state):
                p *= weights[k] ** n
            brute += p
        assert mass == brute
    return N + 1


def finite_mass_mean(M, r, a=2.0, delta=0.0, c=0.0):
    mu = 1 / (a - 1)
    N = int(mu * M + delta * sqrt(M))
    logs = []
    hub_sums = []
    hub_x = []
    cur_sum = 0.0
    cur_x = 0.0
    for s in range(N + 1):
        ell = N - s
        # Negative-binomial probability, up to an s-independent factor.
        logp = (lgamma(ell + M) - lgamma(ell + 1)
                - lgamma(M) - ell * log(a))
        if r == 1:
            hs = exp(c * s / sqrt(M))
            hx = s * hs
        elif r == 2:
            term = exp(c * s / sqrt(M))
            cur_sum += term
            cur_x += s * term
            hs, hx = cur_sum, cur_x
        else:
            assert c == 0.0
            hs = comb(s + r - 1, r - 1)
            hx = hs * s / r
        logs.append(logp + log(hs))
        hub_sums.append(s)
        hub_x.append(hx / hs)
    shift = max(logs)
    probs = [exp(z - shift) for z in logs]
    Z = sum(probs)
    return (sum(p * s for p, s in zip(probs, hub_sums)) / Z / sqrt(M),
            sum(p * x for p, x in zip(probs, hub_x)) / Z / sqrt(M))


def simpson(fn, hi=18.0, panels=16000):
    assert panels % 2 == 0
    step = hi / panels
    acc = fn(0.0) + fn(hi)
    for i in range(1, panels):
        acc += (4 if i & 1 else 2) * fn(i * step)
    return acc * step / 3


def continuum_biased_means(c=1.0, sigma=sqrt(2)):
    # Integrate in total mass t=x+y, then integrate over 0<=x<=t.
    def row(t):
        return exp(-t * t / (2 * sigma * sigma))
    def H(t):
        return (exp(c * t) - 1.0) / c
    def HX(t):
        return (exp(c * t) * (c * t - 1) + 1) / (c * c)
    Z = simpson(lambda t: row(t) * H(t))
    return (simpson(lambda t: t * row(t) * H(t)) / Z,
            simpson(lambda t: row(t) * HX(t)) / Z)


def main():
    exact_states = 0
    marginal_cases = 0
    for M, ws, N in [
        (1, [F(2), F(5, 2), F(1)], 3),
        (2, [F(2), F(5, 2), F(1), F(1)], 3),
        (2, [F(2), F(3), F(5, 2), F(1), F(1)], 2),
        (2, [F(2), F(2), F(1), F(1)], 4),
    ]:
        exact_states += exact_stationary_linear(N, ws)
        marginal_cases += exact_hub_marginal(N, ws, M)
    print(f"exact stationary states checked={exact_states}; exact marginal identities={marginal_cases}")
    assert exact_states == 10 + 20 + 15 + 35
    assert marginal_cases == 4 + 4 + 3 + 5
    # Central critical chi_r predictions, with sigma=sqrt(2).
    for r in (1, 2, 3):
        expected = sqrt(2) * sqrt(2) * gamma((r + 1) / 2) / gamma(r / 2)
        means = [finite_mass_mean(M, r)[0] for M in (100, 400, 1600, 6400)]
        print(f"critical r={r}: limiting mean={expected:.9f}, finite={means}")
        assert abs(means[-1] - expected) < 0.09
        assert abs(means[-1] - expected) < abs(means[0] - expected)
    limiting = continuum_biased_means(1.0)
    means = [finite_mass_mean(M, 2, c=1.0) for M in (100, 400, 1600, 6400)]
    print("critical two-hub weak bias limiting (total, first) =", limiting)
    print("finite weak bias (total, first) =", means)
    for col in (0, 1):
        assert abs(means[-1][col] - limiting[col]) < 0.10
        assert abs(means[-1][col] - limiting[col]) < abs(means[0][col] - limiting[col])
    print("PASS: exact generator solutions, combinatorial marginals, chi and weak-bias scaling checks")


if __name__ == "__main__":
    main()
