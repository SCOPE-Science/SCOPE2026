"""Independent finite consistency checks for divisor-sum coefficient content.

Proof of the universal identity is in RESULT.md, not established by this program.
"""
from math import gcd


def sigma_via_divisors(n, k):
    return sum(d**k for d in range(1, n + 1) if n % d == 0)


def sigma_via_factors(n, k):
    x, ans, p = n, 1, 2
    while p*p <= x:
        if x % p == 0:
            term, power = 1, 1
            while x % p == 0:
                x //= p
                power *= p**k
                term += power
            ans *= term
        p += 1
    if x > 1:
        ans *= 1+x**k
    return ans


def coeff(n, k, l, sigma):
    return (n**l+1)*sigma(n,k)-(n**k+1)*sigma(n,l)


def prime_factors(n):
    p, facts = 2, {}
    while p*p <= n:
        while n % p == 0:
            facts[p] = facts.get(p,0)+1
            n //= p
        p += 1
    if n > 1: facts[n] = facts.get(n,0)+1
    return facts


def is_prime(p):
    return p > 1 and not any(p % d == 0 for d in range(2, int(p**0.5)+1))


def primitive_content(k, l):
    t=l-k
    assert k >= 1 and l > k
    e2 = min(k, 1 if t % 2 else 2 + prime_factors(t).get(2,0))
    out = 2**e2
    for p in range(3,t+2,2):
        if is_prime(p) and t%(p-1)==0:
            out *= p**min(k,1+prime_factors(t).get(p,0))
    return out


def run():
    tested = 0
    for k in range(1, 9):
        for l in range(k+1, 13):
            predicted = primitive_content(k,l)
            g=0
            for n in range(2,181):
                a = coeff(n,k,l,sigma_via_divisors)
                b = coeff(n,k,l,sigma_via_factors)
                assert a==b,(n,k,l,a,b)
                assert a%predicted==0,(n,k,l,a,predicted)
                g = gcd(g,a)
            assert g==predicted,(k,l,g,predicted)
            tested += 1
    k,l=3,7
    observed={n:coeff(n,k,l,sigma_via_factors) for n in (4,6,22)}
    assert observed == {4: 122760,6: 9295440,22: 3132424966320}, observed
    assert gcd(*observed.values())==120
    for p in (2,3,5,7,11,13):
        for k,l in ((1,2),(1,3),(3,7),(4,12)):
            computed=coeff(p*p,k,l,sigma_via_divisors)
            expected = (p**k-p**l)*(1-p**(k+l))
            assert computed==expected,(p,k,l,computed,expected)
    print(f'VERIFY_OK families={tested} sample_coefficients={tested*179} two_methods=yes gcds_agree=yes prime_square_identity=24 f_3_7_content=120')
    print('VERIFICATION_LIMIT finite data only; infinite equality follows from the documented proof')

if __name__ == '__main__':
    run()
