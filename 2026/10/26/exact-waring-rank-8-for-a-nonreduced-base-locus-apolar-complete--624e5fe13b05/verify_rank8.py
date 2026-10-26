"""Exact checks of the degree-six apolar instance; Python standard library only.
The lower-bound proof is geometric and is not replaced by these checks.
"""
from math import factorial
from itertools import combinations

# Homogeneous polynomials are sparse integer coefficient dictionaries.
def add(*polys):
    out={}
    for p in polys:
        for mon,c in p.items():out[mon]=out.get(mon,0)+c
    return {m:c for m,c in out.items() if c}
def neg(p):return {m:-c for m,c in p.items()}
def mul(a,b):
    out={}
    for m,c in a.items():
        for n,d in b.items():
            k=tuple(m[i]+n[i] for i in range(3));out[k]=out.get(k,0)+c*d
    return {m:c for m,c in out.items() if c}
def mon(a,b,c,k=1):return {(a,b,c):k}
def diff(p,k):
    out={}
    for a,c in p.items():
        if a[k]:
            b=list(a);b[k]-=1;out[tuple(b)]=out.get(tuple(b),0)+a[k]*c
    return out
def deriv(p,ds):
    for k in ds:p=diff(p,k)
    return p
def lm(p):return max(p,key=lambda v:(sum(v),v[0],v[1],v[2]))
def shift(p,m,c=1):return {tuple(v[i]+m[i] for i in range(3)):c*a for v,a in p.items()}
def divides(a,b):return all(a[i]<=b[i] for i in range(3))
def remainder(p,G):
    p=dict(p);r={}
    while p:
        m=lm(p);c=p[m]
        for g in G:
            n=lm(g)
            if divides(n,m):
                delta=tuple(m[i]-n[i] for i in range(3))
                p=add(p,neg(shift(g,delta,c//g[n])))
                break
        else:
            r[m]=c;p.pop(m)
    return r
X=mon(1,0,0);Y=mon(0,1,0);Z=mon(0,0,1)
X2=mul(X,X); Y2=mul(Y,Y); Z2=mul(Z,Z)
q1=add(Y2,neg(Z2));q2=mul(X,Y)
x5=mon(5,0,0);z5=mon(0,0,5)
g=add(x5,neg(z5))
F=add(mon(5,0,1,6),mon(0,6,0),mon(0,4,2,15),mon(0,2,4,15),mon(0,0,6))
assert add(deriv(F,(1,1)),neg(deriv(F,(2,2))))=={}
assert deriv(F,(0,1))=={}
assert add(deriv(F,(0,0,0,0,0)),neg(deriv(F,(2,2,2,2,2))))=={}
G=[q2,mul(Y,q1),add(mon(6,0,0),mul(mon(0,0,4),q1))]
for i,j in combinations(range(3),2):
    a,b=lm(G[i]),lm(G[j]);lc=tuple(max(a[k],b[k]) for k in range(3))
    s=add(shift(G[i],tuple(lc[k]-a[k] for k in range(3))),neg(shift(G[j],tuple(lc[k]-b[k] for k in range(3)))))
    assert remainder(s,G)=={},(i,j,s)
assert [lm(h) for h in G]==[(1,1,0),(0,3,0),(6,0,0)]
# Upper-bound inclusion certificate.
identity=add(mul(X,g),mul(mon(0,1,3),q2),mul(add(mon(0,0,4),neg(mon(1,0,3))),q1))
assert identity==G[2]
print('VERIFY_OK: apolar differential identities; 3 Buchberger S-pairs; upper-bound inclusion certificate')
