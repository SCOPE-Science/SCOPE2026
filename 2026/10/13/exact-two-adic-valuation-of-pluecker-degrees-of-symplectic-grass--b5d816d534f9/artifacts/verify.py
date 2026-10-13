from math import factorial, comb

def v2(n):
    assert n > 0
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c

def s2(n):
    return n.bit_count()

def dim_ig(n, k):
    return k * (4*n - 3*k + 1) // 2

def degree_factorial(n, k):
    d = dim_ig(n, k)
    num = (2 ** (k*(k-1)//2)) * factorial(d)
    for i in range(k):
        num *= factorial(i)
    den = 1
    for i in range(1, k+1):
        den *= factorial(2*n - 2*i + 1)
    assert num % den == 0
    return num // den

def degree_root_product(n, k):
    d = dim_ig(n, k)
    num = factorial(d)
    den = 1

    # e_i - e_j with i <= k < j.
    for i in range(1, k+1):
        for j in range(k+1, n+1):
            den *= (j - i)

    # e_i + e_j with i <= k.
    for i in range(1, k+1):
        for j in range(i+1, n+1):
            if j <= k:
                num *= 2
            den *= (2*n - i - j + 2)

    # long roots 2e_i with i <= k.
    for i in range(1, k+1):
        den *= (n - i + 1)

    assert num % den == 0
    return num // den

def valuation_formula(n, k):
    d = dim_ig(n, k)
    return (
        k*(k+1)//2
        - s2(d)
        + sum(s2(j) for j in range(n-k, n))
        - sum(s2(j) for j in range(1, k))
    )

pairs = 0
for n in range(1, 61):
    for k in range(1, n+1):
        a = degree_root_product(n, k)
        b = degree_factorial(n, k)
        assert a == b, (n, k, a, b)
        assert v2(a) == valuation_formula(n, k), (n, k)
        pairs += 1

def catalan(r):
    return comb(2*r, r) // (r+1)

for n in range(2, 501):
    assert degree_factorial(n, 2) == catalan(2*n-2)
    assert valuation_formula(n, 2) == s2(n-1)

for n in range(1, 201):
    M = n*(n+1)//2
    assert valuation_formula(n, n) == M - s2(M)

assert degree_factorial(4, 3) == 2112
assert valuation_formula(4, 3) == 6

print("VERIFY_OK", pairs, 499, 200)
