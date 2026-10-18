"""Independent finite-grid checks for sharp Jackson--Fejer derivative norms.

Requires numpy/scipy; run `python verify_jackson.py`.  This checks examples,
not the quantified asymptotic theorems, which have analytic proofs.
"""
from math import pi, sin, cos, tan, comb, factorial, sqrt
from fractions import Fraction
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import zeta
import numpy as np

checks=0

def check(condition, message):
    global checks
    if not condition: raise AssertionError(message)
    checks+=1

def F(n,t):
    if abs(t)<1e-12:return float(n)
    return sin(n*t/2)**2/(n*sin(t/2)**2)

def Fprime(n,t):
    if abs(t)<1e-8:
        return -(n*(n*n-1)/6)*t
    u=t/2
    return (sin(n*u)*cos(n*u)/sin(u)**2)-(sin(n*u)**2*cos(u)/(n*sin(u)**3))

def max_lobe(n,k):
    # k-th complete noncentral positive lobe, k>=1.
    L=k*pi/n; R=(k+1)*pi/n
    d=1e-10*(R-L)
    def eq(u):return n*cos(n*u)/sin(n*u)-cos(u)/sin(u)
    u=brentq(eq,L+d,R-d,xtol=1e-13)
    # stationary-value expression independent of F evaluation
    return n/(1+(n*n-1)*sin(u)**2), 2*u

def norm_exact(n,q):
    # Fourier coefficients of (1+...+z^{n-1})**q
    c=[1]
    for _ in range(q):
        cc=[0]*(len(c)+n-1)
        for k,a in enumerate(c):
            for j in range(n): cc[k+j]+=a
        c=cc
    Z=Fraction(sum(v*v for v in c),n**q)
    maxima=[max_lobe(n,k)[0] for k in range(1,(n-2)//2+1)]
    TVhalf=n**q+2*sum(x**q for x in maxima)+(n**(-q) if n%2 else 0)
    return TVhalf/(pi*float(Z)),Z,maxima

def direct_norm(n,q):
    # Independent integration by quadrature of |d/dt(F**q)|.
    def term(t):
        z=F(n,t)
        return q*(z**(q-1))*abs(Fprime(n,t))
    x=[0.0]
    for k in range(1,n//2+1):
        a=2*pi*k/n
        if a<pi:x.append(a)
    for k in range(1,(n-2)//2+1):x.append(max_lobe(n,k)[1])
    x.append(pi)
    x=sorted(set(x))
    num=2*sum(quad(term,x[i],x[i+1],epsabs=2e-11,epsrel=2e-11,limit=100)[0] for i in range(len(x)-1))
    den=2*quad(lambda t:F(n,t)**q,0,pi,epsabs=1e-10,epsrel=1e-10,limit=300)[0]
    return num/den

def D_ratio(q):
    s=sum((-1)**j*comb(2*q,j)*(q-j)**(2*q-1) for j in range(q))
    return Fraction(s,factorial(2*q-1)) # D_q/pi

def peaks(M):
    return [brentq(lambda t: sin(t)-t*cos(t), j*pi+1e-12,(j+.5)*pi-1e-8,xtol=2e-14) for j in range(1,M+1)]

# Finite exact mass via convolution, two independent norms and stationary roots.
for n in range(2,25):
    for q in range(1,5):
        v,Z,maxima=norm_exact(n,q)
        vd=direct_norm(n,q)
        check(abs(v-vd)<2e-8*max(1,v),f'integral mismatch n={n} q={q}: {v} {vd}')
        check(Z>0,f'bad mass n={n} q={q}')
        for k,mx in enumerate(maxima,1):
            check(0<mx<n/(4*k*k),f'envelope fail n={n} k={k}')

# Exact small-degree profiles.
check(abs(norm_exact(2,1)[0]-2/pi)<1e-13,'Fejer n=2')
check(abs(norm_exact(3,1)[0]-10/(3*pi))<1e-13,'Fejer n=3')
check(abs(norm_exact(2,2)[0]-8/(3*pi))<1e-13,'Jackson n=2 q=2')
for q in range(1,11):
    check(abs(norm_exact(2,q)[0]-4**q/(pi*comb(2*q,q)))<1e-11,
          f'exact two-node degree check q={q}')
check(D_ratio(1)==1,'sinc square integral')
check(D_ratio(2)==Fraction(2,3),'sinc fourth integral')
check(D_ratio(3)==Fraction(11,20),'sinc sixth integral')

rr=peaks(1000)
# Sum of remaining peak powers q>=2 < (2/pi^2)^q*int tail k^{-2q} bound.
for q in [1,2,3,4]:
    D=pi*float(D_ratio(q))
    S=sum((1+r*r)**(-q) for r in rr)
    tail= (1/(pi*pi*(1000+.5)**2))**q * (1000.5)/(2*q-1) # crude integral bound
    C=(1+2*S)/D
    # For q=1, the first three asymptotic inverse-even-power tail terms
    # are useful for reporting a precise decimal, but not for a proof.
    if q==1:
        M=1000
        correction=(zeta(2,M+1.5)/pi**2 + zeta(4,M+1.5)/pi**4
                    +4*zeta(6,M+1.5)/(3*pi**6))
        print('Fejer-q1-truncated+tail-estimate',format(C+2*correction/D,'.13f'))
    print('fixed-power',q,'D/pi=',D_ratio(q),'C_1000=',format(C,'.12f'),'certified-tail-bound <=',2*tail/D)
    for n in [15,40,100,200]:
        v=norm_exact(n,q)[0]
        # generous finite-n limit tolerance to show convergence.
        if n==200: check(abs(v/n-C)<0.003,f'fixed limit n={n},q={q}')
        print('  mesh',n,'L/n',format(v/n,'.12f'))

# Uniform simultaneous high-power/high-frequency Gaussian regime.
for n in [2,3,5,10,30,100]:
    for q in [10,20,40]:
        v=norm_exact(n,q)[0]
        pred=sqrt(q*(n*n-1)/(3*pi))
        check(abs(v/pred-1)<0.07,f'Gaussian scaling n={n},q={q},ratio={v/pred}')
        print('Gaussian',n,q,'ratio',format(v/pred,'.10f'))
print('checks_passed',checks)
