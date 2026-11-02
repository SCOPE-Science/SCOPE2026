#!/usr/bin/env python3
"""Independent finite checks for Lie complexity of the period-doubling word.

This code is auxiliary evidence only; the all-length proof is combinatorial.
Requires only Python 3 standard library. Run: python3 verify.py
"""

def mu(w):
    return ''.join('01' if x == '0' else '00' for x in w)


def word(k):
    p = '0'
    for _ in range(k):
        p = mu(p)
    return p


def arithmetic_prefix(n):
    a = []
    for i in range(n):
        x = i + 1
        v = 0
        while x % 2 == 0:
            x //= 2
            v += 1
        a.append(str(v % 2))
    return ''.join(a)


def cyclic_class(w):
    return {w[i:] + w[:i] for i in range(len(w))}


def necklaces_full(factors):
    seen = set()
    winners = set()
    for w in factors:
        if w in seen:
            continue
        cl = cyclic_class(w)
        seen.update(cl)
        if cl.issubset(factors):
            winners.add(min(cl))
    return winners


def expected(n):
    while n % 2 == 0:
        n //= 2
    return 2 if n in (1, 3) else 0


def verify():
    # Independent 2-adic definition and morphic generation agree.
    w = word(16)
    assert len(w) == (1 << 16)
    assert w == arithmetic_prefix(len(w))
    assert set(w[i:i+2] for i in range(len(w)-1)) == {'00', '01', '10'}
    assert '11' not in w and '0000' not in w
    checks = 0
    # Every length-n factor of the infinite fixed point appears in the
    # finite prefix mu^(ceil(log2(n))+4)(0): every window of size <= 2^m
    # lies within at most two m-level blocks and every adjacent block
    # pair 00,01,10 already occurs in mu^4(0).
    for n in range(1, 193):
        m = (n-1).bit_length()
        p = word(m + 4)
        facts = {p[i:i+n] for i in range(len(p)-n+1)}
        full = necklaces_full(facts)
        assert len(full) == expected(n), (n, len(full), expected(n))
        if n > 1 and n % 2 == 0:
            smaller = n // 2
            m0 = (smaller-1).bit_length()
            pp = word(m0 + 4)
            small_facts = {pp[i:i+smaller] for i in range(len(pp)-smaller+1)}
            smaller_full = necklaces_full(small_facts)
            images = {min(cyclic_class(mu(v))) for v in smaller_full}
            assert full == images, (n, full, images)
        checks += 1
    print('VERIFY_OK: exact finite-factor coverage and all length classes n=1..192;')
    print('independent arithmetic/morphic prefixes checked to 65536;')
    print('doubling-map class equality checked at every even n=2..192')


if __name__ == '__main__':
    verify()
