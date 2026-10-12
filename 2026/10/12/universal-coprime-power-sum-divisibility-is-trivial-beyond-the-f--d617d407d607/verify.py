"""Exact rational checks for coprime-residue power-sum divisor obstruction.

Python 3 standard library only. Finite checks corroborate an unrestricted proof.
"""
from fractions import Fraction
from math import comb, gcd


def bernoulli_up_to(N):
    b = [Fraction(1)]
    for n in range(1, N + 1):
        b.append(-sum(Fraction(comb(n + 1, j)) * b[j]
                      for j in range(n)) / (n + 1))
    return b


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n**.5) + 1):
        if n % d == 0:
            return False
    return True


def small_good_prime(m, B):
    index = m if m % 2 == 0 else m - 1
    n = m + 3
    while not (is_prime(n) and B[index].numerator % n != 0):
        n += 1
    return n


def fpoly(m, p, B):
    # Coefficient-by-degree for F_{m,p}(X)=S_m(X)-p^m S_m(X/p).
    a = {}
    for j in range(m + 1):
        if j == 1:
            continue
        v = Fraction(comb(m + 1, j), m + 1) * B[j]
        v *= (1 - Fraction(p)**(j-1))
        if v:
            a[m + 1 - j] = v
    return a


def valuation_p(q, p):
    if not q:
        return 999
    num, den = abs(q.numerator), q.denominator
    v = 0
    while num % p == 0:
        num //= p
        v += 1
    while den % p == 0:
        den //= p
        v -= 1
    return v


def polyeval(P, n):
    return sum(c * n**d for d, c in P.items())


def phi_power(m, n):
    return sum(a**m for a in range(1, n + 1) if gcd(a, n) == 1)


def divmod_poly(A, B):
    R = dict(A)
    q = {}
    bd = max(B)
    while R and max(R) >= bd:
        d = max(R) - bd
        t = R[max(R)] / B[bd]
        q[d] = q.get(d, Fraction(0)) + t
        for j, c in B.items():
            e = j + d
            R[e] = R.get(e, Fraction(0)) - t*c
            if not R[e]:
                del R[e]
    return q, R


def main():
    B = bernoulli_up_to(21)
    tests = 0
    primes_used = {}
    H = {}
    for m in range(2, 21):
        p = small_good_prime(m, B)
        primes_used[m] = p
        F = fpoly(m, p, B)
        h = 1 if m % 2 == 0 else 2
        assert min(F) == h and max(F) == m + 1
        assert F[m + 1] == Fraction(p-1, p*(m+1))
        expected_low = B[m] * (1 - p**(m-1)) if m % 2 == 0 else Fraction(m, 2)*B[m-1]*(1-p**(m-2))
        assert F[h] == expected_low
        E = {d - h: p*c for d,c in F.items()}
        assert valuation_p(E[max(E)],p) == 0
        assert valuation_p(E[0],p) == 1
        assert all(valuation_p(c,p) >= 1 for d,c in E.items() if d != max(E))
        H[m] = {d-h:c for d,c in F.items()}
        for a in (1,2):
            n = p**a
            assert polyeval(F,n) == phi_power(m,n)
            tests += 1
    pairs = 0
    for s in range(2,20):
        for k in range(s+1,21):
            p = k + 3
            es = s if s % 2 == 0 else s - 1
            ek = k if k % 2 == 0 else k - 1
            while not (is_prime(p) and B[es].numerator % p != 0
                       and B[ek].numerator % p != 0):
                p += 1
            Fs=fpoly(s,p,B); Fk=fpoly(k,p,B)
            hs=1 if s%2==0 else 2
            hk=1 if k%2==0 else 2
            Hs={d-hs:c for d,c in Fs.items()}
            Hk={d-hk:c for d,c in Fk.items()}
            assert not divmod_poly(Hk,Hs)[1] == {}, (s,k,p)
            pairs += 1
    assert pairs == 171
    print('VERIFY_OK')
    print('exponents_checked=2..20')
    print('prime_power_integer_identity_checks=%d' % tests)
    print('eisenstein_profiles_checked=19')
    print('distinct_exponent_nondivisibility_pairs=%d' % pairs)
    print('admissible_primes_by_exponent=' + ','.join('%d:%d'%(m,p) for m,p in primes_used.items()))
    print('exact_rational_checks=PASS')
    print('scope=finite_regression_only; unrestricted_result_requires_proof')


if __name__ == '__main__':
    main()
