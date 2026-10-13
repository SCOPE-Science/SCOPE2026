from fractions import Fraction
from math import isqrt

def isprime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d=3
    while d*d <= n:
        if n%d==0: return False
        d+=2
    return True

def sigma_prime_power(p,e):
    return (p**(e+1)-1)//(p-1)

assertions=0
primes=[q for q in range(3,200) if isprime(q)]
for q in primes:
    for b in range(3,14,2):
        S=sigma_prime_power(q,b)
        H=sigma_prime_power(q,b+1)
        target=Fraction(S+1,q**b)
        iq=Fraction(H,q**(b+1))
        rhs=Fraction(1,1)+Fraction(q-1,H)
        assert target/iq == rhs
        assertions += 1
        assert S*S > H
        assertions += 1
        assert S > q
        assertions += 1
        # The proof's key size contradiction: every p >= S and every even exponent >=2
        # has p^(2a) > H, so it cannot divide H.
        for a in (1,2,3):
            assert S**(2*a) > H
            assertions += 1

# Direct finite regression over small q,b,p,a: the forbidden minimal layer never
# realizes the target abundancy ratio.
direct=0
for q in [q for q in range(3,44) if isprime(q)]:
    for b in (3,5):
        S=sigma_prime_power(q,b)
        target=Fraction(S+1,q**b)
        for p in [p for p in range(q+2,5000) if isprime(p)]:
            if p < S:
                continue
            for a in (1,2,3):
                nratio=Fraction(sigma_prime_power(q,b+1),q**(b+1))*Fraction(sigma_prime_power(p,2*a),p**(2*a))
                assert nratio != target
                direct += 1

print(f"VERIFY_OK assertions={assertions} direct_forbidden_checks={direct}")
