"""Direct finite checks of coefficient-height extremizers in imaginary quadratic fields."""
from math import isqrt, gcd


def squarefree(n):
    for p in range(2, isqrt(n) + 1):
        if n % (p * p) == 0:
            return False
    return True


def test_family(m):
    d = 4 * m * (m + 1) - 1
    h = m + 1
    actual = set()
    # Enumerate every positive-definite integer quadratic with H <= h.
    for a in range(1, h + 1):
        for c in range(1, h + 1):
            for t in range(1, isqrt(4 * h * h // d) + 1):
                q = 4 * a * c - d * t * t
                if q < 0:
                    continue
                b = isqrt(q)
                if b * b == q and b <= h and gcd(gcd(a, b), c) == 1:
                    actual.add((a, b, c))
                    actual.add((a, -b, c))
    predicted = {(m, 1, m+1), (m, -1, m+1),
                 (m+1, 1, m), (m+1, -1, m)}
    k = isqrt(4 * m + 5)
    if k*k == 4*m + 5 and k <= h:
        predicted |= {(h, k, h), (h, -k, h)}
    assert actual == predicted, (m, actual, predicted)
    # Enumerate integral generators u+v*omega, omega=(1+sqrt(-d))/2.
    # For nonzero |v|, norm=((2u+v)^2+d*v^2)/4.
    observed = []
    for v in range(-4, 5):
        if v == 0:
            continue
        for u in range(-5, 6):
            trace = 2*u+v
            norm4 = trace*trace+d*v*v
            assert norm4%4 == 0
            norm = norm4//4
            observed.append(max(1, abs(trace), norm))
    assert min(observed) == m*(m+1), m
    return len(actual), (k*k == 4*m+5 and k <= h)

checked=exceptional=0
for m in range(1, 81):
    d=4*m*(m+1)-1
    if squarefree(d):
        _, exc=test_family(m)
        checked+=1
        exceptional+=exc
assert checked>40
print('CERTIFICATE_OK squarefree_parameter_checks=',checked,
      'symmetric_exceptional_cases=',exceptional)
