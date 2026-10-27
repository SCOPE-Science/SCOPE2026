#!/usr/bin/env python3
"""Finite sanity checks for f(x)=x^2+1 on Z_3; not an infinite proof."""

def f(x, modulus):
    return (x * x + 1) % modulus

def f3_integer(x):
    y = x
    for _ in range(3):
        y = y * y + 1
    return y

def P(x):
    return x**6 + x**5 + 4*x**4 + 3*x**3 + 7*x**2 + 4*x + 5

# Check the exact polynomial identity at sample integers.
for x in range(-10, 101):
    assert f3_integer(x) - x == (x*x - x + 1) * P(x)

# Check the predicted cycle census on finite quotients.
for n in range(2, 9):
    modulus = 3**n
    ball = {x for x in range(modulus) if x % 3 == 2}
    seen = set()
    lengths = []
    for x in sorted(ball):
        if x in seen:
            continue
        orbit = []
        y = x
        while y not in orbit:
            orbit.append(y)
            y = f(y, modulus)
        assert y == x, "The restriction to the ball should be a permutation."
        seen.update(orbit)
        lengths.append(len(orbit))
    lengths.sort()
    if n == 2:
        expected = [3]
    elif n == 3:
        expected = [3, 3, 3]
    else:
        expected = [3**(n-2)] * 3
    assert lengths == expected, (n, lengths, expected)

print("finite sanity checks passed for 2 <= n <= 8")
