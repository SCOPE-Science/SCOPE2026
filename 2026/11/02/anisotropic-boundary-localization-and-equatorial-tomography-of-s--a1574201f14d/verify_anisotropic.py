"""Reproducible numerical tests for angular boundary laws of spherical cells."""
import numpy as np
from scipy.special import roots_legendre
from scipy.spatial import HalfspaceIntersection


def qh(theta, alpha, eps):
    return (theta/np.pi + eps*np.sin(2*theta)*np.cos(2*alpha)/(6*np.pi),
            .5-eps*np.sin(theta)**2*np.cos(2*alpha)/4)

def a(alpha,eps):
    return (1+eps*np.cos(2*alpha)/3)/np.pi

def exact_integral(n,eps,N=400,M=720):
    nodes, wgts=roots_legendre(N)
    theta=(nodes+1)*np.pi/2
    w=wgts*np.pi/2
    al=2*np.pi*np.arange(M)/M
    q,h=qh(theta[:,None],al[None,:],eps)
    dens=n*h*np.sin(theta[:,None])*np.maximum(1-q,0)**(n-1)
    return np.dot(w, np.sum(dens,axis=1))*(2*np.pi/M)

def random_dirs(rng,n,eps):
    out=[]
    while len(out)<n:
        xyz=rng.normal(size=(max(n,50),3));xyz/=np.linalg.norm(xyz,axis=1)[:,None]
        test=rng.uniform(0,1+abs(eps),size=len(xyz))
        out.extend(xyz[test<1+eps*(xyz[:,0]**2-xyz[:,1]**2)].tolist())
    return np.array(out[:n])

def poly_perimeter(us):
    signs=np.sign(us[:,2])
    # gnomonic polytope with p=(0,0,1). Lines are planar.
    A=-signs[:,None]*us[:,:2]
    b=np.abs(us[:,2])
    hs=np.column_stack((A,-b))
    try:
        mesh=HalfspaceIntersection(hs,np.zeros(2))
    except (ValueError, RuntimeError):
        return None
    v=mesh.intersections
    if len(v)<3:
        return None
    ang=np.arctan2(v[:,1],v[:,0]);v=v[np.argsort(ang)]
    x=np.column_stack((v,np.ones(len(v))))
    x/=np.linalg.norm(x,axis=1)[:,None]
    return np.sum(np.arccos(np.clip(np.sum(x*np.roll(x,-1,axis=0),axis=1),-1,1)))

def main():
    for eps in [0.,.3,.7]:
        # The quadrupolar test family has fully explicit angular separation probability and coarea density.
        # Check exact q via independently discretized integration over normal orientations y,phi.
        for theta in [.17,.7,1.35,2.7]:
            alpha=.37
            # E[f(n)|phi] for n=(sqrt(1-y²)sin(phi), y, sqrt(1-y²)cos(phi)),
            # rotated horizontally by alpha about z: integrate y moments explicitly.
            # As an alternative sample the sphere directly via tensor quadrature over y,phi.
            x=np.array([np.sin(theta)*np.cos(alpha),np.sin(theta)*np.sin(alpha),np.cos(theta)])
            # Midpoint sphere latitude, uniform longitude. Quadrature is exact in degree-two latitudes.
            ym=-1+(np.arange(300)+.5)*2/300
            ph=(np.arange(1300)+.5)*2*np.pi/1300
            py=np.sqrt(1-ym[:,None]**2)
            uxx=py*np.cos(ph)[None,:]
            uyy=py*np.sin(ph)[None,:]
            uzz=ym[:,None]*np.ones((1,len(ph)))
            density=1+eps*(uxx*uxx-uyy*uyy)
            disagreement=(uzz*(uxx*x[0]+uyy*x[1]+uzz*x[2])<0)
            estimate=np.mean(density*disagreement)
            predicted=qh(theta,alpha,eps)[0]
            assert abs(estimate-predicted)<.0015, (eps,theta,estimate,predicted)
        limit=np.pi**3/(1-(eps/3)**2)**1.5
        prev=[]
        for n in [40,120,400]:
            ratio=n*exact_integral(n,eps)/limit
            prev.append(ratio)
        assert abs(prev[-1]-1)<.025,(eps,prev)
        print('eps',eps,'scaled perimeter ratios n40,120,400',prev,'limit',limit)
    rng=np.random.default_rng(20261031)
    eps=.6
    for n,reps in [(20,1000),(60,750)]:
        observed=[]
        for j in range(reps):
            per=poly_perimeter(random_dirs(rng,n,eps))
            if per is not None:observed.append(per)
        assert len(observed)>reps*.97, (n,len(observed))
        numeric=float(np.mean(observed));theory=exact_integral(n,eps)
        print('sim n',n,'count',len(observed),'observed',numeric,'analytic',theory)
        assert abs(numeric/theory-1)<.07
    # Fourier inversion test g(alpha)=1+eps cos2alpha from w(alpha) proportional to a^{-2}.
    alph=np.arange(8192)*2*np.pi/8192
    for eps in [.2,.7]:
        aa=a(alph,eps)
        w=aa**-2; recovered=w**(-.5)
        w=w/(2*np.pi*np.mean(w)) # Normalize the angular probability density.
        J=2*np.pi*np.mean(w**(-.5))
        R=0.5*2*np.pi*np.mean(aa**-2)
        a_absolute=J*w**(-.5)/(4*R)
        h_absolute=J**2/(16*R)
        assert np.max(np.abs(a_absolute-aa))<2e-12
        assert abs(h_absolute-0.5)<2e-12
        f0=np.mean(recovered)
        f2=np.mean(recovered*np.exp(-2j*alph))
        recovered_epsilon=6*(f2/f0).real # a second harmonic cosine = eps/3, Fourier mode = eps/6.
        assert abs(recovered_epsilon-eps)<1e-12
    print('ALL_ANALYTICAL_AND_GEOMETRIC_TESTS_PASSED')
if __name__=='__main__':main()
