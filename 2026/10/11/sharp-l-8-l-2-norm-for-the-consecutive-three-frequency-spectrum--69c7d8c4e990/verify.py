#!/usr/bin/env python3
from fractions import Fraction
from math import factorial
import cmath, math, random

# Sparse polynomials in variables (a,b,c), represented by exponent triples.
def add(P,Q):
    R=dict(P)
    for m,v in Q.items():
        R[m]=R.get(m,0)+v
        if R[m]==0: del R[m]
    return R

def mul(P,Q):
    R={}
    for (i,j,k),u in P.items():
        for (r,s,t),v in Q.items():
            m=(i+r,j+s,k+t)
            R[m]=R.get(m,0)+u*v
    return {m:v for m,v in R.items() if v}

def scale(P,c): return {m:c*v for m,v in P.items() if c*v}

def sq(P): return mul(P,P)

def coeffs_F4():
    ds=[]
    # coefficient of z^k in (a+b z+c z^2)^4
    for k in range(9):
        P={}
        for nc in range(5):
            for nb in range(5-nc):
                na=4-nb-nc
                if nb+2*nc==k:
                    coef=factorial(4)//(factorial(na)*factorial(nb)*factorial(nc))
                    P[(na,nb,nc)]=coef
        ds.append(P)
    return ds

def ABR_to_abc(i,j,k):
    # (a^2+c^2)^i (b^2)^j (ac)^k
    P={(0,0,0):1}
    A={(2,0,0):1,(0,0,2):1}
    B={(0,2,0):1}
    R={(1,0,1):1}
    for _ in range(i): P=mul(P,A)
    for _ in range(j): P=mul(P,B)
    for _ in range(k): P=mul(P,R)
    return P

ds=coeffs_F4()
N={}
for d in ds: N=add(N,sq(d))
terms=[
(4,0,0,1),(3,1,0,16),(2,2,0,36),(1,3,0,16),(0,4,0,1),
(2,1,1,48),(2,0,2,12),(1,2,1,96),(1,1,2,96),
(0,3,1,24),(0,2,2,84),(0,1,3,48),(0,0,4,6)]
RHS={}
for i,j,k,coef in terms: RHS=add(RHS,scale(ABR_to_abc(i,j,k),coef))
assert N==RHS

# Univariate integer-polynomial helpers, ascending coefficients.
def padd(p,q):
    n=max(len(p),len(q)); r=[0]*n
    for i in range(n): r[i]=(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0)
    while len(r)>1 and r[-1]==0:r.pop()
    return r

def pmul(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): r[i+j]+=a*b
    while len(r)>1 and r[-1]==0:r.pop()
    return r

def pscale(p,c): return [c*x for x in p]
def pder(p): return [i*p[i] for i in range(1,len(p))] or [0]
def ppow(p,n):
    r=[1]
    for _ in range(n): r=pmul(r,p)
    return r

num=[1,56,420,560,70]
den=ppow([1,2],4)
lhs=padd(pmul(pder(num),den),pscale(pmul(num,pder(den)),-1))
h=[-2,-21,0,35]
rhs=pscale(pmul(h,ppow([1,2],3)),-24)
assert lhs==rhs

# Resultant certificate is checked by exact substitution in the quotient Q[t]/(35t^3-21t-2).
# Reduce rational polynomials after clearing denominators.
def reduce_h(p):
    p=[Fraction(x) for x in p]
    while len(p)>3:
        d=len(p)-1; lead=p[-1]; p.pop()
        # t^3=(21 t+2)/35
        shift=d-3
        while len(p)<shift+2: p.append(Fraction(0))
        p[shift]+=lead*Fraction(2,35)
        p[shift+1]+=lead*Fraction(21,35)
    while len(p)<3:p.append(Fraction(0))
    return p

# X=Psi(t), check 1331 X^3+403851 X^2-4842915 X-13488475=0 in quotient field.
# Represent rationals as numerator polynomials; verify after multiplying by den^3.
Npoly=num; Dpoly=den
cert=padd(
    padd(pscale(ppow(Npoly,3),1331), pscale(pmul(ppow(Npoly,2),Dpoly),403851)),
    padd(pscale(pmul(Npoly,ppow(Dpoly,2)),-4842915), pscale(ppow(Dpoly,3),-13488475))
)
assert reduce_h(cert)==[Fraction(0),Fraction(0),Fraction(0)]

# Root isolation and numerical values.
def hfun(x): return 35*x*x*x-21*x-2
lo,hi=0.8,0.9
assert hfun(lo)<0<hfun(hi)
for _ in range(120):
    mid=(lo+hi)/2
    if hfun(mid)<0: lo=mid
    else: hi=mid
tau=(lo+hi)/2
assert 0.8184256021542925 < tau < 0.8184256021542930

def psi(t): return (70*t**4+560*t**3+420*t**2+56*t+1)/(1+2*t)**4
K8pow=psi(tau); K=K8pow**(1/8)
assert abs(K8pow-13.787723967226097)<2e-14
assert abs(K-1.3881505596661324)<2e-15
# Check value polynomial numerically as an additional transcription test.
assert abs(1331*K8pow**3+403851*K8pow**2-4842915*K8pow-13488475)<2e-5

# Direct deterministic moment ratio stress tests, not used for the proof.
def conv(p,q):
    r=[0j]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q): r[i+j]+=x*y
    return r

def ratio(a,b,c):
    q=[a,b,c]
    q2=conv(q,q); q4=conv(q2,q2)
    moment=sum(abs(x)**2 for x in q4)
    S=abs(a)**2+abs(b)**2+abs(c)**2
    return moment/(S**4)

# Exact-form extremizer numerically.
r=math.sqrt(tau)
w=ratio(r,1.0,r)
assert abs(w-K8pow)<2e-13
# A phase-resonant modulation preserves equality.
beta=0.731
w2=ratio(r,cmath.exp(1j*beta),r*cmath.exp(2j*beta))
assert abs(w2-K8pow)<2e-13

rng=random.Random(20261006)
mx=0.0
for _ in range(600):
    v=[]
    for __ in range(3):
        rad=10**rng.uniform(-1.5,1.5)
        ang=rng.uniform(-math.pi,math.pi)
        v.append(rad*cmath.exp(1j*ang))
    rr=ratio(*v); mx=max(mx,rr)
    assert rr <= K8pow+2e-11

print(f"VERIFY_OK tau={tau:.16f} K8pow={K8pow:.15f} K={K:.16f} stress_max={mx:.12f}")
