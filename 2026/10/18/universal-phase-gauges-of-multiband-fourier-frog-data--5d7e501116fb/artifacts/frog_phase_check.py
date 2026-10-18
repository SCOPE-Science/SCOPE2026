"""Finite exact relation-lattice and numeric FROG checks for two separated bands.
This is auxiliary reproducibility evidence; the general theorem has a direct proof.
"""
from collections import defaultdict
from math import gcd
from random import Random
import cmath
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def test_structure(a,c,b):
    S=list(range(a+1))+list(range(b,b+c+1))
    n=len(S)
    groups=defaultdict(list)
    for i in range(n):
        for j in range(i,n):groups[S[i]+S[j]].append((i,j))
    rows=[]
    for v in groups.values():
        for i,j in v[1:]:
            p,q=v[0]; z=[0]*n
            z[i]+=1; z[j]+=1; z[p]-=1; z[q]-=1
            rows.append(z)
    mat=sp.Matrix(rows) if rows else sp.zeros(0,n)
    rank=mat.rank()
    target=2 if b<=max(2*a,a+c) else 3
    assert n-rank==target, (a,c,b,n-rank,target)
    if rows:
        D=smith_normal_form(mat,domain=ZZ)
        nonzero=[abs(int(D[j,j])) for j in range(min(D.rows,D.cols)) if D[j,j]!=0]
        assert all(j==1 for j in nonzero),(a,c,b,nonzero)
    l1=max(0,2*a-b+1); l2=max(0,a+c-b+1)
    I=set(range(0,2*a+1)); J=set(range(b,b+a+c+1)); K=set(range(2*b,2*b+2*c+1))
    assert len(I & J)==l1 and len(J & K)==l2 and not(I & K)
    return len(rows)

def frog(a,c,b,aa,steps,phi=None):
    n=4*(b+c)+1; S=list(range(a+1))+list(range(b,b+c+1))
    coef=dict(zip(S,aa))
    vals=[]
    for k in range(n):
        sk=[]
        for m in steps:
            z=sum(coef.get(i,0)*coef.get(k-i,0)*cmath.exp(2j*np.pi*i*m/n) for i in S)
            sk.append(abs(z)**2)
        vals.extend(sk)
    return np.asarray(vals)

count=0; relations=0
for a in range(2,7):
    for c in range(2,7):
        for b in range(a+1,max(2*a,a+c)+4):
            relations+=test_structure(a,c,b)
            count+=1
print('exact_parameters=',count,'relation_rows=',relations)

rng=Random(1729); examples=0
for a,c,b in [(2,2,5),(2,2,4),(2,5,6),(4,2,8),(3,4,8),(5,5,12)]:
    n=4*(b+c)+1; S=list(range(a+1))+list(range(b,b+c+1))
    aa=[complex(rng.uniform(.5,1.5),rng.uniform(-1,1)) for i in S]
    alpha,beta,t=.27,.67,-.41
    gauged=[z*cmath.exp(1j*(alpha+i*t if i<=a else beta+(i-b)*t)) for z,i in zip(aa,S)]
    data=frog(a,c,b,aa,[0,1,2,3])
    new=frog(a,c,b,gauged,[0,1,2,3])
    delta=max(abs(data-new))
    if b>max(2*a,a+c):assert delta<1e-9,(a,c,b,delta)
    else:assert delta>1e-7,(a,c,b,delta)
    flat=[1+0j]*len(S)
    shifted=[1+0j if i<=a else -1+0j for i in S]
    i0=frog(a,c,b,flat,[0]); i1=frog(a,c,b,shifted,[0]); active=int(sum(abs(i0-i1)>1e-7))
    assert active==max(0,2*a-b+1)+max(0,a+c-b+1),(a,c,b,active)
    examples+=1
print('FROG_phase_numeric_and_active_row_examples=',examples)
print('PASS')
