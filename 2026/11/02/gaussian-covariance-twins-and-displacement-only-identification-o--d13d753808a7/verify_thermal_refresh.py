"""Independent finite checks for the OU/Maxwell-refresh inversion theorem.

Scientific artifact: only finite numerical checks; analytical proof in RESULT.md.
Run with Python 3, numpy and scipy: python verify_thermal_refresh.py
"""
import itertools
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.stats import qmc


def var_area(T, gamma, sigma=1.0):
    z=gamma*T
    if abs(z)<1e-5:
        return sigma*sigma*T*T*(1-z/3+z*z/12-z**3/60)
    return 2*sigma*sigma*(z-1+math.exp(-z))/(gamma*gamma)


def J(L, lam):
    z=lam*L
    if abs(z)<0.015:
        return (L**3/6)*(1-z/2+3*z*z/20-z**3/30+z**4/168)
    return (z-2+(z+2)*math.exp(-z))/(lam**3)


def displacement_cumulant4(T, lam, r, sigma):
    return 48*sigma**4*quad(lambda b: math.exp(-2*lam*b)*math.expm1(r*b)*J(T-b,lam),0,T,epsabs=1e-11,epsrel=1e-11)[0]


def velocity_cumulant4(ts,lam,r,sigma):
    t=sorted(ts)
    aa=t[1]-t[0]; bb=t[2]-t[1]; cc=t[3]-t[2]
    return 2*sigma**4*math.exp(-lam*(aa+2*bb+cc))*math.expm1(r*bb)


def partition_moment(ts,lam,r,sigma):
    # Exact sum over 8 no-reset / reset patterns for chronological time gaps.
    t=sorted(ts)
    gaps=np.diff(t)
    total=0.0
    for breaks in itertools.product((False,True),repeat=3):
        prob=math.prod((1-math.exp(-r*g) if br else math.exp(-r*g)) for br,g in zip(breaks,gaps))
        block=[0]
        blocks=[]
        for i,br in enumerate(breaks):
            if br:
                blocks.append(block)
                block=[i+1]
            else: block.append(i+1)
        blocks.append(block)
        v=1.0
        for block in blocks:
            if len(block)%2:
                v=0.0;break
            if len(block)==2:
                i,j=block;v*=sigma**2*math.exp(-(lam-r)*(t[j]-t[i]))
            if len(block)==4:
                i,j,k,l=block
                C=lambda x,y:sigma**2*math.exp(-(lam-r)*(t[y]-t[x]))
                v*=C(i,j)*C(k,l)+C(i,k)*C(j,l)+C(i,l)*C(j,k)
        total+=prob*v
    C=lambda i,j:sigma**2*math.exp(-lam*(t[j]-t[i]))
    return total-C(0,1)*C(2,3)-C(0,2)*C(1,3)-C(0,3)*C(1,2)


def monte_carlo_k4(T,lam,r,sigma,n=150000,seed=401):
    # Conditional on Poisson collision times, displacement is exactly normal,
    # with variance the sum of OU-area variances on each collision interval.
    rng=np.random.default_rng(seed)
    nreset=rng.poisson(r*T,size=n)
    conditional=np.empty(n)
    for i,k in enumerate(nreset):
        if k==0:
            conditional[i]=var_area(T,lam-r,sigma)
        else:
            knots=np.concatenate(([0.],np.sort(rng.uniform(0,T,size=k)),[T]))
            conditional[i]=sum(var_area(float(L),lam-r,sigma) for L in np.diff(knots))
    # Monte Carlo estimate of 3 Var(conditional Gaussian variance).
    cumulant=3*float(np.var(conditional,ddof=1))
    sem_var=math.sqrt(float(np.var((conditional-np.mean(conditional))**2,ddof=1))/n)
    return cumulant,3*sem_var,float(np.mean(conditional))


def main():
    rng=np.random.default_rng(41)
    for _ in range(250):
        lam=float(rng.uniform(0.25,3.5)); r=float(rng.uniform(0.01,lam*0.98)); sigma=float(rng.uniform(0.5,2.2))
        ts=np.cumsum(rng.uniform(.1,1.4,size=4))
        a=velocity_cumulant4(ts,lam,r,sigma)
        b=partition_moment(ts,lam,r,sigma)
        assert math.isclose(a,b,rel_tol=2e-10,abs_tol=1e-13),(a,b,ts,lam,r)
    print('PASS: 250 independent 8-partition fourth-cumulant enumerations')

    for T1,T2 in [(0.3,0.7),(1,2),(2,5)]:
        ratios=[]
        for lam in np.geomspace(.01,20,80):
            ratios.append(var_area(T2,lam)/var_area(T1,lam))
        assert np.all(np.diff(ratios)<0)
        assert T2/T1<ratios[-1]<ratios[0]<(T2/T1)**2
    print('PASS: strict decreasing two-window variance ratios, 237 adjacent comparisons')

    for _ in range(80):
        lam=float(rng.uniform(.5,3.5));r=float(rng.uniform(.02,lam*.95));T=float(rng.uniform(.3,3));sig=float(rng.uniform(.5,2))
        T2=1.8*T
        v1=var_area(T,lam,sig);v2=var_area(T2,lam,sig)
        R=v2/v1
        solved_lam=brentq(lambda z:var_area(T2,z)/var_area(T,z)-R,1e-4,100.)
        solved_sig=math.sqrt(v1/var_area(T,solved_lam))
        k4=displacement_cumulant4(T,lam,r,sig)
        solved_r=brentq(lambda v:displacement_cumulant4(T,solved_lam,v,solved_sig)-k4,0,solved_lam)
        assert abs(solved_lam-lam)<1e-6,(lam,solved_lam)
        assert abs(solved_sig-sig)<1e-6,(sig,solved_sig)
        assert abs(solved_r-r)<1e-5,(r,solved_r)
    print('PASS: 80 full inversions of two variances plus one fourth cumulant')

    lam=1.6;r=.7;sig=1.3;T=2.2
    k4=displacement_cumulant4(T,lam,r,sig)
    est,sem,var=monte_carlo_k4(T,lam,r,sig)
    v=var_area(T,lam,sig)
    print('independent conditional-Gaussian simulation, n=150000:',
          f'kappa4 exact={k4:.8f}, MC={est:.8f} +/- {3*sem:.8f}, var exact={v:.8f}, MC={var:.8f}')
    assert abs(est-k4)<5*sem+0.012
    assert abs(var-v)<.012
    print('PASS: independent renewal-partition simulation agrees with exact cumulants')

    lam=1.6;r=.7;sig=1.3
    short=displacement_cumulant4(0.015,lam,r,sig)/(0.4*sig**4*r*.015**5)
    assert abs(short-1)<.03
    longT=100
    k4long=displacement_cumulant4(longT,lam,r,sig)
    expected=24*sig**4*r/(lam**3*(2*lam-r))*longT
    assert abs(k4long/expected-1)<.03,(k4long/expected)
    print('PASS: short-time fifth-power and long-time linear cumulant asymptotics')

if __name__=='__main__':
    main()
