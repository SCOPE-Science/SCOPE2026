"""Exact finite-word and analytic consistency checks for a binary memory-three chain.

Requires only the Python standard library. Run: python verify.py
The infinite-family assertions follow from the accompanying algebraic proof;
finite computations here independently check its indexing and normalizations.
"""
from fractions import Fraction as F
from itertools import product
import math
import random

WORDS = [''.join(w) for w in product('01', repeat=4)]
TRIPLES = [''.join(w) for w in product('01', repeat=3)]
H = F(1, 8)


def four_law(a, b, x, j):
    y = H - x
    z = {
        '0000': a, '0001': H-a, '0010': x, '0011': y,
        '0100': x-j, '0101': y+j, '0110': b, '0111': H-b,
        '1000': H-a, '1001': a, '1010': y, '1011': x,
        '1100': y+j, '1101': x-j, '1110': H-b, '1111': b,
    }
    assert all(z[w] > 0 for w in WORDS), (a,b,x,j)
    assert sum(z.values()) == 1
    assert all(sum(z[w] for w in WORDS if w[:3] == v) == H for v in TRIPLES)
    assert all(sum(z[w] for w in WORDS if w[1:] == v) == H for v in TRIPLES)
    return z


def word_probability(word, z):
    if len(word) <= 3:
        return F(1, 2**len(word))
    p = H
    for i in range(len(word)-3):
        p *= 8*z[word[i:i+4]]
    return p


def divergence(z, n):
    D = 0.
    for tup in product('01', repeat=n):
        w = ''.join(tup)
        p = word_probability(w,z)
        q = word_probability(w[::-1],z)
        D += float(p)*math.log(float(p/q))
    return D


def variation(z):
    return F(1,2)*sum(abs(z[w]-z[w[::-1]]) for w in WORDS)


def dissipation(z):
    return sum(float(z[w])*math.log(float(z[w]/z[w[::-1]])) for w in WORDS)


def sharp_lower(t):
    return 2*t*math.atanh(2*t)


def main():
    count=0
    rng=random.Random(53219)
    for k in range(32):
        j = F(rng.randint(-30, 30), 256)
        # Bound magnitude strictly below 1/8, and select an interior conditional law.
        if abs(j) >= H:
            j = j/2
        lo=max(F(0), j)
        hi=min(H, H+j)
        x=lo+(hi-lo)*F(rng.randint(1,99),100)
        a=F(rng.randint(1,99),800)
        b=F(rng.randint(1,99),800)
        z=four_law(a,b,x,j)
        assert z['0010']-z['0100'] == j
        assert z['0101']-z['1010'] == j
        assert z['1011']-z['1101'] == j
        assert z['1100']-z['0011'] == j
        assert variation(z) == 4*abs(j)
        d4=dissipation(z)
        assert abs(d4-divergence(z,4)) < 2e-12
        t=float(variation(z))
        assert d4+2e-12 >= sharp_lower(t)
        for n in range(1,9):
            norm=sum(word_probability(''.join(w),z) for w in product('01',repeat=n))
            assert norm == 1
            dn=divergence(z,n)
            expected=max(0,n-3)*d4
            assert abs(dn-expected) < 5e-11, (n,j,dn,expected)
            count+=1
    # Rational sharpness witnesses with exactly fair consecutive triples.
    for jj in [F(1,128),F(1,32),F(1,16),F(3,32),F(15,128)]:
        xm=(H+jj)/2
        z=four_law(F(1,16),F(1,16),xm,jj)
        t=float(variation(z))
        assert abs(dissipation(z)-sharp_lower(t)) < 1e-12
        assert abs(divergence(z,7)-4*sharp_lower(t)) < 2e-12
        count+=2
    # At fixed current the informational cost diverges at a forbidden reversal.
    j=F(1,64)
    vals=[]
    for delta in [F(1,64),F(1,256),F(1,1024),F(1,4096),F(1,16384)]:
        z=four_law(F(1,16),F(1,16),j+delta,j)
        vals.append(dissipation(z))
    assert all(vals[i] < vals[i+1] for i in range(len(vals)-1))
    # Every first-, second- and third-order binary stationary flow is symmetric.
    for i in range(1,4):
        assert all(''.join(w)==''.join(w)[::-1] or \
            word_probability(''.join(w),four_law(F(1,16),F(1,16),F(1,16),F(1,128))) == \
            word_probability(''.join(w)[::-1],four_law(F(1,16),F(1,16),F(1,16),F(1,128)))
            for w in product('01', repeat=i))
    print('PASS',count,'exact block normalization and finite-word checks;',
          '32 rational parameter systems; sharp equality and divergence witnesses')


if __name__ == '__main__':
    main()
