"""Reproducible numerical tests for Crofton-ellipsoid chord endpoint asymptotics.
Run with numpy and scipy: python checker.py. Numerical tests do not replace proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln, betaln

def parameters(axes):
    axes=np.asarray(axes,dtype=float)
    assert len(axes)>=2 and np.all(axes>0)
    a=float(max(axes)); r=int(sum(np.isclose(axes,a,rtol=1e-12,atol=0)))
    gamma=np.array([(a/x)**2-1 for x in axes if x<a*(1-1e-12)])
    assert len(gamma)==len(axes)-r
    return a,r,gamma

def sphere_quadrature_sample(n, axes, seed=314159):
    rng=np.random.default_rng(seed)
    g=rng.normal(size=(n,len(axes)))
    return g/np.linalg.norm(g,axis=1)[:,None]

def constant(a,r,gamma,d,H):
    beta=d-(r+1)/2
    logc=beta*math.log(2)+gammaln(d/2)+gammaln((d+1)/2)-gammaln(r/2)-gammaln(beta+1)-math.log(H)
    if len(gamma):logc-=.5*sum(np.log(gamma))
    return math.exp(logc),beta

def axis_integrals(d,r,gamma,eps):
    """Exact quadrature for spheroids with all shorter semiaxes equal."""
    assert len(gamma)==0 or np.allclose(gamma,gamma[0])
    if len(gamma)==0:
        p=(d-1)/2; return (2*eps-eps*eps)**p,1.
    m=d-r; g=float(gamma[0]); aa=m/2; bb=r/2
    norm=math.exp(-betaln(aa,bb))
    # t=sum of squared coordinates over shorter-axis eigenspace.
    H=quad(lambda t: t**(aa-1)*(1-t)**(bb-1)*math.sqrt(1+g*t)*norm,0,1,
           epsabs=1e-11,epsrel=1e-11,limit=350,points=[0,.5,1])[0]
    delta=2*eps-eps*eps
    tmax=min(1, delta/((1-eps)**2*g))
    p=(d-1)/2
    integral=quad(lambda t: t**(aa-1)*(1-t)**(bb-1)*math.sqrt(1+g*t)
          *(delta-(1-eps)**2*g*t)**p *norm,0,tmax,
          epsabs=1e-14,epsrel=1e-11,limit=350,points=[0,tmax])[0]
    return integral/H,H

def analytic_tail(axes,t,nquad=60000):
    """Approximate via QMC U directions, independent validation uses geometry below."""
    a,r,gamma=parameters(axes)
    g=sphere_quadrature_sample(nquad,axes)
    z=np.sum((a/np.asarray(axes))**2*g*g,axis=1)
    weights=np.sqrt(z)
    p=(len(axes)-1)/2
    return np.mean(weights*np.maximum(1-(t/(2*a))**2*z,0)**p)/np.mean(weights)

def geometric_comparison(axes,n=600,seed=271828):
    """Compare direct quadratic intersections to normalized-ball formula.
    Uses Haar U, projected offsets and cross-section discriminants.
    """
    a=np.asarray(axes,dtype=float); d=len(a)
    rng=np.random.default_rng(seed)
    Q=np.diag(1/a**2); S=np.diag(a*a)
    max_diff=0.
    for i in range(n):
        u=rng.normal(size=d);u/=np.linalg.norm(u)
        # orthonormal matrix with first column u, remaining columns span u-perp
        w=rng.normal(size=(d,d));w[:,0]=u
        # Orthogonalize other columns without changing first one
        U,_=np.linalg.qr(w); U[:,0]*=np.sign(U[:,0]@u)
        B=U[:,1:]
        if abs(U[:,0]@u-1)>1e-10: raise AssertionError('orthogonality')
        z=rng.normal(size=d-1);z/=np.linalg.norm(z)
        z*=rng.random()**(1/(d-1))
        # y=B chol(B^T S B) z; projection space uniform
        C=B.T@S@B
        offset=B@np.linalg.cholesky(C)@z
        q=u@Q@u; cr=u@Q@offset; h=offset@Q@offset
        disc=cr*cr+q*(1-h)
        L=2*math.sqrt(max(disc,0))/q
        expected=2*math.sqrt(1-np.linalg.norm(z)**2)/math.sqrt(q)
        max_diff=max(max_diff,abs(L-expected))
    assert max_diff<2e-11,max_diff
    return max_diff

def endpoint_ratio_importance(axes,eps,seed=161803,n=120000):
    """Independent small-region integral over transverse modes, r may be repeated.
    Samples exactly the limiting beta-ball measure, and integrates true finite eps density.
    """
    a,r,gamma=parameters(axes);d=len(axes);m=d-r
    if not m: return ((2*eps-eps*eps)/(2*eps))**((d-1)/2)
    rng=np.random.default_rng(seed)
    y=rng.normal(size=(n,m))
    y/=np.linalg.norm(y,axis=1)[:,None]
    radii=rng.beta(m/2,(d+1)/2,size=n)
    y*=np.sqrt(radii[:,None])
    delta=2*eps-eps*eps
    X=delta/(1-eps)**2*radii
    zz=delta/(1-eps)**2*np.sum(y*y/gamma[None,:],axis=1)
    assert max(zz)<1, 'asymptotic region not inside z-ball: choose smaller eps'
    v=np.mean((1-zz)**(r/2-1)*np.sqrt(1+X))
    return (delta/(2*eps))**(d-(r+1)/2)*(1-eps)**(-m)*v

def crossover_F(d,r,lam):
    """Beta average in the one-axis coalescence crossover (r+1 equal axes at limit)."""
    beta=d-(r+2)/2
    z=math.exp(-betaln(.5,r/2))
    lim=min(1,2/lam) if lam>0 else 1
    return quad(lambda t:t**(-.5)*(1-t)**(r/2-1)*max(0,1-lam*t/2)**beta*z,
        0,lim,epsabs=2e-12,epsrel=2e-12,limit=350)[0]

def crossover_ratio(d,r,low_axes,lam,eps,n=260000,seed=112358):
    """Direct exact small-region spherical integral, importance sampled.
    Returns true upper-tail / (limiting prefactor*epsilon^beta) via random quadrature.
    """
    k=r+1;m=d-k;p=(d-1)/2;beta=p+m/2
    assert len(low_axes)==m
    gamma=(2/np.asarray(low_axes,dtype=float))**2-1
    assert np.all(gamma>0)
    rng=np.random.default_rng(seed)
    # Uniform spherical normal for independent H_eps/H_0 correction.
    normals=rng.normal(size=(n,d));normals/=np.linalg.norm(normals,axis=1)[:,None]
    X0=np.sum(gamma[None,:]*normals[:,k:]**2,axis=1)
    h0=np.mean(np.sqrt(1+X0));he=np.mean(np.sqrt(1+X0+lam*eps*normals[:,r]**2))
    if m:
        y=rng.normal(size=(n,m));y/=np.linalg.norm(y,axis=1)[:,None]
        rho2=rng.beta(m/2,p+1,size=n);y*=np.sqrt(rho2[:,None])
    else:
        y=np.zeros((n,0));rho2=np.zeros(n)
    t=rng.beta(.5,r/2,size=n)
    delta=2*eps-eps*eps
    z2=delta/(1-eps)**2*np.sum(y*y/gamma[None,:],axis=1)
    assert np.max(z2)<1
    X=delta/(1-eps)**2*rho2 +lam*eps*(1-z2)*t
    v=(1-z2)**(k/2-1)*np.sqrt(1+X)*       (np.maximum(0,1-rho2-(1-eps)**2*lam*eps*(1-z2)*t/delta)/        np.maximum(1-rho2,1e-150))**p
    return (delta/(2*eps))**beta*(1-eps)**(-m)*h0/he*np.mean(v)

def test():
    for d in (2,3,4,7):
        sph=np.ones(d)*1.7
        c,b=constant(1.7,d,[],d,1)
        assert abs(c-2**((d-1)/2))<1e-12
        assert b==(d-1)/2
        for e in (.02,.09,.35):
            val,H=axis_integrals(d,d,[],e)
            assert H==1
            assert abs(val-(2*e-e*e)**((d-1)/2))<1e-12
    for axes in ([2,1,1], [2,2,1], [2,1,1,1], [2,2,1,1], [2,2,2,1], [2,2,2,2]):
        a,r,gamma=parameters(axes); d=len(axes)
        assert len(gamma)==0 or np.allclose(gamma,gamma[0])
        ratios=[]
        for eps in (.045,.0225,.01125,.005625):
            survival,H=axis_integrals(d,r,gamma,eps)
            c,b=constant(a,r,gamma,d,H)
            ratios.append(survival/(c*eps**b))
        print('SPHEROID',axes,'beta',b,'ratios', [round(x,6) for x in ratios]);
        assert abs(ratios[-1]-1)<.08,(axes,ratios)
        assert abs(ratios[-1]-1)<abs(ratios[0]-1)+.001
    for axes in ([2,1.5,1.1,1],[2,2,1.2,1],[2,2,2,1],[1.25,1.25,1.25,1.25]):
        print('CHORD GEOMETRY',axes,geometric_comparison(axes))
    for axes in ([2,1.5,1.1,1],[2,2,1.2,1],[2,2,2,1],[2,1.4,1.1,0.9,0.8]):
        rr=[]
        for eps in (.025,.0125,.00625):
            rr.append(endpoint_ratio_importance(axes,eps))
        print('MULTIAXIS ENDPOINT',axes,[round(v,6) for v in rr])
        assert abs(rr[-1]-1)<.055,(axes,rr)
        assert abs(rr[-1]-1)<abs(rr[0]-1)+.005
    # Test a genuinely nontrivial shape-dependent axis-coalescence crossover.
    for d,r,low,lam in [(4,1,[1.3,.9],1.5),(4,1,[1.3,.9],3.),
         (5,2,[1.2,.85],2.),(4,3,[],2.0),(5,3,[.8],4.0)]:
        F=crossover_F(d,r,lam)
        rr=[]
        for eps in (.028,.014,.007):
            rr.append(crossover_ratio(d,r,low,lam,eps)/F)
        print('COALESCENCE',d,r,low,lam,'F',round(F,7),'ratios',[round(v,5) for v in rr])
        assert abs(rr[-1]-1)<.045,(d,r,rr)
        assert abs(rr[-1]-1)<abs(rr[0]-1)+.012
    # Low-tail exact 1D quadrature for the d=3 prolate spheroid.
    d=3;r=1;g=3.
    aa=(d-r)/2;bb=r/2; norm=math.exp(-betaln(aa,bb)); H=axis_integrals(d,r,np.array([g,g]),.01)[1]
    M=quad(lambda t:t**(aa-1)*(1-t)**(bb-1)*(1+g*t)**1.5*norm,0,1)[0]
    c=(d-1)/(8*2**2)*M/H
    for t in (.02,.05,.1):
        eps=1-t/4
        # Under direction beta, integrate weight*(1 - (1-(t/4)^2 * z)^p)
        val=quad(lambda x:x**(aa-1)*(1-x)**(bb-1)*math.sqrt(1+g*x)*
                (1-(1-(t/4)**2*(1+g*x))**((d-1)/2))*norm,0,1)[0]/H
        print('LOW TAIL t, ratio',t,val/(c*t*t))
        assert abs(val/(c*t*t)-1)<.005
    print('ALL_CROFTON_ELLIPSOID_ENDPOINT_CHECKS_PASSED')
if __name__=='__main__':test()
