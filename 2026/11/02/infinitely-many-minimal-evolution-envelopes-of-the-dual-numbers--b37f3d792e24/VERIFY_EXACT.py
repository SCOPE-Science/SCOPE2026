#!/usr/bin/env python3
"""Exact rational verification of the evolution-algebra envelope family."""
from fractions import Fraction as F

def solve3(A,b):
    x=[[F(q) for q in row]+[F(z)] for row,z in zip(A,b)]
    for j in range(3):
        k=next(i for i in range(j,3) if x[i][j]);x[j],x[k]=x[k],x[j]
        v=x[j][j];x[j]=[t/v for t in x[j]]
        for i in range(3):
            if i!=j:
                v=x[i][j];x[i]=[u-v*t for u,t in zip(x[i],x[j])]
    return [row[3] for row in x]

def verify(lam):
    t=F(lam)
    beta=[F(1),F(2),t]
    V=[[F(1) for i in range(3)],beta,[x*x for x in beta]]
    w=solve3(V,[1,0,0]); z=solve3(V,[0,1,0]);
    assert all(w)
    assert all(sum(q*co for q,co in zip(row,w))==rhs for row,rhs in zip(V,[1,0,0]))
    assert all(sum(q*co for q,co in zip(row,z))==rhs for row,rhs in zip(V,[0,1,0]))
    assert sum(w)==1 and sum(z)==0
    # For all (s,t),(u,v) in a finite verification grid, check formula in A=C[epsilon]/epsilon^2.
    for s in range(-2,3):
      for tt in range(-2,3):
       for u in range(-2,3):
        for v in range(-2,3):
         p=[(F(s)+b*tt)*(F(u)+b*v) for b in beta]
         assert (sum(p[i]*w[i] for i in range(3)),sum(p[i]*z[i] for i in range(3)))==(s*u,s*v+tt*u)
    r=[z[i]/w[i] for i in range(3)]
    tr=sum(r); sq=sum(x*x for x in r)
    assert sq!=0
    inv=tr*tr/sq
    expect=2*(3*t+2)**2/(7*t*t+6*t+4)
    assert inv==expect,(lam,inv,expect)
    return w,z,r,inv
vals=[]
for lam in range(3,24):
    w,z,r,I=verify(lam)
    vals.append(I)
    print(f'lambda={lam} w={w} z={z} spectrum={r} invariant={I}')
assert all(vals[i]>vals[i+1] for i in range(len(vals)-1))
# Symbolic identity: numerator of derivative is 4(3lambda+2)(12-10lambda)/D^2, negative for lambda>=3.
print('VERIFY_OK')
