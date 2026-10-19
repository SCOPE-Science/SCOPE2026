"""Reproducible numerical identities for exact Landweber source-ball calibration.
Run with Python 3, NumPy and SciPy. Numerical experiments are not proofs.
"""
import numpy as np
from scipy.stats import chi2, ncx2


def normalized_bias_spectrum(lam, omega, steps, exponent, mass=1., noise=1.):
    lam = np.asarray(lam, dtype=float)
    u = -np.expm1(steps * np.log1p(-omega*lam))
    power = 1. - u
    return mass/noise * power * lam ** (exponent + .5) / u


def exact_radius(lam, omega, steps, exponent, n, alpha=.05):
    d = np.max(normalized_bias_spectrum(lam,omega,steps,exponent))
    return np.sqrt(ncx2.ppf(1-alpha, n, d*d))


def main():
    rng = np.random.default_rng(19043)
    checks = 0
    for n in [2,3,5,8]:
        for _ in range(90):
            z=rng.normal(size=(n,n))
            q,_=np.linalg.qr(z)
            lam=np.exp(rng.uniform(-5.,1.,size=n))
            B=(q*lam)@q.T
            eig, U=np.linalg.eigh(B)
            omega=.9/np.max(eig)
            k=int(rng.integers(1,11))
            nu=float(rng.choice([.15,.35,.5,.8,1.1,2.]))
            M=float(rng.uniform(.5,2))
            sigma=float(rng.uniform(.3,1.5))
            R = np.eye(n)-omega*B
            # Compute spectral covariance and bias from direct matrix powers.
            eigpow=(1-omega*eig)**k
            Cov=(U*(sigma**2*(1-eigpow)**2/eig))@U.T
            Cinv=(U*(eig/(sigma**2*(1-eigpow)**2)))@U.T
            Bnu=(U*eig**nu)@U.T
            bias=np.linalg.matrix_power(R,k)@Bnu
            whitened_gram=bias.T@Cinv@bias
            qlam=np.linalg.eigvalsh(whitened_gram)
            delta=M*np.sqrt(np.max(qlam))
            delta2=np.max(normalized_bias_spectrum(eig,omega,k,nu,M,sigma))
            assert np.isclose(delta,delta2,rtol=4.e-7,atol=4.e-8), (delta,delta2)
            checks+=1
            worst_vec=M*U[:,np.argmax(normalized_bias_spectrum(eig,omega,k,nu))]
            achieved=np.sqrt((bias@worst_vec)@Cinv@(bias@worst_vec))
            assert np.isclose(achieved,delta,rtol=1e-6,atol=1e-7), (achieved,delta)
            checks+=1
            w=M*rng.normal(size=n)
            w*=M*rng.uniform(.0,1.)/np.linalg.norm(w)
            d2=(bias@w)@Cinv@(bias@w)
            assert d2 <= delta**2*(1+1.e-7)
            checks+=1
            r=np.sqrt(ncx2.ppf(.95,n,delta*delta))
            assert np.isclose(ncx2.cdf(r*r,n,delta*delta),.95,rtol=1e-8,atol=2e-8)
            assert ncx2.cdf(r*r,n,d2) >= .95-1e-10
            checks+=2
            # Algebraic polynomial formula should match direct sum covariance.
            S=np.zeros((n,n)); T=np.eye(n)
            for j in range(k):
                S+=T
                T=T@R
            direct=sigma**2*omega**2*(S@B@S)
            assert np.allclose(direct,Cov,rtol=1e-8,atol=2.e-9)
            checks+=1
            # A conservative radius always dominates exact radius.
            ub=M*np.max(eigpow*eig**nu)
            rtri=np.sqrt(chi2.ppf(.95,n))+ub/np.sqrt(np.min(np.linalg.eigvalsh(Cov)))
            assert rtri + 1e-8>=r
            checks+=1
    omega=.5
    for nu in [.15,.35,.5,.65,1.,2.]:
        for k in [1,2,4,10]:
            t=np.geomspace(1.e-3,1.e-12,6)
            small=normalized_bias_spectrum(t,omega,k,nu)
            expected=t**(nu-.5)/(k*omega)
            assert np.allclose(small[-1]/expected[-1],1.,rtol=4e-7), (small,expected)
            checks+=1
            all_delta=np.array([np.max(normalized_bias_spectrum([1.,v],omega,k,nu)) for v in t])
            rr=np.array([exact_radius([1.,v],omega,k,nu,2) for v in t])
            if nu<.5:
                assert rr[-1] > rr[0] and all_delta[-1] > all_delta[0]
                checks+=1
            else:
                assert all_delta[-1]<100
                assert rr[-1]<150
                checks+=2
            # Triangle bound diverges although exact radius bounded for smooth sources.
            if nu>=.5:
                b_high=(1-omega)**k
                gamma_small=(-np.expm1(k*np.log1p(-omega*t[-1])))**2/t[-1]
                rtri=np.sqrt(chi2.ppf(.95,2))+b_high/np.sqrt(gamma_small)
                assert rtri/rr[-1] > 10
                checks+=1
    nu=.5
    for t in [.9,.4,.02,1e-4,1e-7]:
        dd=np.max(normalized_bias_spectrum([1.,t],.5,1,nu))
        assert np.isclose(dd,2-t)
        checks+=1
    print('PASS',checks,'deterministic checks')

if __name__=='__main__':
    main()
