#!/usr/bin/env python3
"""Exact finite checks for a parameterized piecewise-affine map's central-coordinate correlations.
Scientific, reproducible checks; not an infinite proof.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt,pi
import sympy as sp

def weights(a, length):
    a=F(a);q=1-2*a
    d={0:F(1)};vals=[]
    for n in range(length+1):
        vals.append(sum((v/F(2)**k for k,v in d.items()),F(0)))
        nd={}
        for k,v in d.items():
            if k==0:
                nd[0]=nd.get(0,F(0))+a*v
                nd[1]=nd.get(1,F(0))+q*v
            else:
                nd[k-1]=nd.get(k-1,F(0))+2*a*v
                nd[k+1]=nd.get(k+1,F(0))+q*v
        d=nd
    return vals

def series_formula(a,length):
    a=F(a);q=1-2*a
    # truncated series r=s*(2a+q*r*r)
    r=[F(0)]*(length+1)
    for n in range(1,length+1):
        r[n]=(2*a if n==1 else F(0)) +q*sum(r[i]*r[n-1-i] for i in range(1,n))
    def multiply(u,v):
        return [sum(u[i]*v[n-i] for i in range(n+1)) for n in range(length+1)]
    r2=multiply(r,r)
    num=[4*(2*a if n==0 else 0)+4*q*r2[n] for n in range(length+1)]
    # ((2-r)*(4a-q*r))*G=num
    u=[F(2)]+[-r[n] for n in range(1,length+1)]
    v=[4*a]+[-q*r[n] for n in range(1,length+1)]
    d=multiply(u,v)
    G=[F(0)]*(length+1)
    for n in range(length+1):
        G[n]=(num[n]-sum(d[j]*G[n-j] for j in range(1,n+1)))/d[0]
    return G

def Fstep(z,branch):
    if branch==0:return z/2
    if branch==1:return (z+1)/2
    return 2*z if z<F(1,2) else 2*z-1

def integrate_direct(a,n):
    # exact sum over i.i.d. branch words and integrals on dyadic cells
    # endpoints avoided: evaluate two interior points on each cell
    a=F(a); q=1-2*a
    probs=[a,a,q]
    N=2**n; total=F(0)
    for path in product(range(3),repeat=n):
        prob=F(1)
        for j in path:prob*=probs[j]
        integ=F(0)
        for k in range(N):
            left=F(k,N);right=F(k+1,N)
            z1=left+(right-left)/4;z2=left+3*(right-left)/4
            v1=z1;v2=z2
            for branch in path:
                v1=Fstep(v1,branch)
                v2=Fstep(v2,branch)
            slope=(v2-v1)/(z2-z1)
            intercept=v1-slope*z1
            # integrate (z-1/2)*(slope*z+intercept-1/2)
            int1=(right**3-left**3)/3-(right**2-left**2)/4
            int2=(right**2-left**2)/2-(right-left)/2
            integ+=slope*int1+(intercept-F(1,2))*int2
        total+=prob*integ
    return total

def symbolic_residue_checks():
    a,r=sp.symbols('a r', positive=True);q=1-2*a
    s=r/(q*r**2+2*a)
    H=4*(2*a+q*r**2)/((2-r)*(4*a-q*r))
    checks=0
    for rp,expect_lambda,expect_amp in [
       (4*a/q,(1+6*a)/2,(1-10*a)/(1-4*a)),
       (sp.Integer(2),2-3*a,2*(5*a-2)/(4*a-1))]:
        spole=sp.factor(s.subs(r,rp))
        res=sp.factor(sp.limit((r-rp)*H,r,rp))
        amp=sp.factor(-sp.diff(s,r).subs(r,rp)/spole*res)
        assert sp.simplify(1/spole-expect_lambda)==0
        assert sp.simplify(amp-expect_amp)==0
        checks+=2
    # branch collision at a=1/10 and a=2/5, equal constants
    for av in [sp.Rational(1,10),sp.Rational(2,5)]:
        qv=1-2*av;rr=sp.sqrt(2*av/qv)
        # singular H ~ B/(r*-r), r*-r ~ r*sqrt(2)*sqrt(delta)
        B=sp.limit((rr-r)*H.subs(a,av),r,rr)
        K=sp.simplify(B/(rr*sp.sqrt(2)))
        assert sp.simplify(K-4*sp.sqrt(2)/3)==0,(av,K)
        checks+=1
    # Green-Kubo variance at s=1
    for rv,expect in [(2*a/q,2/(1-3*a)),(sp.Integer(1),4/(6*a-1))]:
        assert sp.simplify(H.subs(r,rv)-expect)==0
        checks+=1
    return checks

def weights_float(a, length):
    q=1-2*a
    d=[1.0]; ans=[]
    for n in range(length+1):
        ans.append(sum(v/(2**k) for k,v in enumerate(d) if k<1020))
        nd=[0.0]*(len(d)+1)
        for k,v in enumerate(d):
            if k==0:
                nd[0]+=a*v;nd[1]+=q*v
            else:
                nd[k-1]+=2*a*v;nd[k+1]+=q*v
        d=nd
    return ans

def main():
    counter=0
    for a in [F(1,20),F(1,10),F(3,20),F(1,5),F(1,4),F(3,10),F(1,3),F(2,5),F(9,20)]:
        acoeff=weights(a,16); bcoeff=series_formula(a,16)
        for n,(u,v) in enumerate(zip(acoeff,bcoeff)):
            assert u==v,(a,n,u,v)
            counter+=1
        for n in range(0,5):
            brute=integrate_direct(a,n)
            assert brute==acoeff[n]/12,(a,n,brute,acoeff[n]/12)
            counter+=1
    counter+=symbolic_residue_checks()
    # Markov reciprocity and full covariance positivity
    for a in [F(1,20),F(1,10),F(1,4),F(1,3),F(2,5),F(9,20)]:
        u=weights(a,80)
        assert all(v>0 for v in u)
        counter+=len(u)
    # external asymptotic approximations numerically, not a proof
    for a in [.05,.1,.2,.25,1/3,.4,.45]:
        aa=F(str(a)); q=1-2*a
        seq=weights_float(a,500)
        c=float(seq[-1])
        rho=sqrt(8*a*q)
        if a<.1: pred=((1-10*a)/(1-4*a))*((1+6*a)/2)**500
        elif a>.4:pred=(2*(5*a-2)/(4*a-1))*(2-3*a)**500
        elif a==.1 or a==.4:pred=4*sqrt(2)/(3*sqrt(pi))*.8**500/sqrt(500)
        else:
            rstar=sqrt(2*a/q)
            def Hprime(x):
                N=4*(2*a+q*x*x);Np=8*q*x
                D=(2-x)*(4*a-q*x)
                Dp=-(4*a-q*x)-q*(2-x)
                return (Np*D-N*Dp)/D**2
            pred=(rstar/sqrt(2*pi))*(Hprime(rstar)-Hprime(-rstar))*rho**500/500**1.5
        assert abs(c/pred-1)<.15,(a,c,pred,c/pred)
        counter+=1
    print('PASS exact checks + asymptotic diagnostics:',counter)
    print('For a=1/3, normalized first 10 coefficients:',[str(v) for v in weights(F(1,3),9)])
    print('Critical a=1/4 first five normalized coefficients:',[str(v) for v in weights(F(1,4),4)])
    print('Green-Kubo asymptotic variance at a=1/3 = 7/12 and at a=1/4 = 5/4 (symbolic).')
if __name__=='__main__':main()
