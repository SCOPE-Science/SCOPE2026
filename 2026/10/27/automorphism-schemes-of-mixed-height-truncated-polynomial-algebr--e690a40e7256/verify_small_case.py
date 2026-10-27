"""Finite sanity check for A=F_2[x,y]/(x^2,y^4)."""
BASIS = [(i, j) for i in range(2) for j in range(4)]
INDEX = {m: i for i, m in enumerate(BASIS)}
ONE = 1 << INDEX[(0, 0)]

def multiply(u, v):
    out = 0
    for i, (a, b) in enumerate(BASIS):
        if (u >> i) & 1:
            for j, (c, d) in enumerate(BASIS):
                if ((v >> j) & 1) and a + c < 2 and b + d < 4:
                    out ^= 1 << INDEX[(a + c, b + d)]
    return out

def power(u, n):
    out = ONE
    while n:
        if n & 1:
            out = multiply(out, u)
        u = multiply(u, u)
        n //= 2
    return out

def coefficient(u, monomial):
    return (u >> INDEX[monomial]) & 1

x_images = [u for u in range(1 << len(BASIS)) if power(u, 2) == 0]
y_images = [u for u in range(1 << len(BASIS)) if power(u, 4) == 0]
count = 0
for f in x_images:
    a, b = coefficient(f, (1, 0)), coefficient(f, (0, 1))
    for g in y_images:
        c, d = coefficient(g, (1, 0)), coefficient(g, (0, 1))
        # Over F_2, the 2x2 linear-part determinant is ad-bc = ad+bc.
        if (a * d) ^ (b * c):
            count += 1
expected = 2 ** 11
assert len(x_images) == 64
assert len(y_images) == 128
assert count == expected == 2048
print(f"x-images={len(x_images)} y-images={len(y_images)} automorphisms={count} formula={expected} PASS")
