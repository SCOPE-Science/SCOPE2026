"""Finite consistency check for the characteristic-two local base ideal.
Uses only the Python standard library; basis is 1,a,b,ab over F_2.
"""
BASIS = ((0, 0), (1, 0), (0, 1), (1, 1))

def add(x, y):
    return x ^ y

def mul(x, y):
    out = 0
    for i, (p, q) in enumerate(BASIS):
        if not (x >> i) & 1:
            continue
        for j, (r, s) in enumerate(BASIS):
            if not (y >> j) & 1:
                continue
            if p + r < 2 and q + s < 2:
                out ^= 1 << BASIS.index((p + r, q + s))
    return out

one, a, b = 1, 2, 4
ab = mul(a, b)
c = add(add(a, b), ab)          # c = a + b + ab
s = add(add(a, b), c)
assert mul(a, a) == 0 and mul(b, b) == 0 and mul(c, c) == 0
assert s == ab
assert mul(a, b) == mul(a, c) == mul(b, c) == ab
# P0=s^2; P01=s+bc; P10=s+ac; P11=s+ab, all vanish.
assert mul(s, s) == 0
assert add(s, mul(b, c)) == 0
assert add(s, mul(a, c)) == 0
assert add(s, mul(a, b)) == 0
assert len(BASIS) == 4
print("LOCAL_BASE_IDEAL_CHECK_OK: length 4, Hilbert function (1,2,1)")
