"""Exact arithmetic checks for the equilibrium-multiplicity moments on binary fashion-game cycles.

Run: python3 verify.py
Requires only the Python 3 standard library.  This checker is not a substitute
for the all-size transfer-matrix proof in RESULT.md.
"""
from fractions import Fraction
from decimal import Decimal, localcontext
from itertools import product

C = ((1, 1), (1, 0))
R = ((0, 1), (1, 1))
D = ((1, 0), (0, -1))


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b)))
                       for j in range(len(b))) for i in range(len(a)))


def eye(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def madd(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(len(a))) for i in range(len(a)))


def mscale(a, c):
    return tuple(tuple(c * a[i][j] for j in range(len(a))) for i in range(len(a)))


def mpow(a, n):
    out = eye(len(a))
    while n:
        if n & 1:
            out = matmul(out, a)
        a = matmul(a, a)
        n //= 2
    return out


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def kron(a, b):
    return tuple(tuple(a[i // len(b)][j // len(b)] *
                       b[i % len(b)][j % len(b)]
                       for j in range(len(a) * len(b)))
                 for i in range(len(a) * len(b)))


def count_transfer(types):
    m, signed = eye(2), eye(2)
    for typ in types:
        a = C if typ == 0 else R
        m = matmul(m, a)
        signed = matmul(signed, matmul(D, a))
    return tr(m) + tr(signed)


def count_direct(types):
    n = len(types)
    count = 0
    for x in product((0, 1), repeat=n):
        ok = True
        for i, typ in enumerate(types):
            left, right = x[(i - 1) % n], x[(i + 1) % n]
            if left == right and ((typ == 0 and x[i] != left) or
                                  (typ == 1 and x[i] == left)):
                ok = False
                break
        count += ok
    return count


def count_edge_parity(types):
    n = len(types)
    total = 0
    for y in product((0, 1), repeat=n):
        if sum(y) % 2:
            continue
        if all(not (types[i] == 0 and y[(i-1)%n] == y[i] == 1) and
               not (types[i] == 1 and y[(i-1)%n] == y[i] == 0)
               for i in range(n)):
            total += 2
    return total


def annihilates(a, polynomial):
    # Coefficients are in ascending power order.
    z = tuple(tuple(0 for _ in range(len(a))) for _ in range(len(a)))
    x = eye(len(a))
    for c in polynomial:
        z = madd(z, mscale(x, c))
        x = matmul(x, a)
    return all(v == 0 for row in z for v in row)


def characteristic_polynomial(a):
    # Newton's identities independently reconstruct det(z I - a),
    # listing coefficients from constant term upward.
    dim = len(a)
    power_traces = [0] + [tr(mpow(a, j)) for j in range(1, dim + 1)]
    elementary = [Fraction(1)]
    for k in range(1, dim + 1):
        elementary.append(sum((-1)**(j-1) * elementary[k-j] * power_traces[j]
                              for j in range(1, k + 1)) / k)
    return tuple((-1)**k * elementary[k] for k in range(dim, -1, -1))


T2 = madd(C, R)
DT2 = matmul(D, T2)
DC, DR = matmul(D, C), matmul(D, R)
U2 = madd(kron(C, C), kron(R, R))
V2 = madd(kron(C, DC), kron(R, DR))
W2 = madd(kron(DC, DC), kron(DR, DR))

assert characteristic_polynomial(T2) == (-3, -2, 1)
assert characteristic_polynomial(DT2) == (3, 0, 1)
assert characteristic_polynomial(U2) == (4, -4, -11, -2, 1)
assert characteristic_polynomial(V2) == (4, 0, 7, 0, 1)
assert characteristic_polynomial(W2) == (4, 4, -3, -2, 1)
assert annihilates(U2, (4, -4, -11, -2, 1)), 'U characteristic polynomial'
assert annihilates(V2, (4, 0, 7, 0, 1)), 'V characteristic polynomial'
assert annihilates(W2, (4, 4, -3, -2, 1)), 'W characteristic polynomial'
print('EXACT_CHARACTERISTIC_IDENTITIES_OK')

# Independent exhaustive action checks for small cycles.
seen = 0
for n in range(3, 10):
    for types in product((0, 1), repeat=n):
        direct = count_direct(types)
        assert direct == count_transfer(types), (n, types, direct, 'matrix')
        assert direct == count_edge_parity(types), (n, types, direct, 'edges')
        seen += 1
print('DIRECT_ACTION_AND_EDGE_ENUMERATION_OK', seen)

# Exact moments over every type sequence through 12 players.
for n in range(3, 13):
    first, second, no_equilibrium = 0, 0, 0
    for types in product((0, 1), repeat=n):
        k = count_transfer(types)
        first += k
        second += k*k
        no_equilibrium += (k == 0)
    mean = Fraction(first, 2**n)
    second_moment = Fraction(second, 2**n)
    transfer_mean = Fraction(tr(mpow(T2, n)) + tr(mpow(DT2, n)), 2**n)
    transfer_second = Fraction(tr(mpow(U2, n)) + 2*tr(mpow(V2, n)) +
                               tr(mpow(W2, n)), 2**n)
    assert mean == transfer_mean, (n, 'mean', mean, transfer_mean)
    assert second_moment == transfer_second, (n, 'second', second_moment, transfer_second)
    assert no_equilibrium == (2 if n % 4 == 2 else 0), (n, 'zero', no_equilibrium)
    with localcontext() as ctx:
        ctx.prec = 75
        one, two = Decimal(1), Decimal(2)
        alpha = (Decimal(5) + Decimal(17).sqrt()) / 4
        beta = (Decimal(5) - Decimal(17).sqrt()) / 4
        gamma = (Decimal(7) + Decimal(33).sqrt()) / 8
        delta = (Decimal(7) - Decimal(33).sqrt()) / 8
        sign_cos = (1 if n % 4 == 0 else (-1 if n % 4 == 2 else 0))
        mean_formula = (Decimal(3)/2)**n + (Decimal(-1)/2)**n
        if sign_cos:
            mean_formula += 2*sign_cos*(Decimal(3).sqrt()/2)**n
        second_formula = alpha**n + beta**n + Decimal((-1)**n) + 2 + 3*(Decimal(-1)/2)**n
        if n % 2 == 0:
            second_formula += 4*((-1)**(n//2))*(gamma**(n//2) + delta**(n//2))
        assert abs(mean_formula - Decimal(mean.numerator)/Decimal(mean.denominator)) < Decimal('1e-50')
        assert abs(second_formula - Decimal(second_moment.numerator)/Decimal(second_moment.denominator)) < Decimal('1e-50')
    print('EXACT_MOMENTS', n, str(mean), str(second_moment), 'zero_profiles', no_equilibrium)
print('VERIFICATION_OK')
