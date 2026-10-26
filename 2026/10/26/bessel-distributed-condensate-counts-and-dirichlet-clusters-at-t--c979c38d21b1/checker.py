"""Finite canonical partition checks for a fast-rate zero-range process.
All coefficient convolutions use exact integers, followed by stable log sums.
Requires Python 3 and no third-party dependencies.
"""
from math import exp, fsum, lgamma, log


def logsumexp(values):
    if not values:
        return float('-inf')
    maximum = max(values)
    return maximum + log(fsum(exp(v - maximum) for v in values))


def bulk_coefficients(L, weights):
    arrays = [[1]]
    for _ in range(L):
        prev = arrays[-1]
        row = [0] * (len(prev) + len(weights) - 1)
        for i, val in enumerate(prev):
            for j, weight in enumerate(weights):
                row[i + j] += val * weight
        arrays.append(row)
    return arrays


def finite_law(L, weights, N, theta):
    A = len(weights)
    bulk = bulk_coefficients(L, weights)
    log_z = []
    for k in range(0, min(L, N // A) + 1):
        if k == 0:
            h = bulk[L][N] if N < len(bulk[L]) else 0
            log_z.append(log(h) if h else float('-inf'))
            continue
        terms = []
        for s, h in enumerate(bulk[L - k]):
            excess = N - A * k - s
            if excess >= 0 and h:
                terms.append(log(h) + lgamma(excess + k) - lgamma(k) - lgamma(excess + 1))
        if not terms:
            log_z.append(float('-inf'))
        else:
            log_z.append(lgamma(L + 1) - lgamma(k + 1) - lgamma(L - k + 1)
                         - k * log(theta) + logsumexp(terms))
    total = logsumexp(log_z)
    return [exp(v - total) for v in log_z]


def brute_law(L, weights, N, theta):
    A = len(weights)
    contributions = [0.0] * (min(L, N // A) + 1)
    def visit(remaining_sites, remaining_mass, clusters, product):
        if remaining_sites == 0:
            if remaining_mass == 0:
                contributions[clusters] += product
            return
        for n in range(remaining_mass + 1):
            weight = weights[n] if n < A else 1 / theta
            visit(remaining_sites - 1, remaining_mass - n,
                  clusters + (n >= A), product * weight)
    visit(L, N, 0, 1.0)
    norm = fsum(contributions)
    return [x / norm for x in contributions]


def limiting_law(b, terms=300):
    # Factorial recurrence avoids overflow and makes the tail negligible.
    vals = [1.0]
    for k in range(2, terms + 1):
        vals.append(vals[-1] * b / (k * (k - 1)))
    norm = fsum(vals)
    return [0.0] + [x / norm for x in vals]


def report(weights, rho, Theta):
    A = len(weights)
    z = sum(weights)
    mu = sum(i * weight for i, weight in enumerate(weights)) / z
    assert rho > mu
    b = (rho - mu) / (Theta * z)
    limiting = limiting_law(b)
    print(f'weights={weights}, rho={rho}, Theta={Theta}, b={b:.12g}')
    print('Limiting P(K=1..4)', *[f'{limiting[k]:.9f}' for k in range(1, 5)])
    errors = []
    for L in (40, 80, 160):
        N = round(rho * L)
        assert abs(N - rho * L) < 1e-9
        law = finite_law(L, weights, N, Theta * L * L)
        error = (fsum(abs(law[k] - limiting[k]) for k in range(len(law)))
                 + fsum(limiting[len(law):]))
        errors.append(error)
        print(f'  L={L:3d}, P(K=1..4)', *[f'{law[k]:.9f}' for k in range(1, 5)],
              f' l1_error={error:.7f}')
    assert errors[0] > errors[1] > errors[2] and errors[2] < 0.03


if __name__ == '__main__':
    for example in ((4, (1, 1), 4, 8.0), (5, (1, 1, 1), 10, 12.5),
                    (4, (1, 2, 3), 8, 8.0)):
        L, weights, N, theta = example
        direct = brute_law(L, weights, N, theta)
        formula = finite_law(L, weights, N, theta)
        assert len(direct) == len(formula)
        assert max(abs(x - y) for x, y in zip(direct, formula)) < 1e-11
    print('Three independent finite-state enumeration identities passed.')
    report((1, 1), 1, 0.5)
    report((1, 1, 1), 2, 0.5)
    report((1, 2, 3), 2, 0.5)
    print('Finite canonical and asymptotic checks passed.')
