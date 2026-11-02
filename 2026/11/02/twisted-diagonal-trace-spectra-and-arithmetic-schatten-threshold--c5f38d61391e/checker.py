"""Finite reproducibility checks for twisted-diagonal trace spectra.
Uses only Python's standard library. Infinite conclusions require the proof.
"""
import math
import cmath
from fractions import Fraction

def poch_ratio(r,n):
    return math.exp(math.lgamma(r+n)-math.lgamma(r)-math.lgamma(n+1))

def gegenbauer(r,theta,N):
    c=math.cos(theta)
    out=[1.0]
    if N>=1: out.append(2*r*c)
    for n in range(1,N):
        out.append((2*(n+r)*c*out[-1]-(n+2*r-1)*out[-2])/(n+1))
    return out

def eigenvalues(r,theta,N):
    cs=gegenbauer(r,theta,N)
    return [0.5*(1+cs[n]/poch_ratio(2*r,n)) for n in range(N+1)]

def direct_row(r,theta,n):
    zeta=cmath.exp(1j*theta)
    row=0.0
    for j in range((n+1)//2):
        k=n-j
        amp=math.sqrt(poch_ratio(r,j)*poch_ratio(r,k)/2)*(zeta**j+zeta**k)
        row+=abs(amp)**2
    if n%2==0:
        j=n//2
        amp=poch_ratio(r,j)*zeta**j
        row+=abs(amp)**2
    return row/poch_ratio(2*r,n)

checks=0
for r in (0.5,1.0,2.0,3.5):
  for theta in (0.0,0.39,math.pi/2,2*math.pi/3,math.pi):
    v=eigenvalues(r,theta,20)
    for n,x in enumerate(v):
      y=direct_row(r,theta,n)
      assert abs(x-y)<1e-8,(r,theta,n,x,y)
      assert -1e-8<x<1+1e-8
      checks+=2
    if theta==0:
      assert max(abs(x-1) for x in v)<1e-8; checks+=1
    if theta==math.pi:
      assert max(abs(x-(n%2==0)) for n,x in enumerate(v))<1e-8; checks+=1

# Exact rational check at right-angle twisted slice and integral exponent r=2.
def c_int(r,n): return math.comb(r+n-1,n)
for n in range(70):
    C=Fraction(0) if n%2 else Fraction((-1)**(n//2)*c_int(2,n//2))
    u=C/Fraction(c_int(4,n))
    lam=(Fraction(1)+u)/2
    assert lam>=0 and lam<=1
    checks+=1
    if n<21:
        assert abs(float(lam)-eigenvalues(2,math.pi/2,20)[n])<1e-12
        checks+=1

# Check the exact Hardy identity C_n^(1)(cos theta)=sin((n+1)theta)/sin(theta).
for theta in (0.2,0.6,math.pi/2,2*math.pi/3):
    v=eigenvalues(1,theta,100)
    for n,x in enumerate(v):
        y=0.5*(1+math.sin((n+1)*theta)/((n+1)*math.sin(theta)))
        assert abs(x-y)<2e-11
        checks+=1

# Critical asymptotic rank constants: theta=pi/2 has a closed exact subsequence.
# r=1, delta_(2j)=(-1)^j/[2(2j+1)] and delta_(2j+1)=0.
for j in range(1,100):
    lam=eigenvalues(1,math.pi/2,2*j)[2*j]
    assert abs(abs(lam-0.5)-1/(2*(2*j+1)))<1e-12
    checks+=1

# Verify the leading Gegenbauer Darboux coefficient at fixed theta with integer r.
r=2.0; theta=0.7
v=eigenvalues(r,theta,1000)
beta=math.gamma(2*r)/(math.gamma(r)*(2*math.sin(theta))**r)
for n in (200,400,700,1000):
    predicted=beta*n**(-r)*math.cos((n+r)*theta-r*math.pi/2)
    observed=v[n]-0.5
    assert abs(observed-predicted) < 0.1*n**(-r), (n,observed,predicted)
    checks+=1

print('PASS:',checks,'finite checks; analytic proof required for infinite claims')
