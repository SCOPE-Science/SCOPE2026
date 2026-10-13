#!/usr/bin/env python3
LIMIT = 1_000_000

spf = list(range(LIMIT + 2))
spf[0] = 0
spf[1] = 1
p = 2
while p * p <= LIMIT + 1:
    if spf[p] == p:
        for m in range(p*p, LIMIT + 2, p):
            if spf[m] == m:
                spf[m] = p
    p += 1

def factorization(n):
    out = {}
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out[p] = e
    return out

def uphi(n):
    out = 1
    for p,e in factorization(n).items():
        out *= p**e - 1
    return out

def omega(n):
    return len(factorization(n))

def Omega(n):
    return sum(factorization(n).values())

def is_prime_power_odd(x):
    if x <= 1 or x % 2 == 0 or x >= len(spf):
        return False
    return len(factorization(x)) == 1

def reconstruct(n):
    assert omega(n) == omega(n+1) == 2
    assert uphi(n) == uphi(n+1)
    if n % 2 == 0:
        even, odd, orient = n, n+1, 'L'
    else:
        odd, even, orient = n, n+1, 'R'
    fe = factorization(even)
    a = fe[2]
    A = 2**a
    B = even // A
    odd_blocks = sorted(p**e for p,e in factorization(odd).items())
    C,D = odd_blocks
    assert is_prime_power_odd(B)
    assert is_prime_power_odd(C) and is_prime_power_odd(D)
    if orient == 'L':
        u = A-C
        v = D-A
        assert u > 0 and v > 0 and u*v == A-1
        assert B == A-1+v-u
        branch = 'L'
    else:
        t = B-A-1
        assert t != 0
        if t > 0:
            u = C-A
            v = D-A
            assert 1 <= u < v and u*v == A-1
            assert B == A+1+u+v
            branch = 'R+'
        else:
            u = A-D
            v = A-C
            assert 1 <= u < v and u*v == A-1
            assert B == A+1-u-v
            branch = 'R-'
    return (branch,A,B,C,D,u,v)

hits = []
for n in range(2, LIMIT):
    if omega(n) == 2 and omega(n+1) == 2 and uphi(n) == uphi(n+1):
        hits.append(n)

assert hits == [20,35,143,208,2623,5183], hits
expected = {
    20:   ('L', 4,5,3,7,1,3),
    35:   ('R+',4,9,5,7,1,3),
    143:  ('R-',16,9,11,13,3,5),
    208:  ('L',16,13,11,19,5,3),
    2623: ('R-',64,41,43,61,3,21),
    5183: ('R+',64,81,71,73,7,9),
}
for n in hits:
    assert reconstruct(n) == expected[n], (n,reconstruct(n))

low = [n for n in hits if Omega(n) <= 3 and Omega(n+1) <= 3]
assert low == [20]

# Generate every branch whose resulting pair stays in the direct-search window.
generated = set()
A = 2
while A <= LIMIT:
    M = A-1
    for u in range(1, int(M**0.5)+1):
        if M % u:
            continue
        v0 = M//u
        ordered = [(u,v0)] if u == v0 else [(u,v0),(v0,u)]
        for x,y in ordered:
            B = A-1+y-x
            C = A-x
            D = A+y
            if B > 1 and C > 1 and D > C and is_prime_power_odd(B) and is_prime_power_odd(C) and is_prime_power_odd(D):
                n = A*B
                if n < LIMIT and n+1 == C*D and omega(n) == omega(n+1) == 2:
                    assert uphi(n) == uphi(n+1)
                    generated.add(n)
        if u < v0:
            x,y = u,v0
            B = A+1+x+y
            C = A+x
            D = A+y
            if is_prime_power_odd(B) and is_prime_power_odd(C) and is_prime_power_odd(D):
                n = C*D
                if n < LIMIT and n+1 == A*B and omega(n) == omega(n+1) == 2:
                    assert uphi(n) == uphi(n+1)
                    generated.add(n)
            B = A+1-x-y
            C = A-y
            D = A-x
            if B > 1 and C > 1 and D > C and is_prime_power_odd(B) and is_prime_power_odd(C) and is_prime_power_odd(D):
                n = C*D
                if n < LIMIT and n+1 == A*B and omega(n) == omega(n+1) == 2:
                    assert uphi(n) == uphi(n+1)
                    generated.add(n)
    A *= 2

assert generated == set(hits), (sorted(generated), hits)
print('VERIFY_OK', f'range=2..{LIMIT-1}', f'hits={hits}', f'low_Omega={low}', f'branches={[expected[n][0] for n in hits]}')
