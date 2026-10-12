#!/usr/bin/env python3
from fractions import Fraction

# Univariate polynomials in l, coefficient tuples low-to-high.
def trim(p):
    p = tuple(Fraction(c) for c in p)
    i = len(p) - 1
    while i > 0 and p[i] == 0:
        i -= 1
    return p[:i+1]

def padd(a,b):
    n=max(len(a),len(b)); out=[Fraction(0)]*n
    for i in range(n):
        out[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    return trim(out)

def pneg(a): return trim([-c for c in a])
def psub(a,b): return padd(a,pneg(b))
def pmul(a,b):
    out=[Fraction(0)]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b): out[i+j]+=ai*bj
    return trim(out)
def ppow(a,n):
    out=(Fraction(1),)
    for _ in range(n): out=pmul(out,a)
    return out

class RF:
    def __init__(self,n=0,d=1):
        self.n=trim(n if isinstance(n,(tuple,list)) else (Fraction(n),))
        self.d=trim(d if isinstance(d,(tuple,list)) else (Fraction(d),))
        assert any(self.d)
    def __add__(self,o):
        o=asrf(o); return RF(padd(pmul(self.n,o.d),pmul(o.n,self.d)),pmul(self.d,o.d))
    __radd__=__add__
    def __neg__(self): return RF(pneg(self.n),self.d)
    def __sub__(self,o): return self+(-asrf(o))
    def __rsub__(self,o): return asrf(o)-self
    def __mul__(self,o):
        o=asrf(o); return RF(pmul(self.n,o.n),pmul(self.d,o.d))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=asrf(o); assert any(o.n); return RF(pmul(self.n,o.d),pmul(self.d,o.n))
    def __rtruediv__(self,o): return asrf(o)/self
    def __pow__(self,n):
        assert n>=0; return RF(ppow(self.n,n),ppow(self.d,n))
    def __eq__(self,o):
        o=asrf(o); return trim(pmul(self.n,o.d))==trim(pmul(o.n,self.d))
    def __repr__(self): return f"RF({self.n}/{self.d})"

def asrf(x): return x if isinstance(x,RF) else RF(x)

l=RF((0,1)); one=RF(1)

# Sparse homogeneous polynomials in x,y,z with RF coefficients.
def clean(P): return {m:c for m,c in P.items() if not c==0}
def add(P,Q):
    R=dict(P)
    for m,c in Q.items(): R[m]=R.get(m,RF(0))+c
    return clean(R)
def neg(P): return {m:-c for m,c in P.items()}
def sub(P,Q): return add(P,neg(Q))
def mul(P,Q):
    R={}
    for a,ca in P.items():
        for b,cb in Q.items():
            m=tuple(a[i]+b[i] for i in range(3)); R[m]=R.get(m,RF(0))+ca*cb
    return clean(R)
def scale(c,P): return clean({m:asrf(c)*v for m,v in P.items()})
def peq(P,Q):
    keys=set(P)|set(Q)
    return all(P.get(k,RF(0))==Q.get(k,RF(0)) for k in keys)

def var(i):
    e=[0,0,0]; e[i]=1; return {tuple(e):RF(1)}
X,Y,Z=var(0),var(1),var(2)
def sq(P): return mul(P,P)

def Lf(X,Y,Z): return add(add(mul(X,Y),mul(X,Z)),mul(Y,Z))
def Gf(t,X,Y,Z):
    return sub(sub(sub(sq(X),scale(one+t,mul(X,Y))),scale(t,mul(X,Z))),scale(one+t,mul(Y,Z)))
def Df(t,X,Y,Z):
    inv=one/t
    return sub(sub(sub(sq(Z),scale(one+inv,mul(X,Y))),scale(inv,mul(X,Z))),scale(one+inv,mul(Y,Z)))
def conic(name,t,X=X,Y=Y,Z=Z): return {'L':Lf,'G':Gf,'D':Df}[name](t,X,Y,Z) if name!='L' else Lf(X,Y,Z)

def lin(a,b,d,e,h):
    return add(scale(a,X),scale(b,Z)), scale(h,Y), add(scale(d,X),scale(e,Z))

maps=[
    ('id', l, (1,0,0,1,1), ('L','G','D'), (1,1,1)),
    ('swap_GD', one/l, (0,1,1,0,1), ('L','D','G'), (1,1,1)),
    ('swap_LG', -l-one, ((l+one)/l,0,-one/l,1,(l+one)**2/l**2), ('G','L','D'), ((l+one)**2/l,-(l+one)/l**2,1)),
    ('cycle_LGD', -(l+one)/l, (0,-(l+one)/l,-one/l,1,-(l+one)**2/l), ('G','D','L'), ((l+one)**2/l**3,one/l**2,-(l+one)/l)),
    ('cycle_LDG', -one/(l+one), (-one/(l+one),l/(l+one),1,0,(l+one)/l), ('D','L','G'), (l,-one/(l+one),l**2/(l+one)**2)),
    ('swap_LD', -l/(l+one), (one/(l+one),-l/(l+one),0,1,l+one), ('D','G','L'), (one/l,one/(l+one)**2,-l/(l+one))),
]

for name,mu,coeffs,perm,scalars in maps:
    Xp,Yp,Zp=lin(*coeffs)
    for src,target,k in zip(('L','G','D'),perm,scalars):
        lhs=conic(target,mu,Xp,Yp,Zp)
        rhs=scale(k,conic(src,l))
        assert peq(lhs,rhs), (name,src,target)

# J as a rational function and invariance under all six transforms.
def J(t): return RF(256)*(t*t+t+one)**3/(t*t*(t+one)**2)
for name,mu,*_ in maps:
    assert J(mu)==J(l), name

# Bivariate integer-polynomial check for numerator factorization.
def bclean(P): return {k:v for k,v in P.items() if v}
def badd(P,Q):
    R=dict(P)
    for m,c in Q.items(): R[m]=R.get(m,0)+c
    return bclean(R)
def bneg(P): return {m:-c for m,c in P.items()}
def bsub(P,Q): return badd(P,bneg(Q))
def bmul(P,Q):
    R={}
    for (i,j),a in P.items():
        for (k,r),b in Q.items(): R[(i+k,j+r)]=R.get((i+k,j+r),0)+a*b
    return bclean(R)
def bpow(P,n):
    R={(0,0):1}
    for _ in range(n): R=bmul(R,P)
    return R
BL={(1,0):1}; BM={(0,1):1}; BO={(0,0):1}
def bs(c): return {(0,0):c}
left=bsub(
    bmul(bpow(badd(badd(bpow(BL,2),BL),BO),3), bmul(bpow(BM,2),bpow(badd(BM,BO),2))),
    bmul(bpow(badd(badd(bpow(BM,2),BM),BO),3), bmul(bpow(BL,2),bpow(badd(BL,BO),2)))
)
factors=[
    bsub(BL,BM),
    bsub(bmul(BL,BM),BO),
    badd(badd(BL,BM),BO),
    badd(badd(bmul(BL,BM),BL),BO),
    badd(badd(bmul(BL,BM),BL),BM),
    badd(badd(bmul(BL,BM),BM),BO),
]
right=BO
for f in factors: right=bmul(right,f)
assert left==right

# Fixed-point identities for the five nonidentity transforms.
assert one/l-l == RF((1,0,-1),(0,1))
assert (-l-one)-l == RF((-1,-2))
assert (-(l+one)/l)-l == RF((-1,-1,-1),(0,1))
assert (-one/(l+one))-l == RF((-1,-1,-1),(1,1))
assert (-l/(l+one))-l == RF((0,-2,-1),(1,1))

print('VERIFY_OK')
