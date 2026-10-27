"""Independent deterministic and Monte Carlo checks of two-site reset-gap laws.

Uses only numpy, scipy, mpmath. Not a substitute for the analytic proof.
"""
import math
import numpy as np
from scipy import integrate, special
from mpmath import gammainc, inf, mp

mp.dps = 40
D = mu = 1.0
r = 2.0 # r/(2 mu) = 1: scaled stationary variance is uniform on [0,S^2]
rng = np.random.default_rng(260526)
checks = 0

def g_numeric(z, beta):
    S2 = D/(beta*mu)
    b=z*z/(4*S2)
    # independent derivation by transforming reset age into a uniform scale
    a=beta/2-1
    val=float(mp.power(b,-a)*gammainc(a,b,inf))
    return 2**(1-beta)/math.gamma(beta/2)*S2**(-beta/2)*z**(beta-1)*val

def pred_g(z,beta):
    a=2*D/beta
    S2=D/(beta*mu)
    if beta < 2:
        J = (S2)**(-beta/2)/(1-beta/2) # uniform-variance moment
        return 2**(1-beta)/math.gamma(beta/2)*J*z**(beta-1)
    if beta == 2:
        return r/a*z*math.log(1/z)
    return r/(a*(beta-2))*z

def sim_numeric(z,beta):
    S2=D/(beta*mu)
    b=z*z/(4*S2)
    shape=(beta+1)/2
    val=float(mp.power(b,1-shape)*gammainc(shape-1,b,inf))
    return 2**(-beta)/math.gamma(shape)*S2**(-shape)*z**beta*val

def pred_sim(z,beta):
    a=2*D/beta
    S2=D/(beta*mu)
    if beta < 1:
        J=S2**(-(beta+1)/2)/(1-(beta+1)/2)
        return 2**(-beta)/math.gamma((beta+1)/2)*J*z**beta
    if beta == 1:
        return r/a*z*math.log(1/z)
    return r/(a*(beta-1))*z

print('offdiagonal density small-gap asymptotic convergence')
for beta in [0.6,1.0,1.5,2.,2.5,3.,4.]:
    ratios=[]
    for z in [1e-2,1e-3,1e-4,1e-5]:
        g=g_numeric(z,beta)
        assert math.isfinite(g) and g>0
        ratios.append(g/pred_g(z,beta))
        checks +=1
    if beta != 2:
        assert abs(ratios[-1]-1)<0.04, (beta,ratios)
    else: assert abs(ratios[-1]-1)<0.22,(beta,ratios)
    checks += 1
    print(beta, 'independent', ['%.5f'%x for x in ratios])

print('simultaneous density small-gap asymptotic convergence')
for beta in [0.5,1.,1.5,2.,4.]:
    ratios=[]
    for z in [1e-2,1e-3,1e-4,1e-5]:
        s=sim_numeric(z,beta)
        assert math.isfinite(s) and s>0
        ratios.append(s/pred_sim(z,beta))
        checks+=1
    if beta != 1:
        assert abs(ratios[-1]-1)<0.04, (beta,ratios)
    else: assert abs(ratios[-1]-1)<0.22,(beta,ratios)
    checks+=1
    print(beta,'simultaneous', ['%.5f'%x for x in ratios])

# h(0) exact integration, one independent rectangle quadrature evaluation.
for beta in [0.8,2.,3.5]:
    S2=D/(beta*mu)
    h_exact=(4./3)*(2.**1.5-2)/math.sqrt(2*math.pi*S2)
    def h_integral(v):
        return integrate.quad(lambda u:1/math.sqrt(2*math.pi*S2*(u+v)),0,1,epsabs=1e-10)[0]
    h_quad=integrate.quad(h_integral,0,1,epsabs=2e-9)[0]
    assert abs(h_exact/h_quad-1)<1e-7
    checks+=1

# Monte Carlo values compare exact shared E[gap^2] for independently reset
# and simultaneous clocks. The low-gap exponent is proven by quadrature,
# not inferred from Monte Carlo histograms.
for beta in [0.8,1.,2.,3.5,5.]:
    n=350000
    S2=D/(beta*mu)
    variance=lambda u: S2*u
    ui=rng.uniform(size=(3,n))
    diag_a=rng.standard_normal(n)*np.sqrt(variance(ui[0]))
    diag_b=rng.standard_normal(n)*np.sqrt(variance(ui[1]))
    y=rng.gamma(shape=beta/2,scale=2*variance(ui[2]))
    gap_i=np.sqrt((diag_a-diag_b)**2+2*y)
    us=rng.uniform(size=n)
    diag_a=rng.standard_normal(n)*np.sqrt(variance(us))
    diag_b=rng.standard_normal(n)*np.sqrt(variance(us))
    y=rng.gamma(shape=beta/2,scale=2*variance(us))
    gap_s=np.sqrt((diag_a-diag_b)**2+2*y)
    exact=4*D*(beta+1)/(beta*(r+2*mu))
    assert abs(np.mean(gap_i**2)/exact-1)<0.025
    assert abs(np.mean(gap_s**2)/exact-1)<0.025
    checks+=2
    print('mean gap squared',beta,exact,round(np.mean(gap_i**2),5),round(np.mean(gap_s**2),5))
print('PASS',checks,'assertion groups')

# A separate exact integration of the full independent-reset spectral-gap
# density: convolution of two diagonal Gaussian variance mixtures and the
# offdiagonal mixture, followed by the angular change of variables.
def h_difference(w,beta):
    S2=D/(beta*mu)
    c=w*w/(2*S2)
    k=1/math.sqrt(2*math.pi*S2)
    if c==0:
        return k*(4./3)*(2**1.5-2)
    v1=integrate.quad(lambda q: math.sqrt(q)*math.exp(-c/q),0,1,epsabs=1e-11)[0]
    v2=integrate.quad(lambda q: (2-q)/math.sqrt(q)*math.exp(-c/q),1,2,epsabs=1e-11)[0]
    return k*(v1+v2)

def spectral_density_ind(z,beta):
    def integrand(theta):
        return h_difference(z*math.sin(theta),beta)*g_numeric(z*math.cos(theta),beta)
    return 2*z*integrate.quad(integrand,0,math.pi/2,epsabs=3e-9,limit=160)[0]

def predicted_ind_gap(z,beta):
    h0=h_difference(0,beta)
    a=2*D/beta
    S2=D/(beta*mu)
    if beta<2:
        J=S2**(-beta/2)/(1-beta/2)
        coeff= h0*2**(1-beta)/math.gamma(beta/2)*J*special.beta(.5,beta/2)
        return coeff*z**beta
    if beta==2:
        return 2*h0*r/a*z*z*math.log(1/z)
    return 2*h0*r/(a*(beta-2))*z*z

for beta in [0.7,1.3,2.,3.,4.]:
    ratios=[]
    for z in [1e-2,1e-3]:
        rat=spectral_density_ind(z,beta)/predicted_ind_gap(z,beta)
        ratios.append(rat)
        checks+=1
    assert abs(ratios[-1]-1)<(.075 if beta in (1.3,2.) else .04), (beta,ratios)
    checks+=1
    print('exact gap density ratio',beta, ['%.6f'%x for x in ratios])
print('PASS including spectral density quadratures:',checks,'assertion groups')

# Non-unit reset-age shape: independent check of the beta negative moment
# and hence of the exact all-parameter leading coefficient for beta<2.
for alpha in [0.4, 1.7, 3.0]:
    for beta in [0.7,1.3,1.8]:
        S2=D/(beta*mu)
        numeric=alpha*S2**(-beta/2)*integrate.quad(
            lambda v: v**(-beta/2)*(1-v)**(alpha-1),
            0,1,epsabs=1e-10,limit=150)[0]
        analytic=alpha*S2**(-beta/2)*special.beta(alpha,1-beta/2)
        assert abs(numeric/analytic-1)<1e-8,(alpha,beta,numeric,analytic)
        checks+=1
print('FINAL PASS',checks,'assertion groups')
