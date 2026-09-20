import math


def log_choose(n, k):
    if k < 0 or k > n:
        return float('-inf')
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def log_hypergeom_pmf(N, K, m, h):
    return log_choose(K, h) + log_choose(N - K, m - h) - log_choose(N, m)


def freidling_ratio_squared(n, n1):
    n0 = n - n1
    m, M = sorted((n0, n1))
    Hn = sum(1.0 / j for j in range(1, n + 1))
    eps = (Hn - 1.0) / (n - Hn)
    return 4.0 * m * (M + 1.0) / ((1.0 + eps) * n * n)


def cre_binary_constant(n, p, exponent=0.2):
    n1 = int(round(n * p))
    n0 = n - n1
    p = n1 / n
    K = n // 2
    t = n ** (-exponent)
    delta = (1.0 - p) * t
    h = int(round(n1 * (0.5 + delta)))
    lp = log_hypergeom_pmf(n, K, n1, h)
    return p, t, -lp / (n * t * t), 2.0 * p * (1.0 - p)


def stratified_binary_constant(n, weights, props, exponent=0.2):
    raw = [int(round(n * w)) for w in weights]
    raw[-1] += n - sum(raw)
    Ns = []
    for N in raw[:-1]:
        Ns.append(max(2, (N // 20) * 20))
    Ns.append(max(2, (n - sum(Ns)) // 20 * 20))
    n_eff = sum(Ns)
    t = n_eff ** (-exponent)
    ps = []
    for N, p in zip(Ns, props):
        m = int(round(N * p))
        ps.append(m / N)
    Gamma = sum((N / n_eff) / (p * (1.0 - p)) for N, p in zip(Ns, ps))
    target = 2.0 / Gamma
    lp = 0.0
    attained = 0.0
    for N, p in zip(Ns, ps):
        m = int(round(N * p))
        e = t / (Gamma * p * (1.0 - p))
        delta = (1.0 - p) * e
        h = int(round(m * (0.5 + delta)))
        lp += log_hypergeom_pmf(N, N // 2, m, h)
        realized_e = (h / m - 0.5) / (1.0 - p)
        attained += (N / n_eff) * realized_e
    return n_eff, t, -lp / (n_eff * t * t), target, attained / t


def main():
    print('Finite comparison with the Hoeffding interval of Freidling (2026)')
    max_ratio = 0.0
    argmax = None
    for n in range(2, 501):
        for n1 in range(1, n):
            r2 = freidling_ratio_squared(n, n1)
            if r2 > max_ratio:
                max_ratio = r2
                argmax = (n, n1)
    print(f'max squared half-width ratio for n<=500: {max_ratio:.12f} at {argmax}')
    print()

    print('Complete-randomization binary sharp-null point-mass check, p=0.3')
    for n in (10_000, 100_000, 1_000_000, 5_000_000):
        p, t, value, target = cre_binary_constant(n, 0.3)
        print(f'n={n:7d} p={p:.6f} t={t:.9f} normalized={value:.12f} target={target:.12f}')
    print()

    print('Stratified binary sharp-null point-mass check')
    weights = (0.4, 0.6)
    props = (0.25, 0.60)
    Gamma = sum(w / (p * (1.0 - p)) for w, p in zip(weights, props))
    print(f'limiting Gamma={Gamma:.12f} target 2/Gamma={2.0/Gamma:.12f}')
    for n in (20_000, 100_000, 500_000, 2_000_000):
        n_eff, t, value, target, attained = stratified_binary_constant(n, weights, props)
        print(
            f'n={n_eff:7d} t={t:.9f} normalized={value:.12f} '
            f'target={target:.12f} attained/t={attained:.12f}'
        )


if __name__ == '__main__':
    main()
