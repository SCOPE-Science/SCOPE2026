"""Check the length-four single-previous-symbol-overwrite construction.

Run: python3 verify_latin_grain.py
This finite test complements, but does not replace, the all-q proof.
"""
from itertools import product

def idempotent_latin(q):
    """Find one idempotent Latin square by exact constraint propagation."""
    L = [[-1] * q for _ in range(q)]
    rowmask = [0] * q
    colmask = [0] * q
    for i in range(q):
        L[i][i] = i
        rowmask[i] = colmask[i] = 1 << i
    full = (1 << q) - 1
    def fill(left):
        if left == 0:
            return True
        best = None
        best_bits = 0
        best_count = q + 1
        for i in range(q):
            for j in range(q):
                if L[i][j] != -1:
                    continue
                bits = full & ~(rowmask[i] | colmask[j])
                count = bits.bit_count()
                if count == 0:
                    return False
                if count < best_count:
                    best = (i,j)
                    best_count = count
                    best_bits = bits
        i,j = best
        while best_bits:
            bit = best_bits & -best_bits
            best_bits ^= bit
            sym = bit.bit_length() - 1
            L[i][j] = sym
            rowmask[i] ^= bit
            colmask[j] ^= bit
            if fill(left - 1):
                return True
            rowmask[i] ^= bit
            colmask[j] ^= bit
            L[i][j] = -1
        return False
    assert fill(q*q-q), 'No Latin square found'
    assert all(set(row)==set(range(q)) for row in L)
    assert all(set(L[i][j] for i in range(q))==set(range(q)) for j in range(q))
    assert all(L[i][i]==i for i in range(q))
    return L

def ball(x):
    out={x}
    for i in (1,2,3):
        w=list(x)
        w[i]=w[i-1]
        out.add(tuple(w))
    return out

def construction(q,L=None):
    if q==2:
        return {tuple(int(ch) for ch in s) for s in
                ('0000','0011','0110','1001','1100','1111')}
    assert L is not None
    return {(a,a,a,a) for a in range(q)} | {
        (a,b,c,L[b][c])
        for a in range(q) for b in range(q) if b!=a for c in range(q)
    }

def verify_code(q,C):
    assert len(C)==q**3-q**2+q,(q,len(C))
    images={}
    for x in C:
        for y in ball(x):
            if y in images and images[y]!=x:
                raise AssertionError((q,images[y],x,y))
            images[y]=x
    print(f'CHECK q={q} words={len(C)} disjoint_outputs={len(images)}')

for q in (2,3,4,5,6):
    L = None if q==2 else idempotent_latin(q)
    C=construction(q,L)
    verify_code(q,C)
print('VERIFICATION_OK')
