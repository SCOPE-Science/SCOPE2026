"""Reproduce the exact one-probe Nyström log-determinant calculations."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import spence

PI=math.pi

def formulas(a,b):
    assert a >= b > 0
    u=(math.sqrt(a)-math.sqrt(b))/(math.sqrt(a)+math.sqrt(b))
    v=(math.sqrt(a*(1+a))-math.sqrt(b*(1+b)))/(math.sqrt(a*(1+a))+math.sqrt(b*(1+b)))
    mean=math.log((1+a)*(1+b))+2*math.log((math.sqrt(a)+math.sqrt(b))/(math.sqrt(a*(1+a))+math.sqrt(b*(1+b))))
    var=2*(spence(1-u*u)+spence(1-v*v)-2*spence(1-u*v))
    return mean,var,2*(mean*mean+var)

def log_residual(a,b,theta):
    x=a*math.cos(theta)**2+b*math.sin(theta)**2
    y=a*(1+a)*math.cos(theta)**2+b*(1+b)*math.sin(theta)**2
    return math.log((1+a)*(1+b)*x/y)

def from_angular_integrals(a,b):
    m=quad(lambda t:log_residual(a,b,t)/PI,0,PI,epsabs=1e-11,epsrel=1e-11,limit=300)[0]
    m2=quad(lambda t:log_residual(a,b,t)**2/PI,0,PI,epsabs=1e-11,epsrel=1e-11,limit=300)[0]
    return m,m2-m*m,2*m2

def matrix_residual(A,omega):
    B=(A@omega).reshape(2,1)
    N=(B@B.T)/float(omega@A@omega)
    P=np.eye(2)+N
    ev,Q=np.linalg.eigh(P)
    invs=(Q*(ev**-0.5))@Q.T
    M=invs@(np.eye(2)+A)@invs
    L,eigvec=np.linalg.eigh(M)
    assert np.min(L)>0.9999999999
    return float(np.sum(np.log(L))),M

def main():
    rng=np.random.default_rng(45089)
    counts={'independent_angular_integrals':0,'direct_matrix_orientations':0,'asymptotic_scales':0,'two_step_Lanczos':0}
    for idx in range(100):
        a=math.exp(rng.uniform(-4,7));b=math.exp(rng.uniform(-5,math.log(a)))
        mean,var,mse=formulas(a,b)
        m2,v2,q2=from_angular_integrals(a,b)
        assert np.isclose([mean,var,mse],[m2,v2,q2],rtol=2e-7,atol=2e-9).all(),(a,b,mean,var,mse,m2,v2,q2)
        assert var>=-1e-10 and mse>=2*math.log1p(b)**2-1e-9
        counts['independent_angular_integrals']+=1
    for idx in range(480):
        a=math.exp(rng.uniform(-2,7));b=math.exp(rng.uniform(-3,math.log(a)))
        theta=float(rng.uniform(-PI,PI))
        omega=rng.normal(size=2)
        if np.linalg.norm(omega)<1e-6: continue
        U=np.array([[math.cos(theta),-math.sin(theta)],[math.sin(theta),math.cos(theta)]])
        A=U@np.diag([a,b])@U.T
        z,M=matrix_residual(A,omega)
        z_formula=math.log((1+a)*(1+b)*(a*(U.T@omega)[0]**2+b*(U.T@omega)[1]**2)/(a*(1+a)*(U.T@omega)[0]**2+b*(1+b)*(U.T@omega)[1]**2))
        assert abs(z-z_formula)<8e-11,(z,z_formula,a,b)
        # A matrix with two distinct eigenvalues is integrated exactly by two-step Lanczos.
        w=rng.normal(size=2);norm=float(np.linalg.norm(w));q0=w/norm
        h=float(q0@M@q0);v1=M@q0-h*q0;beta=float(np.linalg.norm(v1))
        if beta>1e-9:
            q1=v1/beta
            T=np.array([[h,beta],[beta,float(q1@M@q1)]])
            e,V=np.linalg.eigh(T)
            SLQ=norm**2*float((V[0]**2)@np.log(e))
            em,Q=np.linalg.eigh(M)
            exact=float((Q.T@w)**2@np.log(em))
            assert abs(SLQ-exact)<2e-9,(SLQ,exact)
            counts['two_step_Lanczos']+=1
        counts['direct_matrix_orientations']+=1
    b=1.0;lb=math.log1p(b)
    ratios=[]
    for a in [1e5,1e6,1e7,1e8]:
        eps=math.sqrt(b/a);rho=(1+b)/(1+a)
        def integrand(s):
            h=math.log1p(s*s)-math.log1p(rho*s*s)
            return (2*lb*h+h*h)/(s*s+eps*eps)
        # Integrate the excess directly: angular quadrature misses rare directions.
        excess=(4*eps/PI)*(quad(integrand,0,1,epsabs=1e-12,limit=300)[0]+quad(integrand,1,np.inf,epsabs=1e-12,limit=300)[0])
        leading=8*eps*(lb+2*math.log(2))
        rat=excess/leading
        assert 0.95<rat<1.02,(a,rat)
        ratios.append(rat);counts['asymptotic_scales']+=1
    assert ratios[-1]>ratios[0]
    print('VERIFY_OK',counts,'asymptotic_ratios',ratios)

if __name__=='__main__':main()
