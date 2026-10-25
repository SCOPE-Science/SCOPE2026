#!/usr/bin/env python3
"""Exact, standard-library verification of a hyperelliptic Hasse-divisor calculation."""
P=11
# Polynomial in a (tuple of mod-11 coefficients, lowest degree first).
def norm(v):
    v=list(v)
    while len(v)>1 and not v[-1]: v.pop()
    return tuple((x%P) for x in v)
def add(a,b):
    return norm([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def mul(a,b):
    o=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):o[i+j]=(o[i+j]+x*y)%P
    return norm(o)
def neg(a):return tuple((-x)%P for x in a)
def sub(a,b):return add(a,neg(b))
def deriv(a):return norm([i*a[i] for i in range(1,len(a))] or [0])
def rem(a,b):
    assert b!=(0,)
    a=list(a); lb=len(b)-1; inv=pow(b[-1],-1,P)
    while len(a)-1>=lb and any(a):
        shift=len(a)-1-lb; fac=a[-1]*inv%P
        for j,x in enumerate(b):a[shift+j]=(a[shift+j]-fac*x)%P
        a=list(norm(a))
    return norm(a)
def gcd(a,b):
    while b!=(0,): a,b=b,rem(a,b)
    return norm([x*pow(a[-1],-1,P) for x in a])
zero=(0,); one=(1,); avar=(0,1)
# Dict of powers of z to coefficient polynomials in a.
poly={0:one}
for _ in range(5):
    nxt={}
    for z,c in poly.items():
        for dz,co in [(0,one),(1,avar),(2,one)]:
            nxt[z+dz]=add(nxt.get(z+dz,zero),mul(c,co))
    poly=nxt
u=sub((5,),mul(avar,avar))
v=mul(avar,mul(sub(mul(avar,avar),(3,)),add(mul(avar,avar),one)))
assert poly[2]==u==poly[8],(poly[2],u,poly[8])
assert poly[5]==v,(poly[5],v)
# All H_ij = [x^(11*i-j)] f(x)^5, and [x^m] vanishes if 4 does not divide m.
H={}
for i in range(1,4):
    for j in range(1,4):
        m=11*i-j
        H[(i,j)]=poly.get(m//4,zero) if m%4==0 else zero
assert [H[i,j] for i in range(1,4) for j in range(1,4)]==[zero,zero,u,zero,v,zero,u,zero,zero]
assert gcd(u,v)==one
assert gcd(u,deriv(u))==one
assert gcd(v,deriv(v))==one
# The determinant is -u*u*v, with no root shared by u and v.
det=neg(mul(mul(u,u),v))
assert len(det)-1==9
assert det==neg(mul(mul(sub((5,),mul(avar,avar)),sub((5,),mul(avar,avar))),v))
# Concrete F_11 points corroborate but do not establish geometric completeness.
def ev(f,t):
    return sum(x*pow(t,i,P) for i,x in enumerate(f))%P
strata={1:[],2:[],3:[]}
for a in range(P):
    if (a*a-4)%P==0:continue
    c=ev(u,a);d=ev(v,a)
    strata[ (int(c!=0)*2+int(d!=0)) ].append(a)
assert strata=={1:[4,7],2:[0,5,6],3:[1,3,8,10]},strata
print('VERIFY_OK: characteristic-eleven Hasse-Witt identity, determinant, disjoint squarefree factors, and finite-field spot checks')
