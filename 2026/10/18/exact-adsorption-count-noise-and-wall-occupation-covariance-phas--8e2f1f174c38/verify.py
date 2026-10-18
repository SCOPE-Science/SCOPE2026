"""Independent numerical checks of a sticky-wall return/collision fluctuation theorem.
Run: python verify.py
Only finite numerical checks; the analytic theorem requires its separate proof.
"""
import math
import numpy as np
from scipy.optimize import brentq

V, ALPHA, X0 = 1.0, 1.0, 1.0

def quantities(r, gamma):
    b = (X0/V)*math.sqrt(r*(r+2*ALPHA))
    bp = (X0/V)*(r+ALPHA)/math.sqrt(r*(r+2*ALPHA))
    m = math.expm1(b)/r
    vv = (math.exp(2*b)-2*r*bp*math.exp(b)-1)/r**2
    bd = 1/gamma
    mu = m+bd
    return m, vv, (vv+bd**2)/mu**2, bd*(vv-bd*m)/mu**3

def telegraph_T_samples(r, n, rng):
    # Independent exact event-driven CTMC trajectories from (x0,-).
    x=np.full(n,X0); vel=np.full(n,-1.0); t=np.zeros(n)
    alive=np.ones(n,dtype=bool)
    attempts=0
    while alive.any():
        attempts+=1
        assert attempts<10000
        indices=np.flatnonzero(alive)
        k=len(indices)
        dt=rng.exponential(scale=1/(ALPHA+r),size=k)
        xi=x[indices]; vi=vel[indices]
        hit=(vi<0) & (xi/V<=dt)
        hitids=indices[hit]
        t[hitids]+=xi[hit]/V
        alive[hitids]=False
        contids=indices[~hit]
        t[contids]+=dt[~hit]
        x[contids]+=vi[~hit]*V*dt[~hit]
        reset=rng.random(len(contids))<r/(ALPHA+r)
        if reset.any():
            x[contids[reset]]=X0
            vel[contids[reset]]=-1
        if (~reset).any():
            vel[contids[~reset]]*=-1
    return t

def stationary_counts_cov(r,gamma,horizon,reps,rng):
    # Direct independent renewal-cycle simulation.  The initial state is the
    # beginning of a wall sojourn, not stationary; horizon >> mean cycle.
    counts=np.zeros(reps,dtype=int);wall=np.zeros(reps)
    clock=np.zeros(reps);live=np.ones(reps,dtype=bool)
    while live.any():
        idx=np.flatnonzero(live)
        b=rng.exponential(scale=1/gamma,size=len(idx))
        # Generate excursions; each follows actual velocity/tumble/reset path.
        t=telegraph_T_samples(r,len(idx),rng)
        remaining=horizon-clock[idx]
        wall[idx]+=np.minimum(b,remaining)
        completed=(b+t<=remaining)
        yes=idx[completed];counts[yes]+=1;clock[yes]+=b[completed]+t[completed]
        no=idx[~completed];live[no]=False
    return counts,wall

def main():
    rng=np.random.default_rng(20261014)
    rstar=brentq(lambda r: (r+ALPHA)/(r+2*ALPHA)*((X0/V)*math.sqrt(r*(r+2*ALPHA)))/(1-math.exp(-(X0/V)*math.sqrt(r*(r+2*ALPHA))))-1,.000001,10)
    print('unique CV crossing rstar=',format(rstar,'.10f'))
    for r in [.1,.5,1.0]:
        m,vv,_,_=quantities(r,.2)
        samples=telegraph_T_samples(r,100000,rng)
        err_m=abs(np.mean(samples)/m-1)
        err_v=abs(np.var(samples)/vv-1)
        print('excursions',r,'mean',m,'variance',vv,'empirical relative errors',round(err_m,4),round(err_v,4))
        assert err_m<.05 and err_v<.12
    for r,gamma in [(.1,.04),(.1,.15),(.1,.5),(1.0,.05),(1.0,1.)]:
        m,vv,F,C=quantities(r,gamma)
        cnt,occup=stationary_counts_cov(r,gamma,750.,2500,rng)
        Fs=np.var(cnt,ddof=1)/np.mean(cnt)
        Cs=np.cov(cnt,occup,ddof=1)[0,1]/750.
        print('r gamma',r,gamma,'Fano analytic empirical',round(F,5),round(Fs,5),'cov rate analytic empirical',round(C,5),round(Cs,5))
        assert abs(F-Fs)<.18 and abs(C-Cs)<.17
    for r in [1.e-6,1.e-5,1.e-4,1.e-3]:
        b=(X0/V)*math.sqrt(r*(r+2*ALPHA));bp=(X0/V)*(r+ALPHA)/math.sqrt(r*(r+2*ALPHA))
        m,vv,_,_=quantities(r,1.)
        gc=m/vv;gf=2*m/(vv-m*m)
        print('weak resetting r',r,'gamma_cov/r',gc/r,'gamma_fano/r',gf/r)
        assert abs(gc/r-1)<.07 and abs(gf/r-2)<.20
    print('ALL FINITE CHECKS PASSED')
if __name__=='__main__': main()
