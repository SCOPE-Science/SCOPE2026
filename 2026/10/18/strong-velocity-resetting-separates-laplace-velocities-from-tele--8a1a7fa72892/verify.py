"""Standalone stochastic and algebraic checks for fast velocity-only resetting.
All random-number draws use a fixed seed. Simulation does not certify limiting proofs.
"""
import math
import numpy as np
rng=np.random.default_rng(20261014)

def drift(v, kind):
    return math.tan(v) if kind=='thick' else math.tanh(v)

def advance(v, sigma, dt, kind, amplitude):
    # Numerically integrate dv/dt=amplitude*sigma-drift(v) and dx/dt=v
    # 4th-order Runge-Kutta, h <=0.025
    n=max(1, math.ceil(dt/0.025)); h=dt/n; displacement=0.0
    for _ in range(n):
        k1=amplitude*sigma-drift(v,kind)
        k2=amplitude*sigma-drift(v+h*k1/2,kind)
        k3=amplitude*sigma-drift(v+h*k2/2,kind)
        k4=amplitude*sigma-drift(v+h*k3,kind)
        vnext=v+h*(k1+2*k2+2*k3+k4)/6
        displacement+=h*(v+vnext)/2
        v=vnext
    return v,displacement

def stationary_state(rate, flip, amplitude, kind):
    age=rng.exponential(1/rate)
    sigma=int(rng.choice([-1,1]))
    v=0.; elapsed=0.
    while elapsed<age:
        interval=min(rng.exponential(1/flip),age-elapsed)
        v,_=advance(v,sigma,interval,kind,amplitude)
        elapsed+=interval
        if elapsed<age-1e-13: sigma=-sigma
    return v,sigma

def evolve(v,sigma,horizon,rate,flip,amplitude,kind):
    t=0.; xpos=0.
    while t<horizon-1e-13:
        a=rng.exponential(1/rate); b=rng.exponential(1/flip)
        delta=min(a,b,horizon-t)
        v,dx=advance(v,sigma,delta,kind,amplitude); xpos+=dx; t+=delta
        if t>=horizon-1e-13: break
        if a<b: v=0.
        else: sigma=-sigma
    return v,sigma,xpos

def check_kind(kind,amplitude,rate,flip=0.8,n=7500):
    obs=np.empty(n); cor=np.empty(n); disp=np.empty(n)
    for i in range(n):
        v,s=stationary_state(rate,flip,amplitude,kind)
        y=rate*v/amplitude
        obs[i]=y
        vt,st,x=evolve(v,s,0.8,rate,flip,amplitude,kind)
        cor[i]=y*(rate*vt/amplitude)
        disp[i]=rate*x/amplitude
    target_cov=math.exp(-2*flip*0.8)
    target_disp=0.8/flip-(1-math.exp(-2*flip*0.8))/(2*flip**2)
    print(kind,'r',rate,'mean |scaled v|',round(np.mean(abs(obs)),4),
          'var scaled v',round(float(np.var(obs)),4),
          'cov(t=0.8)',round(float(np.mean(cor)),4),'target',round(target_cov,4),
          'displacement var',round(float(np.var(disp)),4),'target',round(target_disp,4))
    if rate>=60:
        assert abs(np.mean(abs(obs))-1)<0.12
        assert abs(np.var(obs)-2)<0.3
        assert abs(np.mean(cor)-target_cov)<0.14
        assert abs(np.var(disp)-target_disp)<0.17

# Exact linear-drag moment identities: independent of numerical integration.
for rate in (10.,40.,160.):
    amp=0.9; flip=0.8; kappa=1.3
    b=amp/(rate+kappa+2*flip)
    var=2*amp*b/(rate+2*kappa)
    integrated=(var+amp*b/(2*flip))/(rate+kappa)
    print('linear exact',rate,'scaled variance',rate**2*var/amp**2,
          'scaled diffusivity',rate**2*integrated/amp**2,
          'diffusive coefficient target',1/(2*flip))
for kind,amp in (('thick',1.2),('thin',0.6)):
    for rate in (20.,80.): check_kind(kind,amp,rate)
print('All numerical and algebraic checks completed.')
