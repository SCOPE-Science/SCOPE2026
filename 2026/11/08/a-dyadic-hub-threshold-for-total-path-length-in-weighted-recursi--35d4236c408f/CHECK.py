"""Finite exact checks for dyadic-mass weighted recursive trees.

The conclusions for infinitely many vertices require the accompanying analytic proof.
Run: python3 CHECK.py
"""
from fractions import Fraction
from itertools import product

checks=0

def ck(ok, message):
    global checks
    checks+=1
    if not ok:
        raise AssertionError(message)

def weights(beta,n):
    return [None]+[(j**beta if j & (j-1)==0 else 1) for j in range(1,n+1)]

def rec_moments(beta,n):
    w=weights(beta,n)
    W=Fraction(w[1]); H=Fraction(0); q=Fraction(0)
    AW=Fraction(0); BW=Fraction(0); Vmu=Fraction(0)
    data={1:{'meanD':Fraction(0),'secondD':Fraction(0),'meanT':Fraction(0),'varmu':Fraction(0)}}
    # Var of T_n by orthogonal innovations; recompute for each n
    v={}; p={}
    for j in range(2,n+1):
        Ej=1+H
        Dj2=Ej*Ej+q
        vj=BW/W-H*H-Vmu
        pj=Fraction(w[j],W+w[j])
        ck(vj>=0,f'conditional variance negative: beta={beta} j={j}')
        Vmu+=pj*pj*vj
        AW+=w[j]*Ej; BW+=w[j]*Dj2; W+=w[j]
        H+=pj; q+=pj*(1-pj)
        v[j]=vj;p[j]=pj
        data[j]={'meanD':Ej,'secondD':Dj2,'varmu':Vmu,'meanT':None}
    return w,p,v,data

def enumeration(beta,n):
    w=weights(beta,n)
    totals={j:[Fraction(0),Fraction(0)] for j in range(2,n+1)}
    probs=[]
    for j in range(2,n+1):
        W=sum(w[1:j]); probs.append([Fraction(w[i],W) for i in range(1,j)])
    totalprob=Fraction(0)
    for choices in product(*[range(1,j) for j in range(2,n+1)]):
        depths=[0]*(n+1); T=0; prob=Fraction(1)
        perj={}
        for j,parent in enumerate(choices,start=2):
            depths[j]=depths[parent]+1
            T+=depths[j]
            perj[j]=T
            prob*=probs[j-2][parent-1]
        for j,t in perj.items():
            totals[j][0]+=prob*t
            totals[j][1]+=prob*t*t
        totalprob+=prob
    ck(totalprob==1, 'enumeration normalization')
    return totals

for beta in (0,1,2):
    for n in range(3,9):
        w,p,v,data=rec_moments(beta,n)
        totals=enumeration(beta,n)
        for j in range(2,n+1):
            ET=sum(data[i]['meanD'] for i in range(2,j+1))
            VT=sum((1+(j-i)*p[i])**2*v[i] for i in range(2,j+1))
            ck(totals[j][0]==ET,f'mean mismatch beta={beta} j={j}')
            ck(totals[j][1]-ET*ET==VT,f'variance mismatch beta={beta} j={j}')
        ck(data[n]['varmu']==sum(p[j]**2*v[j] for j in range(2,n+1)), 'martingale variance')

# Exact nontrivial hub variance witnesses for beta >= 1.
for beta in (1,2,3):
    n=256
    w,p,v,data=rec_moments(beta,n)
    C=Fraction(1)+Fraction(1,2**beta-1)
    lower=Fraction(1,2**(3*beta))/(C*C*(C+1)*(C+1))
    for k in range(3,9):
        j=2**k
        ck(v[j]>=lower,f'hub spread lower bound beta={beta}, j={j}')
        ck(p[j]>=1/(C+1), f'hub mass lower bound beta={beta}, j={j}')

# Explicit dyadic weights and divergence of the sufficient-condition requirement.
for beta in (1,2):
    w,p,v,data=rec_moments(beta,256)
    for k in range(3,9):
        j=2**k
        ck(j*p[j]>=1, 'non-small spike')

print('PASS',checks,'exact rational assertions')
