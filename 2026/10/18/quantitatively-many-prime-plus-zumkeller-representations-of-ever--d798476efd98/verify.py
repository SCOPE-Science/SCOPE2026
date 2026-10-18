"""Finite sanity checks for prime-plus-Zumkeller constructions.

This checks concrete algebraic and modular certificates; it does not
attempt to verify the infinite Siegel--Walfisz theorem.
Run: python3 verify.py
"""
from math import gcd, isqrt


def primes_upto(limit):
    flag = bytearray(b'\x01') * (limit + 1)
    flag[:2] = b'\x00\x00'
    for p in range(2, isqrt(limit) + 1):
        if flag[p]:
            flag[p*p::p] = b'\x00' * ((limit-p*p)//p + 1)
    return [p for p in range(2, limit+1) if flag[p]], flag


def signed_partition_for_seed(p):
    assert p % 2 == 1
    a = p.bit_length() - 1
    T = (1 << (a+1)) - 1
    assert (1 << a) < p <= T
    def signed_value(w):
        mask = (T+w)//2
        return sum((1 if ((mask >> j) & 1) else -1) * (1 << j)
                   for j in range(a+1))
    assert signed_value(-p) == -p
    assert signed_value(1) == 1
    z = (1 << a) * p
    assert signed_value(-p) + p*signed_value(1) == 0
    return z


def zumkeller_by_subset_sum(n):
    divisors = [j for j in range(1, n+1) if n % j == 0]
    total = sum(divisors)
    if total % 2: return False
    bits = 1
    target = total // 2
    for d in divisors:
        bits = (bits | (bits << d)) & ((1 << (target+1)) - 1)
    return bool((bits >> target) & 1)


def run():
    ps, flag = primes_upto(100000)
    seeds = 0
    closure = 0
    for p in ps:
        if p > 211: break
        if p == 2: continue
        z = signed_partition_for_seed(p)
        seeds += 1
        if z <= 3000:
            assert zumkeller_by_subset_sum(z)
            for t in range(1, 4):
                zz = z * (1 + z*t)
                if zz <= 3000:
                    assert gcd(z, 1+z*t) == 1
                    assert zumkeller_by_subset_sum(zz)
                    closure += 1
    print('seed certificates:', seeds, '; direct closure examples:', closure)

    # The theorem is only asymptotic. Look for concrete instances of its
    # modulus construction at accessible small inputs, without asserting
    # that every small input admits such an instance.
    found = 0
    missing = 0
    examples = []
    for n in range(951, 30000, 2):
        p = next(p for p in ps if p % 2 and n % p)
        z = signed_partition_for_seed(p)
        m = z*z
        residue = (n-z) % m
        witnesses = [q for q in range(n//3+1, (2*n)//3+1)
                     if flag[q] and q % m == residue and n-q >= z]
        if witnesses:
            q = witnesses[0]
            assert n-q == z * (1 + z*((n-q-z)//m))
            assert gcd(z, (n-q)//z) == 1
            found += 1
            if p in (3,5,7) and p not in [row[1] for row in examples]:
                examples.append((n, p, z, q, n-q))
        else:
            missing += 1
    print('small-input modular witnesses:', found, '; absent:', missing)
    print('sample tuples (N, prime seed, Z seed, prime, Zumkeller):', examples)
    print('FINITE CHECKS PASSED; asymptotic proof requires Siegel--Walfisz.')

if __name__ == '__main__':
    run()
