#!/usr/bin/env python3
"""Reproducible finite checks for the analytic single-site Fock jet theorem.
Uses the Python standard library. Finite tests supplement, not replace, proof.
"""
import math
from fractions import Fraction
from itertools import product

def add(a,b):
    c=[Fraction(0)]*max(len(a),len(b))
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return trim(c)
def trim(a):
    while len(a)>1 and not a[-1]: a.pop()
    return a

def scale(a,v): return trim([x*v for x in a])
def mul(a,b):
    c=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)
def deriv(a): return trim([i*a[i] for i in range(1,len(a))] or [Fraction(0)])
def shift(a,m): return ([Fraction(0)]*m)+a

def charlier_polys(N,k):
    a=[[Fraction(1)],[Fraction(N),Fraction(-1)]]
    for j in range(1,k+1):
        a.append(add(mul([Fraction(N-j),Fraction(-1)],a[j]),scale(shift(a[j-1],1),-j)))
    return a[:k+2]

def exact_identity(N,k):
    C=charlier_polys(N,k)
    T=[Fraction(0)]
    for j in range(k+1):
        T=add(T,scale(shift(mul(C[j],C[j]),k-j),Fraction(1,math.factorial(j))))
    lhs=scale(add(mul([Fraction(N-k),Fraction(-1)],T),shift(deriv(T),1)),math.factorial(k))
    rhs=mul(C[k],C[k+1])
    assert not any(add(lhs,scale(rhs,-1)))
    assert not any(add(deriv(C[k+1]),scale(C[k],k+1)))
    return 1

def C_values(N,lam,k):
    c=[1.,N-lam]
    for j in range(1,k+1):
        c.append((N-lam-j)*c[-1]-j*lam*c[-2])
    return c[:k+2]

def captured(N,lam,k):
    if lam<=0: return 0.
    p=math.exp(-lam+N*math.log(lam)-math.lgamma(N+1))
    C=C_values(N,lam,k)
    return p*sum((C[j]/(lam**(j/2)))**2/math.factorial(j) for j in range(k+1))

def hermite(y,k):
    h=[1.,y]
    for j in range(1,k): h.append(y*h[-1]-j*h[-2])
    return h[:k+1]

def envelope(y,k):
    H=hermite(y,k)
    return math.exp(-y*y/2)*sum(H[j]*H[j]/math.factorial(j) for j in range(k+1))

def first_positive_root_he(k):
    # All roots lie inside +/- 2 sqrt(k+1); smallest strictly positive.
    end=2*math.sqrt(k+1)+1
    f=lambda x:hermite(x,k)[-1]
    if abs(f(0.))<1e-12: return 0.
    nsteps=20000; prev=0.; fp=f(0.)
    for ii in range(1,nsteps+1):
        curr=end*ii/nsteps; fc=f(curr)
        if fc*fp<0:
            lo,hi=prev,curr
            for _ in range(65):
                mid=(lo+hi)/2
                if f(mid)*f(lo)<=0:hi=mid
                else:lo=mid
            return (lo+hi)/2
        prev,fp=curr,fc
    raise ValueError('no root')

def interp_root_validation(N,k):
    # Associated Laguerre polynomial C_{k+1}(N;lambda) has k+1 positive roots.
    end=2*N+5*k+30
    grid=24000; vals=[]
    lastx=0.;last=C_values(N,0.,k)[k+1]
    for i in range(1,grid+1):
        x=end*i/grid; f=C_values(N,x,k)[k+1]
        if f*last<0:
            l,r=lastx,x
            for _ in range(55):
                m=(l+r)/2
                if C_values(N,l,k)[k+1]*C_values(N,m,k)[k+1]<=0:r=m
                else:l=m
            vals.append((l+r)/2)
        lastx,last=x,f
    assert len(vals)==k+1,(N,k,len(vals),vals)
    fs=[captured(N,r,k) for r in vals]
    # Brute continuous mesh comparison; local maxima must occur at candidates.
    for i in range(1000):
        x=end*(i+0.5)/1000
        assert captured(N,x,k)<=max(fs)+1.e-10
    return vals,fs

if __name__=='__main__':
    n=0
    for N,k in product((8,9,11,17,31,52),(0,1,2,3,4,5,6)):
        if N<=k:continue
        n+=exact_identity(N,k)
    print('exact polynomial derivative identities:',n)
    for k in range(2,8):
        roots,F=interp_root_validation(80,k)
        print('finite root candidates',k,'count',len(roots),'max-lambda',round(roots[max(range(len(F)),key=lambda j:F[j])],6))
    for k in range(2,8):
        y=0. if k%2==0 else first_positive_root_he(k+1)
        expected=envelope(y,k)
        for N in (500,2000,10000):
            got=math.sqrt(2*math.pi*N)*captured(N,N+y*math.sqrt(N),k)
            # sqrt(N) local limit, first correction can be >5% at N=500 for high k
            assert abs(got-expected) < 1.3 * (k+2)**2/math.sqrt(N),(N,k,got,expected)
        print('asymptotic',k,'y',round(y,9),'constant',round(expected,9), 'N10000',round(got,9))
    # Independent coefficient extraction from the shifted coherent monomial.
    direct=0
    for N,k in product((9,13,18),(2,3,4,5)):
        for lam in (4.5,9.3,16.7):
            a=math.sqrt(lam)
            captured_direct=0.
            for j in range(k+1):
                coeff=math.exp(-lam/2)*math.sqrt(math.factorial(N)/math.factorial(j))*sum(
                    math.comb(j,l)*(-a)**(j-l)*a**(N-l)/math.factorial(N-l)
                    for l in range(j+1))
                captured_direct+=coeff**2
            got=captured(N,lam,k)
            assert abs(captured_direct-got)<1e-8*(1+got),(N,k,lam,captured_direct,got)
            direct+=1
    print('independent shifted-monomial coefficients:',direct)
    # Derivative via centered finite differences at independent points.
    nder=0
    for N,k in product((15,30,100),(0,1,2,3,4)):
        for s in (0.7,1.1,1.5):
            lam=N*s;h=1e-4
            finite=(captured(N,lam+h,k)-captured(N,lam-h,k))/(2*h)
            C=C_values(N,lam,k)
            pred=math.exp(-lam+N*math.log(lam)-math.lgamma(N+1))*C[k]*C[k+1]/(math.factorial(k)*lam**(k+1))
            assert abs(finite-pred)<1e-7,(N,k,lam,finite,pred)
            nder+=1
    print('numeric derivative assertions:',nder)
    print('ALL CHECKS PASSED')
