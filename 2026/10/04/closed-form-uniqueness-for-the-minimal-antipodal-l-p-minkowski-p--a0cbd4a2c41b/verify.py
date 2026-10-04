#!/usr/bin/env python3
"""Numerical replay for the closed-form minimal antipodal L_p Minkowski solution.

The theorem itself is analytic. This script checks the derived support numbers on two
independent test configurations by reconstructing every prescribed L_p facet mass.
"""
from __future__ import annotations
import math


def det(matrix):
    a=[list(map(float,row)) for row in matrix]
    n=len(a)
    out=1.0
    for i in range(n):
        j=max(range(i,n), key=lambda k: abs(a[k][i]))
        if abs(a[j][i])<1e-15:
            return 0.0
        if j!=i:
            a[i],a[j]=a[j],a[i]
            out=-out
        piv=a[i][i]
        out*=piv
        for k in range(i+1,n):
            f=a[k][i]/piv
            for l in range(i+1,n):
                a[k][l]-=f*a[i][l]
    return out


def solve(normals, alpha_plus, alpha_minus, p):
    n=len(normals)
    q=1.0-p
    d=abs(det(normals))
    if not (p<0 and d>0):
        raise ValueError("requires p<0 and independent unit normals")
    b=[ap**(1.0/q)+am**(1.0/q) for ap,am in zip(alpha_plus,alpha_minus)]
    B=[x**(q/(q-1.0)) for x in b]
    prodB=math.prod(B)
    lam=(d/prodB)**(1.0/(n-p))
    w=[lam*x for x in B]
    aplus=[wi*ap**(1.0/q)/bi for wi,ap,bi in zip(w,alpha_plus,b)]
    aminus=[wi*am**(1.0/q)/bi for wi,am,bi in zip(w,alpha_minus,b)]
    areas=[]
    rec_plus=[]
    rec_minus=[]
    for i in range(n):
        area=math.prod(w[j] for j in range(n) if j!=i)/d
        areas.append(area)
        rec_plus.append(aplus[i]**q*area)
        rec_minus.append(aminus[i]**q*area)
    return lam,w,aplus,aminus,areas,rec_plus,rec_minus


def run_case(normals, ap, am, p):
    lam,w,hp,hm,areas,rp,rm=solve(normals,ap,am,p)
    err=max(abs(x-y) for x,y in zip(rp,ap))
    err=max(err,max(abs(x-y) for x,y in zip(rm,am)))
    split=max(abs((x+y)-z) for x,y,z in zip(hp,hm,w))
    print(f"p={p:g} det={abs(det(normals)):.12g} lambda={lam:.12g}")
    print("widths", " ".join(f"{x:.12g}" for x in w))
    print("max_mass_error", f"{err:.3e}")
    print("max_split_error", f"{split:.3e}")
    assert err < 1e-10
    assert split < 1e-12


if __name__ == "__main__":
    run_case(
        [(1.0,0.0),(3.0/5.0,4.0/5.0)],
        [4.0,9.0],
        [1.0,16.0],
        -1.0,
    )
    run_case(
        [(1.0,0.0,0.0),(0.0,1.0,0.0),(1.0/3.0,2.0/3.0,2.0/3.0)],
        [1.7,0.9,2.4],
        [0.8,1.3,1.1],
        -2.0,
    )
    print("VERIFY_OK")
