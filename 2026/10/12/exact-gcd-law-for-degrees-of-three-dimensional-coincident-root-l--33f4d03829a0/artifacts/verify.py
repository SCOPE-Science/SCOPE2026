from collections import Counter
from math import factorial, gcd

def partitions3(d):
    for a in range(1, d // 3 + 1):
        for b in range(a, (d - a) // 2 + 1):
            c = d - a - b
            if b <= c:
                yield (a, b, c)

def degree(lam):
    mult = Counter(lam)
    num = factorial(3)
    den = 1
    prod = 1
    for part, count in mult.items():
        den *= factorial(count)
        prod *= part ** count
    assert num % den == 0
    return (num // den) * prod

def v3(n):
    e = 0
    while n % 3 == 0:
        n //= 3
        e += 1
    return e

def closed_gcd(d):
    if d % 2:
        alpha = 0
    elif d % 4 == 0:
        alpha = 1
    else:
        alpha = 2
    beta = 0 if v3(d) == 1 else 1
    return (2 ** alpha) * (3 ** beta)

total_partitions = 0
for d in range(3, 501):
    g = 0
    count = 0
    for lam in partitions3(d):
        g = gcd(g, degree(lam))
        count += 1
    assert count > 0
    assert g == closed_gcd(d), (d, g, closed_gcd(d))
    total_partitions += count

# Explicit proof witnesses and low-degree boundary checks.
assert degree((1,1,1)) == 1
assert degree((1,1,2)) == 6
assert degree((1,2,2)) == 12
for d in range(6, 501):
    assert degree((1,1,d-2)) == 3 * (d-2)
    assert degree((1,2,d-3)) == 12 * (d-3)

print("VERIFY_OK", 498, total_partitions)
