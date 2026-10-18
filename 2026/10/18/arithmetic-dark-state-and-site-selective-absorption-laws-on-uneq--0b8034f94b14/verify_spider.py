"""Standalone checks for exact absorption probabilities in a finite absorbing spider."""
from fractions import Fraction
from itertools import product
from math import gcd, sin, cos, pi
import numpy as np
from scipy.linalg import eigh
from sympy import divisors, totient, mobius

def rc(q,n):
    return int(sum(int(d)*int(mobius(q//d)) for d in divisors(gcd(q,n))))

def formula(lengths,i,d):
    m=[v+1 for v in lengths]
    s=Fraction(0)
    for q in divisors(m[i]):
        q=int(q)
        if q<=1: continue
        w=sum((Fraction(1,v) for v in m if v%q==0),Fraction(0))
        term=Fraction(int(totient(q))-rc(q,d),m[i])*(1-Fraction(1,m[i])/w)
        s+=term
    return s

def build_A(lengths):
    N=1+sum(lengths); A=np.zeros((N,N))
    offset=1
    for L in lengths:
        A[0,offset]=A[offset,0]=1
        for v in range(offset,offset+L-1): A[v,v+1]=A[v+1,v]=1
        offset+=L
    return A

def formula_dim(lengths):
    m=[L+1 for L in lengths]
    return sum(int(totient(q))*(sum(v%q==0 for v in m)-1) for q in range(2,max(m)+1) if sum(v%q==0 for v in m)>1)

def direct(lengths):
    A=build_A(lengths)
    ev,U=eigh(A)
    D=np.zeros((len(ev),len(ev)))
    dim=0
    ix=0
    while ix<len(ev):
        j=ix+1
        while j<len(ev) and abs(ev[j]-ev[ix])<2e-8: j+=1
        V=U[:,ix:j]; hub=V[0,:]
        P=V@V.T
        if np.linalg.norm(hub)>1e-8:
            w=V@hub; P-=np.outer(w,w)/np.dot(hub,hub)
            dim+=(j-ix-1)
        else:dim+=(j-ix)
        D+=P
        ix=j
    return np.diag(D),dim,D

cases=0; checks=0; maxerr=0
for B in (2,3,4):
    for lengths in product(range(1,5),repeat=B):
        if sum(lengths)>13:continue
        diag,dim,D=direct(lengths)
        assert dim == formula_dim(lengths),(lengths,dim,formula_dim(lengths))
        index=1
        for i,L in enumerate(lengths):
            for d in range(1,L+1):
                expected=float(formula(lengths,i,d))
                got=diag[index+d-1]
                e=abs(expected-got);maxerr=max(maxerr,e)
                assert e<4e-8,(lengths,i,d,expected,got,e)
                assert (expected>0)==any((gcd(L+1,lengths[j]+1)>1 and d%gcd(L+1,lengths[j]+1)!=0) for j in range(B) if j!=i)
                checks+=1
            index+=L
        cases+=1
print({'cases':cases,'vertex_formula_checks':checks,'max_abs_error':maxerr})
for lengths in ([2,5,7],[1,3,5],[2,4,6],[3,4,6],[1,2,4],[2,3,4]):
    print('L=',lengths, 'D=',formula_dim(lengths),'per_arm=',[[str(formula(lengths,i,d)) for d in range(1,L+1)] for i,L in enumerate(lengths)])
