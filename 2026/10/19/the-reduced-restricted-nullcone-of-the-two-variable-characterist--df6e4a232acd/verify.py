"""Independent finite-field checks for a rank-stratified derivation point count."""
from itertools import product


def field_mul(a, b, q):
    modulus = {2:0b11, 4:0b111}[q]
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & q:
            a ^= modulus
    return out


def rank_over_field(rows, q):
    m = [list(r) for r in rows]
    piv = 0
    ncol = len(m[0])
    for col in range(ncol):
        idx = next((i for i in range(piv, len(m)) if m[i][col]), None)
        if idx is None:
            continue
        m[piv], m[idx] = m[idx], m[piv]
        inv = next(b for b in range(1, q) if field_mul(m[piv][col],b,q)==1)
        m[piv] = [field_mul(v, inv, q) for v in m[piv]]
        for i in range(len(m)):
            if i != piv and m[i][col]:
                s = m[i][col]
                m[i] = [v ^ field_mul(s,w,q) for v,w in zip(m[i],m[piv])]
        piv += 1
        if piv == len(m): break
    return piv


def check(q):
    hist = [0,0,0]
    # Basis (1,x,y,xy); D is built directly from the Leibniz rule.
    for a in product(range(q),repeat=8):
        f,g = a[:4],a[4:]
        dx_y = [0, field_mul(1,g[0],q), f[0], g[2]^f[1]]
        cols = ([0,0,0,0],f,g,dx_y)
        rows = [[cols[j][i] for j in range(4)] for i in range(4)]
        composition = [[0]*4 for i in range(4)]
        for i in range(4):
            for j in range(4):
                s=0
                for k in range(4):s ^= field_mul(rows[i][k],rows[k][j],q)
                composition[i][j]=s
        if any(v for row in composition for v in row): continue
        hist[rank_over_field(rows,q)] += 1
    target = [1,q**3+q**2-q-1,q**4-q**2]
    assert hist == target, (q,hist,target)
    print(f'q={q} all={q**8} squarezero={sum(hist)} rank_hist={hist} VALID')

if __name__ == '__main__':
    check(2)
    check(4)
    print('VERIFY_OK')
