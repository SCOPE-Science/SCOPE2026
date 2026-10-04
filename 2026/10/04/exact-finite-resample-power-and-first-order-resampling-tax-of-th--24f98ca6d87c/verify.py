#!/usr/bin/env python3
import math
from statistics import NormalDist
from fractions import Fraction

ND = NormalDist()
SQRT2 = math.sqrt(2.0)

def phi(x):
    return math.exp(-0.5*x*x)/math.sqrt(2.0*math.pi)

def Phi(x):
    return 0.5*(1.0+math.erf(x/SQRT2))

def gauss_legendre(n, a, b):
    # Nodes and weights from Newton iteration for Legendre roots.
    out=[]
    m=(n+1)//2
    xm=0.5*(b+a); xl=0.5*(b-a)
    for i in range(1,m+1):
        z=math.cos(math.pi*(i-0.25)/(n+0.5))
        while True:
            p1=1.0; p2=0.0
            for j in range(1,n+1):
                p3=p2; p2=p1
                p1=((2*j-1)*z*p2-(j-1)*p3)/j
            pp=n*(z*p1-p2)/(z*z-1.0)
            z1=z; z=z1-p1/pp
            if abs(z-z1)<2e-15:
                break
        w=2.0/((1.0-z*z)*pp*pp)
        x1=xm-xl*z; x2=xm+xl*z
        out.append((x1,xl*w))
        if i != n+1-i:
            out.append((x2,xl*w))
    out.sort()
    return out

def binom_cdf_small(k, n, p):
    if k < 0: return 0.0
    if k >= n: return 1.0
    # Direct exact-combination summation is stable for the modest n used here.
    q=1.0-p
    s=0.0
    for j in range(k+1):
        s += math.comb(n,j)*(p**j)*(q**(n-j))
    return min(1.0,max(0.0,s))

def chi_pdf(r,n):
    if r <= 0.0: return 0.0
    return math.exp((n-1)*math.log(r)-0.5*r*r-(n/2-1)*math.log(2.0)-math.lgamma(n/2))

def reject_given_s(s,B,m):
    # Exceedance probability among null resamples.
    return binom_cdf_small(m-1,B,1.0-Phi(s))

def finite_power(n,delta,B,alpha,Nr=140,Nz=180):
    m=math.floor(alpha*(B+1)+1e-14)
    if m==0: return 0.0
    rs=gauss_legendre(Nr,0.0,max(12.0,math.sqrt(n)+9.0))
    zs=gauss_legendre(Nz,-9.0,9.0)
    den=math.sqrt(1.0+delta*delta)
    total=0.0
    for r,wr in rs:
        inner=0.0
        for z,wz in zs:
            s=(delta*r+z)/den
            inner += wz*phi(z)*reject_given_s(s,B,m)
        total += wr*chi_pdf(r,n)*inner
    return total

def ideal_power(n,delta,alpha,Nr=180):
    zcrit=ND.inv_cdf(1.0-alpha)
    rs=gauss_legendre(Nr,0.0,max(12.0,math.sqrt(n)+9.0))
    den=math.sqrt(1.0+delta*delta)
    return sum(w*chi_pdf(r,n)*Phi(delta*r-den*zcrit) for r,w in rs)

def local_power(h,B,alpha,N=300):
    m=math.floor(alpha*(B+1)+1e-14)
    zs=gauss_legendre(N,-9.0,9.0)
    return sum(w*phi(z)*reject_given_s(h+z,B,m) for z,w in zs)

def assert_close(got,want,tol,label):
    if abs(got-want)>tol:
        raise AssertionError(f'{label}: got {got:.15g}, want {want:.15g}')

alpha=0.05
# Null checks by exact integration after U=Phi(S), so U is uniform.
def null_size_via_beta(B,m):
    total=Fraction(0,1)
    den=math.factorial(B+1)
    for j in range(m):
        num=math.comb(B,j)*math.factorial(j)*math.factorial(B-j)
        total += Fraction(num,den)
    return total
for B in (19,39,99):
    m=math.floor(alpha*(B+1)+1e-14)
    got=null_size_via_beta(B,m)
    want=Fraction(m,B+1)
    if got != want:
        raise AssertionError(f'null B={B}: got {got}, want {want}')

# Finite-n alternative benchmarks.
finite_targets={19:0.551416415204657,39:0.592030337608717,99:0.618152822350510}
for B,want in finite_targets.items():
    assert_close(finite_power(20,0.5,B,alpha),want,6e-9,f'finite alt B={B}')
assert_close(ideal_power(20,0.5,alpha),0.635913252509805,2e-10,'finite ideal')

# Local fixed-B limits and infinite-resample endpoint.
h=2.0
local_targets={19:0.557989575306214,39:0.597144710336423,99:0.622003880745972,199:0.630384040740584}
vals={}
for B,want in local_targets.items():
    vals[B]=local_power(h,B,alpha)
    assert_close(vals[B],want,3e-10,f'local B={B}')
zcrit=ND.inv_cdf(1.0-alpha)
inf=Phi(h-zcrit)
assert_close(inf,0.638760031312335,2e-14,'local ideal')
coef=-alpha*(1-alpha)*h*math.exp(h*zcrit-h*h/2.0)/(2.0*phi(zcrit))
assert_close(coef,-1.672621148903737,3e-13,'coefficient')
scaled99=(vals[99]-inf)*(99+2)
scaled199=(vals[199]-inf)*(199+2)
if not abs(scaled199-coef) < abs(scaled99-coef):
    raise AssertionError('scaled gap did not move toward coefficient')
if abs(scaled199-coef) > 0.02:
    raise AssertionError('scaled gap too far from coefficient')
print('VERIFY_OK')
