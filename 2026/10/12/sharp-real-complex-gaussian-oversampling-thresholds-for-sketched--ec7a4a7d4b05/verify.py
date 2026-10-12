"""Reproduce finite checks for exact real/complex Gaussian Ritz moment laws.

Requires Python 3.10+ and NumPy. All stochastic tests have fixed seeds.
Finite diagnostics supplement, but do not substitute for, the proof.
"""
import math
import numpy as np


def gaussian(shape, rng, field):
    if field == 'complex':
        return (rng.standard_normal(shape) + 1j*rng.standard_normal(shape))/math.sqrt(2.0)
    return rng.standard_normal(shape)


def exact_tail(t, nu, field):
    if field == 'complex':
        return (1.0+t*t)**(-nu)
    # Real normalized Student law, integrating through arctan(t).
    a, b = math.atan(t), math.pi/2
    steps = 1200
    x = np.linspace(a,b,steps+1)
    f = np.cos(x)**(nu-1)
    val = (b-a)/(3*steps)*(f[0]+f[-1]+4*f[1:-1:2].sum()+2*f[2:-1:2].sum())
    coeff = math.gamma((nu+1)/2)/(math.sqrt(math.pi)*math.gamma(nu/2))
    return 2*coeff*val


def moment(p, nu, field):
    cutoff = (2 if field == 'complex' else 1)*nu
    if p >= cutoff:
        return math.inf
    if field == 'complex':
        return math.gamma(1+p/2)*math.gamma(nu-p/2)/math.gamma(nu)
    return (math.gamma((p+1)/2)*math.gamma((nu-p)/2) /
            (math.sqrt(math.pi)*math.gamma(nu/2)))


def full_projection_checks():
    rng = np.random.default_rng(2718281)
    count = 0
    for field in ('real','complex'):
        for m in (2,3,4,5):
            n = m+2
            diag=np.array([-1.25]+[0.3+0.7*j for j in range(1,m)]+[2.6,4.1])
            A=np.diag(diag)
            W=np.zeros((n,m),dtype=float)
            alpha=.38
            W[0,0]=math.sqrt(1-alpha**2)
            W[m+1,0]=alpha
            for j in range(1,m):W[j,j]=1.
            Aw=A@W[:,0]
            rho=float(W[:,0]@Aw)
            r=Aw-rho*W[:,0]
            sigma=np.linalg.norm(r)
            assert sigma>0
            for s in (m,m+1,m+3):
                for _ in range(65):
                    S=gaussian((s,n),rng,field)
                    SW=S@W
                    M=np.linalg.lstsq(SW,S@A@W,rcond=None)[0]
                    for j in range(1,m):
                        ej=np.zeros(m,dtype=complex);ej[j]=diag[j]
                        assert np.max(np.abs(M[:,j]-ej))<2e-10
                    spectator=SW[:,1:]
                    q=SW[:,0]-spectator@np.linalg.lstsq(spectator,SW[:,0],rcond=None)[0]
                    ratio=np.vdot(q,S@r)/np.vdot(q,q)
                    assert abs(M[0,0]-(rho+ratio))<4e-10
                    assert np.min(abs(np.linalg.eigvals(M)-M[0,0]))<2e-9
                    count+=1
    return count


def distribution_checks():
    rng=np.random.default_rng(2114)
    N=280000
    comparisons=0
    for field in ('real','complex'):
        for nu in (1,2,3,6):
            U=gaussian(N,rng,field)
            H=np.sum(np.abs(gaussian((N,nu),rng,field))**2,axis=1)
            Z=np.abs(U)/np.sqrt(H)
            for t in (.5,1.,2.):
                empirical=np.mean(Z>t)
                theoretical=exact_tail(t,nu,field)
                assert abs(empirical-theoretical)<.006, (field,nu,t,empirical,theoretical)
                comparisons+=1
            if field=='complex' and nu>1:
                assert abs(moment(2,nu,field)-1/(nu-1))<1e-13
            if field=='real' and nu>2:
                assert abs(moment(2,nu,field)-1/(nu-2))<1e-13
    return comparisons,2*4*N


def analytic_checks():
    count=0
    for field in ('real','complex'):
        for nu in (1,2,3,5):
            assert math.isinf(moment(nu if field=='real' else 2*nu,nu,field))
            p=(nu if field=='real' else 2*nu)-0.5
            assert math.isfinite(moment(p,nu,field))
            for t in (0,.4,1.5):
                tail=exact_tail(t,nu,field)
                assert 0<tail<=1+1e-12
                if t==0:assert abs(tail-1)<1e-10
                count+=1
    return count


def main():
    a=full_projection_checks()
    b,c=distribution_checks()
    d=analytic_checks()
    print('VERIFY_OK full_reduced_eigenvalue_identities=',a,
          'tail_probability_tests=',b,'gaussian_ratio_samples=',c,
          'analytic_moment_and_normalization_tests=',d)

if __name__=='__main__':
    main()
