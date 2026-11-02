"""Independent numerical checks of the surface-area spectrum for random 3D Minkowski sums.
No external data; Python 3.10+, numpy, scipy."""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.stats import chi2, ks_2samp

PI=np.pi

def p2(t): return (3*t*t-1)/2

def analytic_area(v, c=1., eps=.13):
    n=len(v); d=8*PI*eps**2/5
    gram=np.asarray(v)@np.asarray(v).T
    return 4*PI*n*n*c*c-d*(n+2*np.sum(p2(gram[np.triu_indices(n,1)])))

def quadratic_surface_quadrature(v, c=1., eps=.13, nodes=20, azimuths=64):
    # Directly integrate Gaussian curvature Jacobian det(hI+Hess_S h).
    # For P_2(v.u), Hess_S P_2=3[(v_t)(v_t)^T-(v.u)^2 I].
    z,w=leggauss(nodes); phi=2*PI*np.arange(azimuths)/azimuths
    S=0.
    for j,x in enumerate(z):
        sz=np.sqrt(1-x*x)
        ct=np.cos(phi); st=np.sin(phi)
        u=np.stack([sz*ct,sz*st,np.full(azimuths,x)],axis=-1)
        e1=np.stack([x*ct,x*st,np.full(azimuths,-sz)],axis=-1)
        e2=np.stack([-st,ct,np.zeros(azimuths)],axis=-1)
        t=u@v.T
        v1=e1@v.T; v2=e2@v.T
        scalar=len(v)*(c-eps/2)-1.5*eps*np.sum(t*t,axis=-1)
        b11=scalar+3*eps*np.sum(v1*v1,axis=-1)
        b22=scalar+3*eps*np.sum(v2*v2,axis=-1)
        b12=3*eps*np.sum(v1*v2,axis=-1)
        S+=w[j]*(2*PI/azimuths)*np.sum(b11*b22-b12*b12)
    return S



def p4(t): return (35*t**4-30*t*t+3)/8

def two_mode_area(v,c=1.,eps=.10,eta=.03):
    n=len(v); gram=v@v.T; ij=np.triu_indices(n,1)
    d2=8*PI*eps*eps/5; d4=4*PI*eta*eta
    return 4*PI*n*n*c*c - d2*(n+2*np.sum(p2(gram[ij]))) - d4*(n+2*np.sum(p4(gram[ij])))

def two_mode_quadrature(v,c=1.,eps=.10,eta=.03,nodes=22,azimuths=72):
    n=len(v)
    z,w=leggauss(nodes); phi=2*PI*np.arange(azimuths)/azimuths; res=0.
    for j,x in enumerate(z):
        sz=np.sqrt(1-x*x); ct=np.cos(phi); st=np.sin(phi)
        u=np.stack([sz*ct,sz*st,np.full(azimuths,x)],axis=-1)
        e1=np.stack([x*ct,x*st,np.full(azimuths,-sz)],axis=-1)
        e2=np.stack([-st,ct,np.zeros(azimuths)],axis=-1)
        t=u@v.T; v1=e1@v.T; v2=e2@v.T
        h=n*c + eps*np.sum(p2(t),axis=-1)+eta*np.sum(p4(t),axis=-1)
        fp=eps*3*t+eta*(35*t**3-15*t)/2
        fpp=eps*3+eta*(105*t*t-15)/2
        scalar=h-np.sum(t*fp,axis=-1)
        A=scalar+np.sum(fpp*v1*v1,axis=-1)
        B=scalar+np.sum(fpp*v2*v2,axis=-1)
        C=np.sum(fpp*v1*v2,axis=-1)
        res+=w[j]*(2*PI/azimuths)*np.sum(A*B-C*C)
    return res

def directions(rng,n):
    v=rng.normal(size=(n,3)); return v/np.linalg.norm(v,axis=1)[:,None]

def try_checks():
    rng=np.random.default_rng(202610311)
    c=1.;eps=.13;delta=8*PI*eps**2/5
    for n in (1,2,3,6):
        for _ in range(3):
            v=directions(rng,n)
            a=analytic_area(v,c,eps)
            b=quadratic_surface_quadrature(v,c,eps)
            assert abs(a-b)<1e-10,(n,a,b)
        print('quadrature agrees with spectral formula at n=',n)
    for n in (1,2,4,6):
        v=directions(rng,n)
        a=two_mode_area(v)
        b=two_mode_quadrature(v)
        assert abs(a-b)<1e-10,(n,a,b)
        print('two-harmonic independent area integration, n=',n)
    for n in (2,5,20):
        vals=[]
        for _ in range(4500):
            v=directions(rng,n)
            vals.append(analytic_area(v,c,eps))
        vals=np.array(vals)
        mu=4*PI*n*n*c*c-n*delta
        var=2*n*(n-1)*delta*delta/5
        relmu=abs(np.mean(vals)-mu)/max(1,np.sqrt(var))
        relvar=abs(np.var(vals,ddof=1)/var-1)
        print('n',n,'scaled mean residual',relmu,'relative variance error',relvar)
        assert relmu<.08 and relvar<.13
    m=260; reps=5200; centered=np.empty(reps)
    for i in range(reps):
        v=directions(rng,m)
        H=v.T@v-(m/3)*np.eye(3)
        centered[i]=delta*(1-1.5*np.sum(H*H)/m)
    limit=delta*(1-chi2.rvs(df=5,size=reps,random_state=rng)/5)
    ks=ks_2samp(centered,limit).statistic
    print('finite-n / chi-square limit two-sample KS',ks)
    assert ks<.07
    assert abs(np.mean(centered))<.035*delta
    print('ALL_3D_ROTATED_MINKOWSKI_SURFACE_CHECKS_PASSED')

if __name__=='__main__': try_checks()
