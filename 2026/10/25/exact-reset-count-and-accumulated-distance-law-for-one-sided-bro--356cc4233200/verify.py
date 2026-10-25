"""Reproducible independent tests of the Brownian smart-reset cost/count law."""
import math
import numpy as np


def analytic_checks():
    for D,L,r in [(1.,1.,.25),(1.,1.,4.),(1.,1.,25.),(.7,1.4,2.8),(2.,.4,.9)]:
        k=math.sqrt(r/D)
        p=1/(1+k*L)
        q=1-p
        assert abs(p+q-1)<1.e-14
        assert abs(q/p-k*L)<1.e-13
        for s in [0.,.13,k,1.3,2.71]:
            w0=k*k*L/((1+k*L)*(k+s))
            assert abs(w0-q*k/(k+s))<2.e-14
            assert abs(-w0/L-(k*w0-k*k/(k+s)))<2.e-13
            # Boundary-value residual at two negative sites (special resonance explicit).
            for x in [-1.1/k,-.37/k]:
                if abs(s-k)<1.e-12:
                    # For s=k the resonant inhomogeneous solution is exp(kx)*(w0-kx/2).
                    f=math.exp(k*x)*(w0-k*x/2)
                    f2=math.exp(k*x)*(k*k*(w0-k*x/2)-k*k)
                else:
                    b=k*k/(k*k-s*s)
                    a=w0-b
                    f=a*math.exp(k*x)+b*math.exp(s*x)
                    f2=a*k*k*math.exp(k*x)+b*s*s*math.exp(s*x)
                assert abs(D*f2-r*f+r*math.exp(s*x))<3.e-10
            assert abs(w0*(1-L/L))<1.e-14
        assert abs(q/(p*k)-L)<1.e-13
        variance=L*L+2*L/k
        second=2*q/(p*k)**2
        assert abs(second-L*L-variance)<1.e-12
        assert abs(sum(p*q**n for n in range(450))-1)<2.e-12
        for c in [.04,.8,3.]:
            pmf=[math.exp(-q*k*c)*(q*k*c)**m/math.factorial(m) for m in range(100)]
            assert abs(sum(pmf)-1)<2.e-9
            # Summing the mixed joint N/C density agrees with its exponential marginal.
            terms=[p*q**n*k**n*c**(n-1)*math.exp(-k*c)/math.factorial(n-1) for n in range(1,101)]
            target=p*q*k*math.exp(-p*k*c)
            assert abs(sum(terms)-target)<1.e-9
    print('PASS: boundary-value residuals, matching, distribution normalizations, moments and conditional count.')


def physical_trajectory_check(n=12000,L=1.,D=1.,r=4.,seed=471):
    rng=np.random.default_rng(seed)
    k=math.sqrt(r/D)
    p=1/(1+k*L)
    q=1-p
    active=np.ones(n,dtype=bool)
    x=np.zeros(n)
    cost=np.zeros(n)
    counts=np.zeros(n,dtype=int)
    total_measurements=0
    while active.any():
        indices=np.flatnonzero(active)
        total_measurements+=len(indices)
        dt=rng.exponential(1/r,size=len(indices))
        y=x[indices]+np.sqrt(2*D*dt)*rng.normal(size=len(indices))
        crossed=y>=L
        under=~crossed
        prob=np.zeros(len(indices))
        prob[under]=np.exp(-(L-x[indices[under]])*(L-y[under])/(D*dt[under]))
        crossed |= (rng.random(len(indices))<prob)
        reset=(~crossed)&(y<0)
        reset_ids=indices[reset]
        cost[reset_ids]+=-y[reset]
        counts[reset_ids]+=1
        stay=indices[(~crossed)&(~reset)]
        x[stay]=y[(~crossed)&(~reset)]
        x[reset_ids]=0.
        active[indices[crossed]]=False
    checks=[
       ('zero mass',float(np.mean(cost==0.)),p,.035),
       ('mean number actual resets',float(np.mean(counts)),k*L,.16),
       ('mean reset distance',float(np.sum(cost)/np.sum(counts)),1/k,max(.06,.07/k)),
       ('mean cumulative cost',float(np.mean(cost)),L,.08),
       ('variance of cumulative cost',float(np.var(cost)),L*L+2*L/k,.27),
       ('cost Laplace transform at 1.3',float(np.mean(np.exp(-1.3*cost))),(k+1.3)/(k+1.3*(1+k*L)),.03),
       ('cost tail above 2',float(np.mean(cost>2)),q*math.exp(-2*p*k),.026)
    ]
    for name, empirical, target, tolerance in checks:
        err=abs(empirical-target)
        print(f'r={r:6.2f} {name:30s}: MC={empirical:.6f}, exact={target:.6f}, abs_error={err:.6f}')
        assert err<tolerance, (name,err,tolerance)
    print(f'PASS: {n} exact-bridge Brownian trajectories, r={r}, monitoring samples={total_measurements}.')


if __name__=='__main__':
    analytic_checks()
    for r in [.25,4.,25.]:
        physical_trajectory_check(r=r,n=12000,seed=int(r*10000)+11)
    print('ALL NEW FINDING CHECKS PASS')
