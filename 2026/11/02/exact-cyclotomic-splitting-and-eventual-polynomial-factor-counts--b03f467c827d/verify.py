#!/usr/bin/env python3
"""Exact orbit checks for binomials with root-of-unity constant term.

All arithmetic is integral.  No symbolic factorization or external packages needed.
"""
from math import gcd, lcm


def valuations(n):
    ans = {}
    p = 2
    while p*p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            ans[p] = e
        p = p+1 if p == 2 else p+2
    if n > 1:
        ans[n] = 1
    return ans


def euler_primepower(p, e):
    return 1 if e == 0 else (p - 1)*p**(e - 1)


def cyclotomic_formula(m, M, d, n):
    assert M % m == 0 and d >= 2 and n >= 1
    vm = valuations(m)
    vM = valuations(M)
    result = 1
    for p, b in valuations(d).items():
        f = vm.get(p, 0)
        E = vM.get(p, 0)
        L = n*b
        if f:
            result *= p**min(E-f, L)
        else:
            result *= p**min(E, L) + max(L-E, 0)*euler_primepower(p, E)
    return result


def galois_orbits(m, d, n, base_modulus, allowed, alpha_exponent=1):
    """Count orbits on all roots of X^(d^n)-zeta_m^a under Gal(Q(zeta_L)/K).

    `allowed(u)` describes the congruence subgroup fixing the base field K.
    This is a separate direct enumerator, not the closed-form proof.
    """
    D = d**n
    L = lcm(base_modulus, m*D)
    assert gcd(alpha_exponent, m) == 1
    target = (alpha_exponent * (L // m)) % L
    roots = {t for t in range(L) if (D*t - target) % L == 0}
    units = [u for u in range(L) if gcd(u, L) == 1 and allowed(u)]
    assert len(roots) == D and units
    count = 0
    while roots:
        t = next(iter(roots))
        orbit = {u*t % L for u in units}
        assert orbit <= roots
        roots.difference_update(orbit)
        count += 1
    return count


def main():
    tests = 0
    for m in (1,2,3,4,5,6,8,10,12):
        for M in (m,2*m,3*m,4*m,6*m,8*m):
            for d in (2,3,4,6,10,12):
                for n in (1,2):
                    if m * d**n > 1000:
                        continue
                    observed = galois_orbits(m,d,n,M,
                        lambda u, M=M: u % M == 1 % M)
                    expected = cyclotomic_formula(m,M,d,n)
                    assert observed == expected, (m,M,d,n,observed,expected)
                    tests += 1
    assert tests == 624
    # Q(sqrt(5)) is the quadratic subfield of Q(zeta_5).
    # Its stabilizer in Gal(Q(zeta_L)/Q) consists of u mod 5 in {1,4}.
    for n in (1,2,3):
        observed = galois_orbits(2,10,n,10,lambda u: u % 5 in (1,4))
        assert observed == 2*n+1, (n,observed)
    # Q(sqrt(-15)) is the joint quadratic-character subfield of Q(zeta_15).
    # Its splitting can depend on *both* 3- and 5-power support at once.
    def chi_minus_15(u):
        chi3 = 1 if u % 3 == 1 else -1
        chi5 = 1 if u % 5 in (1,4) else -1
        return chi3*chi5
    for n in (1,2,3):
        observed = galois_orbits(1,15,n,15,lambda u: chi_minus_15(u)==1)
        assert observed == (n+1)**2+n*n
    # The count is unchanged if the chosen primitive target root changes.
    for m,M,d,n,a in ((5,5,6,2,2),(5,20,2,2,2),
                       (3,12,10,2,2),(8,8,3,3,3),(10,20,3,2,3)):
        observed = galois_orbits(m,d,n,M,
            lambda u,M=M: u % M == 1 % M, alpha_exponent=a)
        assert observed == cyclotomic_formula(m,M,d,n)
    # A cyclotomic example has a genuine initial transient, then a polynomial.
    for n in range(1,7):
        assert cyclotomic_formula(2,24,6,n) == 2**min(2,n)*(2*n+1)
        assert cyclotomic_formula(2,8,6,n) == 2**min(2,n)*(n+1)
    print('VERIFY_OK independent_cyclotomic_orbits=', tests,
          'quadratic_subfield_orbits=6', 'nonstandard_targets=5', 'closed_formula=PASS',
          'transient_and_eventual_polynomial=PASS')

if __name__ == '__main__':
    main()
