from math import factorial, comb

def degree(q, c):
    num = factorial(q * c)
    for i in range(1, q):
        num *= factorial(i)
    den = 1
    for j in range(c, c + q):
        den *= factorial(j)
    assert num % den == 0
    return num // den

def euler(q, c):
    return comb(q + c, q)

checks = 0
exceptions = set()

for n in range(4, 101):
    for k in range(2, n - 1):
        q = min(k, n - k)
        c = max(k, n - k)
        D = degree(q, c)
        E = euler(q, c)
        assert D != E
        expected_low = q == 2 and n in (4, 5, 6)
        assert (D < E) == expected_low, (n, k, D, E)
        if D < E:
            exceptions.add((q, n))
        checks += 1

assert exceptions == {(2, 4), (2, 5), (2, 6)}

# Verify the exact growth-ratio inequalities used in the proof.
ratio_checks = 0
for c in range(5, 100):
    lhs_num = degree(2, c + 1) * euler(2, c)
    rhs_num = degree(2, c) * euler(2, c + 1)
    assert lhs_num > rhs_num
    ratio_checks += 1

for q in range(3, 50):
    # Square endpoint.
    assert degree(q, q) > euler(q, q)
    for c in range(q, 100):
        lhs_num = degree(q, c + 1) * euler(q, c)
        rhs_num = degree(q, c) * euler(q, c + 1)
        assert lhs_num > rhs_num
        ratio_checks += 1

print("VERIFY_OK", checks, ratio_checks, sorted(exceptions))
