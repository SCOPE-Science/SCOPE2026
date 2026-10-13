from math import comb

def exponent_vectors(total, length):
    if length == 1:
        yield (total,)
        return
    for a in range(total + 1):
        for tail in exponent_vectors(total-a, length-1):
            yield (a,) + tail

format_checks = cumulative_checks = exact_checks = monomial_checks = 0
for m in range(2, 10):
    for d in range(3, 10):
        hist = [0] * (m + 1)
        for alpha in exponent_vectors(d, m):
            s = sum(1 for a in alpha if a > 0)
            assert 1 <= s <= min(m, d)
            hist[s] += 1
            monomial_checks += 1

        assert sum(hist) == comb(m+d-1, d)
        for s in range(1, m+1):
            expected_exact = comb(m, s) * comb(d-1, s-1) if s <= d else 0
            assert hist[s] == expected_exact, (m, d, s, hist[s], expected_exact)
            exact_checks += 1

        running = 0
        for r in range(1, m+1):
            running += hist[r]
            expected = sum(comb(m,s)*comb(d-1,s-1) for s in range(1, min(r,d)+1))
            assert running == expected, (m, d, r, running, expected)
            cumulative_checks += 1

        assert sum(comb(m,s)*comb(d-1,s-1) for s in range(1,min(m,d)+1)) == comb(m+d-1,d)
        format_checks += 1

print('VERIFY_OK', format_checks, cumulative_checks, exact_checks, monomial_checks)
