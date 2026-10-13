from itertools import combinations_with_replacement
from math import factorial

def degree(a):
    N = sum(a)
    out = factorial(N)
    for x in a:
        out //= factorial(x)
    return out

def euler(a):
    out = 1
    for x in a:
        out *= x + 1
    return out

def predicted_sign(a):
    a = tuple(sorted(a))
    r = len(a)
    if r == 1:
        return -1
    if r == 2:
        x, y = a
        if x == 1 or (x, y) in {(2,2), (2,3)}:
            return -1
        if (x, y) == (2,4):
            return 0
        return 1
    if r == 3:
        if a == (1,1,1):
            return -1
        if a == (1,1,2):
            return 0
        return 1
    return 1

tuple_checks = 0
ratio_checks = 0
for r in range(1, 7):
    for a in combinations_with_replacement(range(1, 11), r):
        D = degree(a)
        E = euler(a)
        sign = (D > E) - (D < E)
        assert sign == predicted_sign(a), (a, D, E, sign, predicted_sign(a))
        tuple_checks += 1

        N = sum(a)
        for j in range(r):
            b = list(a)
            b[j] += 1
            # Exact cross-multiplied ratio identity.
            left_num = degree(tuple(b)) * E
            left_den = euler(tuple(b)) * D
            assert left_num * (a[j] + 2) == left_den * (N + 1), (a, j)
            ratio_checks += 1

assert degree((2,4)) == euler((2,4)) == 15
assert degree((1,1,2)) == euler((1,1,2)) == 12

print("VERIFY_OK", tuple_checks, ratio_checks)
