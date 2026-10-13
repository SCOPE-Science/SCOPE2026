#!/usr/bin/env python3

def digit_square_sum(n, b):
    s = 0
    while n:
        n, d = divmod(n, b)
        s += d*d
    return s

# Exhaust every two-digit X whose double is also two-digit.
hits = []
tested = 0
for b in range(2, 401):
    predicted = []
    if (b - 3) % 5 == 0:
        t = (b - 3)//5
        if t >= 1:
            predicted.append(t*b + (3*t + 2))

    observed = []
    lo = b
    hi = (b*b - 1)//2
    for X in range(lo, hi + 1):
        tested += 1
        if digit_square_sum(X, b) == 2*X and digit_square_sum(2*X, b) == X:
            observed.append(X)
    assert observed == predicted, (b, observed, predicted)
    for X in observed:
        hits.append((b, X, 2*X))

# Verify the constructed family far beyond the exhaustive base window.
for t in range(1, 10001):
    b = 5*t + 3
    X = t*b + (3*t + 2)
    Y = 2*X
    assert b <= X < b*b
    assert b <= Y < b*b
    assert digit_square_sum(X, b) == Y
    assert digit_square_sum(Y, b) == X

# Verify the two branch substitutions and the carry rejection over a grid.
for a in range(1, 10001):
    b1, c1 = 5*a + 3, 3*a + 2
    assert 2*c1 >= b1
    assert a*a + c1*c1 == 2*(a*b1 + c1)
    assert (2*a+1)**2 + (2*c1-b1)**2 == a*b1 + c1

    b2, c2 = 13*a + 5, 5*a + 2
    assert 2*c2 < b2

print(
    "VERIFY_OK",
    f"bases=2..400",
    f"tested={tested}",
    f"hits={len(hits)}",
    f"first={hits[:8]}",
    f"family_t=1..10000",
)
