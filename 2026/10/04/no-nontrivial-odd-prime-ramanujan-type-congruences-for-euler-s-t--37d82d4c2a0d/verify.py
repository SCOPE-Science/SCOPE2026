#!/usr/bin/env python3
from math import gcd, isqrt

ODD_PRIMES = (3, 5, 7, 11, 13, 17, 19)
BOUND = 35

def isprime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def factor(n):
    out = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d; e += 1
            out.append((d,e))
        d = 3 if d == 2 else d + 2
    if n > 1:
        out.append((n,1))
    return out

def phi(n):
    ans = n
    for q,_ in factor(n):
        ans = ans // q * (q-1)
    return ans

def crt2(a,m,b,n):
    assert gcd(m,n) == 1
    return (a + ((b-a) * pow(m,-1,n) % n) * m) % (m*n)

def prime_in_class(a,m,start=2,avoid=None):
    a %= m
    k = max(0, (start-a + m-1)//m)
    while True:
        x = a + k*m
        if x >= 2 and x != avoid and isprime(x):
            return x
        k += 1
        assert k < 200000

def witness(p,A,B):
    assert p % 2 == 1 and isprime(p) and gcd(A,B) == 1
    if A % p != 0:
        u = 2
        if u == p:
            u = 3
        c = crt2(B % A if A > 1 else 0, A, u, p) if A > 1 else u
        q = prime_in_class(c, A*p, start=max(B,2))
        return q, 'prime'
    if B % p != 1:
        q = prime_in_class(B % A, A, start=max(B,2))
        return q, 'prime'

    # A = p^e C; choose u=2 (nonzero and not 1 for odd p).
    pe = 1
    temp = A
    while temp % p == 0:
        pe *= p
        temp //= p
    C = temp
    if C == 1:
        c = 2 % A
    else:
        c = crt2(2 % pe, pe, 1 % C, C)
    assert gcd(c,A) == 1
    d = (B * pow(c,-1,A)) % A
    assert gcd(d,A) == 1
    q = prime_in_class(c,A,start=max(A+1,3))
    r = prime_in_class(d,A,start=max(A+1,3),avoid=q)
    return q*r, 'semiprime'

def main():
    checked = 0
    prime_cases = 0
    hard_cases = 0
    max_witness = 0
    for p in ODD_PRIMES:
        for A in range(1,BOUND+1):
            for B in range(1,BOUND+1):
                if gcd(A,B) != 1:
                    continue
                m,kind = witness(p,A,B)
                assert m >= B and (m-B) % A == 0
                n = (m-B)//A
                assert n >= 0
                assert phi(m) % p != 0, (p,A,B,m,phi(m))
                if A % p == 0 and B % p == 1:
                    fs = factor(m)
                    assert kind == 'semiprime'
                    assert len(fs) == 2 and all(e == 1 for _,e in fs)
                    assert fs[0][0] != fs[1][0]
                    assert all(q % p != 1 for q,_ in fs)
                    hard_cases += 1
                else:
                    assert kind == 'prime' and isprime(m)
                    assert m % p != 1
                    prime_cases += 1
                checked += 1
                max_witness = max(max_witness,m)
    print('VERIFY_OK')
    print('coprime_progressions_checked=' + str(checked))
    print('prime_witness_cases=' + str(prime_cases))
    print('semiprime_exceptional_cases=' + str(hard_cases))
    print('max_witness=' + str(max_witness))

if __name__ == '__main__':
    main()
