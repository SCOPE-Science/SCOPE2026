from math import factorial

def v2(n):
    assert n > 0
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c

def s2(n):
    return n.bit_count()

def complex_degree(a, b):
    assert a >= b >= 2
    num = factorial(a * b)
    for j in range(1, b):
        num *= factorial(j)
    den = 1
    for j in range(b):
        den *= factorial(a + j)
    assert num % den == 0
    return num // den

def real_degree(a, b):
    assert a >= b >= 2 and (a + b) % 2 == 1
    num = factorial(a * b // 2)
    for j in range(1, b):
        num *= factorial(j)
    for r in range(1, b):
        num *= factorial(a - r)

    den = 1
    for q in range(a - b + 2, a + b - 1, 2):
        den *= factorial(q)
    for t in range((a - b + 1)//2, (a + b - 1)//2 + 1):
        den *= factorial(t)

    assert num % den == 0, (a, b)
    return num // den

pairs = 0
for a in range(2, 121):
    for b in range(2, a + 1):
        if (a + b) % 2 == 0:
            continue
        dc = complex_degree(a, b)
        dr = real_degree(a, b)
        digit = (
            sum(s2(a + j) for j in range(b))
            - sum(s2(j) for j in range(1, b))
            - s2(a * b)
        )
        assert v2(dc) == v2(dr), (a, b, v2(dc), v2(dr))
        assert v2(dc) == digit, (a, b, v2(dc), digit)
        pairs += 1

def catalan(n):
    from math import comb
    return comb(2*n, n) // (n + 1)

cat = 0
for a in range(3, 400, 2):
    assert complex_degree(a, 2) == catalan(a)
    assert real_degree(a, 2) == catalan((a - 1)//2)
    assert v2(catalan(a)) == v2(catalan((a - 1)//2))
    cat += 1

print("VERIFY_OK", pairs, cat)
