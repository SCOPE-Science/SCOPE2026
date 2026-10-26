"""Exact rank enumeration for a five-step flag's twisted-commutator map.

Uses only the Python standard library. Run: python verify.py
"""
from itertools import product


def mul(a, b, q):
    if q != 4:
        return a * b % q
    # F_4 = F_2[z]/(z^2+z+1), encoded as 0,1,z,z+1.
    u = 0
    for i in range(2):
        if (b >> i) & 1:
            u ^= a << i
    for i in (2,):
        if (u >> i) & 1:
            u ^= 0b111 << (i - 2)
    return u


def add(a, b, q):
    return a ^ b if q == 4 else (a + b) % q


def neg(a, q):
    return a if q == 4 else (-a) % q


def rank_of(x, lam, q):
    A, B, C, D, E, F, G, H, I = x
    neg_lam = lambda v: neg(mul(lam, v, q), q)
    m = [
        [neg_lam(B), A, 0, 0, 0, 0, 0, 0, 0],
        [0, neg_lam(C), B, 0, 0, 0, 0, 0, 0],
        [0, 0, neg_lam(D), C, 0, 0, 0, 0, 0],
        [neg_lam(F), 0, E, 0, neg_lam(C), A, 0, 0, 0],
        [0, neg_lam(G), 0, F, 0, neg_lam(D), B, 0, 0],
        [neg_lam(I), 0, 0, H, neg_lam(G), 0, E, neg_lam(D), A],
    ]
    piv = 0
    for col in range(9):
        ix = next((r for r in range(piv, 6) if m[r][col]), None)
        if ix is None:
            continue
        m[piv], m[ix] = m[ix], m[piv]
        inv = next(t for t in range(1, q) if mul(t, m[piv][col], q) == 1)
        m[piv] = [mul(v, inv, q) for v in m[piv]]
        for rr in range(piv + 1, 6):
            c = m[rr][col]
            if c:
                m[rr] = [add(m[rr][j], neg(mul(c, m[piv][j], q), q), q) for j in range(9)]
        piv += 1
        if piv == 6:
            break
    return piv


def support_expected(mask, q):
    v = [0] * 7
    if mask == 0:
        v[0] = 1
        v[1] = q*q-1
        v[2] = 3*q*q*(q-1)
        v[3] = q*q*(q-1)**2*(q+2)
    elif mask in (1, 8):
        v[3], v[4] = q**4, q**4*(q-1)
    elif mask in (2, 4):
        v[3], v[4] = q**3, q**3*(q*q-1)
    elif mask in (5, 10):
        v[4] = q**5
    elif mask == 9:
        v[4], v[5] = q**4, q**4*(q-1)
    elif mask in (3, 6, 11, 12, 13):
        v[5] = q**5
    elif mask in (7, 14, 15):
        v[6] = q**5
    else:
        raise AssertionError(mask)
    assert sum(v) == q**5
    return v


def full_expected(q):
    return [
        q,
        q*(q-1)*(q+1),
        3*q**3*(q-1),
        q**3*(q-1)*(3*q*q+3*q-2),
        q**4*(q-1)**2*(q+2)*(2*q+1),
        q**5*(q-1)**2*(2*q*q+2*q-1),
        q**6*(q-1)**3*(q+1),
    ]


def check(q, lam):
    global_counts = [0]*7
    for mask in range(16):
        a = [((mask >> j)&1) for j in range(4)]
        local = [0]*7
        for t in product(range(q), repeat=5):
            local[rank_of(a+list(t), lam, q)] += 1
        assert local == support_expected(mask, q), (q, lam, mask, local)
        weight = (q-1)**mask.bit_count()
        for r in range(7):
            global_counts[r] += weight*q*local[r]  # center entry x15 is arbitrary
    expected = full_expected(q)
    assert global_counts == expected, (q, lam, global_counts)
    assert sum(global_counts) == q**10
    pairs = sum(v*q**(10-r) for r, v in enumerate(global_counts))
    assert pairs == q**10*(5*q**4-5*q*q+1)
    print('PASS', 'q=',q,'lambda=',lam,'rank_counts=',global_counts,'pairs=',pairs)


if __name__ == '__main__':
    for field in (2, 3, 4, 5):
        for scalar in range(1, field):
            check(field, scalar)
    print('TWISTED_FLAG_RANKS_OK')
