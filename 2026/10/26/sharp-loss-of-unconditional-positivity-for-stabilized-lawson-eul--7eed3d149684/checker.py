"""Standalone finite consistency checks for three-state stabilized Lawson--Euler facts.
The mathematical all-parameter statements are proved in RESULT.md; these computations are consistency checks.
"""
from fractions import Fraction
from math import sqrt, log, exp, e
import numpy as np
from scipy.linalg import expm


def generator(a,b):
    return np.array([[-a,a,0.0],[a,-a-b,b],[0.0,b,-b]],float)

def crossing(r,s):
    assert r>s>0
    d=sqrt(r*r-r*s+s*s)
    lo=r+s-d
    hi=r+s+d
    C=(2*r-s-d)/(6*d)
    B=(2*r-s+d)/(6*d)
    assert 0<C<1 and 0<B<1
    return log(hi*B/(lo*C))/(2*d)

def pprime_edge(t,r,s):
    d=sqrt(r*r-r*s+s*s)
    lo=r+s-d
    hi=r+s+d
    C=(2*r-s-d)/(6*d)
    B=(2*r-s+d)/(6*d)
    return -lo*C*exp(-lo*t)+hi*B*exp(-hi*t)

def main():
    checks=0
    # Exact elementary spectral identities for chosen rational edges.
    for a,b in ((Fraction(1),Fraction(1)), (Fraction(2),Fraction(1)),(Fraction(1),Fraction(3))):
        import sympy as sp
        Q=sp.Matrix([[-a,a,0],[a,-a-b,b],[0,b,-b]])
        d2=a*a-a*b+b*b
        assert sp.expand(Q.charpoly().as_expr()-sp.factor(Q.charpoly().as_expr()))==0
        x=sp.symbols('x')
        assert sp.expand(Q.charpoly(x).as_expr()-x*(x*x+2*(a+b)*x+3*a*b))==0
        checks+=2
    rng=np.random.default_rng(20261019)
    for _ in range(1500):
        a=float(np.exp(rng.uniform(-3,3)))
        b=float(np.exp(rng.uniform(-3,3)))
        if abs(a-b)<1e-12:continue
        r=max(a,b); s=min(a,b)
        ts=crossing(r,s)
        assert ts>0
        for f, expected in ((0.5,1), (1.0,0),(2.0,-1)):
            tp=ts*f
            pred=pprime_edge(tp,r,s)
            actual=expm(tp*generator(a,b)).dot(generator(a,b))[0,1] if a>b else expm(tp*generator(a,b)).dot(generator(a,b))[1,2]
            assert abs(pred-actual)<2e-9*max(1,r,s)
            if expected==1: assert pred>0
            elif expected==-1: assert pred<0
            else: assert abs(pred)<1e-9*max(1,r,s)
            checks+=3
    for a in (0.1,1.,10.):
        for alpha in (0.1,2/(3*e),0.3,0.8,2.):
            for x in np.geomspace(1e-3, 30, 151):
                h=x/(alpha*a)
                M=np.eye(3)+h*expm(alpha*h*generator(a,a)).dot(generator(a,a))
                assert np.linalg.norm(M.sum(axis=1)-1,np.inf)<1e-10
                if alpha>=2/(3*e)-1e-14:
                    assert M.min()>-1e-10
                checks+=2
        aa=2/(3*e)
        h=1/(3*a*aa)
        M=np.eye(3)+h*expm(aa*h*generator(a,a)).dot(generator(a,a))
        assert abs(M[1,1])<1e-13
        checks+=1
    for d in [1e-2,1e-3,1e-4,1e-5]:
        st=crossing(1+d,1.)
        est=0.5*log(4/d)
        assert abs(st-est)<5e-2
        checks+=1
    for alpha in [0.2,0.3,0.9]:
        r,s=2.0,1.0; ht=crossing(r,s)/alpha
        for fac in [0.7,1.,1.2]:
            h=ht*fac
            M=np.eye(3)+h*expm(alpha*h*generator(r,s)).dot(generator(r,s))
            if fac<1:assert M[0,1]>0
            elif fac>1:assert M[0,1]<0
            else:assert abs(M[0,1])<1e-10
            checks+=1
    print('PASS',checks,'deterministic check units; analytic claims require proof in RESULT.md')

if __name__=='__main__':main()
