"""Independent finite Fourier and exact rational checks for p-adic radial covariance."""
import math, cmath, random
from fractions import Fraction

def analytic(p,r,theta,eps,a,m):
    z=r*cmath.exp(1j*theta)
    c0=(1-r)/(1-r/p)
    c=(1-z)/(1-z/p)
    return a*p**(-m)*r**(m-1)*(c0+eps*(c*cmath.exp(1j*(m-1)*theta)).real)

def finite_fourier(p,n,r,theta,eps,a,m):
    N=p**n
    f=[]
    for x in range(N):
        if x==0: f.append(1.)
        else:
            k=0;y=x
            while y%p==0:
                k+=1;y//=p
            f.append(1-a*r**k*(1+eps*math.cos(k*theta)))
    freq=p**(n-m)
    value=sum(f[x]*cmath.exp(-2j*math.pi*freq*x/N) for x in range(N))/N
    return value

def finite_formula(p,n,r,theta,eps,a,m):
    z=r*cmath.exp(1j*theta)
    rem=a*(1-1/p)*p**(-n)*(r**n/(1-r/p)+eps*(z**n/(1-z/p)).real)
    return analytic(p,r,theta,eps,a,m)+rem

maxerr=0.0;count=0
for p in (2,3,5):
 for n in (2,3,4):
  if p**n>625:continue
  for r,th,eps,a in ((.6,2*math.pi/3,.7,.5),(.38,math.pi/math.sqrt(2),.4,.3),(.82,math.pi,.2,.5),(.23,.321,.97,.13)):
   for m in range(1,n+1):
    d=finite_fourier(p,n,r,th,eps,a,m)
    e=finite_formula(p,n,r,th,eps,a,m)
    err=abs(d-e)
    maxerr=max(maxerr,err)
    assert err < 2e-11,(p,n,r,th,m,d,e,err)
    count+=1

# Exact rational certificate at the threefold angular resonance.
p=2; r=Fraction(3,5); eps=Fraction(7,10); a=Fraction(1,2)
C0=(1-r)/(1-r/p)
# Re[(1-z)/(1-z/p) * exp(2 pi i k/3)] for k = 0,1,2.
re_parts=[Fraction(163,139),Fraction(-59,139),Fraction(-104,139)]
assert C0==Fraction(4,7)
assert min(C0+eps*x for x in re_parts)==Fraction(232,4865)
assert C0/(-min(re_parts))==Fraction(139,182)
def f(k):
    cosine=(Fraction(1),Fraction(-1,2),Fraction(-1,2))[k%3]
    return 1-a*r**k*(1+eps*cosine)
assert [f(k) for k in range(4)]==[
    Fraction(3,20), Fraction(161,200), Fraction(883,1000), Fraction(2041,2500)]
assert f(3)-f(2)==-Fraction(333,5000)
print('PASS',count,'finite group Fourier comparisons; max error',maxerr)
print('PASS exact rational threefold resonance and nonmonotone covariance')
