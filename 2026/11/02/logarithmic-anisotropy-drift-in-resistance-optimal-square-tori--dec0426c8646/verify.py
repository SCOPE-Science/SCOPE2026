#!/usr/bin/env python3
"""Reproduce exact spectra and asymptotics of priced toroidal conductance allocation.
Uses only the Python 3 standard library. Run: python verify.py
"""
import math
from fractions import Fraction

PI=math.pi
EULER=0.57721566490153286060651209

def eigs(n):
    return [4*math.sin(PI*j/n)**2 for j in range(n)]

def spectral(n,t):
    a=eigs(n)
    return sum(1/(t*x+y) for x in a for y in a if x+y>1e-14)

def resolvent(n,t):
    s=math.sin
    terms=[]
    for j in range(1,n):
        z=s(PI*j/n)
        terms.append(n/(4*math.sqrt(t)*z*math.sqrt(1+t*z*z)*math.tanh(n*math.asinh(math.sqrt(t)*z))))
    return (n*n-1)/12 + math.fsum(terms)

def constant(t):
    u=math.sqrt(t)
    H=-2*math.fsum(math.log1p(-math.exp(-2*PI*u*k)) for k in range(1,200) if 2*PI*u*k<740)
    return 1/12+(EULER+math.log(2/(PI*math.sqrt(1+t)))+H)/(2*PI*u)

def kappa(t):
    u=math.sqrt(t)
    E=math.fsum(k*math.exp(-2*PI*u*k)/(1-math.exp(-2*PI*u*k)) for k in range(1,200) if 2*PI*u*k<700)
    return -4*PI*t**1.5*(1/12-u/(2*PI*(1+t))-2*E)

def optimum(n,P,Q):
    lo=math.log(Q/P)-1.5
    hi=math.log(Q/P)+1.5
    phi=(math.sqrt(5)-1)/2
    def obj(z):
        t=math.exp(z)
        return (P*t+Q)*resolvent(n,t)/n**2
    c=hi-phi*(hi-lo);d=lo+phi*(hi-lo)
    fc=obj(c);fd=obj(d)
    for it in range(110):
        if fc<fd:
            hi=d;d=c;fd=fc;c=hi-phi*(hi-lo);fc=obj(c)
        else:
            lo=c;c=d;fc=fd;d=lo+phi*(hi-lo);fd=obj(d)
    return math.exp((lo+hi)/2)

def matrix_trace_inverse(m):
    N=len(m)
    b=[[Fraction(m[i][j])+(Fraction(1,N)) for j in range(N)] for i in range(N)]
    aug=[row+[Fraction(int(i==j)) for j in range(N)] for i,row in enumerate(b)]
    for k in range(N):
        p=next(i for i in range(k,N) if aug[i][k]!=0)
        aug[k],aug[p]=aug[p],aug[k]
        pivot=aug[k][k];aug[k]=[v/pivot for v in aug[k]]
        for i in range(N):
            if i!=k:
                q=aug[i][k]
                if q:aug[i]=[a-q*b for a,b in zip(aug[i],aug[k])]
    return sum(aug[i][N+i] for i in range(N))-1

def exact_trace(n,x,y):
    N=n*n
    m=[[Fraction(0) for j in range(N)] for i in range(N)]
    for i in range(n):
        for j in range(n):
            u=i*n+j
            for v,w in [((((i+1)%n)*n+j),x),((i*n+(j+1)%n),y)]:
                m[u][u]+=w;m[v][v]+=w;m[u][v]-=w;m[v][u]-=w
    return matrix_trace_inverse(m)

def check():
    checks=0
    for n in [3,4,5,7,10,17,32]:
        for t in [.12,.3,.8,1,2,5,11]:
            s=spectral(n,t);v=resolvent(n,t)
            assert abs(s-v)<=3e-11*max(1,s),(n,t,s,v)
            checks+=1
    for n in (3,4):
        for x,y in [(Fraction(1),Fraction(1)),(Fraction(2),Fraction(3)),(Fraction(5),Fraction(2))]:
            direct=exact_trace(n,x,y)
            a=eigs(n)
            spectral_value=sum(1/(float(x)*a[j]+float(y)*a[k]) for j in range(n) for k in range(n) if j or k)
            assert abs(float(direct)-spectral_value)<2e-10
            checks+=1
    for t in [.1,.25,.5,1,2,4,10]:
        a=1/(2*PI*math.sqrt(t));C=constant(t)
        for n in [500,2000,6000]:
            E=resolvent(n,t)/n**2-a*math.log(n)-C
            assert abs(E)<1e-5,(n,t,E)
            checks+=1
    for P,Q in [(1,1),(2,1),(4,1),(10,1),(1,4)]:
        t0=Q/P
        vals=[]
        for n in [50,200,1000,3000]:
            t=optimum(n,P,Q)
            assert t>0
            if P==Q:assert abs(t-1)<1e-5
            vals.append((n,t))
            checks+=1
        n,t=vals[-1]
        if P!=Q:
            # Two-term law has slowly vanishing 1/log(n) corrections.
            assert abs((t-t0)*math.log(n)-kappa(t0))<.35,(P,Q,t,kappa(t0))
            checks+=1
    print('VERIFY_OK',checks,'checks; exact traces, Fourier-resolvent identity, finite-size constant, optimized drift')

if __name__=='__main__':check()
