"""Reproducible finite checks for the local power-class formula.

The checks below compare finitely many polynomial values and finite-level
power maps. The theorem for all integers is proved algebraically in RESULT.md.
"""
from math import gcd


def vp_unit(x, p):
    assert x != 0
    v = 0
    while x % p == 0:
        v += 1
        x //= p
    return v, x


def cls(x, p, degree):
    v, u = vp_unit(x, p)
    d = gcd(degree, p - 1)
    symbol = pow(u % p, (p - 1) // d, p)
    return v % degree, symbol


def quotient_class(s, t, degree, p):
    return ((s[0] - t[0]) % degree, (s[1] * pow(t[1], -1, p)) % p)


def check_case(degree, p, a, b, extent):
    assert gcd(degree, p) == 1
    assert (vp_unit(a, p)[0] - vp_unit(b, p)[0]) % degree != 0
    allowed_values = {cls(a, p, degree), cls(b, p, degree)}
    found = set()
    tests = 0
    for x in range(-extent, extent + 1):
        for y in range(-extent, extent + 1):
            z = a * (x ** degree) + b * (y ** degree)
            if not z:
                continue
            s = cls(z, p, degree)
            assert s in allowed_values, (degree, p, a, b, x, y, z, s)
            found.add(s)
            tests += 1
    assert found == allowed_values
    actual_quotients = {
        quotient_class(x, y, degree, p) for x in found for y in found
    }
    t = quotient_class(cls(a, p, degree), cls(b, p, degree), degree, p)
    ti = quotient_class(cls(b, p, degree), cls(a, p, degree), degree, p)
    assert actual_quotients == {(0, 1), t, ti}
    order = degree * gcd(degree, p - 1)
    is_dense = (len(actual_quotients) == order)
    assert is_dense == (degree == 3 and p % 3 == 2)
    return tests, len(actual_quotients), order


def check_power_map(degree, p, exponent):
    assert gcd(degree, p) == 1
    modulus = p ** exponent
    domain = [x for x in range(modulus) if x % p]
    power_image = {pow(x, degree, modulus) for x in domain}
    allowed = {
        x for x in domain
        if pow(x % p, (p - 1) // gcd(degree, p - 1), p) == 1
    }
    assert power_image == allowed, (degree, p, exponent)
    return len(domain), len(power_image)


def main():
    cases = [
        (3, 2, 2, 1, 45), (3, 5, 5, 1, 45), (3, 7, 7, 1, 45),
        (3, 13, 26, 1, 45), (4, 3, 3, 1, 35), (4, 5, 5, 1, 35),
        (5, 2, 2, 1, 35), (5, 7, 49, 1, 30), (6, 5, 25, 1, 30),
        (6, 7, 343, 1, 30), (9, 2, 8, 1, 30), (3, 5, 25, 5, 35),
    ]
    total_values = 0
    for n, p, a, b, extent in cases:
        count, realized, order = check_case(n, p, a, b, extent)
        total_values += count
        print(f"value classes: degree={n} p={p} coefficients=({a},{b}) "
              f"values={count} quotient_classes={realized}/{order} PASS")
    powers_checked = 0
    for n, p, exponent in [
        (3, 2, 8), (3, 5, 4), (3, 7, 4), (3, 13, 3),
        (4, 3, 5), (4, 5, 4), (5, 2, 8), (5, 7, 3),
        (6, 5, 4), (6, 7, 3), (9, 2, 8),
    ]:
        size, image_size = check_power_map(n, p, exponent)
        powers_checked += size
        print(f"unit power map: degree={n} p={p} level={exponent} "
              f"units={size} image={image_size} PASS")
    print(f"PASS: {len(cases)} form cases; {total_values} nonzero values; "
          f"11 complete finite unit-power comparisons with {powers_checked} units")


if __name__ == "__main__":
    main()

# Cyclic Singer difference sets give the sharp low-variable examples.
def check_difference_basis(n, exponents):
    assert len(set(exponents)) == len(exponents)
    residues = [(x-y) % n for x in exponents for y in exponents if x!=y]
    assert len(residues) == n-1 and set(residues) == set(range(1,n))
    assert len(exponents) * (len(exponents)-1) == n-1
    print(f"Singer parameters: degree={n} variables={len(exponents)} "
          f"difference multiplicities one for all {n-1} nonzero residues PASS")


def check_multivariable_class(degree, p, exponents, alphabet):
    from itertools import product
    coefficients=[p**v for v in exponents]
    allowed={cls(a,p,degree) for a in coefficients}
    found=set()
    checked=0
    for xx in product(alphabet, repeat=len(coefficients)):
        z=sum(a*x**degree for a,x in zip(coefficients,xx))
        if not z:
            continue
        result=cls(z,p,degree)
        assert result in allowed, (degree,p,xx,result)
        found.add(result)
        checked+=1
    assert found==allowed
    differences={quotient_class(x,y,degree,p) for x in found for y in found}
    assert len(differences)==degree*gcd(degree,p-1), (degree,differences)
    print(f"full quotient power classes: degree={degree} p={p} "
          f"variables={len(exponents)} tested_nonzero_values={checked} "
          f"classes={len(differences)} PASS")


def check_singer_instances():
    cases=[(7,[0,1,3]),(13,[0,1,3,9]),(21,[0,1,4,14,16])]
    for degree,exponents in cases:
        check_difference_basis(degree,exponents)
        check_multivariable_class(degree,2,exponents,[-1,0,1])

# Append-only entry point preserves the independently coded binary checks.
if __name__ == '__main__':
    check_singer_instances()
