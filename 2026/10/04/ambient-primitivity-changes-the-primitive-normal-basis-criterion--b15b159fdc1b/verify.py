"""Exact finite-field replay for the (q,n)=(4,3) Dickson-nearfield example."""

MOD = 0b1000011  # X^6 + X + 1 over F_2
DEG = 6
MASK = (1 << DEG) - 1


def mul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
        if a & (1 << DEG):
            a ^= MOD
    return r & MASK


def fpow(a, e):
    r = 1
    while e:
        if e & 1:
            r = mul(r, a)
        a = mul(a, a)
        e >>= 1
    return r


g = 0b10  # the residue class of X
# Order 63 proves that g generates all nonzero residue classes, so the quotient is F_64.
assert fpow(g, 63) == 1
assert fpow(g, 63 // 3) != 1
assert fpow(g, 63 // 7) != 1

# Build the discrete-log table and the H=<g^3> cosets.
log = {}
x = 1
for e in range(63):
    log[x] = e
    x = mul(x, g)
assert len(log) == 63

b = fpow(g, 34)
assert b == ((1 << 5) | (1 << 2))  # g^5 + g^2 in polynomial coordinates
one_plus_b = b ^ 1
assert one_plus_b == fpow(g, 31)
assert log[b] % 3 == 1 and log[one_plus_b] % 3 == 1

# For (q,n)=(4,3), n divides q-1, so H,gH,g^2H carry Frobenius exponents
# 4^3 (the identity on F_64), 4, and 4^2 respectively.
def circle(a, d):
    if a == 0:
        return 0
    c = log[a] % 3
    exponent = {0: 4**3, 1: 4, 2: 4**2}[c]
    return mul(a, fpow(d, exponent))

D = []
for d in range(64):
    if circle(one_plus_b, d) == (circle(1, d) ^ circle(b, d)):
        D.append(d)
F4 = [d for d in range(64) if fpow(d, 4) == d]
assert set(D) == set(F4)
assert len(D) == 4

# No element of F_4 has multiplicative order 63, hence none is primitive in F_64.
for u in D:
    if u != 0:
        assert fpow(u, 3) == 1

print("CHECK_OK")
print("b_log=34 one_plus_b_log=31 coset=gH")
print("D_size=4 D_equals_F4=true")
print("ambient_primitive_in_D=false")
