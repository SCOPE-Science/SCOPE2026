"""Independent exact-moment and numerical checks for partial-reset diffusion.

The infinite-dimensional convex-order statement is proved analytically in RESULT.md;
finite tests here detect normalization and boundary mistakes only.
"""
from fractions import Fraction as F
from math import factorial, comb, prod, sqrt
import numpy as np
from scipy.integrate import quad

CHECKS = 0

def check(condition, message):
    global CHECKS
    assert condition, message
    CHECKS += 1

def moments_v_generator(dist, D=F(7,5), rate=F(9,4), order=7):
    # Stationarity of D f'' + rate(E f(AX)-f(X)), f(x)=x^(2j).
    out=[F(1)]
    for j in range(1,order+1):
        uj=sum(p*a**(2*j) for p,a in dist)
        out.append(D*F(2*j*(2*j-1))*out[-1]/(rate*(1-uj)))
    return out

def moments_v_perpetuity(u_dist,D=F(7,5),rate=F(9,4),order=7):
    # V = 2D E + U V', E exponential(rate). Direct binomial recursion.
    out=[F(1)]
    ups=[sum(p*u**j for p,u in u_dist) for j in range(order+1)]
    for k in range(1,order+1):
        numerator=sum(F(comb(k,j))*factorial(k-j)*(2*D/rate)**(k-j)
                      *ups[j]*out[j] for j in range(k))
        out.append(numerator/(1-ups[k]))
    return out

def to_a(u_dist):
    # Square roots only used for floating tests; exact generator uses powers of U.
    return [(p,sqrt(float(u))) for p,u in u_dist]

def generator_from_u(u_dist,D=F(7,5),rate=F(9,4),order=7):
    out=[F(1)]
    for j in range(1,order+1):
        uj=sum(p*u**j for p,u in u_dist)
        out.append(D*(2*j)*(2*j-1)*out[-1]/(rate*(1-uj)))
    return out

def fourth(D,rate,u,v):
    return 24*D**2/(rate**2*(1-u)*(1-v))

D,r=F(7,5),F(9,4)
for u in [F(1,4),F(1,2),F(3,4)]:
    det=[(F(1),u)]
    bern=[(1-u,F(0)),(u,F(1))]
    mv_det=moments_v_perpetuity(det,D,r)
    mv_ber=moments_v_perpetuity(bern,D,r)
    check(mv_det[1] == 2*D/(r*(1-u)), 'variance mixing mean')
    check(mv_ber[1] == mv_det[1], 'fixed mean across protocols')
    check(generator_from_u(det,D,r,7)[2] == fourth(D,r,u,u*u), 'deterministic fourth')
    check(generator_from_u(bern,D,r,7)[2] == fourth(D,r,u,u), 'Bernoulli fourth')
    check(3*(1-u)/(1+u) == 6/(1+u)-3,'lower excess kurtosis')
    check(mv_ber[2] == 2*mv_ber[1]**2,'exponential variance mixing')
    for theta in [F(0),F(1,7),F(1,3),F(2,3),F(1)]:
        mu=[(1-theta,u), (theta*(1-u),F(0)),(theta*u,F(1))]
        mm=moments_v_perpetuity(mu,D,r)
        gx=generator_from_u(mu,D,r)
        for k in range(1,8):
            check(mv_det[k] <= mm[k] <= mv_ber[k],f'sharp moment order {u,theta,k}')
            double_factorial=prod(range(1,2*k,2))
            check(gx[k] == double_factorial*mm[k], f'generator/perpetuity cross-check {u,theta,k}')
    # Every binary law with fixed mean: support (0,z), z>=u.
    for z in [u, (u+1)/2, F(1)]:
        mu=[(1-u/z,F(0)),(u/z,z)]
        mm=moments_v_perpetuity(mu,D,r)
        for k in range(1,8):
            check(mv_det[k] <= mm[k] <= mv_ber[k],f'binary 0-z comparison {u,z,k}')
    # Every binary law with fixed mean: support (w,1), w<=u.
    for w in [F(0),u/2,u]:
        p1=(u-w)/(1-w)
        mu=[(1-p1,w),(p1,F(1))]
        mm=moments_v_perpetuity(mu,D,r)
        for k in range(1,8):
            check(mv_det[k] <= mm[k] <= mv_ber[k],f'binary w-1 comparison {u,w,k}')

# A finite Fourier-inversion check of the deterministic endpoint's central density,
# against the all-or-nothing effective-reset Laplace density.
def phi_det(k,u,D=1.4,r=2.25):
    factors = np.power(u,np.arange(0,550))
    return np.exp(-np.log1p(D*k*k*factors/r).sum())
for u in [0.15,0.45,0.7]:
    density,err=quad(lambda k: phi_det(k,u),0,np.inf,epsabs=3e-9,epsrel=3e-9,limit=150)
    density/=np.pi
    p_bern=.5*sqrt(float(r)*(1-u)/float(D))
    check(0 < density < p_bern, f'central density strict inequality at u={u}')
    gaussian_peak=1/sqrt(2*np.pi*(2*float(D)/(float(r)*(1-u))))
    check(gaussian_peak < density, 'Gaussian maximum-entropy peak vs mixture peak')

# Independent Monte Carlo check for the same stationary variance and distinct quartic tails.
rng=np.random.default_rng(210412)
u=.45
n=65
batch=48000
noise=rng.exponential(scale=1/float(r),size=(batch,n))*(2*float(D))
V=[]
for kind in ('det','mix','ber'):
    if kind=='det': mult=np.full((batch,n-1),u)
    elif kind=='ber': mult=(rng.random((batch,n-1))<u).astype(float)
    else:
        mult=np.where(rng.random((batch,n-1))<.55,u,
                      (rng.random((batch,n-1))<u).astype(float))
    # Evaluate perpetuity backward, which is distributionally equivalent to forward iid series.
    v=noise[:,-1].copy()
    for j in range(n-2,-1,-1): v=noise[:,j]+mult[:,j]*v
    V.append(v)
    check(abs(v.mean()-2*float(D)/(float(r)*(1-u))) < .045, 'Monte Carlo variance matching')
check(np.mean(V[0]**2)<np.mean(V[1]**2)<np.mean(V[2]**2), 'Monte Carlo squared-variance ordering')
check(np.mean(np.sqrt(V[0]))>np.mean(np.sqrt(V[1]))>np.mean(np.sqrt(V[2])), 'subquadratic moment reversal')
print(f'PASS: {CHECKS} checks; exact rational moments, Fourier central densities and reproducible stochastic corroboration.')
