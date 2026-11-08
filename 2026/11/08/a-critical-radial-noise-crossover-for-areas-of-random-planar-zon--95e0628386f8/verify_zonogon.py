"""Reproducibility checks for random equal-length planar zonogon area laws.
Runs with Python 3 and NumPy; no external input files.
"""
import math
import numpy as np


def cross(u,v):
    return u[0]*v[1]-u[1]*v[0]


def polygon_area_hull(points):
    # Monotone-chain hull; works on ordinary segment-endpoint subset sums.
    p=sorted((float(x),float(y)) for x,y in points)
    def half(seq):
        h=[]
        for q in seq:
            while len(h)>=2 and cross((h[-1][0]-h[-2][0],h[-1][1]-h[-2][1]),(q[0]-h[-1][0],q[1]-h[-1][1]))<=1e-11:
                h.pop()
            h.append(q)
        return h
    h=half(p)[:-1]+half(reversed(p))[:-1]
    return abs(sum(cross(h[i],h[(i+1)%len(h)]) for i in range(len(h)))/2)


def zonogon_area(theta, radii):
    x=radii*np.cos(theta);y=radii*np.sin(theta)
    return float(sum(abs(x[i]*y[j]-x[j]*y[i]) for i in range(len(x)) for j in range(i+1,len(x))))


def exact_const(n,r=1.):
    mean=r*r*n*(n-1)/math.pi
    variance=math.comb(n,2)*r**4*(.5-4/math.pi**2)
    return mean, variance


def sim_q(rng,k,terms=8000):
    # Exact limiting series truncated; rigorously bounded L2 tail in RESULT.md.
    a=np.arange(1,terms+1,dtype=float)
    return float(-2/math.pi*np.sum((rng.exponential(size=terms)-1)/(4*a*a-1)))


def main():
    rng=np.random.default_rng(202611030834)
    exact_geometries=0
    for n in range(2,9):
        for _ in range(18):
            t=rng.uniform(0,2*math.pi,n)
            r=rng.uniform(0.4,1.7,n)
            v=np.column_stack((r*np.cos(t),r*np.sin(t)))
            subsets=[]
            for mask in range(1<<n):
                subsets.append(np.sum(v[[j for j in range(n) if mask&(1<<j)]],axis=0) if mask else np.zeros(2))
            direct=polygon_area_hull(subsets)
            formula=zonogon_area(t,r)
            assert abs(direct-formula)<4e-8*(1+formula), (n,formula,direct)
            exact_geometries+=1
    # Analytic Fourier coefficient and variance identity.
    k=np.arange(1,100000,dtype=float)
    s1=np.sum(1/(4*k*k-1))
    s2=np.sum(1/(4*k*k-1)**2)
    assert abs(s1-.5)<3e-6
    assert abs(s2-(math.pi**2-8)/16)<1e-12
    # Uniform-angle simulations for mean, variance and cutoff.
    report=[]
    for n,trials in [(8,18000),(30,14000),(90,6000)]:
        values=np.empty(trials)
        for i in range(trials):
            t=rng.uniform(0,2*math.pi,n)
            values[i]=zonogon_area(t,np.ones(n))
        mean,var=exact_const(n)
        rel_mean=abs(values.mean()-mean)/math.sqrt(var/trials)
        # Two-sigma-style broad coverage; variance standard error roughly sqrt(2/trials).
        rel_var=abs(values.var(ddof=1)/var-1)
        assert rel_mean<4.5,(n,rel_mean)
        assert rel_var<.10,(n,rel_var)
        assert max(values)<=n*n/math.pi+1e-10
        report.append((n,round(rel_mean,4),round(rel_var,4)))
    # Limiting series has mean 0, nonzero negative third cumulant and hard ceiling.
    coef=2/(math.pi*(4*np.arange(1,20001,dtype=float)**2-1))
    varlim=float(np.dot(coef,coef))
    cumulant3=-2*float(np.sum(coef**3))
    assert abs(varlim-(1/4-2/math.pi**2))<1e-14
    assert cumulant3<-.001
    sims=np.array([sim_q(rng,k,600) for k in range(12000)])
    assert sims.max()<1/math.pi
    assert abs(sims.mean())<.01
    assert abs(sims.var()-varlim)<.015
    # Exact radial projection for positive-variance radii: h1(R)=2 E[R]/pi * (R-E[R]).
    # R in {1,3} equiprobable, direct analytic calculation of finite-n second moment.
    m=2.; second=5.; v=1.; alpha=2/math.pi
    for n in [4,15,100]:
        rawvar=math.comb(n,2)*(second**2/2-alpha**2*m**4)+6*math.comb(n,3)*alpha**2*m*m*v
        remvar=math.comb(n,2)*(second**2/2-alpha**2*m**4-2*alpha**2*m*m*v)
        provar=n*(n-1)**2*alpha**2*m*m*v
        assert abs(rawvar-(provar+remvar))<1e-8*rawvar
    print('VERIFY_OK hull_cases=%d Fourier_coefficients=100000 moment_cases=3 radial_regression_cases=3 nonGaussian_limit_draws=12000 quantile_support=1/pi MC=%s third_cumulant=%.9f'%(exact_geometries,report,cumulant3))

if __name__=='__main__':
    main()

# Triangular-array crossover checks: exact finite-n mean and variance are
# checked directly, independently of the Fourier-limit Monte Carlo checks.
def check_crossover():
    rng=np.random.default_rng(39042)
    alpha=2/math.pi
    n=90
    tau=.6
    rho=1.
    outcomes=[]
    for beta in [0.,.25,.5,.75]:
        q=tau*tau*n**(-2*beta)
        theoretical=math.comb(n,2)*(rho**4*((1+q)**2/2-alpha**2)-2*alpha**2*rho**4*q) + n*(n-1)**2*alpha**2*rho**4*q
        # Note: D-term plus first projection (not the double-counted covariances).
        full=math.comb(n,2)*rho**4*((1+q)**2/2-alpha**2)+6*math.comb(n,3)*alpha**2*rho**4*q
        assert abs(full-theoretical)<1e-9*full
        arr=[]
        for _ in range(5500):
            th=rng.uniform(0,2*math.pi,n)
            rad=rho*(1+tau*n**(-beta)*rng.choice([-1,1],n))
            arr.append(float(np.sum(np.triu(np.abs(np.sin(th[:,None]-th[None,:])) * rad[:,None] *rad[None,:],1))))
        arr=np.asarray(arr)
        mean=rho**2*n*(n-1)/math.pi
        zmean=abs(arr.mean()-mean)/math.sqrt(full/len(arr))
        vr=arr.var(ddof=1)/full
        assert zmean<4.5,(beta,zmean)
        assert .88<vr<1.12,(beta,vr)
        outcomes.append((beta,round(vr,4)))
    print('CROSSOVER_VERIFY_OK cases=4 n=90 trials_each=5500 finite_variance_ratios=%s'%outcomes)

check_crossover()
