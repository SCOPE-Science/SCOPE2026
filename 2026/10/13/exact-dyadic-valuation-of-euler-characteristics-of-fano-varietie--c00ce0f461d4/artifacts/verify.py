from math import comb

def v2(n):
    n = abs(n)
    assert n > 0
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c

def chi_y_closed(d):
    return ((-2) ** (d + 2) - 1) // 3 + d + 2

def chi_y_chern(d):
    # 3 * coefficient of H^d in (1+H)^(d+2)/(1+3H)
    coeff = 0
    for j in range(d + 1):
        coeff += ((-3) ** j) * comb(d + 2, d - j)
    return 3 * coeff

def chi_f(d):
    c = chi_y_closed(d)
    return c * (c - 3) // 2

for d in range(2, 201):
    assert chi_y_closed(d) == chi_y_chern(d)

for d in range(2, 5001):
    c = chi_y_closed(d)
    f = chi_f(d)
    assert f != 0
    if d % 2 == 0:
        assert c % 2 == 1
        assert (c - 3) % 2 == 0
        assert abs(3 * d - 4) < 2 ** (d + 2)
        want = v2(3 * d - 4) - 1
    else:
        assert c % 2 == 0
        assert (c - 3) % 2 == 1
        assert 3 * d + 5 < 2 ** (d + 2)
        want = v2(3 * d + 5) - 1
    assert v2(f) == want

for t in range(0, 9):
    mod = 2 ** (t + 2)
    residues = []
    for d in range(mod):
        if d % 2 == 0:
            ok = (3 * d - 4) % mod == 2 ** (t + 1)
        else:
            ok = (3 * d + 5) % mod == 2 ** (t + 1)
        if ok:
            residues.append(d)
    assert len(residues) == 2, (t, residues)

assert [chi_f(d) for d in range(2, 10)] == [
    27, 27, 324, 702, 4185, 13365, 61074, 226800
]

print("VERIFY_OK", 199, 4999, 9)
