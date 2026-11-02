"""Exact arithmetic checks for the Ma-Wang infinity-point gap-weight identity.

The finite tests check algebraic and arithmetic premises; the infinite theorem
uses the separate proof by Kummer valuations, genus and Dedekind reciprocity.
Run: python3 verify.py
"""
from fractions import Fraction
from math import gcd


def parameters(q, n):
    assert q >= 3 and n >= 4 and n % 2 == 0
    N = q ** n + 1
    r = (q ** (n - 1) - 1) // (q - 1)
    b = q * (q - 1)
    assert N == b * r + q + 1
    assert r % (q + 1) == 1
    assert gcd(N, r) == 1
    return N, r, b


def polynomial_weight(q, n):
    d = q ** n
    A = q**5 - q**4 + 2*q*q - 3*q - 1
    B = 2*q**6 + 2*q**5 - 2*q**4 - 8*q**3 - 10*q*q + 10*q + 10
    C = 2*q**6 - 2*q**5 - 2*q**4
    top = A*d*d + B*d + C
    assert top % (24*(q+1)) == 0
    return top // (24*(q+1))


def dedekind_sum(q, n, N, r):
    actual = sum((Fraction(j, N)-Fraction(1, 2)) *
                 (Fraction((r*j) % N, N)-Fraction(1, 2))
                 for j in range(1, N))
    b = q*(q-1); c = q+1
    predicted = (Fraction(b) + Fraction(r, N)-Fraction(r, c) +
                 Fraction(1, N*r)-Fraction(1, c*r) +
                 Fraction((c-1)*(c-2), c))/12
    assert actual == predicted, (q, n, actual, predicted)
    return actual


def check_case(q, n, check_dedekind=False):
    N, r, b = parameters(q, n)
    w = [q*j + b*((r*j) % N) for j in range(N)]
    assert all(x >= 0 and x % N == (-j) % N for j, x in enumerate(w))
    assert len({x % N for x in w}) == N
    g = (q*q-1)*(N-1)//2
    assert sum(w) == N*(g + (N-1)//2) if N % 2 else 2*sum(w) == N*(2*g+N-1)
    # Here residue a_j=(-j) mod N, and w_j=a_j+N*h_j.
    gaps = 0
    gap_sum = 0
    for x in w:
        a = x % N
        h = (x-a)//N
        assert h >= 0
        gaps += h
        gap_sum += h*a + N*h*(h-1)//2
    assert gaps == g, (q,n,gaps,g)
    weight = gap_sum - g*(g+1)//2
    assert weight == polynomial_weight(q,n), (q,n,weight,polynomial_weight(q,n))
    kstar = q*r//(q+1)
    conductor = (q*q-1)*(N-1)-b*kstar
    assert max(w)-N+1 == conductor
    assert 2*g-conductor == b*kstar > 0
    if check_dedekind:
        dedekind_sum(q,n,N,r)
    return g, conductor, weight


def main():
    checks = 0
    for q in (3, 4, 5, 7, 8, 9, 11):
        for n in (4, 6):
            N, _, _ = parameters(q,n)
            if N > 250000:
                continue
            check_case(q,n,check_dedekind=(N<=5000))
            checks += 1
    assert check_case(3, 4, check_dedekind=True) == (324, 594, 12906)
    assert check_case(4, 4, check_dedekind=True) == (1920, 3648, 449280)
    assert check_case(5, 4, check_dedekind=True) == (7500, 14500, 7026250)
    print('VERIFY_OK: %s distinct parameter pairs; exact gap genus, conductor and weight; Dedekind checks at small degrees' % checks)

if __name__ == '__main__':
    main()
