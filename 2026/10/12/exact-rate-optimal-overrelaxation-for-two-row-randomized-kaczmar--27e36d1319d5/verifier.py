#!/usr/bin/env python3
"""Exact algebraic and numeric checks for a two-row relaxed randomized Kaczmarz rate."""
from fractions import Fraction as F
import sympy as S

def exact_symbolic():
    p,t,r,U,W,V=S.symbols('p t r U W V', real=True)
    q=1-p
    X=S.Matrix([[U,W],[W,V]])
    A=S.Matrix([[1-t*p,-t*r],[-t*r,1-t*q]])
    B=S.Matrix([[1-t*p,t*r],[t*r,1-t*q]])
    E=S.expand((A*X*A+B*X*B)/2)
    target=[(1-t*p)**2*U+t**2*p*q*V,
            t**2*p*q*U+(1-t*q)**2*V,
            (1-t+2*t**2*p*q)*W]
    for l,rhs in zip([E[0,0],E[1,1],E[0,1]],target):
        expr=S.Poly(S.expand(l-rhs),r)
        # In this model r^2=p*q; replace its even powers and check no odd powers.
        rem=S.Integer(0)
        for (power,),coef in expr.terms():
            assert power%2==0, (power,coef)
            rem+=coef*(p*q)**(power//2)
        assert S.simplify(rem)==0, rem
    pp,qq,omega,delta=S.symbols('pp qq omega delta',positive=True)
    vec=S.Matrix([pp,qq])
    M=S.eye(2)-2*omega*S.diag(pp,qq)+omega**2*vec*vec.T
    assert S.simplify(M[0,0]-(1-omega*pp)**2)==0
    assert S.simplify(M[0,1]-omega**2*pp*qq)==0
    f=pp**2/(2*pp-delta/omega)+qq**2/(2*qq-delta/omega)
    determinant=S.det(2*omega*S.diag(pp,qq)-omega**2*vec*vec.T-delta*S.eye(2))
    certificate=(2*omega*pp-delta)*(2*omega*qq-delta)*(1-omega*f)
    assert S.simplify(determinant-certificate)==0
    z=S.symbols('z',real=True)
    ss=pp**2/(2*pp-z)+qq**2/(2*qq-z)
    assert S.simplify(ss-z*S.diff(ss,z)-2*(pp**2*(pp-z)/(2*pp-z)**2+qq**2*(qq-z)/(2*qq-z)**2))==0
    print('SYMBOLIC_OK')

def matrix(p,t):
    q=1-p
    return (((1-t*p)**2,t*t*p*q),(t*t*p*q,(1-t*q)**2))

def eig_rho(m):
    a,b=m[0]; _,d=m[1]
    return (float(a+d)+((float(a-d)**2+4*float(b)**2)**0.5))/2

def verify_rational_samples():
    cases=0
    for d in range(2,41):
      for j in range(1,d):
        p=F(j,d)
        q=1-p
        for wt in [F(1,10),F(1,2),F(1,1),F(7,5),F(3,2),F(19,10),F(2,1),F(21,10)]:
            mat=matrix(p,wt)
            aa=(1-wt*p)**2; bb=(1-wt*q)**2; off=wt**2*p*q
            assert mat==((aa,off),(off,bb))
            K=((1-aa,-off),(-off,1-bb))
            assert (K[0][0]*K[1][1]-K[0][1]**2)==(1-aa)*(1-bb)-off**2
            if 0<wt<2:
                assert (1-aa)>0 and K[0][0]*K[1][1]-K[0][1]**2>0
            if wt==2:
                assert (mat[0][0]+mat[0][1])==1
                assert (mat[1][0]+mat[1][1])==1
            cases+=1
    print('RATIONAL_CASES_OK',cases)

def optimize(c):
    p=(1+c)/2; q=(1-c)/2
    def ss(z): return p*p/(2*p-z)+q*q/(2*q-z)
    def numerator(z):
        return p*p*(p-z)/(2*p-z)**2 + q*q*(q-z)/(2*q-z)**2
    lo,hi=0.0,2*q
    for _ in range(120):
        mid=(lo+hi)/2
        if numerator(mid)>0: lo=mid
        else: hi=mid
    z=(lo+hi)/2
    t=1/ss(z)
    rho=1-z/ss(z)
    return t,rho,z

def numerical_tests():
    for c in [0.0,.05,.2,.5,.8,.95,.99,.9999]:
        t,r,z=optimize(c)
        assert 1-1e-8<=t<2
        assert r<=(1+c*c)/2+1e-8
        assert abs(eig_rho(matrix((1+c)/2,t))-r)<3e-12
        assert all(eig_rho(matrix((1+c)/2,w))>=r-1e-8 for w in [.001,.25,.75,1.,t,1.2,1.5,1.75,1.999])
        print('COS',c,'optimal_relaxation',round(t,12),'optimal_rate',round(r,12),'default_rate',round((1+c*c)/2,12))
    for c in [.9,.99,.999,.9999]:
        t,r,z=optimize(c)
        default_gap=(1-c*c)/2
        optimal_gap=1-r
        print('GAP_RATIO',c,optimal_gap/default_gap)

if __name__=='__main__':
    exact_symbolic();verify_rational_samples();numerical_tests();print('VERIFY_OK')
