#!/usr/bin/env python3
"""Exact harmonic interpolation certificate for the 31 icosahedral symmetry axes.
Standard-library only. The characteristic-zero calculation covers all low
singular degrees; modular determinants and a uniform Legendre bound cover all
higher degrees without numerical extrapolation.
"""
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
from time import monotonic

class Q5:
    __slots__=('a','b')
    def __init__(self,a=0,b=0):
        if isinstance(a,Q5):self.a,self.b=a.a,a.b
        else:self.a,self.b=F(a),F(b)
    def __add__(self,o):
        o=Q5(o);return Q5(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return Q5(-self.a,-self.b)
    def __sub__(self,o):return self+(-Q5(o))
    def __rsub__(self,o):return Q5(o)-self
    def __mul__(self,o):
        o=Q5(o);return Q5(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=Q5(o);d=o.a*o.a-5*o.b*o.b
        if not d:raise ZeroDivisionError
        return Q5((self.a*o.a-5*self.b*o.b)/d,(self.b*o.a-self.a*o.b)/d)
    def __rtruediv__(self,o):return Q5(o)/self
    def __eq__(self,o):
        o=Q5(o);return self.a==o.a and self.b==o.b
    def __bool__(self):return bool(self.a or self.b)
    def __hash__(self):return hash((self.a,self.b))
    def __pow__(self,k):
        assert isinstance(k,int) and k>=0
        v=Q5(1);a=self
        while k:
            if k&1:v*=a
            a*=a;k//=2
        return v
    def __repr__(self):return '(%s)+(%s)*sqrt(5)'%(self.a,self.b)
    def sign(self):
        if not self:return 0
        if not self.b:return 1 if self.a>0 else -1
        if not self.a:return 1 if self.b>0 else -1
        if self.a*self.b>0:return 1 if self.a>0 else -1
        diff=self.a*self.a-5*self.b*self.b
        assert diff
        return (1 if diff>0 else -1)*(1 if self.a>0 else -1)
    def mod(self,p,r):
        def red(x):return (x.numerator%p)*pow(x.denominator%p,-1,p)%p
        return (red(self.a)+r*red(self.b))%p

phi=Q5(F(1,2),F(1,2));phi_inv=phi-1
ONE=Q5(1);ZERO=Q5(0);NI=phi+2;ND=Q5(3)
I=[];D=[];M=[]
for a,b in product((-1,1),repeat=2):
    for coords in ((ZERO,Q5(a),Q5(b)*phi),(Q5(b)*phi,ZERO,Q5(a)),(Q5(a),Q5(b)*phi,ZERO)):
        I.append(coords)
for s in product((-1,1),repeat=3):D.append(tuple(Q5(t) for t in s))
for a,b in product((-1,1),repeat=2):
    for coords in ((ZERO,Q5(a)*phi,Q5(b)*phi_inv),(Q5(b)*phi_inv,ZERO,Q5(a)*phi),(Q5(a)*phi,Q5(b)*phi_inv,ZERO)):
        D.append(coords)

def dot(x,y):return sum((a*b for a,b in zip(x,y)),ZERO)
for i,u in enumerate(I):
    for v in I[i+1:]:
        if dot(tuple(a-b for a,b in zip(u,v)),tuple(a-b for a,b in zip(u,v)))==4:
            M.append(tuple((a+b)/(2*phi) for a,b in zip(u,v)))
assert len(I)==12 and len(D)==20 and len(M)==30
assert all(dot(v,v)==NI for v in I)
assert all(dot(v,v)==ND for v in D)
assert all(dot(v,v)==ONE for v in M)

points=[]
for label,vs,norm in [('I',I,NI),('D',D,ND),('M',M,ONE)]:
    for v in vs:
        if next(x for x in v if x).sign()>0:points.append((label,v,norm))
assert len(points)==31 and [sum(t==a for t,_,_ in points) for a in 'IDM']==[6,10,15]
assert len({tuple(str(z) for z in v) for _,v,_ in points})==31

# The Gram entries are in Q(sqrt(5)) in both parities. For odd degree
# positive diagonal congruence removes normalization square roots.
Z=[];PAIR=[]
for t,x,nx in points:
    rr=[]
    for u,y,ny in points:
        raw=dot(x,y);z=raw*raw/(nx*ny)
        assert (ONE-z).sign()>=0
        rr.append((raw,z))
        Z.append(z)
    PAIR.append(rr)
Z=sorted(set(Z),key=lambda v:float(v.a)+float(v.b)*5**.5)
zi={v:i for i,v in enumerate(Z)}
PAIRIDX=[[(raw,zi[z]) for raw,z in row] for row in PAIR]
assert len(Z)<35
# All non-antipodal distinct directions have squared dot strictly below 22/25.
# This implies sine separation above sqrt(3/25)=0.3464, insufficient for
# 1700 at a 30-row factor; use exact stronger t bound below.
MAX_Z=max((PAIR[i][j][1] for i in range(31) for j in range(i+1,31)),key=lambda v:float(v.a)+float(v.b)*5**.5)
assert MAX_Z==Q5(F(1,2),F(1,6))
assert (Q5(F(7,8))-MAX_Z).sign()>0,MAX_Z # implies sine > sqrt(1/8) > 0.35

def parts(k,z):
    E,O=ONE,ONE
    for h in range(k//2):
        En=((4*h+3)*z*O-(2*h+1)*E)/(2*h+2)
        On=((4*h+5)*En-(2*h+2)*O)/(2*h+3)
        E,O=En,On
    return E if not k%2 else O

def gram(k):
    pp=[parts(k,z) for z in Z]
    return [[pp[iz]*(raw if k%2 else ONE) for raw,iz in row] for row in PAIRIDX]

def rank_Q5(K):
    n=len(K);A=[row[:] for row in K];r=0
    for j in range(n):
        q=next((i for i in range(r,n) if A[i][j]),None)
        if q is None:continue
        A[r],A[q]=A[q],A[r]
        inv=ONE/A[r][j]
        for i in range(r+1,n):
            if A[i][j]:
                scale=A[i][j]*inv
                for h in range(j+1,n):A[i][h]-=scale*A[r][h]
                A[i][j]=ZERO
        r+=1
        if r==n:break
    return r

def rank_mod(A,p):
    n=len(A);r=0
    for j in range(n):
        q=next((i for i in range(r,n) if A[i][j]),None)
        if q is None:continue
        A[r],A[q]=A[q],A[r]
        inv=pow(A[r][j],-1,p)
        for i in range(r+1,n):
            if A[i][j]:
                s=A[i][j]*inv%p
                row_i=A[i];row_r=A[r]
                for h in range(j+1,n):row_i[h]=(row_i[h]-s*row_r[h])%p
                row_i[j]=0
        r+=1
        if r==n:break
    return r

def all_modular_ranks(p,r5,begin,end):
    zs=[v.mod(p,r5) for v in Z]
    raws=[[d.mod(p,r5) for d,_ in row] for row in PAIRIDX]
    indices=[[iz for d,iz in row] for row in PAIRIDX]
    E=[1]*len(Z);O=[1]*len(Z)
    exceptions=[];reached=[]
    for h in range((end+1)//2+1):
        for k,pv in ((2*h,E),(2*h+1,O)):
            if k<begin or k>=end:continue
            isodd=k&1
            A=[[pv[indices[i][j]]*(raws[i][j] if isodd else 1)%p for j in range(31)] for i in range(31)]
            r=rank_mod(A,p)
            if r!=31:exceptions.append((k,r))
            reached.append(k)
        # update E,O for next pair
        En=[((4*h+3)*zs[i]*O[i]-(2*h+1)*E[i])*pow(2*h+2,-1,p)%p for i in range(len(Z))]
        On=[((4*h+5)*En[i]-(2*h+2)*O[i])*pow(2*h+3,-1,p)%p for i in range(len(Z))]
        E,O=En,On
    assert len(reached)==end-begin
    return exceptions

if __name__=='__main__':
    import time
    start=monotonic()
    print('NODES',len(points),'DOT_SQUARES',len(Z),'MAX_SQUARE',repr(MAX_Z),flush=True)
    expected=[]
    for k in range(0,75):
        q=rank_Q5(gram(k));expected.append(q)
        print('EXACT_RANK',k,q,flush=True)
    TARGET_RANKS=[1,3,5,7,9,11,10,15,14,19,15,18,19,22,19,22,24,25,24,25,29,25,29,28,29,28,29,28,29,31,30,31,29,28,29,31,30,31,29,31,30,31,30,31,29,31,30,31,30,31,30,31,30,31,30,31,30,31,30,31,31,31,30,31,30,31,31,31,30,31,31,31,31,31,30]
    assert expected==TARGET_RANKS, (expected,TARGET_RANKS)
    print('FIRST_75',expected,flush=True)
    p=10009
    assert all(p%d for d in range(2,int(p**0.5)+1))
    r5=next(a for a in range(p) if a*a%p==5)
    assert r5*r5%p==5
    print('MODULUS',p,r5,flush=True)
    bad=all_modular_ranks(p,r5,75,1700)
    print('EXCEPTIONS_75_1699',bad,flush=True)
    # Exact geometric bound |cos angle|^2 < 7/8 (true from MAX_Z).
    # Then sin angle > sqrt(1/8)>7/20 (49/400<1/8).
    # Bernstein yields |P_k| <= sqrt(2/(pi*k*sin(theta))).
    # Gershgorin: 30*sqrt(2/((157/50)*1700*(7/20))) < 1.
    assert 30**2*2*50*20 < 157*1700*7
    assert not bad
    print('ICOSAHEDRAL_31_AXES_ALL_DEGREE_CERTIFICATE_OK',round(monotonic()-start,2),flush=True)
