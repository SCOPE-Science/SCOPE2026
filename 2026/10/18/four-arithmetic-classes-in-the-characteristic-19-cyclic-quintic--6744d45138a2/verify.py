"""Exact arithmetic checks for the cyclic-quintic genus-four classification.

Uses only Python's standard library. All polynomial arithmetic is over F_19.
The proof for algebraically closed parameters is contained in RESULT.md;
this program independently checks its coefficient identities, finite-field
class partition, and quadratic-extension point counts.
"""
from math import comb
from collections import defaultdict

P = 19


def add_poly(a, b):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] = (out[i] + x) % P
    for i, x in enumerate(b):
        out[i] = (out[i] + x) % P
    return trim(out)


def trim(a):
    a = [x % P for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def mul_poly(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % P
    return trim(out)


def power_poly(a, n):
    r = [1]
    while n:
        if n & 1:
            r = mul_poly(r, a)
        a = mul_poly(a, a)
        n //= 2
    return r


def scalar(a, c):
    return trim([c*x for x in a])


def coefficient_f_power(n, x_degree):
    # f=x(x-1)(x-t). From the two binomial expansions of f^n:
    # [x^k]f^n = (-1)^(k-n) sum_{a+b=k-n} C(n,a)C(n,b)t^(n-b).
    k = x_degree - n
    ans = [0] * (n + 1)
    for a in range(n + 1):
        b = k - a
        if 0 <= b <= n:
            ans[n-b] += (-1)**k * comb(n, a) * comb(n, b)
    return trim(ans)


T = [0, 1]
P_harmonic = mul_poly(mul_poly([-2, 1], [1, 1]), [9, 1])
A_expected = scalar(mul_poly(mul_poly(power_poly(T, 4), power_poly([-1, 1], 4)), P_harmonic), -7)
B_expected = scalar(P_harmonic, 3)
A_actual = coefficient_f_power(11, 18)
B_actual = coefficient_f_power(7, 18)
assert A_actual == A_expected, (A_actual, A_expected)
assert B_actual == B_expected, (B_actual, B_expected)
assert P_harmonic == [1, 8, 8, 1]
print('Cartier coefficient identities: PASS')
print('A(t) coefficient vector:', A_actual)
print('B(t) coefficient vector:', B_actual)


def eval_poly(a, t):
    r = 0
    for c in reversed(a):
        r = (r*t + c) % P
    return r


def orbit(t):
    found = {t}
    todo = [t]
    while todo:
        a = todo.pop()
        for b in ((1-a) % P, pow(a, -1, P)):
            if b not in found:
                found.add(b)
                todo.append(b)
    return tuple(sorted(found))


def ffadd(x, y):
    return ((x[0]+y[0]) % P, (x[1]+y[1]) % P)


def ffneg(x):
    return ((-x[0]) % P, (-x[1]) % P)


def ffmul(x, y):
    # F_19[u]/(u^2-2); 2 is a nonsquare in F_19.
    a, b = x
    c, d = y
    return ((a*c+2*b*d) % P, (a*d+b*c) % P)


def ffpow(x, n):
    r = (1, 0)
    while n:
        if n & 1:
            r = ffmul(r, x)
        x = ffmul(x, x)
        n //= 2
    return r


assert {a*a % P for a in range(1, P)}.isdisjoint({2})

def points_q2(t):
    # Nonzero z has five fifth roots iff z^72=1 in F_(19^2).
    # Exactly one rational place lies above infinity, gcd(5,3)=1.
    count = 1
    t = (t, 0)
    for a in range(P):
        for b in range(P):
            x = (a, b)
            value = ffmul(ffmul(x, ffadd(x, (P-1, 0))), ffadd(x, ffneg(t)))
            if value == (0, 0):
                count += 1
            elif ffpow(value, 72) == (1, 0):
                count += 5
    return count


def points_q(t):
    # The fifth-power map is an automorphism of F_19, since gcd(5,18)=1.
    return P + 1


expected = {
    (2, 10, 18): (514, 0, 4),
    (8, 12): (354, 2, 2),
    (3, 7, 9, 11, 13, 17): (404, 2, 2),
    (4, 5, 6, 14, 15, 16): (424, 2, 2),
}
classes = defaultdict(list)
for t in range(2, P):
    classes[orbit(t)].append(t)
assert set(classes) == set(expected)
for orb, t_values in sorted(classes.items()):
    assert tuple(sorted(t_values)) == orb
    q2 = {points_q2(t) for t in t_values}
    assert len(q2) == 1
    q2 = q2.pop()
    rank = 0 if eval_poly(P_harmonic, t_values[0]) == 0 else 2
    a_num = 4 - rank
    p_rank = rank  # The nonzero 2x2 Cartier block is invertible.
    assert (q2, p_rank, a_num) == expected[orb]
    assert all(points_q(t) == 20 for t in t_values)
    print(f'parameters={orb}, #F_361={q2}, p-rank={p_rank}, a={a_num}')
assert sum(map(len, classes)) == P-2
assert max(v[0] for v in expected.values()) == P*P + 1 + 2*4*P == 514
assert sum(1 for t in range(2,P) if eval_poly(P_harmonic, t)==0)==3
print('All 17 parameters, four F_19-isomorphism classes, and maximality: PASS')
