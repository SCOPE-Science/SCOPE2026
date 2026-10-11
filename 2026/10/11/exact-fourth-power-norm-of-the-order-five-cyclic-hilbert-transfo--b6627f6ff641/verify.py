#!/usr/bin/env python3
import cmath, math, random

# Integer polynomials use ascending coefficients.
def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def add(a,b):
    n=max(len(a),len(b)); c=[0]*n
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return trim(c)

def sub(a,b):
    n=max(len(a),len(b)); c=[0]*n
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]-=x
    return trim(c)

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)

def scale(a,s): return trim([s*x for x in a])
def power(a,n):
    r=[1]; b=a[:]
    while n:
        if n&1: r=mul(r,b)
        b=mul(b,b); n//=2
    return r

def deriv(a): return trim([i*a[i] for i in range(1,len(a))] or [0])
def divmod_poly(a,b):
    a=trim(a); b=trim(b); q=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and a!=[0]:
        if a[-1] % b[-1] != 0: raise AssertionError('nonexact leading division')
        k=len(a)-len(b); c=a[-1]//b[-1]; q[k]=c
        a=sub(a,[0]*k+scale(b,c))
    return trim(q),trim(a)

def peval(a,x):
    y=0
    for c in reversed(a): y=y*x+c
    return y

N=[3,-4,12,4,3]
D=[3,-4,12,-4,3]
g=[-9,8,-12,0,3]
left=sub(mul(deriv(N),D),mul(N,deriv(D)))
right=mul([0,0,-8],g)
assert left==right, (left,right)

# P(N/D) D^4, with P(X)=3185X^4-17948X^3+42750X^2-47500X+15625.
E=add(add(add(add(scale(power(N,4),3185),scale(mul(power(N,3),D),-17948)),scale(mul(power(N,2),power(D,2)),42750)),scale(mul(N,power(D,3)),-47500)),scale(power(D,4),15625))
q,rem=divmod_poly(E,power(g,2))
assert rem==[0] and q!=[0]

def gf(x): return 3*x**4-12*x**2+8*x-9
lo,hi=1.85,1.86
assert gf(lo)<0<gf(hi)
for _ in range(100):
    mid=(lo+hi)/2
    if gf(mid)<0: lo=mid
    else: hi=mid
t=(lo+hi)/2

def R(x):
    return (3*x**4+4*x**3+12*x**2-4*x+3)/(3*x**4-4*x**3+12*x**2-4*x+3)
X=R(t); K=X**0.25
assert 2.08968<X<2.08970
P=3185*X**4-17948*X**3+42750*X**2-47500*X+15625
assert abs(P)<2e-10

# Fourier helpers with normalized forward transform and unnormalized inverse.
def inverse(h):
    n=len(h)
    return [sum(h[k]*cmath.exp(2j*math.pi*k*x/n) for k in range(n)) for x in range(n)]
def norm4(v): return sum(abs(z)**4 for z in v)/len(v)
def hilbert_hat(h):
    n=len(h); m=(n-1)//2; out=[0j]*n
    for k in range(1,m+1): out[k]=-1j*h[k]
    for k in range(m+1,n): out[k]=1j*h[k]
    return out

alpha=2*math.pi/5; beta=-math.pi/5
h=[0j, cmath.exp(1j*alpha), t*cmath.exp(1j*beta), t*cmath.exp(-1j*beta), cmath.exp(-1j*alpha)]
f=inverse(h); hf=inverse(hilbert_hat(h))
assert max(abs(z.imag) for z in f+hf)<2e-12
ratio=norm4(hf)/norm4(f)
assert abs(ratio-X)<2e-12

rng=random.Random(20261006)
max_excess=-1e9
moment_err=0.0
for _ in range(4000):
    r=10**rng.uniform(-1,1); s=10**rng.uniform(-1,1)
    a=rng.uniform(-math.pi,math.pi); b=rng.uniform(-math.pi,math.pi)
    hh=[0j,r*cmath.exp(1j*a),s*cmath.exp(1j*b),s*cmath.exp(-1j*b),r*cmath.exp(-1j*a)]
    ff=inverse(hh); hff=inverse(hilbert_hat(hh))
    C=6*r**4+24*r*r*s*s+6*s**4
    mf=C+8*r**3*s*math.cos(3*a+b)+8*r*s**3*math.cos(a-3*b)
    mh=C+8*r**3*s*math.cos(3*a+b)-8*r*s**3*math.cos(a-3*b)
    moment_err=max(moment_err,abs(norm4(ff)-mf),abs(norm4(hff)-mh))
    rr=norm4(hff)/norm4(ff)
    max_excess=max(max_excess,rr-X)
assert moment_err<1e-9
assert max_excess<1e-10

# C3: random conjugate Fourier pairs give exact numerical L4 isometry.
c3err=0.0
for _ in range(400):
    a=(rng.uniform(-2,2)+1j*rng.uniform(-2,2))
    hh=[0j,a,a.conjugate()]
    ff=inverse(hh); hff=inverse(hilbert_hat(hh))
    c3err=max(c3err,abs(norm4(ff)-norm4(hff)))
assert c3err<2e-10

print('VERIFY_OK derivative=exact elimination=exact t=%.17g X=%.17g K=%.17g moment_err=%.3e max_sample_excess=%.3e c3_err=%.3e' % (t,X,K,moment_err,max_excess,c3err))
