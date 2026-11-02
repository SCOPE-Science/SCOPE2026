"""Reproduce finite checks for the stationary covariance of a damped oscillator
with exponentially correlated unit-variance propulsion. Python 3 standard library.
The infinite-parameter threshold follows from the written proof, not these tests.
Run: python3 checker.py
"""
from math import sin,cos,exp,sqrt,pi,log,isclose
from random import Random

checks=0

def test(cond,msg):
    global checks
    if not cond: raise AssertionError(msg)
    checks+=1

def cov_closed(t,b,w,q,a=1.0):
    assert 0<b<w and q>0 and a!=0 and t>=0
    o=sqrt(w*w-b*b)
    M=w*w+2*b*q+q*q
    H=w*w+q*q-2*b*q
    K=a*a/(M*H)
    AA=q*(w*w+q*q-4*b*b)/(2*b*w*w)
    BB=q*(3*w*w+q*q-4*b*b)/(2*w*w*o)
    return K*(exp(-q*t)+exp(-b*t)*(AA*cos(o*t)+BB*sin(o*t)))

def rhs(vec,b,w,q,a):
    x,y,z=vec
    return (y,-w*w*x-2*b*y+a*z,-q*z)

def rk4_step(vec,dt,b,w,q,a):
    k1=rhs(vec,b,w,q,a)
    k2=rhs(tuple(vec[i]+dt*k1[i]/2 for i in range(3)),b,w,q,a)
    k3=rhs(tuple(vec[i]+dt*k2[i]/2 for i in range(3)),b,w,q,a)
    k4=rhs(tuple(vec[i]+dt*k3[i] for i in range(3)),b,w,q,a)
    return tuple(vec[i]+dt*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6 for i in range(3))

def cov_rk(t,b,w,q,a=1.0):
    M=w*w+2*b*q+q*q
    initial=(a*a*(2*b+q)/(2*b*w*w*M),0.0,a/M)
    dt=t/max(1,int(t/0.004)+1)
    s=initial
    for _ in range(max(1,int(t/0.004)+1)):
        s=rk4_step(s,dt,b,w,q,a)
    return s[0]

rng=Random(1061024)
for i in range(120):
    w=0.7+1.5*rng.random()
    b=w*(0.08+0.87*rng.random())
    q=0.07+2.9*rng.random()
    a=0.3+1.4*rng.random()
    for t in (0.,.3,1.,2.4,5.1):
        direct=cov_rk(t,b,w,q,a)
        formula=cov_closed(t,b,w,q,a)
        test(abs(direct-formula)<=3e-9*max(1,abs(formula),abs(direct)),f'RK covariance mismatch {i} {t} {direct} {formula}')

for i in range(200):
    w=.7+1.3*rng.random()
    b=w*(.05+.94*rng.random())
    q=b*(.001+.999*rng.random())
    o=sqrt(w*w-b*b)
    # Frequency-space smoothing: the covariance at q is a positive convolution
    # of the strictly positive one at rate b. Its critical case has R/K<1.
    critical_ratio=sqrt(1+3*b*b/(w*w))/2
    test(0<critical_ratio<1,'critical positive envelope')
    for t in (0,.11,.7,3,8,16):
        test(cov_closed(t,b,w,q)>0,f'nonpositive sample below threshold {i} {t}')

# A simple exact-sign witness at beta=1/2, omega_0=1, q=1:
# C(2pi/sqrt(3)) = (a^2/3)(e^{-2pi/sqrt(3)} - e^{-pi/sqrt(3)}) < 0.
t0=2*pi/sqrt(3)
explicit=(exp(-t0)-exp(-t0/2))/3
test(explicit<0,'exact witness sign')
test(abs(cov_closed(t0,.5,1,1)-explicit)<1e-13,'exact witness formula')

# Long-lag sign bands, certified analytically by the nonvanishing sinusoid.
for b,w,q in ((.5,1.,1.),(.3,1.,.8),(.9,1.,1.3)):
    o=sqrt(w*w-b*b)
    M=w*w+2*b*q+q*q
    H=w*w+q*q-2*b*q
    A=q*(w*w+q*q-4*b*b)/(2*b*w*w)
    B=q*(3*w*w+q*q-4*b*b)/(2*w*w*o)
    R=sqrt(A*A+B*B)
    test(R>0,'oscillatory coefficient nonzero')
    # Choose a cosine phase with the oscillatory term -R.
    import math
    phi=math.atan2(B,A)
    n=max(8,int((log(2/R)/(q-b)+phi-pi)*o/(2*pi))+2)
    t=(phi+pi+2*pi*n)/o
    test(cov_closed(t,b,w,q)<0,'late negative lobe')

# Near-critical first-negative-lag envelope; theorem proves its sharp limit.
b,w=.5,1.
lim=log(2/sqrt(1+3*b*b/(w*w)))
test(lim>0,'positive onset constant')
for delta in (0.01,0.003,0.001):
    q=b+delta
    o=sqrt(w*w-b*b)
    A=q*(w*w+q*q-4*b*b)/(2*b*w*w)
    B=q*(3*w*w+q*q-4*b*b)/(2*w*w*o)
    R=sqrt(A*A+B*B)
    threshold=log(1/R)/delta
    test(threshold>0,'positive envelope threshold')
    test(abs(delta*threshold-lim)<.035,'onset scaling check')

print(f'PASS: {checks} standalone finite diagnostics; analytic proof required for the infinite claims.')
