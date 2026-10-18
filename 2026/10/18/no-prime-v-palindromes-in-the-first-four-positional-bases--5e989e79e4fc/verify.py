#!/usr/bin/env python3
"""Exact auxiliary finite checks for the four-base prime-v-palindrome theorem.

The infinite theorem is proved by elementary inequalities in RESULT.md;
this checker independently exhausts only its listed small-prime exceptions.
No third-party packages are needed.
"""


def prime(n):
    if n < 2:
        return False
    t = 2
    while t*t <= n:
        if n % t == 0:
            return False
        t += 1
    return True


def val(n):
    total = 0
    q = 2
    while q*q <= n:
        if n % q == 0:
            e = 0
            while n % q == 0:
                n //= q
                e += 1
            total += q + (e if e > 1 else 0)
        q += 1
    if n > 1:
        total += n
    return total


def reverse(n, b):
    out = 0
    while n:
        out = out*b + n % b
        n //= b
    return out


def check():
    thresholds = {2:8, 3:9, 4:64, 5:25}
    exceptions = {2:[3,5,7], 3:[2,5,7],
                  4:[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61],
                  5:[2,3,7,11,13,17,19,23]}
    finite_count = 0
    bound_count = 0
    for base, limit in thresholds.items():
        ps = [n for n in range(2,limit) if prime(n) and n % base]
        assert ps == exceptions[base], (base,ps)
        finite_count += len(ps)
        for p in ps:
            r = reverse(p,base)
            assert p == r or val(r) != p, (base,p,r,val(r))
            print('finite',base,p,r,val(r),int(p==r))
    assert reverse(37,4)==22 and val(22)==13
    assert reverse(19,4)==49 and val(49)==9
    # A distinct exhaustive cross-check, not part of the infinite proof.
    for base in range(2,6):
        for p in range(2,40000):
            if prime(p) and p % base:
                r = reverse(p,base)
                assert r == p or val(r) != p, (base,p,r)
    # Check the component estimates on a complete finite range.
    for n in range(4,10001):
        if prime(n):
            continue
        bound_count += 1
        q = next(p for p in range(2,n+1) if n % p == 0 and prime(p))
        assert val(n) <= q+n//q, (n,q,val(n))
        if n%2:
            assert val(n) <= n/3+3
        if n%2 and n%3:
            assert val(n) <= n/5+5
    print(f'VERIFIED four bases; {finite_count} small primes, all primes below 40000 per base, {bound_count} composite bounds')


if __name__ == '__main__':
    check()
