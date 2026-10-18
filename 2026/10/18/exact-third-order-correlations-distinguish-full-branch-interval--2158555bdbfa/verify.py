#!/usr/bin/env python3
"""Exact rational cylinder checks for fully covering affine interval maps."""
from fractions import Fraction as Q
from itertools import product

def params(lengths, signs):
    cur=Q(0); mid=[]
    for ell in lengths:
        mid.append(cur+ell/2);cur+=ell
    assert cur==1 and all(0<z<1 for z in lengths)
    theta=sum((s*l*l for l,s in zip(lengths,signs)),Q(0))
    alpha=sum((l**3 for l in lengths),Q(0))
    beta=2*sum((s*l*l*(c-Q(1,2)) for l,s,c in zip(lengths,signs,mid)),Q(0))
    return theta,alpha,beta

def analytic(lengths,signs,j,l):
    th,A,B=params(lengths,signs)
    return th**j*B*sum((A**(l-1-z)*th**z for z in range(l)),Q(0))/12

def cylinder(lengths,signs,j,l):
    k=j+l
    # Affine inverse on each branch of the Markov partition.
    phi=[];edge=Q(0)
    for h,sign in zip(lengths,signs):
        phi.append((edge if sign==1 else edge+h,sign*h))
        edge+=h
    total=Q(0); n=0
    for word in product(range(len(lengths)),repeat=k):
        # x_{t} = phi_{word[t]}(x_{t+1}); terminal x_k=u.
        vals=[None]*(k+1)
        vals[k]=(Q(0),Q(1))
        jac=Q(1)
        for t in range(k-1,-1,-1):
            q,r=phi[word[t]];c,d=vals[t+1]
            vals[t]=(q+r*c,r*d)
            jac*=lengths[word[t]]
        poly=[Q(1)]
        for t in [0,j,k]:
            c,d=vals[t]
            c-=Q(1,2)
            nxt=[Q(0)]*(len(poly)+1)
            for i,z in enumerate(poly):
                nxt[i]+=z*c
                nxt[i+1]+=z*d
            poly=nxt
        total+=jac*sum((coef/Q(i+1) for i,coef in enumerate(poly)),Q(0))
        n+=1
    return total,n

count=0;cases=[([Q(1,3),Q(2,3)],[1,-1]),([Q(2,5),Q(3,5)],[1,1]),([Q(1,4),Q(1,2),Q(1,4)],[1,-1,1]),([Q(1,6),Q(1,3),Q(1,2)],[-1,1,1]),([Q(1,2),Q(1,2)],[1,-1])]
for lengths,signs in cases:
    for j,l in [(1,1),(1,2),(2,1),(1,3),(3,1),(2,2)]:
        target=analytic(lengths,signs,j,l)
        actual,n=cylinder(lengths,signs,j,l)
        assert target==actual,(lengths,signs,j,l,target,actual)
        count+=1
    th,A,B=params(lengths,signs)
    assert analytic(lengths,signs,1,2)-analytic(lengths,signs,2,1)==th*A*B/12
    count+=1
# Four equal-length maps with indistinguishable linear and quadratic ACFs.
L=[Q(1,4)]*4
S1=[-1,1,1,1]; S2=[1,-1,1,1]
th,A,B=params(L,S1);th2,A2,B2=params(L,S2)
assert (th,A,B)==(Q(1,8),Q(1,16),Q(3,32))
assert (th2,A2,B2)==(th,A,Q(1,32))
assert analytic(L,S1,1,1)==Q(1,1024)
assert analytic(L,S2,1,1)==Q(1,3072)
assert analytic(L,S1,1,2)-analytic(L,S1,2,1)==Q(1,16384)
assert analytic(L,S2,1,2)-analytic(L,S2,2,1)==Q(1,49152)
for s in [S1,S2]:
    for j,l in [(1,1),(1,2),(2,1),(2,2)]:
        assert analytic(L,s,j,l)==cylinder(L,s,j,l)[0]
        count+=1
count+=6
# Numerical verification of sharp critical location using exact symbolic derivatives.
import sympy as sp
z=sp.symbols('z',real=True)
f=z*(1-z*z)*(1+3*z*z)/192
assert sp.expand(sp.diff(f,z))== (1+6*z*z-15*z**4)/192
root=sp.sqrt((3+2*sp.sqrt(6))/15)
assert sp.simplify(sp.diff(f,z).subs(z,root))==0
print('VERIFY_OK',count,'exact rational independent cylinder and witness checks; sharp critical',sp.N(root,14),'amplitude',sp.N(f.subs(z,root),14))
