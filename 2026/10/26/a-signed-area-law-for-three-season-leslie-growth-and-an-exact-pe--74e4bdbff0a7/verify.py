"""Reproducible executable arithmetic checks for a three-season two-age Leslie model.

These finite checks test examples and identities; the accompanying proof establishes
universal statements over real parameters.
"""
from fractions import Fraction as F
from itertools import permutations
from math import sqrt
import random


def mult(a,b):
    return ((a[0][0]*b[0][0]+a[0][1]*b[1][0],a[0][0]*b[0][1]+a[0][1]*b[1][1]),
            (a[1][0]*b[0][0]+a[1][1]*b[1][0],a[1][0]*b[0][1]+a[1][1]*b[1][1]))


def mat(f,s,b):return ((f,b),(s,F(0)))
def trace(a):return a[0][0]+a[1][1]
def det(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def monodromy(ms,chronological):
    product=((F(1),F(0)),(F(0),F(1)))
    for i in chronological:
        product=mult(ms[i],product)
    return product

def rho(tr,d):return (float(tr)+sqrt(float(tr)**2-4*float(d)))/2

def test():
    rng=random.Random(452026)
    count=0
    for _ in range(3000):
        f=[F(rng.randint(1,18),rng.randint(2,22)) for j in range(3)]
        s=[F(rng.randint(1,20),20) for j in range(3)]
        b=F(rng.randint(1,14),rng.randint(1,12))
        ms=[mat(x,y,b) for x,y in zip(f,s)]
        Fprod=f[0]*f[1]*f[2]
        Q=s[0]*s[1]*s[2]
        Lplus=f[0]*s[2]+f[1]*s[0]+f[2]*s[1]
        Lminus=f[0]*s[1]+f[1]*s[2]+f[2]*s[0]
        p123=monodromy(ms,(0,1,2))
        p132=monodromy(ms,(0,2,1))
        assert trace(p132)==Fprod+b*Lplus
        assert trace(p123)==Fprod+b*Lminus
        assert det(p123)==det(p132)==-b**3*Q
        for p in permutations(range(3)):
            m=monodromy(ms,p)
            expected=Fprod+b*(Lplus if p in ((0,2,1),(2,1,0),(1,0,2)) else Lminus)
            assert trace(m)==expected and det(m)==-b**3*Q
            assert all(v>0 for row in m for v in row)
        Rp=rho(trace(p132),det(p132));Rm=rho(trace(p123),det(p123))
        delta=Lplus-Lminus
        assert (Rp>Rm) == (delta>0) if delta!=0 else abs(Rp-Rm)<1e-9
        count+=1
    f=[F(1,5),F(1,2),F(9,10)]
    s=[F(1,5),F(4,5),F(1,2)]
    b=F(1)
    ms=[mat(x,y,b) for x,y in zip(f,s)]
    plus=monodromy(ms,(0,2,1)); minus=monodromy(ms,(0,1,2))
    assert trace(plus)==F(101,100) and trace(minus)==F(17,25)
    assert det(plus)==det(minus)==-F(2,25)
    assert F(1)-trace(plus)+det(plus)==-F(9,100)
    assert F(1)-trace(minus)+det(minus)==F(6,25)
    def pol(b,L):return F(1)-F(9,100)-b*L-b**3*F(2,25)
    def root(L):
        a,c=0.,4.
        for i in range(90):
            m=(a+c)/2
            if float(pol(m,L))>0:a=m
            else:c=m
        return (a+c)/2
    Bp=root(F(23,25));Bm=root(F(59,100))
    assert Bp<1<Bm
    print('PASS 3000 exact-rational six-permutation trace/determinant and ordering checks')
    print('PASS exact rational persistence witness with opposite signs at unit adult fertility')
    print('positive roots for adult fecundity:',repr(Bp),repr(Bm))
    print('Perron multipliers high/low:',repr(rho(trace(plus),det(plus))),repr(rho(trace(minus),det(minus))))
if __name__=='__main__':test()
