from itertools import product

def formula(p, a, b):
    assert 1 <= a < b
    if (a, b) == (1, 2):
        return p * (2*p**3 - 4*p**2 + 1)
    if a == 1:
        return p**b * (p - 2) * (2*p - 1)
    if b == a + 1:
        return p**(4*a - 3) * (p - 1) * (2*p*p - 3*p - 1)
    return 2 * p**(3*a + b - 3) * (p - 1) * (p - 2)

def brute(p, a, b):
    pa = p**a
    pb = p**b
    gap = b - a
    count_p = 0
    aut_count = 0
    for alpha in range(pa):
        if alpha % p == 0:
            continue
        for beta in range(pa):
            for gamma in range(pa):
                lower = (p**gap) * gamma
                for delta in range(pb):
                    if delta % p == 0:
                        continue
                    aut_count += 1
                    fixed = 0
                    for x in range(pa):
                        for y in range(pb):
                            if ((alpha - 1)*x + beta*y) % pa:
                                continue
                            if (lower*x + (delta - 1)*y) % pb:
                                continue
                            fixed += 1
                    if fixed == p:
                        count_p += 1
    expected_aut = p**(3*a + b - 2) * (p - 1)**2
    assert aut_count == expected_aut, (p, a, b, aut_count, expected_aut)
    return count_p

tests = [
    (2,1,2),
    (2,1,3),
    (2,2,3),
    (2,2,4),
    (3,1,2),
    (3,1,3),
    (3,2,3),
    (3,2,4),
    (5,1,2),
    (5,1,3),
]

for p, a, b in tests:
    got = brute(p, a, b)
    want = formula(p, a, b)
    assert got == want, (p, a, b, got, want)

# Published special cases simplify to the corresponding theorem branches.
for p in (2,3,5,7):
    # C_p + C_{p^2}, Hayat--Lopez-Aguayo--Abbas.
    known12 = p * (2*p**3 - 4*p**2 + 1)
    assert formula(p,1,2) == known12

    # C_p + C_{p^3}, Hayat--Ali.
    known13 = p**3 * (2*p**2 - 5*p + 2)
    assert formula(p,1,3) == known13

    # C_{p^2} + C_{p^3}, Ali--Hayat--Li.
    known23 = p**5 * (2*p**3 - 5*p**2 + 2*p + 1)
    assert formula(p,2,3) == known23

# Characteristic-two phase transition.
for a in range(1, 8):
    for b in range(a+1, a+5):
        positive = formula(2,a,b) > 0
        assert positive == (b == a + 1), (a,b,formula(2,a,b))

print("VERIFY_OK")
