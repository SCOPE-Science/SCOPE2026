"""Independent numerical checks of partial-reset diffusion fingerprints.
Dependencies: numpy, scipy, mpmath. Finite tests do not replace proofs.
"""
import math
import numpy as np
from scipy.integrate import quad
import mpmath as mp
mp.mp.dps=60
checks=0

def approx(got,want,tol=2e-6):
    global checks
    assert abs(float(got-want)) <= tol*max(1,abs(float(got)),abs(float(want))), (got,want)
    checks+=1

def positive(x):
    global checks
    assert x>0,x
    checks+=1

def phi_float(k,q):
    j=np.arange(0,120,dtype=float)
    return math.exp(-np.log1p((k*q**j)**2).sum())

def integral(n,q,x=0):
    fun=lambda k: k**(2*n)*math.cos(k*x)*phi_float(k,q)
    return sum(quad(fun,lo,hi,epsabs=2e-10,epsrel=5e-10,limit=100)[0] for lo,hi in zip([0,1,5,20,100,400,2000],[1,5,20,100,400,2000,30000]))/math.pi

def p(s,q):
    a=-mp.log(q)
    return a*s*(1-s)+mp.fsum(mp.log1p(mp.exp(-2*a*(s+j))) for j in range(150))+mp.fsum(mp.log1p(mp.exp(-2*a*(j-s))) for j in range(1,151))

def char_mp(k,q):
    out=mp.mpf(1)
    fac=mp.mpf(1)
    for j in range(400):
        u=(k*fac)**2
        out/=(1+u)
        if u<mp.mpf('1e-112'):break
        fac*=q
    return out

for q in (0.5,0.7):
    f0=integral(0,q)
    positive(f0)
    for n in range(1,4):
        target=f0*q**(-n*n)*np.prod([1-q**(2*j+1) for j in range(n)])
        approx(integral(n,q),target,5e-8)
    qmp=mp.mpf(str(q))
    for x in (0.15,0.5,1):
        # partial fraction solution, independent of the inversion integral
        terms=[(-1)**j*qmp**(j*j)*mp.exp(-mp.mpf(str(x))*qmp**(-j))/mp.fprod(1-qmp**(2*h) for h in range(1,j+1)) for j in range(40)]
        fseries=mp.fsum(terms)/(2*mp.qp(qmp**2,qmp**2))
        approx(integral(0,q,x),fseries,3e-8)

for qstr in ('0.2','0.4','0.7'):
    q=mp.mpf(qstr)
    a=-mp.log(q)
    amp=2*mp.fsum(1/(m*mp.sinh(mp.pi**2*m/a)) for m in range(1,20,2))
    approx(p(mp.mpf('0.5'),q)-p(0,q),amp,1e-30)
    positive(amp)
    approx(p(0,q),p(1,q),1e-30)
    for s in (mp.mpf(0),mp.mpf('.23'),mp.mpf('.77')):
        for n in (4,9,16):
            t=(n+s)*a
            remainder=mp.log(char_mp(mp.exp(t),q))+t*t/a+t+p(s,q)
            expected=mp.fsum(mp.log1p(mp.exp(-2*a*(s+m))) for m in range(n+1,151))
            # Avoid cancellation at extremely small remainder by modest precision floor
            approx(remainder,expected,1e-28)
            positive(remainder)
            assert remainder <= q*q*mp.exp(-2*t)/(1-q*q)*(1+mp.mpf('1e-25'))
            checks+=1
print(f'PASS: {checks} independently evaluated numerical assertions')
