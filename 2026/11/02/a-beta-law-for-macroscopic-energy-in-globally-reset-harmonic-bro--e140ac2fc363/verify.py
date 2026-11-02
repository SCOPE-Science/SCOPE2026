"""Reproduce exact moment identities for a globally reset harmonic Brownian population."""
import numpy as np
from numpy.testing import assert_allclose


def c(t, damping, diffusion):
    if damping == 0.0:
        return 2.0 * diffusion * t
    return diffusion * (-np.expm1(-2.0 * damping * t)) / damping


def K(x, y, r, d):
    if x > 0 and y > 0:
        return (d*d/(x*y))*(1-r/(r+2*x)-r/(r+2*y)+r/(r+2*x+2*y))
    # Explicit partial fraction using the limiting ratio when a damping vanishes.
    if x == 0 and y == 0:
        return 8*d*d/(r*r)
    if x == 0:
        x,y = y,x
    return (2*d*d/x)*(1/r-r/(r+2*x)**2)


def analytic(n, kappa, interaction, r, d):
    b=kappa+interaction
    m0=2*d/(r+2*kappa)
    mb=2*d/(r+2*b)
    k00=K(kappa,kappa,r,d)
    kbb=K(b,b,r,d)
    k0b=K(kappa,b,r,d)
    mean=(m0+(n-1)*mb)/n
    second=(3*k00+(n*n-1)*kbb+2*(n-1)*k0b)/n**2
    # Generator identities, independent of the age-mixture evaluation:
    assert_allclose(3*k00,12*d*m0/(r+4*kappa),rtol=1e-11,atol=1e-11)
    assert_allclose((n*n-1)*kbb,4*d*(n+1)*((n-1)*mb)/(r+4*b),rtol=1e-11,atol=1e-11)
    assert_allclose((n-1)*k0b,2*d*((n-1)*mb+(n-1)*m0)/(r+2*kappa+2*b),rtol=1e-11,atol=1e-11)
    return mean,second-mean**2


def main():
    rng=np.random.default_rng(410025)
    cases=[(8,0.0,1.1,0.8,0.5),(14,0.6,0.9,1.2,0.7),(90,1.3,0.25,0.5,1.0),(320,0.4,1.5,3.4,0.8)]
    for n,k,l,r,d in cases:
        mean,variance=analytic(n,k,l,r,d)
        age=rng.exponential(1/r,size=100000)
        v0=c(age,k,d);v1=c(age,k+l,d)
        samples=(v0*rng.chisquare(1,size=len(age))+v1*rng.chisquare(n-1,size=len(age)))/n
        # Sampling fluctuations are not certificates. Tolerances cover the
        # heavier-tailed zero-center-damping case.
        rel_mean=abs(samples.mean()-mean)/mean
        rel_var=abs(samples.var()-variance)/variance
        assert rel_mean<0.035,(n,'mean',rel_mean)
        assert rel_var<(0.12 if k==0 else 0.045),(n,'variance',rel_var)
        print('N=%d mean=%.8g sample=%.8g variance=%.8g sample=%.8g'%(n,mean,samples.mean(),variance,samples.var()))
    for a in [0.2,0.7,1.,5.]:
        for n in [2,8,100]:
            global_cv2=a/(a+2)+4*(a+1)/(n*(a+2))
            local_cv2=(5*a+4)/(n*(a+2))
            assert_allclose(global_cv2-local_cv2,(a/(a+2))*(1-1/n),atol=1e-15)
    for a in [0.3,1.,4.]:
        r=2*a; b=1.;d=0.6
        age=rng.exponential(1/r,size=400000)
        U=-np.expm1(-2*b*age)
        assert abs(U.mean()-1/(a+1))<0.008
        assert abs(U.var()-a/((a+1)**2*(a+2)))<0.008
    print('PASS: finite-N moment balance, Monte Carlo, finite-size local/global gap and beta moments')


if __name__=='__main__':
    main()
