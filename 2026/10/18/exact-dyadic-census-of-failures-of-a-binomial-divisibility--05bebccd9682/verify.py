#!/usr/bin/env python3
"""Exact polynomial certificate and independent arithmetic checks for a binomial divisibility census."""
from math import comb

# Seven states after reading the compulsory odd least-significant digit.
# Rows are source states; -1 means the transition is forbidden.
NEXT = ((1, 2), (3, 4), (5, -1), (3, 6), (1, -1), (3, 2), (-1, 2))
TERMINAL = (1, 1, 1, 1, 1, 1, 0)
# Q(z) and the seven numerators Q(z)G_i(z), in ascending degree order.
Q = (1, -1, -1, 1, -1)
H = ((1, 1), (1, 1, -1, 1), (1,), (1, 0, 0, 1), (1,),
     (1, 1, -1, 1), (0, 1))

def plus(a, b):
    return tuple((a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b))))

def shift(a):
    return (0,) + tuple(a)

def valuation_two(x):
    assert x > 0
    return (x & -x).bit_length() - 1

def popcount_valuation(n):
    # Legendre's identity, computed independently of the automaton.
    return n.bit_count() + (3 * n).bit_count() - (5 * n).bit_count()

def accepted(n):
    if n <= 0 or n % 2 == 0:
        return False
    # Input begins with bit 1; the first bit cannot generate a carry.
    p, a, b, phase = 1, 0, 0, 0
    for bit_index in range(1, max(n.bit_length() + 5, 8)):
        bit = (n >> bit_index) & 1
        three = bit + p + a
        v, aa = three % 2, three // 2
        bb = (v + p + b) // 2
        if phase == 0:
            if v and bb != 1:
                return False
            if not v and bb != 0:
                return False
            if not v:
                phase = 1
        elif bb != 0:
            return False
        p, a, b = bit, aa, bb
    assert (p, a, b) == (0, 0, 0)
    return phase == 1

# Exact formal-power-series proof of the rational generating function:
# G_i = terminal_i + z * sum_{i -> j} G_j, and H_i = Q G_i.
for i in range(7):
    rhs = tuple(q * TERMINAL[i] for q in Q)
    for j in NEXT[i]:
        if j >= 0:
            rhs = plus(rhs, shift(H[j]))
    maxlen = max(len(rhs), len(H[i]))
    assert [rhs[k] if k < len(rhs) else 0 for k in range(maxlen)] == [
        H[i][k] if k < len(H[i]) else 0 for k in range(maxlen)]
assert H[0] == (1, 1)

# Check the finite-state transitions against a second, explicit bit arithmetic rule.
states = ((1, 0, 0, 0), (0, 0, 1, 0), (1, 1, 0, 1),
          (0, 0, 0, 1), (1, 0, 1, 0), (0, 1, 0, 1), (1, 0, 0, 1))
for i, (p, a, b, phase) in enumerate(states):
    for digit in (0, 1):
        w = digit + p + a
        v, aa = w % 2, w // 2
        bb = (v + p + b) // 2
        permitted = bb == (1 if phase == 0 and v else 0)
        newstate = (digit, aa, bb, int(phase or not v))
        assert (states[NEXT[i][digit]] if NEXT[i][digit] >= 0 else None) == (
            newstate if permitted else None)

# Independently compute the dyadic census, first with exact integer binomials.
for n in range(1, 600):
    actual = comb(5 * n, 2 * n) % (3 * n + 1) != 0
    assert accepted(n) == actual, (n, actual)
for n in range(1, 1 << 14):
    h = valuation_two(3 * n + 1)
    actual = bool(n & 1) and popcount_valuation(n) == h - 1
    assert accepted(n) == actual, n

# Independent coefficient recurrence for F(z)=z(1+z)/Q(z).
N = 19
coeff = [0] * (N + 1)
for l in range(N + 1):
    num = int(l in (1, 2))
    coeff[l] = num + sum((-Q[k]) * coeff[l - k]
                          for k in range(1, min(l, 4) + 1))
vector = [int(x) for x in TERMINAL]
assert coeff[0] == 0
for l in range(1, N + 1):
    assert vector[0] == coeff[l], (l, vector[0], coeff[l])
    vector = [sum(vector[j] for j in NEXT[i] if j >= 0)
              for i in range(7)]
print('VERIFY_OK: seven exact polynomial certificates; transition identities; '
      'integer binomial cross-check; 16383 digit checks; 19 census levels')
