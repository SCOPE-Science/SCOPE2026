"""Finite-field consistency tests for the radical-depth one-line-subalgebra theorem.

Run with Python 3, no external dependencies. Tests prime fields; the theorem's
prime-power cases follow from the field-independent argument in RESULT.md.
"""
from itertools import combinations, product
from math import comb


def qbin(n, k, q):
    num = den = 1
    for j in range(k):
        num *= q ** (n-j) - 1
        den *= q ** (k-j) - 1
    return num // den


def predicted(n, q):
    c2, c3, c4 = comb(n, 2), comb(n, 3), comb(n, 4)
    h = c3 + c4
    if q % 2 == 0:
        s1 = (q**n - 1) * q**(c2+h) // (q-1)
        s2 = (q**c2 - 1) * q**h // (q-1)
    else:
        g = qbin(n, 2, q)
        s1 = q**h * (q**n - 1 + (q-1)*g*(q**2-1)) // (q-1)
        s2 = g * q**h
    s3 = (q**c3-1) * q**c4 // (q-1)
    s4 = (q**c4-1) // (q-1)
    return (1, s1, s2, s3, s4)


def basis(n):
    return [b for b in range(1, 1 << n) if b.bit_count() <= 4]


def wedge_mask(u, v, q):
    if u & v:
        return None
    inv = sum((v & ((1 << i)-1)).bit_count() for i in range(8) if u & (1 << i))
    return u|v, (-1 if inv % 2 else 1) % q


def multiply(v, w, q):
    out = {}
    for a, av in v.items():
        for b, bv in w.items():
            z = wedge_mask(a, b, q)
            if z is not None and z[0].bit_count() <= 4:
                out[z[0]] = (out.get(z[0],0) + av*bv*z[1]) % q
    return {k: vv for k, vv in out.items() if vv}


def brute_ab(n, q):
    inds = [b for b in basis(n) if b.bit_count() in (1,2)]
    counts = [0]*5
    for coeffs in product(range(q), repeat=len(inds)):
        v = {k:x for k,x in zip(inds,coeffs) if x}
        if not multiply(v,v,q):
            order = min((k.bit_count() for k in v),default=0)
            counts[order]+=1
    return counts


def verify_brute_ab(n, q):
    c3, c4 = comb(n,3), comb(n,4)
    c = brute_ab(n,q)
    s = predicted(n,q)
    # Deleting degree >=3 terms preserves the square, and each lift
    # has exactly q^(c3+c4) choices.
    assert c[0] == 1
    for j in [1,2]:
        assert c[j] * q**(c3+c4) == s[j]*(q-1), (n,q,j,c,s)
    assert sum(c[1:3])*q**(c3+c4) + q**(c3+c4) == 1+(q-1)*sum(s[1:]), (n,q,c,s)
    print('AB_OK', n,q,tuple(c), 'expected polynomial',s)


def verify_full(n, q):
    inds = basis(n)
    counts = [0]*5
    for coeffs in product(range(q), repeat=len(inds)):
        v = {k:x for k,x in zip(inds,coeffs) if x}
        if not multiply(v,v,q):
            order = min((k.bit_count() for k in v),default=0)
            counts[order]+=1
    want = predicted(n,q)
    for j in range(1,5):
        assert counts[j] == (q-1)*want[j], (n,q,j,counts,want)
    assert counts[0] == 1
    print('FULL_OK',n,q,counts,'expected polynomial',want)


if __name__ == '__main__':
    for n,q in [(4,2),(4,3),(3,3),(3,5)]:
        # n=5 q=2 has 16 input degrees <=2, fine.
        verify_brute_ab(n,q)
    for n,q in [(2,3),(3,2),(3,3),(4,2)]:
        verify_full(n,q)
    print('VERIFY_OK')
