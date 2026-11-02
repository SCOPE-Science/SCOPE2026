#!/usr/bin/env python3
"""Direct finite-field group-ring checks for square-zero elements of generalized dihedral algebras."""
from itertools import product
from collections import Counter


def fmul(a, b, q):
    if q == 2:
        return a & b
    assert q == 4
    r = 0
    for i in range(2):
        if b & (1 << i):
            r ^= a << i
    if r & 8:
        r ^= 0b1100  # X^3 = X^2+X, using X^2=X+1
    if r & 4:
        r ^= 0b111   # X^2=X+1
    return r


def rank_field(columns, n, q):
    rows = [[columns[c][r] for c in range(n)] for r in range(n)]
    pivot = 0
    inv = {x: next(y for y in range(1, q) if fmul(x, y, q) == 1) for x in range(1, q)}
    for c in range(n):
        found = next((r for r in range(pivot, n) if rows[r][c]), None)
        if found is None: continue
        rows[pivot], rows[found] = rows[found], rows[pivot]
        factor = inv[rows[pivot][c]]
        rows[pivot] = [fmul(z, factor, q) for z in rows[pivot]]
        for r in range(n):
            if r != pivot and rows[r][c]:
                coef = rows[r][c]
                rows[r] = [z ^ fmul(coef, v, q) for z, v in zip(rows[r], rows[pivot])]
        pivot += 1
        if pivot == n: break
    return pivot


def integer_digits(x, base, count):
    out = []
    for _ in range(count):
        out.append(x % base)
        x //= base
    return out


def orbit_degrees(orders, q):
    chars = list(product(*[range(z) for z in orders]))
    zero = tuple(0 for _ in orders)
    unseen = {min(t, tuple((-v) % z for v, z in zip(t, orders))) for t in chars if t != zero}
    deg = []
    while unseen:
        start = min(unseen)
        t = start
        orbit = set()
        while t not in orbit:
            orbit.add(t)
            t1 = tuple((-v) % z for v, z in zip(t, orders))
            t2 = min(t, t1)
            t = min(tuple((q*v) % z for v, z in zip(t2, orders)),
                    tuple((-q*v) % z for v, z in zip(t2, orders)))
        assert t == start or t in orbit
        unseen.difference_update(orbit)
        deg.append(len(orbit))
    assert sum(deg) * 2 == len(chars) - 1
    return sorted(deg)


def expected_hist(orders, q):
    hist = {0: 1, 1: q-1}
    for d in orbit_degrees(orders, q):
        nxt = Counter(hist)
        for rank, count in hist.items():
            nxt[rank+2*d] += count*(q**(2*d)-1)
        hist = dict(nxt)
    return hist


def run(orders, q, exhaustive=True):
    H = list(product(*[range(z) for z in orders]))
    m = len(H); n = 2*m
    idx = {x: j for j, x in enumerate(H)}
    basis = [(h, eps) for eps in (0,1) for h in H]
    multiplication = [[0]*n for _ in range(n)]
    for i,(h,eps) in enumerate(basis):
        for j,(g,delta) in enumerate(basis):
            hg = tuple((h[k] + (1 if eps == 0 else -1)*g[k]) % orders[k] for k in range(len(orders)))
            multiplication[i][j] = idx[hg] + m*((eps+delta)%2)

    def multiply(x, y):
        result = [0]*n
        for i,v in enumerate(x):
            if not v: continue
            for j,w in enumerate(y):
                if w: result[multiplication[i][j]] ^= fmul(v,w,q)
        return result

    def rank_left(x):
        cols = [[0]*n for _ in range(n)]
        for j in range(n):
            for i,v in enumerate(x):
                if v: cols[j][multiplication[i][j]] ^= v
        return rank_field(cols,n,q)

    hist = Counter()
    if exhaustive and q**n <= 16384:
        for code in range(q**n):
            x = integer_digits(code,q,n)
            if not any(multiply(x,x)):
                hist[rank_left(x)] += 1
        kind = 'full direct group-ring endomorphism enumeration'
    else:
        # Exhaustively test all q^(2m) coefficient pairs using the unexpanded group-ring
        # square identities in H, without assuming that the unique square root exists.
        def bmul(x,y):
            z = [0]*m
            for i, a in enumerate(x):
                if a == 0: continue
                for j, b in enumerate(y):
                    if b: z[idx[tuple((H[i][k]+H[j][k])%orders[k] for k in range(len(orders)))]] ^= fmul(a,b,q)
            return z
        inv_idx=[idx[tuple((-u)%orders[k] for k,u in enumerate(h))] for h in H]
        a_squares = []
        a_pluses = []
        for i in range(q**m):
            a=integer_digits(i,q,m)
            a_squares.append(bmul(a,a))
            a_pluses.append([a[j] ^ a[inv_idx[j]] for j in range(m)])
        for ib in range(q**m):
            b=integer_digits(ib,q,m)
            norm=bmul(b,[b[inv_idx[j]] for j in range(m)])
            for ia in range(q**m):
                if a_squares[ia] != norm: continue
                if any(bmul(b,a_pluses[ia])): continue
                a=integer_digits(ia,q,m)
                x=a+b
                assert not any(multiply(x,x))
                hist[rank_left(x)] += 1
        kind = 'complete two-coset coefficient enumeration with direct group-product replay'
    exp = Counter(expected_hist(orders,q))
    assert hist == exp, (orders,q,hist,exp)
    assert sum(hist.values()) == q**m
    print(f'H={"x".join(map(str,orders))} q={q}, source_size={q**n}, method={kind}, orbits={orbit_degrees(orders,q)}, rank_counts={dict(sorted(hist.items()))}, total={sum(hist.values())}')

if __name__ == '__main__':
    for orders,q,full in [((1,),2,True),((3,),2,True),((3,),4,True),((5,),2,True),((7,),2,True),((3,3),2,False),((9,),2,False)]:
        run(orders,q,full)
    print('ODD_ABELIAN_DIHEDRAL_SQUAREZERO_CHECKS_OK 7_CONFIGURATIONS')
