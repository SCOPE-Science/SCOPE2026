"""Exact finite-field checks for period census of binary circulant cat maps."""
from itertools import product
from random import Random


def symmetric_steps(n, mask):
    c = [0] * n
    c[0] = mask & 1
    for a in range(1, n // 2):
        c[a] = c[n-a] = (mask >> a) & 1
    c[n // 2] = (mask >> (n // 2)) & 1
    return c


def valuation(c):
    n = len(c)
    p = sum(x << j for j, x in enumerate(c))
    for v in range(n):
        if p.bit_count() & 1:
            return v
        q = 0
        while p.bit_length() > 1:
            j = p.bit_length() - 1
            p ^= (1 << j) | (1 << (j-1))
            q ^= 1 << (j-1)
        assert p == 0
        p = q
    return n


def mat_identity(n):
    return [1 << i for i in range(n)]


def mul(A, B):
    out = []
    for row in A:
        s = 0
        while row:
            b = row & -row
            s ^= B[b.bit_length()-1]
            row ^= b
        out.append(s)
    return out


def rank(A):
    rows = A[:]
    r = 0
    for col in range(len(rows)):
        q = next((j for j in range(r,len(rows)) if (rows[j] >> col) & 1), None)
        if q is None:
            continue
        rows[r], rows[q] = rows[q], rows[r]
        for j in range(len(rows)):
            if j != r and ((rows[j] >> col) & 1):
                rows[j] ^= rows[r]
        r += 1
    return r


def make_map(c):
    n = len(c)
    C = [sum(c[(j-i)%n] << j for j in range(n)) for i in range(n)]
    C2 = mul(C, C)
    rows = []
    for i in range(n):
        rows.append((1 << i) | (C[i] << n))
    for i in range(n):
        rows.append(C[i] | ((C2[i] ^ (1 << i)) << n))
    return rows


def predict(c):
    n = len(c)
    eps = sum(c) % 2
    if eps:
        a = c[:]
        a[0] ^= 1
        v = valuation(a)
        base = 3
        w = 2 * v
    else:
        v = valuation(c)
        base = 1
        w = v
    J = 0
    while (w << J) < n:
        J += 1
    return eps, v, base, w, J


def check(c):
    n = len(c)
    A = make_map(c)
    I = mat_identity(2*n)
    eps, v, base, w, J = predict(c)
    # Direct matrix powering and rank: each predicted fixed-space dimension.
    power = I[:]
    for _ in range(base):
        power = mul(power, A)
    for j in range(J+1):
        actual = 2*n-rank([a ^ b for a,b in zip(power, I)])
        expected = 2 * min(n, w << j)
        assert actual == expected, (n,c,base,j,expected,actual)
        if j < J:
            assert power != I
        else:
            assert power == I
        power = mul(power, power)
    if eps:
        # Any nonmultiple-of-three iterate is fixed-point-free off zero.
        assert rank([a^b for a,b in zip(A,I)])==2*n
        AA = mul(A,A)
        assert rank([a^b for a,b in zip(AA,I)])==2*n
    if n <= 4:
        seen = set()
        for x in range(1<<(2*n)):
            if x in seen:continue
            seq = []
            q = x
            while q not in seen:
                seen.add(q)
                seq.append(q)
                q = sum(((row&q).bit_count()&1)<<i for i,row in enumerate(A))
            assert q == x
            p=len(seq)
            assert p in ([1 << j for j in range(J+1)] if not eps else [1]+[3 << j for j in range(J+1)]), (n, c, p, eps, v, J)
    return 1


def main():
    count=0
    for n in [4,8,16]:
        for mask in range(1 << (n//2+1)):
            count+=check(symmetric_steps(n,mask))
    rng=Random(20261031)
    for _ in range(128):
        count+=check(symmetric_steps(32,rng.getrandbits(17)))
    # Different graph degrees, identical complete cycle statistics.
    n=16
    a=[int(i in (1,15)) for i in range(n)]
    b=[int(i in (1,15,2,14)) for i in range(n)]
    assert predict(a)[1:]==predict(b)[1:]
    assert sum(a)==2 and sum(b)==4
    print('PASS: symmetric_circulants_checked=',count, 'full_state_censuses_for_n4=8')

if __name__ == '__main__': main()
