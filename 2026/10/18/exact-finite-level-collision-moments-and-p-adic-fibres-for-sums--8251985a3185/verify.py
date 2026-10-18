"""Exact arithmetic checks for the local two-cube fibre and collision laws."""
from fractions import Fraction


def exact_residue(p, n):
    modulus = p ** n
    cubes = [0] * modulus
    for x in range(modulus):
        cubes[pow(x, 3, modulus)] += 1
    nonzero = [(i, multiplicity) for i, multiplicity in enumerate(cubes) if multiplicity]
    counts = [0] * modulus
    for a, ra in nonzero:
        for b, rb in nonzero:
            counts[(a+b) % modulus] += ra * rb
    assert sum(counts) == modulus ** 2
    return counts


def moment_formula(p, n, r1):
    assert p >= 5 and p % 2
    g = 3 if p % 3 == 1 else 1
    S = sum(r1[a] ** 2 for a in range(1, p))
    expected = (p-1)*(p*p - 2*p + 4) if g == 3 else (p-1)*p*p
    assert S == expected
    c = Fraction(g*(p-1), p)
    limit = Fraction(p*p + (7 if g == 3 else 1)*p + 1, p*p)
    moments = [Fraction(1),
               Fraction(S + (g*(p-1)+1)**2, p**3),
               Fraction(S, p**3) + c*c/p + (2*c+1)/p**2]
    while len(moments) <= n:
        moments.append((1-Fraction(1,p))*limit + moments[-3]/p)
    assert moments[n] == limit + (moments[n % 3]-limit)/p**(n//3)
    return moments[n]


def run_checks():
    total = 0
    for p, max_level in [(5,4), (7,4), (11,3), (13,3),
                         (17,3), (19,3), (31,2), (37,2)]:
        r1 = exact_residue(p, 1)
        lower = {0: [1]}
        g = 3 if p % 3 == 1 else 1
        for n in range(1, max_level+1):
            m = p**n
            if m > 2500:
                continue
            counts = r1 if n == 1 else exact_residue(p, n)
            lower[n] = counts
            actual = Fraction(sum(r*r for r in counts), m**3)
            predicted = moment_formula(p, n, r1)
            assert actual == predicted, (p, n, actual, predicted)
            if n >= 2:
                smooth = g*(p-1)*p**(n-1)
                for a, count in enumerate(counts):
                    if a % p:
                        expected = p**(n-1)*r1[a % p]
                    elif n == 2:
                        expected = smooth + (p*p if a % (p*p) == 0 else 0)
                    elif a % (p**3):
                        expected = smooth
                    else:
                        expected = smooth + p**4 * lower[n-3][(a // (p**3)) % p**(n-3)]
                    assert count == expected, (p, n, a, count, expected)
            total += 1
            print('prime',p,'level',n,'modulus',m,'moment',str(actual),'OK')
    print('VERIFICATION_OK', total, 'complete fibre distributions and collision moments')


if __name__ == '__main__':
    run_checks()
