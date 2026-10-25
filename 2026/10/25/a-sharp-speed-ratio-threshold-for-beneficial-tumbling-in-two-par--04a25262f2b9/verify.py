"""Reproduce the two-speed persistent-encounter expansion and numerical checks.

Run: python verify.py. Requires numpy, scipy and sympy.
"""
import numpy as np
import sympy as sp
from scipy.linalg import expm

x, ell, r = sp.symbols('x ell r', positive=True)
z = sp.symbols('z')
vel = [1-r, 1+r, -1-r, -1+r]
neighbor = [(1,2), (0,3), (0,3), (1,2)]
coeff = []
zeroth = [(ell-x)/vel[i] if i < 2 else -x/vel[i] for i in range(4)]
coeff.append(zeroth)
for degree in (1,2):
    prior=coeff[-1]
    next_order=[]
    for i in range(4):
        Qp=sp.expand(sum(prior[j]-prior[i] for j in neighbor[i]))
        primitive=Qp.subs(x,z)/vel[i]
        f=sp.integrate(primitive, (z,x,ell)) if i<2 else -sp.integrate(primitive,(z,0,x))
        f=sp.factor(f)
        next_order.append(f)
        assert sp.simplify(vel[i]*sp.diff(f,x)+Qp)==0
        assert sp.simplify(f.subs(x,ell if i<2 else 0))==0
    coeff.append(next_order)
for i,f in enumerate(zeroth):
    assert sp.simplify(vel[i]*sp.diff(f,x)+1)==0
    assert sp.simplify(f.subs(x,ell if i<2 else 0))==0
means=[sp.factor(sum(sp.integrate(f,(x,0,ell))/ell for f in fs)/4) for fs in coeff]
expected=[ell/(2*(1-r*r)),ell**2*(1-5*r*r)/(6*(1-r*r)**2),2*ell**3*r*r/(3*(1-r*r)**3)]
assert all(sp.simplify(a-b)==0 for a,b in zip(means,expected))
assert sp.simplify(means[1].subs(r,1/sp.sqrt(5)))==0
assert sp.simplify(means[2].subs(r,1/sp.sqrt(5))-25*ell**3/96)==0
print('Exact generator equations, mixed absorbing boundaries, mean coefficients and threshold: PASS')

def bvp_mean(length, fast_speed, slow_speed, alpha):
    w=np.array([fast_speed-slow_speed,fast_speed+slow_speed,
                -fast_speed-slow_speed,-fast_speed+slow_speed])
    q=np.array([[-2,1,1,0],[1,-2,0,1],[1,0,-2,1],[0,1,1,-2]],float)
    A=np.zeros((5,5))
    A[:4,:4]=-alpha*q/w[:,None]
    A[:4,4]=-1/w
    B=expm(A*length)
    start=np.zeros(5)
    start[:2]=np.linalg.solve(B[:2,:2],-B[:2,4])
    start[4]=1
    grid=np.linspace(0,length,201)
    values=np.array([(expm(A*y)@start)[:4] for y in grid])
    return float(np.mean(np.trapezoid(values,x=grid,axis=0)/length))

for speed_ratio in (.2,.3,1/np.sqrt(5),.5,.7,.9):
    al=.0001
    observed=bvp_mean(1,1,speed_ratio,al)
    predicted=sum(float(v.subs({ell:1,r:speed_ratio}))*al**j for j,v in enumerate(means))
    assert abs(observed-predicted)<2.e-7,(speed_ratio,observed,predicted)
print('Independent four-state matrix-exponential boundary-value checks (six speed ratios): PASS')

def monte_carlo(length,fast_speed,slow_speed,alpha,n,seed):
    rng=np.random.default_rng(seed)
    y=rng.uniform(0,length,size=n)
    sign1=rng.choice(np.array([-1,1]),size=n)
    sign2=rng.choice(np.array([-1,1]),size=n)
    time=np.zeros(n)
    living=np.ones(n,dtype=bool)
    for step in range(3000):
        idx=np.flatnonzero(living)
        if not len(idx): break
        velocity=fast_speed*sign1[idx]-slow_speed*sign2[idx]
        hitting=np.where(velocity>0,(length-y[idx])/velocity,-y[idx]/velocity)
        flip=rng.exponential(1/(2*alpha),size=len(idx))
        hit=hitting<flip
        elapsed=np.minimum(hitting,flip)
        time[idx]+=elapsed
        living[idx[hit]]=False
        other=idx[~hit]
        y[other]=(y[other]+velocity[~hit]*flip[~hit])%length
        first=rng.random(len(other))<.5
        sign1[other[first]]*=-1
        sign2[other[~first]]*=-1
    assert not living.any(), 'Monte Carlo unfinished'
    return float(np.mean(time)),float(np.std(time,ddof=1)/np.sqrt(n))
for ratio,rate in ((.2,.1),(.5,.1),(.7,.3)):
    estimate,se=monte_carlo(1,1,ratio,rate,40000,int(ratio*10000+rate*100))
    expectation=bvp_mean(1,1,ratio,rate)
    assert abs(estimate-expectation)<5*se+0.001,(ratio,rate,estimate,expectation,se)
print('Independent event-driven Monte Carlo vs boundary-value solution (three cases): PASS')
