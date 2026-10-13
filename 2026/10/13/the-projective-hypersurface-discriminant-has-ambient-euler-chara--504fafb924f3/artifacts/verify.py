from itertools import combinations

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

def smooth_monomial_hypersurface(alpha):
    n = len(alpha)
    d = sum(alpha)
    support = [a for a in alpha if a > 0]
    if len(support) == 1:
        return False
    if n >= 3:
        return False
    # n = 2: a divisor on P^1 is smooth iff it is reduced.
    return d == 2 and sorted(support) == [1, 1]

format_checks = monomial_checks = weight_checks = 0
smooth_cases = []

for n in range(2, 9):
    for d in range(2, 11):
        B = d + 1
        alphas = list(compositions(d, n))
        weights = [sum(a * (B ** i) for i, a in enumerate(alpha)) for alpha in alphas]
        assert len(set(weights)) == len(weights)
        weight_checks += len(weights)

        for alpha in alphas:
            monomial_checks += 1
            if smooth_monomial_hypersurface(alpha):
                smooth_cases.append((n, d, alpha))

        expected_N = 1
        for j in range(1, n):
            expected_N = expected_N * (d + j) // j
        assert len(alphas) == expected_N
        format_checks += 1

assert smooth_cases == [(2, 2, (1, 1))]
print("VERIFY_OK", format_checks, monomial_checks, weight_checks, len(smooth_cases))
