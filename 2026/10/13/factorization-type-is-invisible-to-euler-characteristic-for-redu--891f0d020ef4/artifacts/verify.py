from itertools import combinations
from math import comb

def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for bars in combinations(range(total + length - 1), length - 1):
        prev = -1
        out = []
        for b in bars + (total + length - 1,):
            out.append(b - prev - 1)
            prev = b
        yield tuple(out)

def partitions(n, max_part=None):
    if max_part is None or max_part > n:
        max_part = n
    if n == 0:
        yield ()
        return
    for first in range(max_part, 0, -1):
        for tail in partitions(n-first, first):
            yield (first,) + tail

def factor_exponent(alpha, degrees):
    # Expand alpha into a list of variable indices, then cut into blocks.
    tokens = []
    for j, a in enumerate(alpha):
        tokens.extend([j] * a)
    assert len(tokens) == sum(degrees)

    factors = []
    pos = 0
    m = len(alpha)
    for deg in degrees:
        beta = [0] * m
        for j in tokens[pos:pos+deg]:
            beta[j] += 1
        pos += deg
        factors.append(tuple(beta))
    return factors

format_checks = monomial_checks = factorization_checks = 0

for m in range(2, 6):
    for d in range(2, 9):
        B = d + 1
        alphas = list(compositions(d, m))
        assert len(alphas) == comb(d+m-1, m-1)

        weights = [sum(a * (B ** j) for j, a in enumerate(alpha)) for alpha in alphas]
        assert len(set(weights)) == len(weights)

        lambdas = [lam for lam in partitions(d) if len(lam) >= 2]
        for alpha in alphas:
            monomial_checks += 1
            for lam in lambdas:
                factors = factor_exponent(alpha, lam)
                assert [sum(beta) for beta in factors] == list(lam)
                recovered = tuple(sum(beta[j] for beta in factors) for j in range(m))
                assert recovered == alpha
                factorization_checks += 1

        format_checks += 1

print("VERIFY_OK", format_checks, monomial_checks, factorization_checks)
