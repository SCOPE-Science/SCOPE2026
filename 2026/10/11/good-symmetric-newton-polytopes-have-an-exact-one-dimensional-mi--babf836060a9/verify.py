#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations
import math
import numpy as np
from scipy.optimize import minimize

def layers(alpha,beta):
    m=len(alpha)
    return [tuple(beta[:i]+alpha[i:]) for i in range(m+1)]

def exact_center(alpha,beta):
    m=len(alpha)
    a=list(map(Fraction,alpha))
    b=list(map(Fraction,beta))
    h=[None]+[(a[j]+b[j])/2 for j in range(m)]+[None]
    c=[]
    for i in range(m+1):
        c.append((sum(b[:i],Fraction(0))+sum(a[i:],Fraction(0)))/m)

    cand=[]
    for i in range(m+1):
        lo = h[i+1] if i<m else None
        hi = h[i] if i>0 else None
        oklo = (lo is None or lo <= c[i])
        okhi = (hi is None or c[i] <= hi)
        if oklo and okhi:
            cand.append(c[i])
    for i in range(1,m+1):
        if c[i-1] <= h[i] <= c[i]:
            cand.append(h[i])

    uniq=[]
    for x in cand:
        if x not in uniq:
            uniq.append(x)
    assert len(uniq)==1,(alpha,beta,c,h,cand)
    return uniq[0]

def exact_radius2(alpha,beta,c):
    return sum(max((Fraction(x)-c)**2,(Fraction(y)-c)**2)
               for x,y in zip(alpha,beta))

def all_vertices(alpha,beta):
    vs=set()
    for lam in layers(alpha,beta):
        vs.update(permutations(lam))
    return np.array(sorted(vs),dtype=float)

cases=[
    ([3,1,0],[3,3,3]),
    ([4,2,0],[6,5,3]),
    ([7,5,2,2],[9,9,6,4]),
    ([2,2,1,0],[5,4,2,1]),
    ([3,3,0,0],[4,3,2,1]),
    ([5,4,2,1,0],[8,6,5,2,1]),
]

for alpha,beta in cases:
    assert all(alpha[i]>=alpha[i+1] for i in range(len(alpha)-1))
    assert all(beta[i]>=beta[i+1] for i in range(len(beta)-1))
    assert all(alpha[i]<=beta[i] for i in range(len(alpha)))

    c=exact_center(alpha,beta)
    r2=exact_radius2(alpha,beta,c)
    V=all_vertices(alpha,beta)
    m=len(alpha)

    # Directly verify the exact diagonal formula against all expanded source vertices.
    d2=np.sum((V-float(c))**2,axis=1)
    assert abs(np.max(d2)-float(r2))<2e-10

    # Independent ambient-space numerical minimum enclosing problem.
    # Smooth epigraph formulation: variables center z and squared-radius t.
    def obj(w):
        return w[-1]
    cons=[]
    for v in V:
        cons.append({
            "type":"ineq",
            "fun":lambda w,v=v: w[-1]-np.sum((v-w[:-1])**2)
        })
    x0=np.r_[np.full(m,float(c)),float(r2)*1.01+1e-4]
    res=minimize(
        obj,x0,method="SLSQP",constraints=cons,
        options={"ftol":1e-12,"maxiter":5000}
    )
    assert res.success,(alpha,beta,res.message)
    assert abs(res.fun-float(r2))<3e-7,(alpha,beta,res.fun,float(r2))
    assert np.max(np.abs(res.x[:-1]-float(c)))<3e-5,(alpha,beta,res.x,c)

# Source example.
c=exact_center([3,1,0],[3,3,3])
assert c==2
assert exact_radius2([3,1,0],[3,3,3],c)==6

print(f"VERIFY_OK good-symmetric-Newton-MEB cases={len(cases)} full_orbit_expansion=yes ambient_epigraph=yes")
