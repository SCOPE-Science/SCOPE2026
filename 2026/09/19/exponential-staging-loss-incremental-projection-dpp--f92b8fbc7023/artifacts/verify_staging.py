from mpmath import mp

mp.dps = 80


def givens_family(d, eps):
    eps = mp.mpf(eps)
    c = [None] * (d + 1)
    c[1] = 1 / mp.sqrt(2)
    for s in range(2, d + 1):
        c[s] = eps ** (2 ** (s - 2))

    O = mp.eye(d + 1)
    for s in range(1, d + 1):
        cs = c[s]
        ss = mp.sqrt(1 - cs * cs)
        G = mp.eye(d + 1)
        G[s - 1, s - 1] = cs
        G[s - 1, s] = -ss
        G[s, s - 1] = ss
        G[s, s] = cs
        O = O * G
    return O, c


def staged_omission_distribution(d, eps):
    _, c = givens_family(d, eps)
    weights = [1 - c[1] ** 2, c[1] ** 2]
    probs = list(weights)

    for s in range(2, d + 1):
        cs2 = c[s] ** 2
        ss2 = 1 - cs2
        next_weights = [ss2 * w for w in weights] + [cs2]
        next_probs = [mp.mpf('0')] * (s + 1)
        p_new = mp.mpf('0')
        for j, (p, w) in enumerate(zip(probs, weights)):
            u = ss2 * w
            v = cs2
            next_probs[j] += p * u / (u + v)
            p_new += p * v / (u + v)
        next_probs[-1] = p_new
        weights, probs = next_weights, next_probs

    return weights, probs, c


def metrics(d, eps):
    O, c = givens_family(d, eps)
    weights, probs, _ = staged_omission_distribution(d, eps)
    z = O[:, d]
    weight_residual = max(abs(weights[j] - z[j] ** 2) for j in range(d + 1))

    # Fixed, distinct leading singular values make the ordered dominant right
    # singular vectors unique up to signs.
    tau = [mp.mpf(2) - mp.mpf(i + 1) / (4 * d) for i in range(d)]
    sigma2 = c[d] ** 4

    b = []
    for j in range(d + 1):
        b_j = mp.fsum((O[j, i] ** 2) / (tau[i] ** 2) for i in range(d))
        b.append(b_j)

    staged_oblique = mp.fsum(probs[j] / weights[j] for j in range(d + 1))
    staged_orth = mp.fsum(
        probs[j] / (weights[j] + sigma2 * b[j]) for j in range(d + 1)
    )
    oneshot_orth = mp.fsum(
        weights[j] / (weights[j] + sigma2 * b[j]) for j in range(d + 1)
    )

    return {
        'prob_sum': mp.fsum(probs),
        'weight_sum': mp.fsum(weights),
        'weight_residual': weight_residual,
        'staged_oblique': staged_oblique,
        'staged_orth': staged_orth,
        'oneshot_orth': oneshot_orth,
        'target_staged': mp.mpf(2) ** d,
        'target_oneshot': mp.mpf(d + 1),
    }


print('mpmath', mp.__version__ if hasattr(mp, '__version__') else '1.3.0')
print('d eps staged_oblique staged_orth one_shot_orth target_staged target_one_shot')
for d in (2, 3, 4, 5, 6):
    for eps in ('0.1', '0.03'):
        m = metrics(d, eps)
        print(
            d,
            eps,
            mp.nstr(m['staged_oblique'], 16),
            mp.nstr(m['staged_orth'], 16),
            mp.nstr(m['oneshot_orth'], 16),
            int(m['target_staged']),
            int(m['target_oneshot']),
        )
        assert abs(m['prob_sum'] - 1) < mp.mpf('1e-60')
        assert abs(m['weight_sum'] - 1) < mp.mpf('1e-60')
        assert m['weight_residual'] < mp.mpf('1e-60')