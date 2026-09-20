from itertools import product
from math import isclose, log2


def vecs(q, n):
    return list(product(range(q), repeat=n))


def mat_vec(H, x, q):
    return tuple(sum(row[j] * x[j] for j in range(len(x))) % q for row in H)


def rank_mod_q(rows, q):
    A = [list(r) for r in rows]
    if not A:
        return 0
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if A[i][c] % q), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][c] % q, -1, q)
        A[r] = [(v * inv) % q for v in A[r]]
        for i in range(m):
            if i != r and A[i][c] % q:
                f = A[i][c] % q
                A[i] = [(A[i][j] - f * A[r][j]) % q for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def all_matrices(q, m, n, full_rank=False):
    rows = vecs(q, n)
    for choice in product(rows, repeat=m):
        H = tuple(choice)
        if (not full_rank) or rank_mod_q(H, q) == m:
            yield H


def check_case(q, n, m, probs, rhos):
    xs = vecs(q, n)
    order = sorted(range(len(xs)), key=lambda i: (-probs[i], xs[i]))
    pos = {idx: j + 1 for j, idx in enumerate(order)}
    g0 = [pos[i] for i in range(len(xs))]

    def ensemble(full_rank):
        Hs = list(all_matrices(q, m, n, full_rank=full_rank))
        vals = {rho: 0.0 for rho in rhos}
        means = 0.0
        for H in Hs:
            synd = [mat_vec(H, x, q) for x in xs]
            for i, x in enumerate(xs):
                earlier = 0
                for j in order:
                    if j == i:
                        break
                    if synd[j] == synd[i]:
                        earlier += 1
                gh = 1 + earlier
                means += probs[i] * gh / len(Hs)
                for rho in rhos:
                    vals[rho] += probs[i] * (gh ** rho) / len(Hs)
        return len(Hs), means, vals

    nH, meanH, momentsH = ensemble(False)
    eg0 = sum(probs[i] * g0[i] for i in range(len(xs)))
    exact_mean = 1 + (q ** (-m)) * (eg0 - 1)
    assert isclose(meanH, exact_mean, rel_tol=1e-11, abs_tol=1e-11)

    # Binary exact second moment identity from pairwise independence.
    if q == 2 and 2.0 in rhos:
        M1 = sum(probs[i] * (g0[i] - 1) for i in range(len(xs)))
        M2fac = sum(probs[i] * (g0[i] - 1) * (g0[i] - 2) for i in range(len(xs)))
        lam = 2 ** (-m)
        exact2 = 1 + 3 * lam * M1 + (lam ** 2) * M2fac
        assert isclose(momentsH[2.0], exact2, rel_tol=1e-11, abs_tol=1e-11)

    full_info = None
    if m <= n:
        nF, meanF, momentsF = ensemble(True)
        if nF:
            k = n - m
            collision = 0.0 if k == 0 else (q ** k - 1) / (q ** n - 1)
            exact_full_mean = 1 + collision * (eg0 - 1)
            assert isclose(meanF, exact_full_mean, rel_tol=1e-11, abs_tol=1e-11)
            full_info = (nF, meanF, momentsF)

    ratios = {}
    lam = q ** (-m)
    for rho in rhos:
        proxy = sum(probs[i] * ((1 + lam * (g0[i] - 1)) ** rho) for i in range(len(xs)))
        ratios[rho] = momentsH[rho] / proxy
        assert ratios[rho] > 0
    return nH, meanH, exact_mean, ratios, full_info


def bernoulli_probs(q, n, p0):
    assert q == 2
    xs = vecs(q, n)
    return [(p0 ** sum(x)) * ((1-p0) ** (n-sum(x))) for x in xs]


def arbitrary_probs(q, n):
    xs = vecs(q, n)
    raw = [1 + ((7*i + 3) % 11) for i in range(len(xs))]
    s = sum(raw)
    return [r/s for r in raw]


if __name__ == '__main__':
    checks = []
    checks.append((2, 3, 1, bernoulli_probs(2, 3, 0.17)))
    checks.append((2, 4, 2, arbitrary_probs(2, 4)))
    checks.append((3, 2, 1, arbitrary_probs(3, 2)))
    rhos = [0.5, 1.0, 1.7, 2.0, 3.0]
    for q, n, m, probs in checks:
        nH, meanH, exact, ratios, full = check_case(q, n, m, probs, rhos)
        print(f'q={q} n={n} m={m} matrices={nH} mean={meanH:.12f} exact={exact:.12f}')
        print('  moment/proxy ratios:', ' '.join(f'rho={r:g}:{ratios[r]:.6f}' for r in rhos))
        if full is not None:
            print(f'  full-rank matrices={full[0]} full-rank mean={full[1]:.12f}')
    print('PASS')
