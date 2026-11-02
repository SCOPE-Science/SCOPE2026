"""Exact symbolic and finite numerical checks for biased-cube mixing theorem.

Run: python verify.py
Requires sympy and numpy. The universal inequality is proved in RESULT.md;
finite checks here are independent supporting tests, not infinite certificates.
"""
import itertools
import math
import random
from fractions import Fraction

import numpy as np
import sympy as sp

count = 0

def check(ok, text):
    global count
    if not ok:
        raise AssertionError(text)
    count += 1

m, a = sp.symbols('m a', positive=True)
d = sp.symbols('d', integer=True, positive=True)
b = 1-a
s = a*b
z = 1-m
# Reduced positivity obstruction for a hypothetical SLEM <= m.
K = (d+1)*m-(d-1)
F = sp.expand(K*K + K*(d-1)*z -4*d*s*z*z)
quad = (d+1-2*d*s)*m*m+(1-d+4*d*s)*m-2*d*s
check(sp.simplify(F-2*quad)==0,'quadratic feasibility identity')
check(sp.simplify(sp.discriminant(quad,m)-((d-1)**2+16*d*s))==0,'quadratic discriminant')
p=(a+m*b)/(d+1)
q=(b+m*a)/(d+1)
c=s*(1-m)
check(sp.simplify(1-c/a-d*p-p)==0,'rare layer holding probability')
check(sp.simplify(1-c/b-d*q-q)==0,'common layer holding probability')

sqrt_s=sp.sqrt(s)
stationary=sp.Matrix([sp.sqrt(a),sp.sqrt(b)])
contrast=sp.Matrix([sp.sqrt(b),-sp.sqrt(a)])
proj=contrast*contrast.T
D=sp.diag(p,q)
A=(1-m)*stationary*stationary.T/2
B=(m*proj+(1+m)*stationary*stationary.T/2)/d
U=sp.simplify(B[0,0]-A[0,0]);V=sp.simplify(B[1,1]-A[1,1])
check(sp.simplify(p-A[0,0]-d*U/(d+1))==0,'lower diagonal split p')
check(sp.simplify(q-A[1,1]-d*V/(d+1))==0,'lower diagonal split q')
check(sp.simplify(sp.expand((D-A).det())-quad/(2*(d+1)**2))==0,'lower bound determinant factor')
check(sp.simplify(sp.expand((B-D).det())-quad/(2*d*d*(d+1)**2))==0,'upper bound determinant factor')

rng=random.Random(20261030)

def exact_mu(dim,left):
    v=left*(1-left)
    return (dim-1-4*dim*v+sp.sqrt((dim-1)**2+16*dim*v))/(2*(dim+1-2*dim*v))

def chain(dim,left):
    t=float(exact_mu(dim,sp.Rational(left.numerator,left.denominator)))
    aa=float(left);bb=1-aa
    pp=(aa+t*bb)/(dim+1)
    qq=(bb+t*aa)/(dim+1)
    cc=aa*bb*(1-t)
    states=list(itertools.product([0,1],repeat=dim+1))
    ind={x:i for i,x in enumerate(states)}
    n=len(states)
    pi=np.array([(aa if x[0]==0 else bb)/(2**dim) for x in states])
    T=np.zeros((n,n))
    for i,x in enumerate(states):
        zz=x[0]
        pz=pp if zz==0 else qq
        y=(1-zz,)+x[1:]
        T[i,ind[y]]=cc/(aa if zz==0 else bb)
        for j in range(1,dim+1):
            w=list(x);w[j]^=1
            T[i,ind[tuple(w)]]=pz
        T[i,i]=pz
    return T,pi,t

for dim in range(1,6):
    for left in (Fraction(1,100),Fraction(1,9),Fraction(1,4),Fraction(2,5),Fraction(1,2)):
        mm=exact_mu(dim,sp.Rational(left.numerator,left.denominator))
        ss=sp.Rational(left.numerator,left.denominator)*(1-sp.Rational(left.numerator,left.denominator))
        check(sp.simplify(quad.subs({d:dim,a:sp.Rational(left.numerator,left.denominator),m:mm}))==0,'exact radical root')
        check(sp.N(mm)>=0,'nonnegative optimum')
        check(sp.N(mm)<=1,'optimum below one')
        check(sp.N(mm)>=sp.Rational(dim-1,dim+1)-sp.Float('1e-13'),'lower endpoint')
        check(sp.N(mm)<=sp.Rational(dim,dim+2)+sp.Float('1e-13'),'upper endpoint')
        T,pi,t=chain(dim,left)
        check(np.max(np.abs(T.sum(axis=1)-1))<2e-14,'stochastic rows')
        check(T.min()>=-1e-15,'nonnegative entries')
        check(np.max(np.abs(pi[:,None]*T-(pi[:,None]*T).T))<2e-14,'detailed balance')
        check(np.max(np.abs(pi@T-pi))<2e-14,'invariant measure')
        H=np.sqrt(pi[:,None]/pi[None,:])*T
        eig=np.linalg.eigvalsh(H)
        check(abs(eig[-1]-1)<1e-13,'stationary eigenvalue')
        check(abs(max(abs(eig[0]),abs(eig[-2]))-t)<1e-11,'sharp SLEM')
        # An independently generated reversible transition is an unrestricted comparator.
        states=list(itertools.product([0,1],repeat=dim+1))
        n=len(states)
        for _ in range(12):
            C=np.zeros((n,n))
            for i,x in enumerate(states):
                for j in range(i+1,n):
                    y=states[j]
                    if sum(u!=v for u,v in zip(x,y))!=1:continue
                    w=rng.uniform(.01,.99)*min(pi[i],pi[j])/(dim+1)
                    C[i,j]=w;C[j,i]=w
            P=C/pi[:,None]
            np.fill_diagonal(P,1-P.sum(axis=1))
            check(P.min()>-1e-12,'random admissibility')
            J=np.sqrt(pi[:,None]/pi[None,:])*P
            eigj=np.linalg.eigvalsh(J)
            sm=max(abs(eigj[0]),abs(eigj[-2]))
            check(sm+1e-10>=t,'unrestricted chain does not beat optimum')
print(f'ALL_CHECKS_PASSED {count}')
