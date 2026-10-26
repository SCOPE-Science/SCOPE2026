#!/usr/bin/env python3
"""Independent numerical checks for the two-point beam placement theorem.

Requires Python 3, numpy, scipy. Run: python beam_instability_checker.py
This script tests representative finite-separation configurations; it does not
replace the analytical proof for the continuous, infinite-domain operator.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.sparse import diags, eye
from scipy.sparse.linalg import eigsh

SQ2=math.sqrt(2)
G0=1/(2*SQ2)

def analytic_green(d):
    t=abs(d)/SQ2
    return G0*math.exp(-t)*(math.cos(t)+math.sin(t))

def numeric_green(d):
    # Independent direct Fourier quadrature, no closed Green formula used.
    value, error=quad(lambda k: math.cos(k*d)/(k**4+1),0,100,
                      epsabs=2e-11,epsrel=2e-11,limit=500)
    # Truncation bound on the omitted 1/(k^4+1) tail: <= 1/(3*100^3).
    return value/math.pi

def exact_negative_count(a,d):
    g=analytic_green(d)
    vals=[a*(G0+g),a*(G0-g)]
    return sum(v>1+1e-11 for v in vals)

def finite_diff_neg_count(a,d,h=0.15,padding=25):
    # Fourth-derivative finite difference on a long periodic ring, with point
    # stiffness represented as a/h. The model discretization is independent
    # of the free Green function and determinant derivation.
    gap_steps=max(1,round(d/h))
    n=2*math.ceil(padding/h)+gap_steps+1
    index=np.arange(n)
    # Sparse symmetric circulant second-difference operator.
    row=np.concatenate([index,index,index,index,index])
    col=np.concatenate([index,(index+1)%n,(index-1)%n,
                        (index+2)%n,(index-2)%n])
    data=np.concatenate([np.full(n,6.),np.full(n,-4.),np.full(n,-4.),
                         np.full(n,1.),np.full(n,1.)])/h**4
    from scipy.sparse import coo_matrix
    H=coo_matrix((data,(row,col)),shape=(n,n)).tocsc()+eye(n,format='csc')
    # The two defects are at 0 and +d up to grid rounding; periodic images
    # are > 2*padding away.
    defect=np.zeros(n)
    base=math.ceil(padding/h)
    defect[[base,base+gap_steps]]=-a/h
    H=H+diags(defect,0,format='csc')
    eigs=np.sort(eigsh(H,k=4,sigma=-0.4,which='LM',tol=2e-10,
                        maxiter=20000,return_eigenvectors=False))
    return int(sum(eigs< -0.002)),eigs

def run():
    total=0
    for t in np.concatenate([np.linspace(0,13,57),
                             np.array([math.pi,2*math.pi,3*math.pi,
                                      0.75*math.pi,1.75*math.pi])]):
        d=t*SQ2
        actual=numeric_green(d)
        expected=analytic_green(d)
        assert abs(actual-expected)<2.0e-6,(d,actual,expected)
        total+=1
    for n in range(1,5):
        a_n=2*SQ2/(1+math.exp(-n*math.pi))
        assert abs(1/a_n-(G0+abs(analytic_green(n*math.pi*SQ2)))) < 2e-15
        # Exactly at each threshold there is a zero eigenvalue, not a negative one.
        assert exact_negative_count(a_n,n*math.pi*SQ2)==0
        total+=1
    # Lobe arithmetic independently evaluated from sign variations.
    for a in (1.45,2.0,2.75,2.81,2.827):
        r=2*SQ2/a-1
        expected=sum(math.exp(-n*math.pi)>r for n in range(10))
        for t in np.linspace(0.0001,10*math.pi,2001):
            count=exact_negative_count(a,t*SQ2)
            assert count==int(abs(math.exp(-t)*(math.cos(t)+math.sin(t)))>r+1e-11)
        peaks=sum(exact_negative_count(a,n*math.pi*SQ2) for n in range(10))
        assert peaks==expected,(a,peaks,expected)
        total+=2001
    # Independent spatial discretization: comparisons selected away from
    # thresholds by a margin greater than expected h^2 discretization error.
    cases=[(1.7,0.3),(1.7,3.0),(2.4,0.4),(2.4,3.0),
           (2.78,math.pi*SQ2),(2.6,math.pi*SQ2),
           (2.78,5.5),(2.70,2*math.pi*SQ2)]
    for a,d in cases:
        exp=exact_negative_count(a,d)
        got,eigs=finite_diff_neg_count(a,d)
        assert got==exp,(a,d,exp,got,eigs)
        total+=1
    print('PASS:',total,'quadrature/phase/threshold/finite-difference checks')

if __name__=='__main__':
    run()
