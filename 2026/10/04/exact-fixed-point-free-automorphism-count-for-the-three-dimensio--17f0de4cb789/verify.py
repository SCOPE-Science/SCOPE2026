from itertools import product


def count_prime_field(q):
    gl2 = good = 0
    for a, b, c, d in product(range(q), repeat=4):
        det = (a*d - b*c) % q
        if det == 0:
            continue
        gl2 += 1
        det_minus_identity = ((a-1)*(d-1) - b*c) % q
        if det_minus_identity != 0 and det != 1 % q:
            good += 1
    return gl2, good


# GF(4) = F_2[t]/(t^2+t+1), encoded by a + b t -> a + 2b.
def gf4_add(x, y):
    return x ^ y


def gf4_mul(x, y):
    a0, a1 = x & 1, (x >> 1) & 1
    b0, b1 = y & 1, (y >> 1) & 1
    c0 = a0 & b0
    c1 = (a0 & b1) ^ (a1 & b0)
    c2 = a1 & b1
    # t^2 = t + 1 in characteristic two.
    return (c0 ^ c2) | ((c1 ^ c2) << 1)


def count_gf4():
    gl2 = good = 0
    for a, b, c, d in product(range(4), repeat=4):
        det = gf4_add(gf4_mul(a, d), gf4_mul(b, c))
        if det == 0:
            continue
        gl2 += 1
        det_minus_identity = gf4_add(
            gf4_mul(gf4_add(a, 1), gf4_add(d, 1)),
            gf4_mul(b, c),
        )
        if det_minus_identity != 0 and det != 1:
            good += 1
    return gl2, good


def formula_good_linear(q):
    return q * (q + 1) * (q - 2) ** 2


def formula_fpf_automorphisms(q):
    return q**3 * (q + 1) * (q - 2) ** 2


for q in (2, 3, 5, 7):
    gl2, good = count_prime_field(q)
    assert gl2 == q * (q - 1) ** 2 * (q + 1)
    assert good == formula_good_linear(q)
    print(f"F_{q}: GL2={gl2}, good_A={good}, fpf_aut={q*q*good}")

q = 4
gl2, good = count_gf4()
assert gl2 == q * (q - 1) ** 2 * (q + 1)
assert good == formula_good_linear(q)
print(f"F_4: GL2={gl2}, good_A={good}, fpf_aut={q*q*good}")

for q in (2, 3, 4, 5, 7):
    assert q*q*formula_good_linear(q) == formula_fpf_automorphisms(q)

print("CHECK_OK")
