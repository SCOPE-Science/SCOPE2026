#!/usr/bin/env python3
"""Independent numerical checks for finite-network logistic confidence equilibria.
Scientific tests only; results are not an infinite-family proof.
"""
from itertools import product, combinations
import numpy as np
from scipy.special import expit
from scipy.optimize import root, brentq

def build_adj(n, edges):
    a=np.zeros((n,n),dtype=float)
    for i,j in edges: a[i,j]=a[j,i]=1.
    return a

def weighted(x,A,g,d):
    n=len(x)
    ze=np.r_[-1.,1.]
    vals=np.concatenate((x,ze))
    mask=np.concatenate((A,np.ones((n,2))),axis=1)
    dif=vals[np.newaxis,:]-x[:,np.newaxis]
    w=expit(g*(d-dif*dif))*mask
    return dif,w

def F(x,A,g,d):
    diff,w=weighted(x,A,g,d)
    return (w*diff).sum(axis=1)/w.sum(axis=1)

def jac(x,A,g,d):
    n=len(x)
    diff,w=weighted(x,A,g,d)
    dwddiff=-2*g*diff*w*(1-w) # derivative w wrt diff
    npart=(w*diff).sum(axis=1)
    denominator=w.sum(axis=1)
    J=np.zeros((n,n))
    for i in range(n):
        for k in range(n):
            dN=0.;dD=0.
            for j in range(n+2):
                ddelta=(1 if j==k else 0)-(1 if i==k else 0)
                dN+=(dwddiff[i,j]*diff[i,j]+w[i,j])*ddelta
                dD+=dwddiff[i,j]*ddelta
            J[i,k]=(dN*denominator[i]-npart[i]*dD)/denominator[i]**2
    return J

def zcoefficient(signs,A):
    n=len(signs)
    same=(signs[:,None]==signs[None,:])*A
    opp=(signs[:,None]!=signs[None,:])*A
    L=np.diag(same.sum(axis=1))-same
    return np.linalg.solve(np.eye(n)+L,-2*signs*(1+opp.sum(axis=1)))

def test_graph(n,edges,g,d):
    a=build_adj(n,edges)
    stable=0;maxres=0.;maxerr=0.;minmargin=1e9
    r=np.exp(-g*(4-d))
    for signs in product([-1.,1.],repeat=n):
        signs=np.array(signs)
        sol=root(F,signs+ r*zcoefficient(signs,a),args=(a,g,d),tol=1e-12)
        x=sol.x
        residual=np.linalg.norm(F(x,a,g,d),np.inf)
        maxres=max(maxres,residual)
        if residual>1e-9 or np.linalg.norm(x-signs,np.inf)>.15:
            raise AssertionError((n,edges,g,d,signs,x,residual))
        eig=np.linalg.eigvals(jac(x,a,g,d));minmargin=min(minmargin,-np.max(eig.real))
        assert max(eig.real)<-1e-4,(x,eig)
        stable+=1
        z=zcoefficient(signs,a)
        maxerr=max(maxerr,np.linalg.norm((x-signs)/r-z,np.inf))
    x0=np.zeros(n);assert np.linalg.norm(F(x0,a,g,d),np.inf)<1e-14
    eig=np.linalg.eigvals(jac(x0,a,g,d));assert max(eig.real)<0,('center',eig)
    stable+=1
    return stable,maxres,maxerr,minmargin

def test_scalar(d,g):
    def f(x):return F(np.array([x]),np.zeros((1,1)),g,d)[0]
    xs=np.r_[0,np.linspace(1e-7,.999999,20001),1]
    ys=np.array([f(x) for x in xs])
    zeros=[]
    for i in range(1,len(xs)-1):
        if ys[i]*ys[i+1]<0:zeros.append(brentq(f,xs[i],xs[i+1],xtol=1e-14))
    assert len(zeros)==2, (d,g,zeros)
    small,large=zeros
    assert jac(np.array([0.]),np.zeros((1,1)),g,d)[0,0]<0
    assert jac(np.array([small]),np.zeros((1,1)),g,d)[0,0]>0
    assert jac(np.array([large]),np.zeros((1,1)),g,d)[0,0]<0
    a=np.sqrt(d)-1
    coeff=np.log(2*a/(1-a))/(2*np.sqrt(d))
    print('scalar',d,g,'roots',small,large,'small 1/g coeff est',(small-a)*g,'theory',coeff,'large deficit /r',(1-large)/np.exp(-g*(4-d)))

if __name__=='__main__':
    checks=0
    for n in range(1,5):
        E=list(combinations(range(n),2))
        tested=[(),tuple(E),tuple((i,i+1) for i in range(n-1))]
        if n>=4:tested.append(((0,1),(1,2),(0,2),(2,3)))
        for ee in dict.fromkeys(tested):
            for g,d in [(12.,3.2),(18.,3.2),(13.,2.8)]:
                stable,res,err,margin=test_graph(n,ee,g,d)
                assert stable==2**n+1
                checks+=stable
                print('graph',n,len(ee),'gamma',g,'delta',d,'attractors',stable,'maxres',res,'leading-term-error',err,'spectral-margin',margin)
    for g in [18.,24.,32.]:
        for d in [1.5,2.0,2.5,3.0,3.5]:
            test_scalar(d,g);checks+=3
    print('PASS, stable configurations checked=',checks)

# Independent high-precision scalar limit checks (not an infinite proof).
def test_scalar_high_precision():
    import mpmath as mp
    mp.mp.dps=75
    cases=0
    for ds in ('1.5','2.0','2.8','3.4'):
        d=mp.mpf(ds); a=mp.sqrt(d)-1
        leading=mp.log(2*a/(1-a))/(2*mp.sqrt(d))
        for gi in (20,30,40):
            g=mp.mpf(gi)
            def w(z): return 1/(1+mp.exp(g*(z*z-d)))
            def scalar(x): return (1-x)*w(x-1)-(1+x)*w(x+1)
            # A sign-change bracket strictly enclosing the inner root.
            lo=a/2
            hi=(a+1)/2
            # widened if finite-gamma root is more displaced.
            lo=max(mp.mpf('0.0000001'),lo)
            hi=min(mp.mpf('0.9999999'),hi)
            if scalar(lo)*scalar(hi)>=0:
                lo=mp.mpf('0.0000001'); hi=mp.mpf('0.99999')
            assert scalar(lo)<0 and scalar(hi)>0,(ds,gi,scalar(lo),scalar(hi))
            for _ in range(250):
                md=(lo+hi)/2
                if scalar(md)>0:hi=md
                else:lo=md
            small=(lo+hi)/2
            r=mp.exp(-g*(4-d))
            lo=1-10*r; hi=mp.mpf('1')
            assert scalar(lo)>0 and scalar(hi)<0,(ds,gi,scalar(lo),scalar(hi))
            for _ in range(260):
                md=(lo+hi)/2
                if scalar(md)>0:lo=md
                else:hi=md
            large=(lo+hi)/2
            assert abs(scalar(small))<mp.mpf('1e-55')
            assert abs(scalar(large))<mp.mpf('1e-50')
            assert abs((1-large)/r-2)<mp.mpf('0.02'),(ds,gi,mp.nstr((1-large)/r,20))
            assert abs((small-a)*g-leading)<mp.mpf('0.5'),(ds,gi)
            print('high_precision_scalar',ds,gi,'inner_shift_coefficient',mp.nstr((small-a)*g,18),'predicted',mp.nstr(leading,18),'outer_ratio',mp.nstr((1-large)/r,18))
            cases+=1
    return cases

if __name__=='__main__':
    print('PASS, arbitrary-precision scalar cases=',test_scalar_high_precision())
