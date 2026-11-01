#!/usr/bin/env python3
"""Numerical and exact finite checks for boundary-logarithmic Hausdorff commutators.
No finite test is used as a substitute for the analytic infinite-dimensional proof.
"""
from fractions import Fraction
from math import comb, sqrt, pi, cosh, log
import numpy as np

def H(n,k,t):
    if k>n: return Fraction(0)
    return Fraction(comb(n,k))*t**k*(1-t)**(n-k)

def check_columns():
    ct=0
    for t in [Fraction(1,2), Fraction(2,3), Fraction(3,5)]:
        for k in range(15):
            for n in range(25):
                lhs=H(n,k+1,t)- (H(n-1,k,t) if n>0 else Fraction(0))
                rhs=(H(n-1,k,t)*(t*Fraction(n,k+1)-1) if n>0 and n>=k+1 else Fraction(0))
                assert lhs==rhs,(t,n,k,lhs,rhs)
                ct+=1
    return ct

def column_energy(tvals,coeffs,tau,k,grid=55001):
    # theta=u/sqrt(k) exactly.  The Gaussian tails suppress |u| much larger than 1.
    us=np.linspace(-32,32,grid)
    th=us/np.sqrt(k)
    z=np.exp(1j*th)
    h2=np.exp(-2*tau*np.angle(1-z))
    h2[grid//2]=0.0 # set the irrelevant single null point to zero
    terms=np.zeros_like(z,dtype=complex)
    for t,a in zip(tvals,coeffs):
        den=1-(1-t)*z
        phase=(den)**(-1j*tau)-1
        B=np.exp(k*np.log(t/den))
        terms+=a*phase/den*B
    return np.trapezoid(h2*np.abs(terms)**2,us)/(2*pi*np.sqrt(k))

def asymptotic_coefficient(tvals,coeffs,tau):
    return cosh(pi*tau)/(2*sqrt(pi))*sum(abs(a)**2*abs(t**(-1j*tau)-1)**2/(t*sqrt(1-t)) for t,a in zip(tvals,coeffs))

if __name__=='__main__':
    ct=check_columns()
    print('exact rational commutator matrix identities:',ct)
    combos=[([0.5],[1.0],0.75),([0.4,0.72],[1.0,-0.85j],0.7),([0.3,0.55,0.8],[1.,-1.,1.3j],1.1)]
    for ts,aa,tau in combos:
        goal=asymptotic_coefficient(ts,aa,tau)
        print('case:',ts,aa,tau,'predicted sqrt(k)*column-energy:',goal)
        vals=[]
        for k in [200,600,1500,4000]:
            got=np.sqrt(k)*column_energy(ts,aa,tau,k)
            vals.append(got)
            print('k:',k,'value:',got,'relative error:',abs(got-goal)/goal)
        # asymptotic verification only; no quantitative theorem at these cutoffs
        assert abs(vals[-1]-goal)/goal<0.10,(vals[-1],goal)
    # For a shift commutator, summing all degrees has exact norm q/(1-q^2).
    # Check the finite truncations approach it from below via explicit H-coefficients.
    for t in [Fraction(1,3), Fraction(1,2), Fraction(3,4)]:
        q=1-t; target=float(q/(1-q*q))
        total=0.
        for k in range(0,100):
            for m in range(0,200):
                # binomial probability expression, finite double-sum approximation.
                # Evaluated through a stable recurrence across m.
                if m==0:
                    v=float(t**k)*(float(t)-1.)
                else:
                    # directly via a binomial pmf to avoid enormous integers
                    from scipy.special import gammaln
                    llog=float(k)*log(float(t))+m*log(float(q))+gammaln(k+m+1)-gammaln(k+1)-gammaln(m+1)
                    v=np.exp(llog)*(float(t)*(1+m/(k+1))-1)
                total+=v*v
        assert 0<total<target and abs(total-target)<0.15,(t,total,target)
        print('shift exact HS target',t,target,'finite partial sum',total)
    print('All checker assertions PASSED')
