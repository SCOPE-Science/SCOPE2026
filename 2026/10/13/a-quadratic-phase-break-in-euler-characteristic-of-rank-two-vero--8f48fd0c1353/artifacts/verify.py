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

def cat2_rank_monomial(alpha):
    m = len(alpha)
    count = 0
    for i in range(m):
        if alpha[i] >= 2:
            count += 1
        for j in range(i+1, m):
            if alpha[i] >= 1 and alpha[j] >= 1:
                count += 1
    return count

format_checks = monomial_checks = excluded_checks = 0
for n in range(1, 8):
    m = n + 1
    for d in range(2, 11):
        kept = 0
        total = 0
        for alpha in compositions(d, m):
            total += 1
            support = sum(a > 0 for a in alpha)
            cat1 = support
            cat2 = cat2_rank_monomial(alpha)

            if d == 2:
                in_fixed_secant = True
            else:
                pure = max(alpha) == d
                tangent = support == 2 and max(alpha) == d-1 and min(a for a in alpha if a > 0) == 1
                in_fixed_secant = pure or tangent
                if not in_fixed_secant:
                    assert cat1 >= 3 or cat2 >= 3, (n, d, alpha, cat1, cat2)
                    excluded_checks += 1

            if in_fixed_secant:
                kept += 1
            monomial_checks += 1

        assert total == comb(n+d, n)
        expected = comb(n+2, 2) if d == 2 else (n+1)**2
        assert kept == expected, (n, d, kept, expected)
        exact = kept - (n+1)
        expected_exact = n*(n+1)//2 if d == 2 else n*(n+1)
        assert exact == expected_exact
        format_checks += 1

print('VERIFY_OK', format_checks, monomial_checks, excluded_checks)
