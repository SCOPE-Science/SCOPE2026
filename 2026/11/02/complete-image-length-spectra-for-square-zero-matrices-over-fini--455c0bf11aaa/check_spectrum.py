#!/usr/bin/env python3
"""Exhaustive small-ring check of a square-zero centralizer census.

Pure Python; no dependencies. Each ring element is an integer encoding its
truncated-polynomial coefficients, or an integer modulo a prime power.
The image length is computed from an explicit set of image vectors, not
from the determinant or Smith normal form used in the proof.
"""
from collections import Counter
from itertools import product


def field_ops(q):
    if q in (2, 3):
        return (lambda a, b: (a + b) % q,
                lambda a, b: (a * b) % q)
    if q == 4:
        # F_4=F_2[alpha]/(alpha^2+alpha+1), low bits = coefficients.
        def mul(a, b):
            a0, a1 = a & 1, (a >> 1) & 1
            b0, b1 = b & 1, (b >> 1) & 1
            x = (a0*b0) ^ (a1*b1)
            y = (a0*b1) ^ (a1*b0) ^ (a1*b1)
            return x | (y << 1)
        return (lambda a, b: a ^ b, mul)
    raise ValueError(q)


def build_ring(kind, q, length):
    size = q ** length
    if kind == 'chain':
        assert q in (2, 3)
        add = [[(x+y) % size for y in range(size)] for x in range(size)]
        mul = [[(x*y) % size for y in range(size)] for x in range(size)]
        val = [next((k for k in range(length) if x % (q**(k+1)) != 0), length)
               for x in range(size)]
    else:
        fadd, fmul = field_ops(q)
        digs = [tuple(x // q**i % q for i in range(length)) for x in range(size)]
        weights = [q**i for i in range(length)]
        add, mul = [], []
        for a in range(size):
            ar, mr = [], []
            for b in range(size):
                ar.append(sum(weights[i]*fadd(digs[a][i],digs[b][i]) for i in range(length)))
                coeff = [0]*length
                for i in range(length):
                    for j in range(length-i):
                        coeff[i+j] = fadd(coeff[i+j],fmul(digs[a][i],digs[b][j]))
                mr.append(sum(weights[i]*coeff[i] for i in range(length)))
            add.append(ar); mul.append(mr)
        val = [next((k for k, v in enumerate(digs[x]) if v != 0), length)
               for x in range(size)]
    return size, add, mul, val



def predicted_image_spectrum(q,n):
    """Closed finite-sum spectrum derived by content and Smith invariants."""
    h=(n+1)//2
    m=n//2
    out=Counter({0:1})
    for k in range(h):
        ell=n-2*k
        P=(q*q-1)*q**(2*ell-2)
        out[n-k] += P*q**(3*k)
        for j in range(k):
            out[n-j] += P*(q-1)*q**(4*k-j-1)
    U=(q-1)*(q+1)**2
    for ell in range(1,m+1):
        out[2*ell] += q**(4*(ell-1))*(q*q-1)*(q*q-q)
        out[ell] += U*q**(3*ell-3)
        for v in range(1,ell):
            out[2*ell-v] += U*(q-1)*q**(4*ell-v-4)
    return out

def verify(kind, q, n):
    size, add, mul, val = build_ring(kind, q, n)
    expected_layer = (q*q-1)*q**(2*n-2)
    expected_total = ((n+1)//2)*expected_layer + q**(4*(n//2))
    expected_max = (q*q-1)*q**(2*n-3)*(q+(n//2)*(q-1))
    layers = Counter(); maxima = Counter(); total = 0; rank_hist = Counter()
    elems = tuple(range(size)); vectors = tuple(product(elems,repeat=2))
    # Enumerate all matrices; use the four defining products as the only filter.
    for a,b,c,d in product(elems,repeat=4):
        if (add[mul[a][a]][mul[b][c]] or
            add[mul[a][b]][mul[b][d]] or
            add[mul[c][a]][mul[d][c]] or
            add[mul[c][b]][mul[d][d]]):
            continue
        total += 1
        k = min(val[a],val[b],val[c],val[d]); layers[k] += 1
        # Genuine image enumeration over the finite additive group R^2.
        image = {(add[mul[a][x]][mul[b][y]],add[mul[c][x]][mul[d][y]])
                 for x,y in vectors}
        image_size = len(image)
        length_im = 0
        while image_size > 1:
            assert image_size % q == 0
            image_size //= q
            length_im += 1
        rank_hist[length_im] += 1
        if length_im == n: maxima[k] += 1
        assert length_im <= n, (kind,q,n,k,length_im)
    assert rank_hist == predicted_image_spectrum(q,n), (kind,q,n,rank_hist,predicted_image_spectrum(q,n))
    assert total == expected_total, (kind,q,n,total,expected_total)
    assert sum(maxima.values()) == expected_max, (kind,q,n,maxima,expected_max)
    for k in range((n+1)//2):
        assert layers[k] == expected_layer, (kind,q,n,k,layers[k],expected_layer)
    assert sum(layers[k] for k in range((n+1)//2,n+1)) == q**(4*(n//2))
    assert maxima[0] == expected_layer
    flat = (q*q-1)*(q-1)*q**(2*n-3)
    for k in range(1,n//2+1):
        assert maxima[k] == flat, (kind,q,n,k,maxima[k],flat)
    for k in range(n//2+1,n+1):
        assert not maxima[k], (kind,q,n,k,maxima[k])
    print(f'{kind} q={q} length={n}: squarezero={total}, maximal-image={sum(maxima.values())}, '
          f'layers={dict(sorted(layers.items()))}, maxima={dict(sorted(maxima.items()))}, image-sizes={dict(sorted(rank_hist.items()))}')


def main():
    configs = [
        ('poly',2,1),('poly',2,2),('poly',2,3),('poly',2,4),
        ('poly',3,1),('poly',3,2),('poly',4,1),('poly',4,2),
        ('chain',2,2),('chain',2,3),('chain',2,4),('chain',3,2),
    ]
    for config in configs:
        verify(*config)
    print('SQUAREZERO_TWO_BLOCK_CHAIN_CENSUS_OK',len(configs))

if __name__ == '__main__':
    main()
