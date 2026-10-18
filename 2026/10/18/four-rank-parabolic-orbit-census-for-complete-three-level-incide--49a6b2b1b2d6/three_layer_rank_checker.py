"""Independent small-field verification of three-layer parabolic nilradical orbit counts.

Run with Python 3; no third-party packages are required.
"""
from collections import Counter
from itertools import product
from math import prod


def gf_mul(x, y, q):
    if q != 4:
        return (x * y) % q
    z = 0
    for i in range(2):
        if (y >> i) & 1:
            z ^= x << i
    for i in (3, 2):
        if (z >> i) & 1:
            z ^= 0b111 << (i - 2)
    return z


def gf_add(x, y, q):
    return x ^ y if q == 4 else (x + y) % q


def gf_sub(x, y, q):
    return x ^ y if q == 4 else (x - y) % q


def gf_inv(x, q):
    assert x
    return next(y for y in range(1, q) if gf_mul(x, y, q) == 1)


def rank(matrix, q):
    if not matrix:
        return 0
    a = [list(row) for row in matrix]
    n, m = len(a), len(a[0])
    row = 0
    for col in range(m):
        pivot = next((k for k in range(row, n) if a[k][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = gf_inv(a[row][col], q)
        a[row] = [gf_mul(x, inv, q) for x in a[row]]
        for k in range(n):
            if k == row or not a[k][col]:
                continue
            fac = a[k][col]
            a[k] = [gf_sub(v, gf_mul(fac, x, q), q) for v, x in zip(a[k], a[row])]
        row += 1
        if row == n:
            break
    return row


def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    num = prod(q ** (n - i) - 1 for i in range(k))
    den = prod(q ** (k - i) - 1 for i in range(k))
    return num // den


def injection(n, k, q):
    if k > n or k < 0:
        return 0
    return prod(q ** n - q ** i for i in range(k))


def rank_count(m, n, r, q):
    return gaussian(m, r, q) * injection(n, r, q)


def predicted(a, b, c, q):
    out = Counter()
    for u in range(min(a, b) + 1):
        for v in range(min(b, c) + 1):
            for t in range(max(0, u + v - b), min(u, v) + 1):
                middle = gaussian(b-u, v-t, q) * gaussian(u, t, q) * q ** ((b-u-v+t)*t)
                base = gaussian(b, u, q) * injection(a, u, q) * middle * injection(c, v, q)
                for w in range(min(a-u, c-v) + 1):
                    val = base * q ** (a*c-(a-u)*(c-v)) * rank_count(a-u, c-v, w, q)
                    if val:
                        out[u,v,t,w] += val
    return out


def brute(a,b,c,q):
    out = Counter()
    d = a + b + c
    entries = a*b + b*c + a*c
    for flat in product(range(q), repeat=entries):
        off=0
        A = [flat[off+i*b:off+(i+1)*b] for i in range(a)]
        off += a*b
        B = [flat[off+i*c:off+(i+1)*c] for i in range(b)]
        off += b*c
        C = [flat[off+i*c:off+(i+1)*c] for i in range(a)]
        M = [[0 for j in range(d)] for i in range(d)]
        M2 = [[0 for j in range(d)] for i in range(d)]
        for i in range(a):
            for j in range(b): M[i][a+j] = A[i][j]
            for k in range(c):
                M[i][a+b+k] = C[i][k]
                s = 0
                for j in range(b): s=gf_add(s,gf_mul(A[i][j], B[j][k], q),q)
                M2[i][a+b+k] = s
        for j in range(b):
            for k in range(c): M[a+j][a+b+k] = B[j][k]
        u,v,t,r = rank(A,q),rank(B,q),rank(M2,q),rank(M,q)
        w = r - u - v
        assert w >= 0 and r >= 2*t and d-2*r+t >= 0
        out[u,v,t,w] += 1
    return out


def run():
    tested=0
    for q,a,b,c in [(2,1,1,1),(3,1,1,1),(4,1,1,1),(5,1,1,1),
                    (2,2,1,1),(2,1,2,1),(2,1,1,2),
                    (2,2,2,1),(2,1,2,2),(2,2,1,2),
                    (2,2,2,2),(3,1,2,1),(3,1,2,2)]:
        got = brute(a,b,c,q)
        want = predicted(a,b,c,q)
        assert got == want, (q,a,b,c,got-want,want-got)
        assert sum(got.values()) == q ** (a*b+b*c+a*c)
        print('PASS',q,(a,b,c),'elements',sum(got.values()),'strata',len(got))
        tested += 1
    print('ALL_THREE_LAYER_RANK_CHECKS_PASSED',tested)

if __name__ == '__main__':
    run()

# Orbit reconstruction is intentionally independent of the counting identity.
def mm(X, Y, q):
    return [[sum_field([gf_mul(x, y, q) for x,y in zip(row, col)], q)
             for col in zip(*Y)] for row in X]


def sum_field(vals, q):
    ans = 0
    for v in vals:
        ans = gf_add(ans,v,q)
    return ans


def inv_matrix(M,q):
    n=len(M)
    a=[list(M[i])+[int(i==j) for j in range(n)] for i in range(n)]
    for i in range(n):
        h=next((r for r in range(i,n) if a[r][i]),None)
        assert h is not None
        a[h],a[i]=a[i],a[h]
        z=gf_inv(a[i][i],q)
        a[i]=[gf_mul(v,z,q) for v in a[i]]
        for j in range(n):
            if j!=i and a[j][i]:
                z=a[j][i]
                a[j]=[gf_sub(v,gf_mul(z,t,q),q) for v,t in zip(a[j],a[i])]
    return [r[n:] for r in a]


def orbit_check(a,b,c,q):
    d=a+b+c
    pairs=[(i,j) for i in range(d) for j in range(d)
           if (i<a<=j) or (a<=i<a+b<=j) or (i<a and j>=a+b)]
    identity=lambda: [[int(i==j) for j in range(d)] for i in range(d)]
    gens=[]
    for i,j in pairs:
        g=identity();g[i][j]=1;gens.append(g)
    for lo,hi in [(0,a),(a,a+b),(a+b,d)]:
        for i in range(lo,hi):
            if q>2:
                g=identity();g[i][i]=2;gens.append(g)
            for j in range(lo,hi):
                if i!=j:
                    g=identity();g[i][j]=1;gens.append(g)
    conjugators=[(g,inv_matrix(g,q)) for g in gens]
    encode=lambda M: tuple(M[i][j] for i,j in pairs)
    decode=lambda z: [[next((z[k] for k,(a0,b0) in enumerate(pairs) if (a0,b0)==(i,j)),0)
                      for j in range(d)] for i in range(d)]
    def invariant(z):
        M=decode(z)
        A=[r[a:a+b] for r in M[:a]]
        B=[r[a+b:] for r in M[a:a+b]]
        u,v=rank(A,q),rank(B,q)
        return u,v,rank(mm(A,B,q),q),rank(M,q)-u-v
    remaining=set(product(range(q),repeat=len(pairs)))
    orbit_counts={}
    while remaining:
        seed=next(iter(remaining))
        todo=[seed]; orbit={seed}
        while todo:
            v=todo.pop()
            M=decode(v)
            for g,gi in conjugators:
                nxt=encode(mm(mm(g,M,q),gi,q))
                if nxt not in orbit:
                    orbit.add(nxt);todo.append(nxt)
        assert orbit <= remaining
        remaining-=orbit
        tag=invariant(seed)
        assert all(invariant(z)==tag for z in orbit)
        assert tag not in orbit_counts, ('separate orbits of same rank tuple',tag)
        orbit_counts[tag]=len(orbit)
    assert orbit_counts == dict(predicted(a,b,c,q))
    print('PASS_PARABOLIC_ORBITS',q,(a,b,c),'orbits',len(orbit_counts))


if __name__ == '__main__':
    for qq, dims in [(2,(1,1,1)),(3,(1,1,1)),(2,(1,2,1)),(2,(2,1,2))]:
        orbit_check(*dims,qq)
    print('ALL_PARABOLIC_ORBIT_CHECKS_PASSED')
