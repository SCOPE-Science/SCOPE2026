from math import comb, factorial

def v2(x):
    assert x > 0
    e = 0
    while x % 2 == 0:
        x //= 2
        e += 1
    return e

def s2(n):
    return n.bit_count()

N = 1000

kappa = [0] * (N + 1)
kappa[0] = kappa[1] = 1
for n in range(2, N + 1):
    kappa[n] = n * kappa[n-1] + comb(n, 2) * kappa[n-2]

U = [0] * (N + 2)
U[0] = 0
U[1] = 1
for m in range(2, N + 2):
    U[m] = 2 * U[m-1] + 2 * U[m-2]

euler_checks = lucas_checks = bridge_checks = 0

for m in range(1, N + 2):
    predicted = m // 2
    if m % 4 == 0:
        predicted += v2(m)
    assert v2(U[m]) == predicted, (m, U[m], v2(U[m]), predicted)
    lucas_checks += 1

for n in range(1, N + 1):
    predicted = (n + 1) // 2 - s2(n)
    if n % 4 == 3:
        predicted += v2(n + 1)
    assert v2(kappa[n]) == predicted, (n, kappa[n], v2(kappa[n]), predicted)
    euler_checks += 1

    numerator = factorial(n) * U[n+1]
    assert numerator % (2 ** n) == 0
    assert numerator // (2 ** n) == kappa[n]
    bridge_checks += 1

assert [kappa[n] for n in range(1, 8)] == [1, 3, 12, 66, 450, 3690, 35280]
assert [v2(kappa[n]) for n in range(1, 8)] == [0, 0, 2, 1, 1, 1, 4]
assert [n for n in range(1, N + 1) if kappa[n] % 2] == [1, 2]

print("VERIFY_OK", euler_checks, lucas_checks, bridge_checks)
