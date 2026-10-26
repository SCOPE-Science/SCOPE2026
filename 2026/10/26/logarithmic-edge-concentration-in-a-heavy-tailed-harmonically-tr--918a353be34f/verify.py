"""Independent numerical checks for stationary alternating-renewal harmonic-trap edge law.
Requires numpy. This checks a finite-parameter stationary sampler, the exact renewal
identity, and convergence of its logarithmic edge coefficient; asymptotic theorem
remains analytic, not inferred from simulations.
"""
import numpy as np
rng=np.random.default_rng(20261024)
N=180000
checks=0
for beta in (1.5,2.0,2.8,4.0):
    # Draw iid Lomax dwell lengths with survival (1+t)**(-beta), and
    # iterate the exact switching-time position map through alternating phases.
    y=np.zeros(N)
    for j in range(32):
        t=rng.pareto(beta,N)
        sign=1 if j%2==0 else -1
        y=sign+(y-sign)*np.exp(-t)
    # 32 phases end in minus state. Values at these switches start a plus run.
    gap=1-y
    assert np.all((gap>0)&(gap<=2))
    mu=1/(beta-1)
    # Exact equilibrium age law: P(A>a)=(1+a)**(1-beta).
    age=np.power(rng.random(N),-1/(beta-1))-1
    side=rng.integers(0,2,N)
    y_stationary=np.where(side==1,1-gap*np.exp(-age),-1+gap*np.exp(-age))
    H=lambda x:np.power(1+np.maximum(x,0),1-beta)/(beta-1)
    for eps in (0.2,0.04,0.005):
        L=np.log(1/eps)
        pos=H(L+np.log(gap))
        neg=mu-H(np.log(gap/(2-eps)))
        predicted=np.mean(pos+neg)/(2*mu)
        measured=np.mean(y_stationary>1-eps)
        err=6*np.sqrt(max(predicted*(1-predicted),1e-8)/N)+0.001
        assert abs(predicted-measured)<err, (beta,eps,predicted,measured,err)
        checks+=1
    for L in (400,1200):
        exact_plus=np.mean(H(L+np.log(gap)))/(2*mu)
        asymptotic=0.5*L**(1-beta)
        ratio=exact_plus/asymptotic
        assert abs(ratio-1)<0.03, (beta,L,ratio)
        checks+=1
    print(f'beta={beta:3.1f}, direct-versus-exact checks passed; '
          f'log-coefficient ratio at L=1200: {np.mean(H(1200+np.log(gap)))/(2*mu)/(.5*1200**(1-beta)):.7f}')
print(f'PASS: {checks} numerical comparisons over four Pareto exponents.')
# A separate half-t dwell law g(t)=(1+t**2)**(-3/2), of mean one.
# This is not the Lomax law: tail coefficient c=1/2, beta=2.
y=np.zeros(N)
for j in range(32):
    u=rng.random(N)
    t=u/np.sqrt(1-u*u)
    sign=1 if j%2==0 else -1
    y=sign+(y-sign)*np.exp(-t)
gap=1-y
assert np.all((gap>0)&(gap<=2))
H=lambda x:1/(np.sqrt(1+np.maximum(x,0)**2)+np.maximum(x,0))
u=rng.random(N)
age=(1-u*u)/(2*u)
side=rng.integers(0,2,N)
y_stationary=np.where(side==1,1-gap*np.exp(-age),-1+gap*np.exp(-age))
for eps in (0.15,0.025):
    L=np.log(1/eps)
    expected=np.mean(H(L+np.log(gap))+1-H(np.log(gap/(2-eps))))/2
    empirical=np.mean(y_stationary>1-eps)
    assert abs(expected-empirical)<6*np.sqrt(expected*(1-expected)/N)+0.001
    checks+=1
for L in (400,1200):
    pplus=np.mean(H(L+np.log(gap)))/2
    assert abs(pplus/(1/(4*L))-1)<0.03
    checks+=1
print('half-t beta=2 checks passed, leading coefficient 1/4')
print(f'ALL PASS: {checks} numerical comparisons including the half-t law.')
