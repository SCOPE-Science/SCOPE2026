"""Reproduce sharp periodic reversal diffusivity bounds using two independent formulas.
All quantities dimensionless except the supplied speed and period. Python >=3.9.
"""
import math
import random


def diffusion_segments(rates, lengths, speed=1.0):
    """Exact long-time diffusivity for periodic piecewise-constant flip rate."""
    assert len(rates) == len(lengths) and rates
    assert all(r>=0 for r in rates) and all(d>0 for d in lengths)
    T=sum(lengths); total=sum(r*d for r,d in zip(rates,lengths))
    assert total>0
    q=[math.exp(-2*r*d) for r,d in zip(rates,lengths)]
    c=[-math.expm1(-2*r*d)/(2*r) if r else d for r,d in zip(rates,lengths)]
    C=0.0; product=1.0
    for qi,ci in zip(q,c):
        C+=product*ci
        product*=qi
    endpoint=C/(-math.expm1(-2*total))
    G=[endpoint]
    for qi,ci in zip(q,c):
        G.append((G[-1]-ci)/qi if qi>1e-250 else float('nan'))
    # Stable: work backwards from the known endpoint instead of inverse products.
    G=[0.0]*(len(rates)+1)
    G[-1]=endpoint
    for k in range(len(rates)-1,-1,-1):
        G[k]=c[k]+q[k]*G[k+1]
    assert abs(G[0]-endpoint)<2e-10*max(1,endpoint)
    area=0.
    for r,d,qi,ci,g_right in zip(rates,lengths,q,c,G[1:]):
        if r:
            area+=d/(2*r)+(g_right-1/(2*r))*ci
        else:
            area+=d*g_right+d*d/2
    return speed*speed*area/T


def phase_double_integral(rates,lengths,speed=1.0,n=240):
    """Independent finite quadrature of the two-time covariance, not the ODE."""
    T=sum(lengths); total=sum(r*d for r,d in zip(rates,lengths)); starts=[0.]
    for d in lengths: starts.append(starts[-1]+d)
    def mass(z):
        turns=math.floor(z/T)
        u=z-turns*T
        acc=turns*total
        for k,r in enumerate(rates):
            acc+=r*max(0.,min(u,starts[k+1])-starts[k])
        return acc
    v=0.
    for a in range(n):
        t=(a+0.5)*T/n; mt=mass(t)
        for b in range(n):
            s=(b+0.5)*T/n
            v+=math.exp(-2*(mass(t+s)-mt))
    return speed*speed*T*v/n**2/(-math.expm1(-2*total))


def bounds(T,total,speed):
    lower=speed*speed*T/(2*total)
    upper=speed*speed*T*math.cosh(total)/(2*math.sinh(total))
    return lower,upper


def run():
    count=0
    for T,L,v in ((1.,0.2,1.),(1.,1.3,3.),(2.7,2.2,0.5),(0.4,4.,1.2)):
        lo,hi=bounds(T,L,v)
        equal=diffusion_segments([L/T],[T],v)
        assert math.isclose(equal,lo,rel_tol=1e-11);count+=1
        for eps in (0.4,0.1,0.025,0.00625):
            pulse=diffusion_segments([L/(T*eps),0.],[T*eps,T*(1-eps)],v)
            assert lo < pulse < hi; count+=1
        pulses=[diffusion_segments([L/(T*e),0.],[T*e,T*(1-e)],v) for e in (0.2,0.05,0.01,0.002)]
        assert all(pulses[i]<pulses[i+1] for i in range(3))
        assert abs(hi-pulses[-1])/hi<0.009
        count+=2
    rng=random.Random(76061)
    for k in range(144):
        m=rng.randrange(2,8)
        rr=[rng.uniform(0.0,5.0) for _ in range(m)]
        if k%3==0:rr[rng.randrange(m)]=0.
        ll=[rng.uniform(.05,1.9) for _ in range(m)]
        T=sum(ll);L=sum(a*b for a,b in zip(rr,ll));v=rng.uniform(0.1,4.)
        lo,hi=bounds(T,L,v)
        val=diffusion_segments(rr,ll,v)
        assert lo-1e-9*max(1,lo)<=val<=hi+1e-9*max(1,hi),(k,val,lo,hi)
        count+=1
        if k<10:
            direct=phase_double_integral(rr,ll,v,240)
            assert abs(val-direct) < 0.002*max(1, val),(k,val,direct)
            count+=1
    # Examples for equality, strict inequalities and pulse concentration.
    for rate in (0.25, 1.0, 4.0):
        T=1.;L=rate;v=1.
        lo,hi=bounds(T,L,v)
        assert lo<=diffusion_segments([rate,rate],[.3,.7])<=hi
        assert lo<diffusion_segments([2*rate,0.],[.5,.5])<hi
        count+=2
    print(f'PASS: {count} independent deterministic assertions')
    return count

if __name__=='__main__':run()
