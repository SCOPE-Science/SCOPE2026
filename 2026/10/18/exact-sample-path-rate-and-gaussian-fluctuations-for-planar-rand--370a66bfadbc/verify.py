"""Reproduce the planar Gaussian-line-search fluctuation formulas.

Requires: numpy, scipy, sympy. No external data or network.
"""
import math
from fractions import Fraction
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.special import spence

def dilog(z):
    return float(spence(1.0-z))

def formula(q):
    beta=2*q/(1+q*q)
    mean=2*math.log((1+q*q)/2)
    var_X=math.pi**2/3+4*dilog(-q*q)
    cov_X=2*(dilog(beta*beta)+dilog(q*q)-2*dilog(beta*q))
    var_total=math.pi**2/3+2*dilog(q**4)+4*dilog(beta*beta)-8*dilog(beta*q)
    lam=(3+q*q+math.sqrt(1+14*q*q+q**4))/8
    return mean,var_X,cov_X,var_total,lam

def kernel(q,theta):
    return (1-q*q)/(2*math.pi*(1-2*q*math.cos(theta)+q*q))

def g(theta):
    return math.log(max((1+math.cos(theta))/2,1.e-300))

def integrate_p(q,fun):
    return quad(lambda theta:kernel(q,theta)*fun(theta),0,2*math.pi,
                points=[math.pi],epsabs=1.e-10,epsrel=1.e-10,limit=200)[0]

def verify():
    s=sp.symbols('s',real=True)
    M=sp.Matrix([[3+4*s+s*s,1-s*s],[1-s*s,3-4*s+s*s]])/8
    t=sp.symbols('t')
    assert sp.factor(M.charpoly(t).as_expr()-
                     (t*t-(3+s*s)*t/4+(1-s*s)/8))==0
    # independent expansion of fourth moments from E[cos(2 theta)]=q, E[cos(4 theta)]=q^2
    z=sp.symbols('z',real=True)
    c=sp.symbols('c',real=True)
    assert sp.expand((1+c)**2/4 -(3+4*c+(2*c*c-1))/8)==0
    tested=0
    for q in (0,.2,1/3,.5,.7,.8,.9):
        mu,V,C,S,lam=formula(q)
        assert abs(S-(V+2*C))<1e-11
        assert V>0 and C>=-1e-12 and S>0
        assert math.exp(mu)<lam and lam<1
        # Independent one-dimensional angular quadratures, not resampling the formula.
        r=q*q
        avg=integrate_p(r,g)
        second=integrate_p(r,lambda theta:g(theta)**2)
        assert abs(mu-avg)<2e-7,(q,'mean',mu,avg)
        assert abs(V-(second-avg*avg))<2e-6,(q,'variance',V,second-avg*avg)
        h=lambda theta:2*math.log(abs(1+q*complex(math.cos(theta),math.sin(theta))))-2*math.log(2)
        ch=integrate_p(q,h)
        C_integral=integrate_p(q,lambda theta:(h(theta)-ch)**2)
        assert abs(C-C_integral)<1e-7,(q,'covariance',C,C_integral)
        tested+=1
    # Direct trajectory simulation of independent Gaussian corrections, without
    # sampling the theoretical angular kernel.
    rng=np.random.default_rng(481025)
    trajectories=240000
    for a,b in ((1.,1.),(1.,2.),(1.,4.),(1.,9.)):
        q=(b-a)/(b+a)
        normals=rng.standard_normal((trajectories+1,2))
        w=np.column_stack((a*normals[:,0],b*normals[:,1]))
        normal_vectors=np.column_stack((-w[:,1],w[:,0]))/np.linalg.norm(w,axis=1)[:,None]
        products=np.sum(normal_vectors[:-1]*normal_vectors[1:],axis=1)
        increments=np.log(np.maximum(products*products,1e-300))
        emp_mean=increments.mean()
        emp_v=increments.var()
        emp_cov=np.mean((increments[:-1]-emp_mean)*(increments[1:]-emp_mean))
        mu,V,C,S,_=formula(q)
        assert abs(emp_mean-mu)<.028,(q,'MC mean',emp_mean,mu)
        assert abs(emp_v-V)<.09,(q,'MC var',emp_v,V)
        assert abs(emp_cov-C)<.065,(q,'MC adjacent',emp_cov,C)
    print('PASS: exact characteristic polynomial; seven independent angular quadratures '+
          '(mean, variance, lag-one covariance); four direct Gaussian trajectory checks.')
if __name__=='__main__': verify()
