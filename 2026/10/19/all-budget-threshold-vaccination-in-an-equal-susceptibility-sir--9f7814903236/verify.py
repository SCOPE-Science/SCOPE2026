"""Independent finite-dimensional arithmetic tests for an SIR final-size formula.

No finite test is offered as a proof of the continuum theorem.
Run with: python3 verify.py
"""
from fractions import Fraction as F
from itertools import product
from math import exp, isclose


def cumulative_force(b, t):
    """Bisect the unique positive zero of h-b-t*(1-exp(-h))."""
    assert b > 0 and t >= 0
    lo, hi = float(b), float(b+t+1)
    for _ in range(160):
        mid = (lo+hi)/2
        if mid-float(b)-float(t)*(-__import__('math').expm1(-mid)) > 0:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2


def optimum_greedy(r, cap, k):
    out=[F(0)]*len(r)
    left=k
    for i in sorted(range(len(r)),key=lambda j:r[j],reverse=True):
        add=min(cap[i],left)
        out[i]=add
        left-=add
    assert left==0
    return out


def weighted_remain(r,cap,v):
    return sum((ri*(si-vi) for ri,si,vi in zip(r,cap,v)),F(0))


def final_survivors(b,r,cap,v):
    m=sum(v,F(0))
    t=weighted_remain(r,cap,v)
    h=cumulative_force(b,t)
    return float(m)+float(sum(cap)-m)*exp(-h)


def rk4_sir(beta,mu,sinitial,iinitial,dt=.005,until=40):
    state=list(sinitial)+list(iinitial)
    n=len(beta)
    def deriv(y):
        ss=y[:n]; ii=y[n:]
        lam=sum(beta[j]*ii[j] for j in range(n))
        return [-x*lam for x in ss]+[ss[j]*lam-mu[j]*ii[j] for j in range(n)]
    for _ in range(round(until/dt)):
        k1=deriv(state)
        k2=deriv([s+dt*k/2 for s,k in zip(state,k1)])
        k3=deriv([s+dt*k/2 for s,k in zip(state,k2)])
        k4=deriv([s+dt*k for s,k in zip(state,k3)])
        state=[s+dt*(a+2*b+2*c+d)/6 for s,a,b,c,d in zip(state,k1,k2,k3,k4)]
    return state[:n],state[n:]


def checks():
    comparisons=0
    b=F(1,5)
    r=[F(5),F(3),F(1)]
    cap=[F(1)]*3
    choices=[F(k,4) for k in range(5)]
    best_by_k={F(k,4):optimum_greedy(r,cap,F(k,4)) for k in range(13)}
    assert all(sum(v)==k for k,v in best_by_k.items())
    last_value=-1.
    for k in sorted(best_by_k):
        vopt=best_by_k[k]
        topt=weighted_remain(r,cap,vopt)
        nopt=final_survivors(b,r,cap,vopt)
        assert nopt>last_value
        last_value=nopt
        for candidate in product(choices,repeat=3):
            if sum(candidate,F(0))!=k:
                continue
            assert topt<=weighted_remain(r,cap,candidate)
            assert nopt >= final_survivors(b,r,cap,candidate)-1e-11
            comparisons+=1
    assert comparisons==5**3
    # Equal-ratio groups exhibit exact alternative optimal allocations.
    r2=[F(4),F(4),F(1)]
    c2=[F(1)]*3
    assert weighted_remain(r2,c2,[F(1),F(0),F(0)]) == weighted_remain(r2,c2,[F(0),F(1),F(0)])
    assert abs(final_survivors(b,r2,c2,[F(1),F(0),F(0)])-final_survivors(b,r2,c2,[F(0),F(1),F(0)]))<1e-13
    # Two populations with a budget exceeding the small-supply threshold 5/4.
    bb=[F(4),F(1)]; cc=[F(1),F(1)]; k=F(3,2)
    assert k>F(1,4)*sum((x*y for x,y in zip(bb,cc)),F(0))
    greedy=[F(1),F(1,2)]
    reversed_allocation=[F(1,2),F(1)]
    assert weighted_remain(bb,cc,greedy)==F(1,2)
    assert weighted_remain(bb,cc,reversed_allocation)==F(2)
    ng=final_survivors(b,bb,cc,greedy)
    nr=final_survivors(b,bb,cc,reversed_allocation)
    assert isclose(ng,1.853622849291979,abs_tol=1e-11)
    assert isclose(nr,1.5746923309513243,abs_tol=1e-11)
    assert ng>nr
    ode_checks=0
    for vv in (greedy,reversed_allocation):
        ss,ii=rk4_sir([4.,1.],[1.,1.],[float(x-y) for x,y in zip(cc,vv)],[.05,0.])
        expected=float(sum(vv))+sum(ss)
        assert abs(expected-final_survivors(b,bb,cc,vv))<1e-8
        assert max(ii)<1e-11
        ode_checks+=1
    # The root remains regular on both sides of the reproduction threshold T=1.
    for t in [F(0),F(1,2),F(1),F(2),F(4),F(12)]:
        h=cumulative_force(b,t)
        assert abs(h-float(b)-float(t)*(-__import__('math').expm1(-h)))<1e-12
        assert h>0 and 1-float(t)*exp(-h)>0
    return comparisons,ode_checks,ng,nr


if __name__=='__main__':
    comparisons,ode_checks,ng,nr=checks()
    print('VERIFY_OK: %d rational-grid vaccine allocations, %d independent SIR trajectory checks; high-budget survivors %.12f > %.12f' % (comparisons,ode_checks,ng,nr))
