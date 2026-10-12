"""Finite checks of a closed recurrence formula and constructive p-adic approximants.
These checks complement, but do not replace, the general proof in RESULT.md.
"""
from fractions import Fraction
from math import gcd


def vp(z, p):
    z = Fraction(z)
    if z == 0:
        return float('inf')
    numerator, denominator = abs(z.numerator), z.denominator
    v = 0
    while numerator % p == 0:
        v += 1
        numerator //= p
    while denominator % p == 0:
        v -= 1
        denominator //= p
    return v


def padic_mod(z, p, precision):
    z = Fraction(z)
    if vp(z, p) < 0:
        raise ValueError('expected a p-adic integer')
    mod = p ** precision
    den = z.denominator
    num = z.numerator
    while den % p == 0:
        assert num % p == 0
        den //= p
        num //= p
    return (num * pow(den, -1, mod)) % mod


count = 0
for a in range(-5, 6):
    for initial0 in range(-4, 5):
        for initial1 in range(-4, 5):
            D = initial1 - a * initial0
            prevprev, prev = initial0, initial1
            assert prev == D + a * initial0
            count += 1
            for n in range(2, 31):
                current = 2*a*prev - a*a*prevprev
                assert current == a**(n-1)*(a*initial0+n*D), (a, initial0, initial1, n)
                prevprev, prev = prev, current
print('recurrence_closed_formula_891_parameter_triples_to_n30=PASS')

# Witness approximation: choose d so that a^d tends to its p-adic limit;
# choose positive n in the desired congruence class, then check exact fraction.
examples = [
    (2, 1, 4, 2),  # p divides a and D; dense
    (3, 1, 6, 3),  # p divides a and D; dense
    (1, 2, 3, 2),  # a unit; dense
    (5, 0, 2, 3),  # c=0; dense
    (-1, 1, 0, 2), # negative root and positive D; dense
]
targets = [Fraction(-3), Fraction(0), Fraction(2), Fraction(1,3), Fraction(7,4)]
checked = 0
for a, initial0, initial1, p in examples:
    D = initial1 - a * initial0
    c = Fraction(a*initial0, D)
    assert vp(c, p) >= 0
    L = 0 if a % p == 0 else 1
    for target in targets:
        if target == L:
            # Obvious exact ratio 1, or zero as a limit, treated in symbolic proof.
            continue
        N = 4
        found = False
        for j in range(1, 12):
            d = j + N if a % p == 0 else (p-1) * p**j
            ad = a**d
            if target == ad:
                continue
            q = Fraction(d*ad, 1)/(target-ad)
            if vp(q, p) < 0 or vp(q-c, p) < 0:
                continue
            # Resolve the 4 p-adic digits of q-c as a positive integer n.
            prec_n = N + max(vp(q,p),0) + max(-vp(target-ad,p),0) + 1
            n = padic_mod(q-c, p, int(prec_n))
            if n == 0:
                n = p**int(prec_n)
            assert n >= 1
            denominator = a*initial0 + n*D
            if denominator == 0:
                continue
            actual = Fraction(a**d * (a*initial0+(n+d)*D), denominator)
            if vp(actual-target, p) >= N:
                found = True
                checked += 1
                break
        assert found, (a,initial0,initial1,p,target)
print(f'constructive_p_adic_approximations_precision_4={checked}_PASS')

# In nonintegral c cases, valuations of x_n have claimed rigidity.
rigidity = 0
for a in range(-5, 6):
    if a == 0:
        continue
    for initial0 in range(-4, 5):
        for initial1 in range(-4, 5):
            D = initial1 - a * initial0
            if D == 0:
                continue
            c = Fraction(a*initial0, D)
            for p in [2,3,5,7]:
                if vp(c, p) >= 0:
                    continue
                valuations = [vp(a**(n-1)*(a*initial0 + n*D), p) for n in range(1,31)]
                assert all(v == (n-1)*vp(a,p) + vp(a*initial0,p) for n,v in enumerate(valuations,1))
                rigidity += 1
print(f'nonintegral_shift_valuation_rigidity_cases={rigidity}_PASS')
print('VERIFY_OK')
