from math import gcd, lcm, factorial
from fractions import Fraction


def nu2(n):
    t = 0
    while n % 2 == 0:
        n //= 2
        t += 1
    return t


def odd_lcm(N):
    out = 1
    for n in range(1, N + 1, 2):
        out = lcm(out, n)
    return out


def negacyclic_mul(a, b):
    D = len(a)
    out = [0] * D
    aa = [(i, x) for i, x in enumerate(a) if x]
    bb = [(j, y) for j, y in enumerate(b) if y]
    for i, x in aa:
        for j, y in bb:
            k = i + j
            if k >= D:
                out[k - D] -= x * y
            else:
                out[k] += x * y
    return out


def geometric_factor(D, step, t):
    out = [0] * D
    modulus = 2 * D
    for r in range(1 << t):
        e = (step * r) % modulus
        if e >= D:
            out[e - D] -= 1
        else:
            out[e] += 1
    return out


def trace_polynomial(N):
    v = N.bit_length() - 1
    D = 1 << v
    O = odd_lcm(N)
    P = [1] + [0] * (D - 1)
    for b in range(2, N + 1):
        t = nu2(b)
        if t == 0:
            continue
        c = b >> t
        base = (1 << (v - t)) * (O // c)
        for a in range(1, N + 1):
            if gcd(a, b) == 1:
                P = negacyclic_mul(P, geometric_factor(D, base * a, t))
    return P


def odd_denominator_factor(N):
    B = 1
    for b in range(3, N + 1, 2):
        count = sum(1 for a in range(2, N + 1, 2) if gcd(a, b) == 1)
        B *= b ** count
    return B


def A_minus_one_from_trace(N):
    P = trace_polynomial(N)
    return (odd_denominator_factor(N) // odd_lcm(N)) * P[0]


def direct_A8_value_and_derivative():
    N = 8
    L = lcm(*range(1, N + 1))
    mod = 2 * L
    count = [0] * mod
    moment = [0] * mod
    count[0] = 1
    for a in range(1, N + 1):
        for b in range(2, N + 1):
            if gcd(a, b) != 1:
                continue
            step = L * a // b
            new_count = [0] * mod
            new_moment = [0] * mod
            for s in range(mod):
                c0 = count[s]
                if c0 == 0:
                    continue
                m0 = moment[s]
                for r in range(b):
                    delta = step * r
                    u = (s + delta) % mod
                    new_count[u] += c0
                    new_moment[u] += m0 + c0 * delta
            count, moment = new_count, new_moment
    value = count[0] - count[L]
    signed_weight_sum = (moment[0] - moment[L]) // L
    derivative = -signed_weight_sum
    return value, derivative


expected_small = {3: 2, 4: 0, 5: 120, 6: 1200, 7: 235200}
for N, expected in expected_small.items():
    got = A_minus_one_from_trace(N)
    assert got == expected, (N, got, expected)

P8 = trace_polynomial(8)
assert P8 == [0, 0, 0, 0, 0, 0, 1024, 0]
value8, derivative8 = direct_A8_value_and_derivative()
assert value8 == 0
assert derivative8 == -592704000

zeros = []
for N in range(3, 101):
    if trace_polynomial(N)[0] == 0:
        zeros.append(N)
expected_zeros = [4, 8, 11, 12, 14, 17, 27, 28, 31, 61, 62, 64]
assert zeros == expected_zeros, (zeros, expected_zeros)

print('published-table-check:', expected_small)
print('P8 mod (x^8+1):', P8)
print('A8(-1):', value8)
print("A8'(-1):", derivative8)
c8 = {a: sum(1 for b in range(2, 9) if gcd(a, b) == 1) for a in range(1, 9)}
M8 = {q: sum(c8[a] for a in range(1, 9) if a % q == 0) for q in range(2, 9)}
prod_even = 1
for a in range(2, 9, 2):
    prod_even *= a ** c8[a]
odd_exp = sum(c8[a] for a in range(1, 9, 2))
principal = Fraction(derivative8, prod_even * (2 ** odd_exp))
parity_m9 = principal / factorial(9)
assert M8 == {2: 11, 3: 7, 4: 6, 5: 6, 6: 2, 7: 6, 8: 3}
assert principal == Fraction(-128625, 34359738368)
assert parity_m9 == Fraction(-1225, 118747255799808)

print('M8(q), 2<=q<=8:', M8)
print('(-1)-pole principal coefficient after cancellation:', principal)
print('parity part of the m^9 coefficient:', parity_m9, '* (-1)^m')
print('cancellation indices 3<=N<=100:', zeros)
print('all exact checks passed')
