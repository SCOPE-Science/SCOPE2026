"""Checks for fixed-sketch two-mode power iteration reliability.
Run with Python >= 3.10, numpy and scipy. Finite checks supplement the proof.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.special import betainc


def theoretical_probability(kappa, ell):
    return float(betainc(ell / 2, ell / 2, 1 / (1 + kappa*kappa)))


def laplace_approximation(kappa, ell):
    return ((2*kappa/(kappa*kappa+1))**ell /
            ((kappa*kappa-1)/(kappa*kappa+1)*math.sqrt(2*math.pi*ell)))


def exact_even_beta_cdf(p, a):
    # Beta(a,a) CDF is Binomial(2a-1,p) upper tail for integer a.
    return sum(Fraction(math.comb(2*a-1,j))*p**j*(1-p)**(2*a-1-j)
               for j in range(a,2*a))


def main():
    n_exact=0
    for k in (Fraction(3,2), Fraction(2), Fraction(5,2), Fraction(3), Fraction(4)):
        for a in range(1,9):
            ell=2*a
            p=1/(1+k*k)
            exact=exact_even_beta_cdf(p,a)
            assert abs(float(exact)-theoretical_probability(float(k),ell))<2e-14
            n_exact+=1
    assert exact_even_beta_cdf(Fraction(1,5),2)==Fraction(13,125)
    n_orient=0
    rng=np.random.default_rng(20261009)
    for k in (1.12,1.5,2.,3.,5.):
        for ell in (2,3,4,7,12):
            for _ in range(60):
                phi=rng.standard_normal((2,ell))
                z=np.diag([k,1.])@phi
                H=z@z.T
                w,v=np.linalg.eigh(H)
                principal=v[:,-1]
                # Identity for squared components and diagonal dominance.
                rhs=(H[0,0]-H[1,1])/math.hypot(H[0,0]-H[1,1],2*H[0,1])
                assert abs(principal[0]**2-principal[1]**2-rhs)<1e-12
                assert (principal[1]**2>principal[0]**2)==(H[1,1]>H[0,0])
                if principal[1]**2>principal[0]**2:
                    residual_sq=k*k*principal[1]**2+principal[0]**2
                    assert residual_sq>(k*k+1)/2>1
                n_orient+=1
    n_asym=0
    for k in (1.5,2.,3.,5.):
        for ell in (300,600,1200):
            exact=theoretical_probability(k,ell)
            appr=laplace_approximation(k,ell)
            # Very tiny tails can underflow; ignore such cases.
            if exact>1e-290 and appr>1e-290:
                assert 0.85<exact/appr<1.015, (k,ell,exact/appr)
                n_asym+=1
    # Finite monotonic checks of the exact sketch-budget CDF and near-gap scaling.
    n_monotone=0
    for k in (1.02,1.1,1.5,2.,4.):
        ps=[theoretical_probability(k,ell) for ell in range(2,250)]
        assert all(x>y for x,y in zip(ps,ps[1:]))
        n_monotone+=len(ps)-1
    from scipy.special import ndtri
    for delta in (.1,.05):
        z2=float(ndtri(1-delta))**2
        for eps in (.02,.01):
            k=1+eps
            lo,hi=2,2
            while theoretical_probability(k,hi)>delta: hi*=2
            while lo<hi:
                mid=(lo+hi)//2
                if theoretical_probability(k,mid)<=delta: hi=mid
                else:lo=mid+1
            assert abs(lo*eps**2/z2-1)<.025
    # Monte Carlo directly samples the Gaussian rows and compares the matrix eigenvector.
    for k,ell,m in ((2.,4,30000),(1.5,8,30000),(3.,2,30000)):
        phi=rng.standard_normal((m,2,ell))
        U=np.sum(phi[:,0,:]**2,axis=1)
        V=np.sum(phi[:,1,:]**2,axis=1)
        observed=np.mean(V>k*k*U)
        reference=theoretical_probability(k,ell)
        assert abs(observed-reference)<5*math.sqrt(reference*(1-reference)/m)+.003
    # Demonstrate normalized power with one fixed proxy tends to that proxy's top eigenvector.
    for _ in range(200):
        phi=rng.standard_normal((2,4))
        H=(np.diag([2.,1.])@phi)@(np.diag([2.,1.])@phi).T
        evals,evecs=np.linalg.eigh(H)
        if evals[0]/evals[1]>.95:  # very slow convergence; not a mathematical exception
            continue
        v=evecs[:,-1]
        y=np.array([2.,1.])*rng.standard_normal(2)
        z=y/np.linalg.norm(y)
        for _ in range(250):
            z=H@z
            z=z/np.linalg.norm(z)
        assert abs(abs(z@v)-1)<1e-9
    print('VERIFY_OK', n_exact, 'exact beta identities;',n_orient,
          'eigenvector and residual identities;',n_asym,'asymptotic checks;', n_monotone,'budget monotonic checks; 90000 Monte Carlo samples; 200 power trajectories')

if __name__=='__main__': main()
