"""Independent numerical checks for a single mass-and-pinning impurity on a harmonic lattice."""
import math
import numpy as np
from scipy.linalg import eigh_tridiagonal


def decay_roots(kappa, mu, kappa0):
    b = mu * (kappa + 2) - (kappa0 + 2)
    return np.roots([2 - mu, b, -mu]) if abs(2 - mu) > 1e-12 else (np.array([mu/b]) if abs(b)>1e-12 else np.array([]))


def bound_modes(kappa, mu, kappa0):
    low = kappa0 < mu * kappa
    high = kappa0 + 4 > mu * (kappa + 4)
    roots = decay_roots(kappa, mu, kappa0)
    found = []
    for r in roots:
        if abs(r.imag) < 1e-11 and abs(r.real) < 1 - 1e-10 and abs(r.real) > 1e-13:
            rr = r.real
            z = kappa + 2 - rr - 1 / rr
            found.append((rr,z))
    assert len(found) == low + high, (kappa,mu,kappa0,roots,found,low,high)
    for r,z in found:
        assert abs(kappa0 + 2 - 2*r - mu*z) < 1e-9 * (1 + abs(mu*z))
        assert (r > 0 and 0 < z < kappa) or (r < 0 and z > kappa + 4)
    return sorted(found, key=lambda t:t[1])


def from_two_frequencies(kappa, zlo, zhi):
    al = kappa + 2 - zlo
    ah = zhi - kappa - 2
    p = 2 / (al + math.sqrt(al * al - 4))
    q = 2 / (ah + math.sqrt(ah * ah - 4))
    mu = 2 * p * q / (1 + p * q)
    kap0 = 2 * (kappa * p * q - (1-p)*(1+q))/(1+p*q)
    return p,q,mu,kap0


def eigvals(kappa,mu,kappa0,n=501):
    diag=np.full(n,kappa+2.0)
    off=np.full(n-1,-1.0)
    mid=n//2
    diag[mid]=(kappa0+2)/mu
    off[mid-1]=-1/math.sqrt(mu)
    off[mid]=-1/math.sqrt(mu)
    low=eigh_tridiagonal(diag,off,select='i',select_range=(0,0),eigvals_only=True)[0]
    high=eigh_tridiagonal(diag,off,select='i',select_range=(n-1,n-1),eigvals_only=True)[0]
    return low,high


def run():
    rng=np.random.default_rng(20261023)
    analytic=0
    inversion=0
    finite=0
    examples=[]
    for trial in range(1600):
        kappa=10**rng.uniform(-1,1.0)
        mu=10**rng.uniform(-1.7,0.65)
        kappa0=10**rng.uniform(-2.0,1.4)
        modes=bound_modes(kappa,mu,kappa0)
        analytic+=1
        if len(modes)==2:
            p,lo=modes[0]; negq,hi=modes[1]
            pp,q,mui,kappai=from_two_frequencies(kappa,lo,hi)
            assert abs(pp-p)<1e-9 and abs(q+negq)<1e-9
            assert abs(mui-mu)<2e-9*(1+mu)
            assert abs(kappai-kappa0)<2e-9*(1+kappa0)
            assert (kappa*pp*q>(1-pp)*(1+q))
            inversion+=1
            if len(examples)<8 and max(abs(p),abs(negq)) < 0.82:
                examples.append((kappa,mu,kappa0,lo,hi))
    assert len(examples) == 8, "insufficient strongly localized comparison cases"
    for kappa,mu,kappa0,lo,hi in examples:
        low,high=eigvals(kappa,mu,kappa0,n=601)
        assert abs(low-lo)<1e-8 and abs(high-hi)<1e-8,(low,lo,high,hi)
        finite+=1
    feasibility_probes=0
    for trial in range(100):
        kappa=10**rng.uniform(-1,1)
        p=float(rng.uniform(0.6,0.99))
        q=float(rng.uniform(0.1,0.99))
        zlo=kappa+2-p-1/p
        zhi=kappa+2+q+1/q
        if zlo<=0: continue
        _,_,mu,kappa0=from_two_frequencies(kappa,zlo,zhi)
        feas=kappa*p*q>(1-p)*(1+q)
        assert (kappa0>0)==feas
        feasibility_probes+=1
    print('PASS',{'random_forward_spectra':analytic,'two_mode_inversions':inversion,'independent_finite_chain_extremes':finite,'inverse_feasibility_probes':feasibility_probes})
    print('sample',examples[:3])

if __name__=='__main__':run()
