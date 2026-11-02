"""Exact arithmetic verification of the stated finite CRT identities."""
from math import gcd, prod
from itertools import product


def prime_divisors(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            while n % d == 0:
                n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        ans.append(n)
    return ans


def eta(t):
    if t % 2 == 0:
        return 0
    return 1 if t % 4 == 3 else -1


def crt_terms(m):
    primes = prime_divisors(m)
    e0 = e1 = 0
    for assignment in product((0, 1, 2), repeat=len(primes)):
        a = prod(p for p, choice in zip(primes, assignment) if choice == 1)
        b = prod(p for p, choice in zip(primes, assignment) if choice == 2)
        mod = a*b
        if b == 1:
            rho = mod
        elif a == 1:
            rho = 1
        else:
            rho = a * pow(a, -1, b)
        assert 1 <= rho <= mod
        assert rho % a == 0 and (rho - 1) % b == 0
        sign = -1 if sum(assignment_i != 0 for assignment_i in assignment) % 2 else 1
        e0 += sign * (1 if rho % 2 else -1)
        e1 += sign * (eta(rho) + eta(rho + mod))
    S = m
    for p in primes:
        S = S // p * (p-2)
    return S, e0, e1


def exact_T(n):
    assert n >= 1
    if n == 1:
        return 0
    e = 0
    m = n
    while m % 2 == 0:
        e += 1
        m //= 2
    if m == 1 and e == 1:
        return 0
    S, E0, E1 = crt_terms(m)
    if e == 0:
        assert (S + E0) % 2 == 0
        return (S + E0)//2
    if e == 1:
        assert (S + E1) % 2 == 0
        return (S + E1)//2
    return (2**(e-2))*S


def direct_T(n):
    if n == 1:
        return 0
    return sum(gcd(t, n) == 1 and gcd((t-1)//2, n) == 1
               for t in range(1, n + 1, 2))


def check():
    for n in range(1, 2001):
        assert exact_T(n) == direct_T(n), (n, exact_T(n), direct_T(n))
    for m in range(3, 1000, 2):
        S, E0, E1 = crt_terms(m)
        R = prod(prime_divisors(m))
        _, F0, F1 = crt_terms(R)
        assert (E0, E1) == (F0, F1), m
        # Count admissible residues to verify the two parity biases directly.
        F = lambda r: gcd(r * (r-1), m) == 1
        assert E0 == sum((1 if r % 2 else -1) for r in range(1,m+1) if F(r)), m
        assert E1 == sum(eta(r) for r in range(1,2*m+1) if F(r)), m
    primes = [p for p in range(3, 100) if prime_divisors(p) == [p]]
    for p in primes:
        for q in primes:
            if p == q: continue
            u = pow(p, -1, q)
            S, E0, _ = crt_terms(p*q)
            assert E0 == (-1 + 2 * (1 if u % 2 else -1)), (p,q,E0,u)
    print('PASS: 2,000 direct T checks, 499 radical/parity checks, and all prime-pair branch checks under 100')

if __name__ == '__main__':
    check()
