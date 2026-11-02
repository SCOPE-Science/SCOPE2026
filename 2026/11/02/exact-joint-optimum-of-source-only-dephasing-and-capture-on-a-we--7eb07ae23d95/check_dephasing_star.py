"""Standalone checks for the weighted quantum star's source-only dephasing law.

Run: python3 check_dephasing_star.py. Requires numpy and scipy.
This program checks finite cases; the general theorem is proved in RESULT.md.
"""
import numpy as np
from scipy.linalg import expm
from numpy.linalg import solve


def lindblad_matrix(h,source,sink,gamma,kappa):
    n=len(h)
    p=np.zeros((n,n)); p[source,source]=1.
    q=np.zeros((n,n)); q[sink,sink]=1.
    basis=[]
    for a in range(n):
        for b in range(n):
            e=np.zeros((n,n), dtype=complex);e[a,b]=1
            y=-1j*(h@e-e@h) + 2*gamma*(p@e@p-(p@e+e@p)/2)-kappa*(q@e+e@q)/2
            basis.append(y.reshape(-1))
    return np.array(basis).T


def run():
    rng=np.random.default_rng(434713)
    residual_max=0.0
    max_time_error=0.0
    exhaustive=0
    for n in range(2,10):
        for j in range(12):
            rates=10**rng.uniform(-0.4,0.4,n)
            a=float(rates[0]);b=float(np.linalg.norm(rates[1:]));om=np.hypot(a,b)
            gamma=float(10**rng.uniform(-0.5,0.5));kappa=float(10**rng.uniform(-0.5,0.5))
            # Full (n+1)-site generator: site 0 is source, site n the hub.
            h=np.zeros((n+1,n+1),dtype=float)
            h[:-1,-1]=rates;h[-1,:-1]=rates
            li=lindblad_matrix(h,0,n,gamma,kappa)
            rho0=np.zeros((n+1,n+1));rho0[0,0]=1
            # Solve the dynamically reachable 3-dimensional subspace; the full star may
            # contain inaccessible dark modes and hence a singular full generator.
            hr=np.array([[0,0,a],[0,0,b],[a,b,0]],dtype=float)
            lr=lindblad_matrix(hr,0,2,gamma,kappa)
            rr=np.zeros((3,3));rr[0,0]=1.
            xr=solve(lr,-rr.reshape(-1)).reshape((3,3))
            lifetime=float(np.trace(xr).real)
            expected=(om*om/gamma+gamma)/(2*a*a)+3/kappa+kappa/(4*a*a)
            err=abs(lifetime-expected)/(1+abs(expected));residual_max=max(err,residual_max)
            assert err < 2e-10, (n,j,lifetime,expected,err)
            assert abs(kappa*xr[-1,-1].real-1)<1e-10
            # The three-dimensional compressed certificate, embedded in the original basis
            s=np.eye(n+1)[:,0]
            c=np.eye(n+1)[:,-1]
            r=np.r_[np.array([0]),np.array(rates[1:])/b,0.] # explicit n+1 coordinates
            u=np.stack((s,r,c),axis=1)
            xx=np.array([[b*b/(2*a*a*gamma)+1/kappa+gamma/(2*a*a)+kappa/(4*a*a),-b/(2*a*gamma),1j/(2*a)],
              [-b/(2*a*gamma),1/kappa+1/(2*gamma),0],[-1j/(2*a),0,1/kappa]],dtype=complex)
            full_cert=u@xx@u.conj().T
            cert_error=np.linalg.norm(full_cert-u@xr@u.conj().T)/(1+np.linalg.norm(full_cert))
            assert cert_error < 2e-10,(n,j,cert_error)
            residual=np.linalg.norm(li@full_cert.reshape(-1)+rho0.reshape(-1))/(1+np.linalg.norm(rho0))
            assert residual<2e-10,(n,j,residual)
            if j==0 and n in (2,4,7):
                # Integrate numerically on a finite interval beyond the decay time.
                eig=np.linalg.eigvals(lr)
                assert max(eig.real)<-1e-8
                t=float(max(80,16/(-max(eig.real))))
                # Exact formula X(t) = X - exp(L*t)X valid in full space even
                # though some unpopulated dark states make full L singular.
                at_t=(full_cert.reshape(-1)-expm(li*t)@full_cert.reshape(-1)).reshape((n+1,n+1))
                max_time_error=max(max_time_error, abs(np.trace(at_t).real-expected)/(1+abs(expected)))
                assert abs(np.trace(at_t).real-expected)/(1+abs(expected))<3e-7
            exhaustive+=1
    # Rate minimizer and total-coupling scaling checks
    for n in range(2,25):
        for j in range(15):
            weights=10**rng.uniform(-1.0,1.0,n)
            a=weights[0];om=np.linalg.norm(weights)
            g=om; k=2*np.sqrt(3)*a
            t=(om**2/g+g)/(2*a*a)+3/k+k/(4*a*a)
            opt=(om+np.sqrt(3)*a)/(a*a)
            assert abs(t-opt)<1e-9*(1+opt)
            for scale in (0.35,0.8,1.2,2.5):
                gs=g*scale
                ks=k*scale
                t1=(om**2/gs+gs)/(2*a*a)+3/k+k/(4*a*a)
                t2=(om**2/g+g)/(2*a*a)+3/ks+ks/(4*a*a)
                assert t1>t+1e-12 and t2>t+1e-12
    print('PASS: 96 original-size full Liouvillian resolvent and certificate comparisons')
    print('PASS: 3 finite-time propagator/integral comparisons')
    print('PASS: 345 joint rate-optimum inequalities and equality identities')
    print('max relative full-system mean error:',residual_max)
    print('max relative finite-time truncation error:',max_time_error)


if __name__=='__main__':
    run()
