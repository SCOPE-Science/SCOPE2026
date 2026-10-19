"""Closed finite-sum formula for polarization on a star with one leaf-to-leaf edge.
No external packages; exact rational arithmetic throughout.
"""
from fractions import Fraction as F
from math import comb, sqrt


def probability(m):
    """Number m of leaves; requires m>=4. Returns exact final-polarization chance."""
    assert isinstance(m,int) and m >= 4
    h=m//2
    k=m-2
    def opposed(j):
        return F(1) if j < h-1 else F(h-1,j+1)
    def same(j):
        return F(0) if j < h+1 else F(j-h,j+1)
    mixed=[F(0)]*(k+1)
    for j in range(k+1):
        mixed[j] = (j*(mixed[j-1] if j else F(0)) + same(j))/(j+1 + (j>=h))
    return sum((F(comb(k,j),4*(1<<k))*(opposed(j)+same(j)+2*mixed[j]) for j in range(k+1)), F(0))


def hub_flip_bound(m):
    """Rigorous upper bound from binomial variance and a competing-rates telescope."""
    assert m>=4
    k=m-2
    T=m//2-1
    return (sqrt(k)/2+1.5)/T

if __name__=='__main__':
    known={4:F(7,48),5:F(41,320),6:F(35,192),7:F(229,1344),8:F(1431,7168)}
    for m,p in known.items():
        assert probability(m)==p
    for m in (4,5,6,7,8,9,16,32,64,128,256):
        p=probability(m)
        assert abs(float(p)-.25) <= hub_flip_bound(m)+1e-12
        print(f'leaves={m} probability={p} decimal={float(p):.12f} bound={hub_flip_bound(m):.8f}')
    print('formula_verified')
