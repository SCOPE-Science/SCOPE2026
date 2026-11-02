"""Independent direct quaternion-multiplication check of the eight formulas.
Run with Python 3: python verify.py
"""
from itertools import product

# Signed quaternion basis (sign,basis) with basis 0,1,2,3 = 1,i,j,k.
BASIS = ((0,1,2,3),(1,0,3,2),(2,3,0,1),(3,2,1,0))
NEG = ((0,0,0,0),(0,1,0,1),(0,1,1,0),(0,0,1,1))
G = tuple(product((0,1),(0,1,2,3)))
ONE=(0,0)
Z=(1,0)

def m(a,b):
    s,i=a;t,j=b
    return (s^t^NEG[i][j],BASIS[i][j])

def inv(g):
    for h in G:
        if m(g,h)==ONE and m(h,g)==ONE:
            return h
    raise AssertionError('no inverse')

for a,b,c in product(G,repeat=3):
    assert m(m(a,b),c)==m(a,m(b,c))

results=set()
for alpha,beta in product((0,1),repeat=2):
    def chi(g):
        return (0,0) if g[1]==0 else ((alpha if g[1]==1 else beta if g[1]==2 else alpha^beta),0)
    families=(tuple(chi(g) for g in G),tuple(m(inv(g),chi(g)) for g in G))
    for images in families:
        B=dict(zip(G,images))
        for g,h in product(G,repeat=2):
            assert m(B[g],B[h])==B[m(m(m(g,B[g]),h),inv(B[g]))]
        dual=tuple(m(inv(g),B[inv(g)]) for g in G)
        assert len(set(images)) in (1,2,8)
        assert not (len(set(images))==8 and len(set(dual))==8)
        results.add(images)
assert len(results)==8
sizes=sorted([len(set(x)) for x in results])
assert sizes==[1,2,2,2,8,8,8,8]
print('FORMULA_CHECK_OK operators=8 image_cardinalities='+','.join(map(str,sizes)))
