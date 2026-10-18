#!/usr/bin/env python3
"""Numerical checks for the stated autocorrelation, spectrum and critical fiber identities."""
import cmath, math, random
R = random.Random(20260428)

def coeffs(a,b):
    n=len(a)-1
    return a+[0j]*(n-1)+[b]

def lag(x,k):
    return sum(x[j+k]*x[j].conjugate() for j in range(len(x)-k))

def check(a,b):
    n=len(a)-1
    x=coeffs(a,b)
    measured=[lag(x,k) for k in range(2*n+1)]
    low=[(measured[2*n-j]/b).conjugate() for j in range(n)]
    assert max(abs(low[j]-a[j]) for j in range(n))<1e-10
    for k in range(1,n):
      core=sum(a[j+k]*a[j].conjugate() for j in range(n-k))
      assert abs(measured[k]-core-a[n]*a[n-k].conjugate())<1e-10
    assert abs(measured[n]-a[n]*a[0].conjugate()-b*a[n].conjugate())<1e-10
    m=4*n+1
    vals=[abs(sum(x[j]*cmath.exp(2j*math.pi*j*l/m) for j in range(2*n+1)))**2 for l in range(m)]
    rec=[sum(vals[l]*cmath.exp(-2j*math.pi*k*l/m) for l in range(m))/m for k in range(2*n+1)]
    assert max(abs(rec[k]-measured[k]) for k in range(2*n+1))<5e-9
    s=sum(abs(t)**2 for t in a[1:-1])
    A=a[0].conjugate(); B=b
    # Two columns for real coordinates of z=x+iy: (A+B), 1j*(A-B)
    columns=[]
    for z in (1,1j):
        t=[a[n-k].conjugate()*z for k in range(1,n)] + [A*z+B*z.conjugate()]
        columns.append([q for v in t for q in (v.real,v.imag)])
    v,w=columns
    g11=sum(t*t for t in v)
    g22=sum(t*t for t in w)
    g12=sum(x*y for x,y in zip(v,w))
    disc=math.sqrt((g11-g22)**2+4*g12*g12)
    sv=sorted([math.sqrt(max(0,(g11+g22-disc)/2)),math.sqrt(max(0,(g11+g22+disc)/2))])
    want=sorted([math.sqrt(s+(abs(A)-abs(B))**2),math.sqrt(s+(abs(A)+abs(B))**2)])
    assert max(abs(u*u-v*v) for u,v in zip(sv,want))<1e-9

N=0
for n in range(1,24):
  for _ in range(60):
    a=[complex(R.uniform(-1.8,1.8),R.uniform(-1.8,1.8)) for j in range(n+1)]
    b=complex(R.uniform(.4,2),R.uniform(-1,1))
    check(a,b); N+=1
for n in range(1,24):
  for _ in range(35):
    a0=R.uniform(.25,2)*cmath.exp(1j*R.uniform(-math.pi,math.pi))
    b=abs(a0)*cmath.exp(1j*R.uniform(-math.pi,math.pi))
    a=[a0]+[0j]*(n-1)+[complex(R.uniform(-1,1),R.uniform(-1,1))]
    check(a,b)
    z=a[-1]; w=(b/a0.conjugate())*z.conjugate()
    f,g=coeffs(a,b),coeffs(a[:-1]+[w],b)
    assert max(abs(lag(f,k)-lag(g,k)) for k in range(2*n+1))<1e-10
    assert abs(abs(w)-abs(z))<1e-10
    N+=1
print('PASS',N,'parameter cases; exact edge coefficients, finite Fourier sample inversion, real singular spectrum, and balanced two-fold fibers')
