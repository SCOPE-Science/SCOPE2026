#!/usr/bin/env python3
from collections import defaultdict

# Sparse integer polynomials in x,y,z for exact identity checks.
def clean(P): return {m:c for m,c in P.items() if c}
def add(P,Q):
    R=dict(P)
    for m,c in Q.items(): R[m]=R.get(m,0)+c
    return clean(R)
def neg(P): return {m:-c for m,c in P.items()}
def sub(P,Q): return add(P,neg(Q))
def mul(P,Q):
    R={}
    for a,ca in P.items():
      for b,cb in Q.items():
        m=tuple(i+j for i,j in zip(a,b)); R[m]=R.get(m,0)+ca*cb
    return clean(R)
def sc(c,P): return clean({m:c*v for m,v in P.items()})
def pw(P,n):
    R={(0,0,0):1}
    for _ in range(n): R=mul(R,P)
    return R
C=lambda n:{(0,0,0):n} if n else {}
x={(1,0,0):1}; y={(0,1,0):1}; z={(0,0,1):1}
S=add(add(x,y),z)
E2=add(add(mul(x,y),mul(x,z)),mul(y,z))
E3=mul(mul(x,y),z)
R=sub(pw(S,2),sc(3,E2))
D=sub(mul(S,E2),sc(9,E3))
assert sub(D,sc(2,mul(x,R))) == sc(-1,mul(mul(sub(x,y),sub(x,z)),sub(sc(2,x),add(y,z))))
assert sub(D,sc(2,mul(y,R))) == sc(-1,mul(mul(sub(x,y),sub(y,z)),add(sub(x,sc(2,y)),z)))
assert sub(D,sc(2,mul(z,R))) == mul(mul(sub(x,z),sub(y,z)),sub(add(x,y),sc(2,z)))
assert sub(sc(3,D),sc(2,mul(S,R))) == sc(-1,mul(mul(add(sub(x,sc(2,y)),z),sub(add(x,y),sc(2,z))),sub(sc(2,x),add(y,z))))

def norm(v,p):
    v=tuple(t%p for t in v)
    for t in v:
        if t:
            inv=pow(t,-1,p)
            return tuple(a*inv%p for a in v)
    return None

def census(p):
    reps=[(a,b,1) for a in range(p) for b in range(p)] + [(a,1,0) for a in range(p)] + [(1,0,0)]
    fibers=defaultdict(list); exceptional=set(); smooth=[]
    for X,Y,Z in reps:
        s=(X+Y+Z)%p
        if X*Y*Z*s%p==0: continue
        if (X-Y)%p==0 and (Y-Z)%p==0: continue
        G=(Y*Z*(2*X-Y-Z), X*Z*(2*Y-X-Z), X*Y*(2*Z-X-Y))
        g=norm(G,p); assert g is not None
        P=(X,Y,Z); fibers[g].append(P); smooth.append(P)
        r=(X*X+Y*Y+Z*Z-X*Y-X*Z-Y*Z)%p
        d=((X+Y+Z)*(X*Y+X*Z+Y*Z)-9*X*Y*Z)%p
        h=((X-Y)*(X-Z)*(Y-Z)*(2*X-Y-Z)*(X-2*Y+Z)*(X+Y-2*Z))%p
        if r==0 or d==0 or h==0: exceptional.add(P)
    sizes=[len(v) for v in fibers.values()]
    assert max(sizes)<=2
    singles={P for v in fibers.values() if len(v)==1 for P in v}
    assert singles==exceptional
    n1=sizes.count(1); n2=sizes.count(2)
    assert len(smooth)==(p-1)*(p-2)
    if p%3==1:
        assert n1==9*p-33
        assert n2==(p-5)*(p-7)//2
        assert len(fibers)==(p*p+6*p-31)//2
    else:
        assert n1==7*p-23
        assert n2==(p-5)*(p-5)//2
        assert len(fibers)==(p*p+4*p-21)//2
    assert n1+2*n2==len(smooth)
    return p,n1,n2,len(fibers)

for p in (5,7,11,13,17,19,23,29,31,37,41,43):
    census(p)
print('VERIFY_OK')
