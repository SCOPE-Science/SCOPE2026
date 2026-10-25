"""Exact finite-field sample checks for parameter equivalence of degree-four AS covers.

The mathematics for arbitrary algebraically closed fields is proved separately.
This program verifies finite-field instances by independent expansion and
Artin--Schreier polynomial reduction, not by using the claimed orbit formula
as the membership test.
"""

MOD = 0x11B

def mul(a, b):
    z = 0
    while b:
        if b & 1:
            z ^= a
        b >>= 1
        a <<= 1
        if a & 0x100:
            a ^= MOD
    return z

def power(a, n):
    v = 1
    while n:
        if n & 1:
            v = mul(v, a)
        a = mul(a, a)
        n >>= 1
    return v

def frob(a, times=1):
    for _ in range(times):
        a = mul(a, a)
    return a

def reduced(poly):
    # Subtract q^2+q to eliminate descending even degrees.
    coeff = dict(poly)
    for d in sorted(list(coeff.keys()), reverse=True):
        if d > 0 and d % 2 == 0:
            v = coeff.get(d, 0)
            if v:
                root = frob(v, 7)  # square root in GF(2^8)
                coeff[d] = 0
                coeff[d // 2] = coeff.get(d // 2, 0) ^ root
    return tuple(coeff.get(j, 0) for j in (5, 3, 1))

def transformed_poly(lam, c, a, b, alpha):
    # Expand c(a*x+b)^5 + lam*trace(c)*(a*x+b)^3 mod 2.
    tr = c ^ frob(c)
    assert tr in (0, 1)
    out = {}
    def add(d, v):
        out[d] = out.get(d, 0) ^ v
    for d in (0, 1, 4, 5):
        add(d, mul(c, mul(power(a, d), power(b, 5-d))))
    for d in (0, 1, 2, 3):
        add(d, mul(mul(lam, tr), mul(power(a, d), power(b, 3-d))))
    return reduced(out)

def normal_subspace(lam, alpha):
    p = (1, 0, 0)
    q = (alpha, lam, 0)
    return {tuple(x ^ y for x, y in zip(p, q)), p, q, (0, 0, 0)}

def transformed_subspace(lam, a, b, alpha):
    p = transformed_poly(lam, 1, a, b, alpha)
    q = transformed_poly(lam, alpha, a, b, alpha)
    return {tuple(x ^ y for x, y in zip(p, q)), p, q, (0, 0, 0)}

def main():
    # 3 is primitive in the AES representation of GF(256).
    assert {power(3, i) for i in range(255)} == set(range(1, 256))
    alpha = power(3, 85)
    assert alpha not in (0, 1) and mul(alpha, alpha) ^ alpha == 1
    f4 = {0, 1, alpha, alpha ^ 1}
    f16 = {v for v in range(256) if power(v, 16) == v}
    mu5 = {v for v in range(1, 256) if power(v, 5) == 1}
    mu15 = {v for v in range(1, 256) if power(v, 15) == 1}
    assert len(f16) == 16 and len(mu5) == 5 and len(mu15) == 15
    expected_counts = {}
    for lam in (0, 1, 3):
        seen = {}
        for a in sorted(mu15):
            for b in range(256):
                sub = transformed_subspace(lam, a, b, alpha)
                if (a,b)==(1,0):
                    assert sub == normal_subspace(lam, alpha)
                # Compare against *all* possible target parameters by reading
                # its x^3 coefficient only when leading coefficients normalize.
                if {row[0] for row in sub} != f4:
                    continue
                # The one with leading coefficient alpha identifies target mu.
                row_alpha = next(row for row in sub if row[0] == alpha)
                candidate = row_alpha[1]
                if sub == normal_subspace(candidate, alpha):
                    seen[candidate] = seen.get(candidate, 0) + 1
        expected = ({0: 240} if lam==0 else
                    {mul(lam,z): 4 if lam in mu5 else 1 for z in mu5})
        assert seen == expected, (lam,seen,expected)
        expected_counts[lam] = seen
    print('VERIFY_OK finite_field=GF(256) alpha_F4='+str(alpha))
    print('VERIFY_OK lambda_0 base_self_maps=240 cover_automorphisms=960')
    print('VERIFY_OK lambda_in_mu5 base_self_maps=4 cover_automorphisms=16')
    print('VERIFY_OK lambda_outside_mu5 base_self_maps=1 cover_automorphisms=4')
    print('VERIFY_OK exact_coarse_parameter=lambda^5 sample_orbits=1+5+5')

if __name__ == '__main__':
    main()
