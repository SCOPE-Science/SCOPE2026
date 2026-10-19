#!/usr/bin/env python3
"""Exact H3 harmonic sampling rank verification; Python 3 standard library only."""
from fractions import Fraction as F
from itertools import product
from math import isqrt

class Q5:
    __slots__ = ('a','b')
    def __init__(self,a=0,b=0): self.a,self.b=F(a),F(b)
    @staticmethod
    def cast(z): return z if isinstance(z,Q5) else Q5(z)
    def __add__(self,z):
        z=Q5.cast(z); return Q5(self.a+z.a,self.b+z.b)
    __radd__=__add__
    def __neg__(self): return Q5(-self.a,-self.b)
    def __sub__(self,z): return self+-Q5.cast(z)
    def __rsub__(self,z): return Q5.cast(z)+-self
    def __mul__(self,z):
        z=Q5.cast(z);return Q5(self.a*z.a+5*self.b*z.b,self.a*z.b+self.b*z.a)
    __rmul__=__mul__
    def __truediv__(self,z):
        z=Q5.cast(z);d=z.a*z.a-5*z.b*z.b
        assert d
        return Q5((self.a*z.a-5*self.b*z.b)/d,(self.b*z.a-self.a*z.b)/d)
    def __eq__(self,z):
        z=Q5.cast(z);return self.a==z.a and self.b==z.b
    def __repr__(self):return f'({self.a})+({self.b})*sqrt(5)'

ZERO,ONE=Q5(0),Q5(1)
base=(Q5(F(1,2)),Q5(F(1,4),F(1,4)),Q5(F(-1,4),F(1,4)))
roots=[]
for j in range(3):
    t=base[j:]+base[:j]
    for s,tg in product((-1,1),repeat=2):
        roots.append((t[0],s*t[1],tg*t[2]))
roots += [(ONE,ZERO,ZERO),(ZERO,ONE,ZERO),(ZERO,ZERO,ONE)]
assert len(roots)==15
D=[[sum((u*v for u,v in zip(x,y)),ZERO) for y in roots] for x in roots]
assert all(D[i][i]==ONE for i in range(15))
a=Q5(F(-1,4),F(1,4));b=Q5(F(1,2));c=Q5(F(1,4),F(1,4))
allowed=(ZERO,a,-a,b,-b,c,-c)
counts={str(t):0 for t in (ZERO,a,b,c)}
for i in range(15):
    for j in range(i+1,15):
        x=D[i][j];assert x in allowed
        for t in (ZERO,a,b,c):
            if x==t or x==-t:
                counts[str(t)]+=1;break
assert list(counts.values())==[15,30,30,30],counts
for i in range(15):
    assert sum(D[i][j]==ZERO for j in range(15) if i!=j)==2
    assert sum(D[i][j] in (a,-a) for j in range(15) if i!=j)==4
    assert sum(D[i][j] in (b,-b) for j in range(15) if i!=j)==4
    assert sum(D[i][j] in (c,-c) for j in range(15) if i!=j)==4

def polys_exact(k):
    prev=[[ONE for j in range(15)] for i in range(15)]
    if k==0:return prev
    cur=D
    for l in range(1,k):
        nex=[[( (2*l+1)*D[i][j]*cur[i][j]-l*prev[i][j])/(l+1) for j in range(15)] for i in range(15)]
        prev,cur=cur,nex
    return cur

def rank_q5(mat):
    a=[row[:] for row in mat];h=len(a);w=len(a[0]);row=0
    for col in range(w):
        pivot=next((i for i in range(row,h) if a[i][col]!=ZERO),None)
        if pivot is None:continue
        a[row],a[pivot]=a[pivot],a[row]
        factor=a[row][col]
        for j in range(col,w):a[row][j]=a[row][j]/factor
        for i in range(row+1,h):
            if a[i][col]!=ZERO:
                factor=a[i][col]
                for j in range(col,w):a[i][j]=a[i][j]-factor*a[row][j]
        row+=1
        if row==h:break
    return row

ranks=[rank_q5(polys_exact(k)) for k in range(16)]
assert ranks==[1,3,5,7,9,11,10,15,14,15,15,15,15,15,14,15],ranks
for k in (8,14):
    m=polys_exact(k)
    assert all(sum(row,ZERO)==ZERO for row in m)

# Modular reductions prove nonzero characteristic-zero determinants.
# A nonzero determinant in some reduction is a sufficient (not necessary) witness.
def isprime(p):
    return p>=2 and all(p%d for d in range(2,isqrt(p)+1))
def mod_of(x,p,r):
    def frac(z):return (z.numerator*pow(z.denominator,-1,p))%p
    return (frac(x.a)+r*frac(x.b))%p

def det_p(m,p):
    a=[row[:] for row in m];n=len(a);out=1
    for j in range(n):
        pivot=next((k for k in range(j,n) if a[k][j]%p),None)
        if pivot is None:return 0
        if pivot!=j:
            a[pivot],a[j]=a[j],a[pivot];out=(-out)%p
        pivot_value=a[j][j]%p
        out=(out*pivot_value)%p
        inv=pow(pivot_value,-1,p)
        for k in range(j+1,n):
            mul=a[k][j]*inv%p
            if mul:
                for t in range(j,n):a[k][t]=(a[k][t]-mul*a[j][t])%p
    return out

def modular_determinants(p,r):
    dots=[[mod_of(D[i][j],p,r) for j in range(15)] for i in range(15)]
    prev=[[1]*15 for i in range(15)]
    cur=dots
    dets=[]
    for l in range(216):
        if l==0:x=prev
        elif l==1:x=cur
        else:
            inv=pow(l,-1,p)
            nex=[[( (2*l-1)*dots[i][j]*cur[i][j]-(l-1)*prev[i][j])*inv%p for j in range(15)] for i in range(15)]
            prev,cur=cur,nex;x=cur
        if l>=16:dets.append(det_p(x,p))
    return dets

assert isprime(1009)
assert 244*244%1009==5
D_CERT=modular_determinants(1009,244)
assert len(D_CERT)==200 and all(x for x in D_CERT)

if __name__=='__main__':
    import json
    from pathlib import Path
    cert=json.loads(Path(__file__).with_name('certificate.json').read_text())
    assert cert['prime']==1009 and cert['sqrt5_mod_prime']==244
    assert cert['degrees']==list(range(16,216))
    assert cert['determinants_mod_prime']==D_CERT
    assert cert['exact_ranks_degrees_0_to_15']==ranks
print('Geometry:',len(roots),'antipodal lines; cross-pair counts',list(counts.values()))
print('Exact field ranks degrees 0..15:',ranks)
print('Modular full-rank witnesses for degrees 16..215:',len(D_CERT), 'prime:',1009)
print('Bernstein/Gershgorin proves rank 15 for degrees >=216 (see proof).')
print('TOTAL_CHECKS:',len(roots)+105+16+2+len(D_CERT))
