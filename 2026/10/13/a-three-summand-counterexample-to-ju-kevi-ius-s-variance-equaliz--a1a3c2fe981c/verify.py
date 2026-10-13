from fractions import Fraction

def conv(a, b):
    out = {}
    for x, px in a.items():
        for y, py in b.items():
            out[x + y] = out.get(x + y, Fraction(0)) + px * py
    return dict(sorted(out.items()))

def mean(d):
    return sum(Fraction(x) * p for x, p in d.items())

def variance(d):
    m = mean(d)
    return sum((Fraction(x) - m) ** 2 * p for x, p in d.items())

def q2(d):
    # For integer support and half-open windows (x,x+2], an extremal window
    # contains either one atom or two consecutive integer atoms.
    keys = sorted(d)
    best = max(d.values())
    for a in keys:
        if a + 1 in d:
            best = max(best, d[a] + d[a + 1])
    return best

T1 = {0: Fraction(1)}
T12 = {-1: Fraction(1, 2), 1: Fraction(1, 2)}
T25 = {j: Fraction(1, 5) for j in range(-2, 3)}

assert sum(T1.values()) == sum(T12.values()) == sum(T25.values()) == 1
assert mean(T1) == mean(T12) == mean(T25) == 0
assert variance(T1) == 0
assert variance(T12) == 1
assert variance(T25) == 2

original = conv(conv(T1, T12), T25)
equalized = conv(conv(T12, T12), T12)

assert original == {
    -3: Fraction(1, 10), -2: Fraction(1, 10), -1: Fraction(1, 5),
     0: Fraction(1, 5),   1: Fraction(1, 5),   2: Fraction(1, 10),
     3: Fraction(1, 10),
}
assert equalized == {
    -3: Fraction(1, 8), -1: Fraction(3, 8),
     1: Fraction(3, 8),  3: Fraction(1, 8),
}
assert q2(original) == Fraction(2, 5)
assert q2(equalized) == Fraction(3, 8)
assert q2(original) - q2(equalized) == Fraction(1, 40)

print("VERIFY_OK", q2(original), q2(equalized), q2(original) - q2(equalized))
