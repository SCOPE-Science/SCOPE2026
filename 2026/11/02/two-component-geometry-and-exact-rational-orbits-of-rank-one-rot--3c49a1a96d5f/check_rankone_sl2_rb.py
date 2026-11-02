#!/usr/bin/env python3
"""Direct finite-field checks of rank-one weight-zero Lie Rota--Baxter geometry.
No external dependencies. The Lie bracket is computed in the E,F,H basis.
"""
from itertools import product
from collections import Counter

class F:
    def __init__(self,q):
        self.q=q
        self.p={3:3,5:5,7:7,9:3,11:11}[q]
        self.degree=2 if q==9 else 1
    def add(self,x,y):
        p=self.p
        return (x+y)%p if self.degree==1 else ((x%p+y%p)%p+p*((x//p+y//p)%p))
    def neg(self,x):
        return (-x)%self.p if self.degree==1 else ((-x%self.p)+self.p*(-(x//self.p)%self.p))
    def sub(self,x,y): return self.add(x,self.neg(y))
    def mul(self,x,y):
        p=self.p
        if self.degree==1: return x*y%p
        a,b=x%p,x//p;c,d=y%p,y//p
        return ((a*c+2*b*d)%p)+p*((a*d+b*c)%p)
    def pow(self,x,n):
        z=1
        for _ in range(n):z=self.mul(z,x)
        return z
    def inv(self,x):
        assert x
        return self.pow(x,self.q-2)


def addv(x,y,F):return tuple(F.add(a,b) for a,b in zip(x,y))
def scale(x,s,F):return tuple(F.mul(a,s) for a in x)
def bracket(x,y,F):
    a,b,c=x;d,e,f=y
    return (F.mul(2%F.p,F.sub(F.mul(c,d),F.mul(a,f))),
            F.mul(2%F.p,F.sub(F.mul(b,f),F.mul(c,e))),
            F.sub(F.mul(a,e),F.mul(b,d)))
def pair(x,y,F):
    return F.add(F.add(F.mul(x[0],y[1]),F.mul(x[1],y[0])),F.mul(2%F.p,F.mul(x[2],y[2])))
def discrim(x,F):return F.add(F.mul(x[2],x[2]),F.mul(x[0],x[1]))
def proportional(x,y,F):
    # Rank at most one of the 2x3 rows.
    return all(F.sub(F.mul(x[i],y[j]),F.mul(x[j],y[i]))==0 for i in range(3) for j in range(i+1,3))
def proj_reps(F):
    q=F.q
    return [(1,a,b) for a in range(q) for b in range(q)]+[(0,1,b) for b in range(q)]+[(0,0,1)]
def rmat(v,w,s,F):
    return tuple(F.mul(s,F.mul(a,b)) for a in v for b in (w[1],w[0],F.mul(2%F.p,w[2])))
def direct_rb(v,w,F):
    basis=[(1,0,0),(0,1,0),(0,0,1)]
    def R(x):return scale(v,pair(w,x,F),F)
    for x in basis:
        for y in basis:
            left=bracket(R(x),R(y),F)
            right=R(addv(bracket(R(x),y,F),bracket(x,R(y),F),F))
            if left!=right:return False
    return True

def gl2_reps(F):
    q=F.q;got=set();mats=[]
    for a,b,c,d in product(range(q),repeat=4):
        det=F.sub(F.mul(a,d),F.mul(b,c))
        if not det:continue
        t=(a,b,c,d)
        pivot=next(z for z in t if z)
        norm=tuple(F.mul(z,F.inv(pivot)) for z in t)
        if norm not in got:got.add(norm);mats.append(norm)
    assert len(mats)==q*(q*q-1)
    return mats

def ad(v,g,F):
    a,b,c,d=g
    z=F.sub(F.mul(a,d),F.mul(b,c));iz=F.inv(z)
    # X=[[h,e],[f,-h]]
    e,f,h=v
    X=(h,e,f,F.neg(h))
    prod=(F.add(F.mul(a,X[0]),F.mul(b,X[2])),
          F.add(F.mul(a,X[1]),F.mul(b,X[3])),
          F.add(F.mul(c,X[0]),F.mul(d,X[2])),
          F.add(F.mul(c,X[1]),F.mul(d,X[3])))
    invg=(F.mul(d,iz),F.mul(F.neg(b),iz),F.mul(F.neg(c),iz),F.mul(a,iz))
    out=(F.add(F.mul(prod[0],invg[0]),F.mul(prod[1],invg[2])),
         F.add(F.mul(prod[0],invg[1]),F.mul(prod[1],invg[3])),
         F.add(F.mul(prod[2],invg[0]),F.mul(prod[3],invg[2])),
         F.add(F.mul(prod[2],invg[1]),F.mul(prod[3],invg[3])))
    assert out[3]==F.neg(out[0]);return (out[1],out[2],out[0])

def run(q):
    F=Fclass=F_factory(q)
    projs=proj_reps(F);q3=q*q*q
    accepted=[]; counts=Counter(); maps={}
    for v in projs:
        for w in projs:
            condition=proportional(bracket(w,v,F),w,F)
            geo= v==w or (discrim(w,F)==0 and pair(v,w,F)==0)
            assert condition==geo,(q,v,w,condition,geo)
            if condition:
                assert direct_rb(v,w,F)
                component='intersection' if (v==w and discrim(w,F)==0) else 'diagonal' if v==w else 'tangent'
                counts[component]+=1
                for s in range(1,q):
                    key=rmat(v,w,s,F)
                    assert key not in maps
                    maps[key]=(v,w,s)
                accepted.append((v,w))
            else:
                assert not direct_rb(v,w,F)
    expect_projective=2*q*q+2*q+1
    expect_affine=2*q3-q-1
    assert len(accepted)==expect_projective
    assert len(maps)==expect_affine
    assert counts=={'intersection':q+1,'diagonal':q*q,'tangent':q*(q+1)}
    orbit_sizes=None
    if q in (3,5):
        gs=gl2_reps(F)
        orbit_sizes=[]
        remaining=set(maps)
        while remaining:
            seed=min(remaining)
            v,w,s=maps[seed]
            orb={rmat(ad(v,g,F),ad(w,g,F),s,F) for g in gs}
            assert orb<=remaining,('orbit escaped',q,len(orb))
            orbit_sizes.append(len(orb));remaining-=orb
        orbit_sizes.sort()
        predicted=sorted([(q*q-1)//2]*2+[q*(q+1)//2]*(q-1)+[q*(q-1)//2]*(q-1)+[q*(q*q-1)])
        assert orbit_sizes==predicted,(q,orbit_sizes,predicted)
    print('q=%d; projective=%d; diagonal_only=%d, tangent_only=%d, overlap=%d; rank_one=%d; orbits=%s; PASS'%
          (q,len(accepted),counts['diagonal'],counts['tangent'],counts['intersection'],len(maps),orbit_sizes))

def F_factory(q):return F(q)

if __name__=='__main__':
    for q in (3,5,7,9):run(q)
    print('RANK_ONE_SL2_ROTA_BAXTER_GEOMETRY_OK 4_FINITE_FIELDS 2_EXACT_ORBIT_CHECKS')
