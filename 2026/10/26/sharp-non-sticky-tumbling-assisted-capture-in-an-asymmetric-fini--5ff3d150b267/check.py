"""Independent numerical tests for the two-boundary velocity-switching theorem.

Run: python3 check.py
Requires: numpy, scipy.
No internet access needed.
"""
import math
import numpy as np
from scipy.optimize import minimize_scalar

def mean_by_boundary_ode(A,B,x,y):
    # Solve the backward equations using boundary values, not the polynomial formula.
    c=(1/B + y/2)/(1/A + 1/B + y)
    return c/A + y*(c*x-x*x/2)

def data(A,B,x):
    S=A+B
    P=A*B
    Q=A*(2*x-x*x)+B*(1-x*x)
    R=P*x*(1-x)
    Delta=Q*S-2*P
    return S,P,Q,R,Delta

def mean_by_polynomial(A,B,x,y):
    S,P,Q,R,Delta=data(A,B,x)
    return (2+Q*y+R*y*y)/(2*(S+P*y))

def derivative_numerator(A,B,x,y):
    S,P,Q,R,Delta=data(A,B,x)
    return Delta+2*R*S*y+R*P*y*y

def optimizer(A,B,x):
    S,P,Q,R,D=data(A,B,x)
    if D>=0: return 0.0
    return (math.sqrt(S*S-D/(x*(1-x)))-S)/P

def montecarlo(A,B,x,y, n=30000, seed=23):
    rng=np.random.default_rng(seed)
    pos=np.full(n,x, dtype=float)
    dire=np.where(rng.random(n)<.5,1.0,-1.0)
    elapsed=np.zeros(n)
    live=np.ones(n,dtype=bool)
    eta0=2*A/(1+A); eta1=2*B/(1+B)
    flips=y/2  # per-direction reversal rate, velocity and length normalized to 1
    for k in range(100000):
        active=np.flatnonzero(live)
        if len(active)==0:break
        p=pos[active]; d=dire[active]
        wall_time=np.where(d>0,1-p,p)
        flip_time=rng.exponential(scale=1/flips,size=len(active)) if flips>0 else np.full(len(active),np.inf)
        t=np.minimum(wall_time,flip_time)
        elapsed[active]+=t
        pos[active]=p+d*t
        hit=wall_time<=flip_time
        ih=active[hit]
        if len(ih):
            # Collisions either permanently absorb or immediately specularly reflect.
            chances=np.where(d[hit]>0,eta1,eta0)
            absorbed=rng.random(len(ih))<chances
            live[ih[absorbed]]=False
            dire[ih[~absorbed]]*=-1
        iff=active[~hit]
        dire[iff]*=-1
    else: raise AssertionError('MC failed to finish')
    return float(np.mean(elapsed)), float(np.std(elapsed,ddof=1)/np.sqrt(n))

def main():
    rng=np.random.default_rng(28)
    cases=1500
    bvp_err=0.0
    derivative_err=0.0
    for _ in range(cases):
        A=float(rng.uniform(.03,1.)); B=float(rng.uniform(.03,1.))
        x=float(rng.uniform(.0005,.9995)); y=float(rng.uniform(0.,30.))
        a=mean_by_boundary_ode(A,B,x,y)
        b=mean_by_polynomial(A,B,x,y)
        bvp_err=max(bvp_err,abs(a-b))
        assert abs(a-b) <= 3e-11 * max(1,a)
        S,P,Q,R,D=data(A,B,x)
        h=1e-5
        dif=(mean_by_polynomial(A,B,x,y+h)-mean_by_polynomial(A,B,x,y-h))/(2*h)
        deriv=derivative_numerator(A,B,x,y)/(2*(S+P*y)**2)
        derivative_err=max(derivative_err,abs(dif-deriv))
        assert abs(dif-deriv)<1e-7*max(1,abs(deriv))
    optimization_cases=250
    for _ in range(optimization_cases):
        A=float(rng.uniform(.01,1.)); B=float(rng.uniform(.01,1.))
        x=float(rng.uniform(.015,.985))
        ystar=optimizer(A,B,x)
        assert derivative_numerator(A,B,x,max(0.01,ystar))>0 if ystar==0 else True
        umax=max(200.,ystar*3+40)
        opt=minimize_scalar(lambda z:mean_by_polynomial(A,B,x,z),method='bounded',bounds=(0.,umax),options={'xatol':1e-9})
        assert opt.success
        assert mean_by_polynomial(A,B,x,ystar) <= opt.fun+2e-9*max(1,opt.fun)
        if ystar>0:
            assert abs(derivative_numerator(A,B,x,ystar))<1e-6*max(1,ystar**2)
            assert mean_by_polynomial(A,B,x,ystar)<mean_by_polynomial(A,B,x,0)
    # Threshold and singular near-boundary exponent for A<B, x->1
    A=.4;B=1.0
    S=A+B
    xc=(A+math.sqrt(A*A-A*B+B*B))/S
    assert .8<xc<1
    assert optimizer(A,B,xc-1e-5)==0
    assert optimizer(A,B,xc+1e-5)>0
    amp=math.sqrt(B-A)/(B*math.sqrt(A))
    boundary_tests=[]
    for dist in [1e-3,1e-4,1e-5,1e-6]:
        ystar=optimizer(A,B,1-dist)
        ratio=ystar*math.sqrt(dist)/amp
        boundary_tests.append((dist,ystar,ratio))
        assert abs(ratio-1)<.11
    # Nontrivial interval: optimum beats ballistic despite zero residence at walls.
    A=.4;B=1.;x=.95
    ystar=optimizer(A,B,x)
    ballistic=mean_by_polynomial(A,B,x,0)
    best=mean_by_polynomial(A,B,x,ystar)
    assert 0<ystar<10 and best<ballistic
    for yy in [0,ystar,ystar*3]:
        mc,se=montecarlo(A,B,x,yy, n=30000,seed=29+int(100*yy))
        exact=mean_by_polynomial(A,B,x,yy)
        assert abs(mc-exact)<=6*se+0.01, (yy,mc,exact,se)
        print(f'MC y={yy:.6f} exact={exact:.7f} sample={mc:.7f} standard_error={se:.7f}')
    print(f'PASS {cases} independent BVP/algebra checks, max absolute error={bvp_err:.4g}')
    print(f'PASS {cases} derivative checks, max absolute error={derivative_err:.4g}')
    print(f'PASS {optimization_cases} independently numerically optimized parameters')
    print(f'PASS threshold x_c={xc:.9f} and near-boundary tests: {boundary_tests}')
    print(f'PASS witness A=.4 B=1 x=.95: alpha*L/v={ystar:.9f}, ballistic={ballistic:.9f}, best={best:.9f}')
if __name__=='__main__': main()
