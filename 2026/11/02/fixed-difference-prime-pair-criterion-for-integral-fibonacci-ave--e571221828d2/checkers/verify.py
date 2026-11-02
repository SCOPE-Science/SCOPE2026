"""Reproduce exact Fibonacci-sum residues for odd-prime pairs with even gaps."""
from math import isqrt


def primes_upto(bound):
    marks = bytearray(b'\x01') * (bound + 1)
    marks[:2] = b'\x00\x00'
    for p in range(2, isqrt(bound) + 1):
        if marks[p]:
            marks[p*p::p] = b'\x00' * ((bound - p*p)//p + 1)
    return [p for p, good in enumerate(marks) if good]


def fib_exact(n):
    if n < 0:
        return (-1)**(-n+1) * fib_exact(-n)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_pair_mod(n, modulus):
    if n == 0:
        return 0, 1
    a, b = fib_pair_mod(n // 2, modulus)
    c = a * (2 * b - a) % modulus
    d = (a*a+b*b) % modulus
    return (d, (c+d) % modulus) if n % 2 else (c, d)


def local_prediction(p,q):
    gap=q-p
    A = fib_exact(gap-3)-1  # gap even >= 4; gap=2 handled separately
    if gap == 2:
        A=0
    B = fib_exact(gap+3)-1
    p_inert = p % 5 in (2, 3)
    q_split = q % 5 in (1, 4)
    rp = A if p_inert else B
    rq = A if q_split else B
    return rp % p, rq % q, (rp%p == 0 and rq%q == 0)


def check():
    prime_list=primes_upto(6000)
    prime_set=set(prime_list)
    trials=0
    hits=[]
    for p in prime_list:
        if p<=5: continue
        for d in range(2, 142, 2):
            q=p+d
            if q not in prime_set: continue
            np=p*q
            actual = (fib_pair_mod(np+2, np)[0]-1) % np
            ap, aq, expect=local_prediction(p,q)
            assert (actual %p,actual%q)==(ap,aq),(p,q,actual,ap,aq)
            assert (actual == 0)==expect,(p,q)
            if d in (2,4):
                assert expect == (p%5 == 2),(p,q)
            if d>=6:
                assert (not expect) or p<=fib_exact(d+3)-1,(p,q)
            trials+=1
            if expect: hits.append((p,q))
    assert (7,11) in hits and (17,19) in hits and (11,29) in hits
    assert (37,41) in hits and (151,199) in hits
    print('VERIFY_OK checked_prime_pairs=',trials,'positive_pairs=',len(hits),'notable=',[(p,q) for p,q in hits if (p,q) in {(7,11),(17,19),(11,29),(37,41),(151,199)}], 'exact_arithmetic=yes',sep='')

if __name__=='__main__':
    check()
