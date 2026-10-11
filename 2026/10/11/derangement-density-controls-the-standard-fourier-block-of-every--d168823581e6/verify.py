from itertools import permutations
from fractions import Fraction


def derangements(n):
    d0, d1 = 1, 0
    if n == 0:
        return d0
    if n == 1:
        return d1
    a, b = d0, d1
    for m in range(2, n + 1):
        a, b = b, (m - 1) * (a + b)
    return b


def check_symmetric(n):
    G = list(permutations(range(n)))
    d = n - 1
    abs_sum = 0
    D = 0
    for p in G:
        f = sum(i == p[i] for i in range(n))
        chi = f - 1
        abs_sum += abs(chi)
        if f == 0:
            D += 1
    assert D == derangements(n)
    assert abs_sum == 2 * D
    pnorm = Fraction(d * abs_sum, len(G))
    expected = Fraction(2 * d * D, len(G))
    assert pnorm == expected
    # The complementary convolution kernel has value 1-d^2/|G| at e
    # and -d*chi(g)/|G| away from e.
    comp_num = len(G) - d * d + d * (abs_sum - d)
    comp = Fraction(comp_num, len(G))
    expected_comp = 1 + Fraction(2 * d * (D - d), len(G))
    assert comp == expected_comp
    return D, pnorm, comp


def check_affine_prime(p):
    # AGL(1,p): x -> a*x+b, a!=0. This action is sharply 2-transitive.
    elems = [(a, b) for a in range(1, p) for b in range(p)]
    d = p - 1
    D = 0
    abs_sum = 0
    values = []
    for a, b in elems:
        f = sum(((a * x + b) % p) == x for x in range(p))
        chi = f - 1
        values.append((a, b, f, chi))
        D += (f == 0)
        abs_sum += abs(chi)
    assert len(elems) == p * (p - 1)
    assert D == p - 1
    assert abs_sum == 2 * D
    pnorm = Fraction(d * abs_sum, len(elems))
    comp = 1 + Fraction(2 * d * (D - d), len(elems))
    assert pnorm == Fraction(2 * (p - 1), p)
    assert comp == 1
    # In the equality case the complementary kernel is uniform on the
    # Frobenius kernel: translations a=1.
    for a, b, f, chi in values:
        if a == 1 and b == 0:
            k = Fraction(1, 1) - Fraction(d * d, len(elems))
        else:
            k = -Fraction(d * chi, len(elems))
        assert (k == Fraction(1, p)) == (a == 1)
    return D, pnorm, comp


for n in range(2, 9):
    D, pn, cn = check_symmetric(n)
    print(f"S_{n}: D={D} P={pn} I-P={cn}")
for p in (3, 5, 7, 11):
    D, pn, cn = check_affine_prime(p)
    print(f"AGL(1,{p}): D={D} P={pn} I-P={cn}")
print("VERIFY_OK symmetric_n=2..8 affine_primes=3,5,7,11")
