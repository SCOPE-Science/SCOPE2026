"""Numerical cross-checks for two-snapshot noisy Anderson acceleration.

No finite test is used to certify the general Gaussian integrability theorem.
The theorem is proved analytically in the accompanying text.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import i0e, i1e


def aa_direct(u, v, residual0, residual1, ridge):
    delta = v-u
    d = residual1-residual0
    t = -float(np.dot(residual0, d))/(float(np.dot(d, d))+ridge)
    return u+residual0 + t*(delta+d)


def aa_half_sum(u, v, residual0, residual1, ridge):
    delta=v-u
    d=residual1-residual0
    h=(residual0+residual1)/2
    sq=float(np.dot(d,d))
    return (u+v)/2+h - (np.dot(h,d)+ridge/2)/(sq+ridge)*(delta+d)


def scalar_mse(ridge, contraction=0.5, sigma=1.):
    delta=1.
    md=(contraction-1)*delta
    sdev=math.sqrt(2)*sigma
    def integrand(d):
        dd=d*d
        a=delta+d
        denom=dd+ridge
        coeff=1-a*d/denom
        baseline=-ridge*a/(2*denom)
        return math.exp(-(d-md)**2/(4*sigma*sigma))/(sdev*math.sqrt(2*math.pi))*(sigma*sigma*coeff*coeff/2+baseline*baseline)
    root=math.sqrt(ridge)
    splits=[-25., -1., -10*root, -root, 0., root, 10*root, 1., 25.]
    splits=sorted(set(splits))
    return sum(quad(integrand,a,b,epsabs=2e-9,epsrel=2e-9,limit=250)[0] for a,b in zip(splits[:-1],splits[1:]))


def planar_mse(ridge, contraction=0.5, sigma=1.):
    mu=(contraction-1)
    def integrand(r):
        z=r*mu/(2*sigma*sigma)
        b=i1e(z)/i0e(z)
        den=r*r+ridge
        ad=r*r+r*b
        an=1+r*r+2*r*b
        ev=(sigma*sigma/2)*(2-2*ad/den+an*r*r/(den*den)) + ridge*ridge*an/(4*den*den)
        return r/(2*sigma*sigma)*math.exp(-(r*r+mu*mu)/(4*sigma*sigma)+abs(z))*i0e(z)*ev
    rt=math.sqrt(ridge)
    splits=sorted(set([0,rt,10*rt,0.01,0.1,1,5,20]))
    return sum(quad(integrand,a,b,epsabs=1e-9,epsrel=1e-9,limit=250)[0] for a,b in zip(splits[:-1],splits[1:]))


def main():
    rng=np.random.default_rng(1729)
    n=0
    for dim in range(1,9):
        for ridge in [0.,0.0001,0.01,1.,15.]:
            for _ in range(20):
                u=rng.standard_normal(dim)
                v=rng.standard_normal(dim)
                r0=rng.standard_normal(dim)
                r1=rng.standard_normal(dim)
                x=aa_direct(u,v,r0,r1,ridge)
                y=aa_half_sum(u,v,r0,r1,ridge)
                assert np.allclose(x,y,rtol=2e-10,atol=2e-10)
                n+=1
    sigma=1.; lam=0.5
    e0=math.exp(-((1-lam)**2)/(4*sigma*sigma))
    c1=math.sqrt(math.pi)*sigma*e0/8 # delta=1, E H^2=sigma^2/2
    c2=e0/8 # delta=1, E||H||^2=sigma^2
    # Leading 1/sqrt(ridge) coefficient and logarithmic increment.
    for ridge in [1e-5,1e-7,1e-9]:
        scaled=scalar_mse(ridge)*math.sqrt(ridge)
        assert abs(scaled/c1-1) < 0.05, (ridge,scaled,c1)
        n+=1
    for ridge in [1e-5,1e-7,1e-9]:
        diff=(planar_mse(ridge/100)-planar_mse(ridge))/math.log(100)
        assert abs(diff/c2-1)<0.1, (ridge,diff,c2)
        n+=1
    print(f"PASS {n} fixed-input update identities and asymptotic checks")
    print("scalar coefficient", c1,"planar coefficient",c2)
    for delta in [1e-5,1e-7,1e-9]:
        print("ridge",delta,"E1",scalar_mse(delta),"E2",planar_mse(delta))


if __name__=='__main__':
    main()
