#!/usr/bin/env python3
"""Independent standard-library numerical checks of the stated Gaussian integrals.
Analytic bounds are proved in RESULT.md; this numerical test does not certify them."""
import math

def gauss_logmax(w,n=24000):
    # Density for max sqrt(w_i)*abs(Z_i), evaluated with independent half-normal CDF.
    # Zero weights can be discarded; at least three positive weights used below.
    w=[x for x in w if x>0]
    tmax=9.0
    dt=tmax/n
    def densitylog(t):
        if t==0: return 0.0
        Fs=[math.erf(t/math.sqrt(2*x)) for x in w]
        fs=[math.sqrt(2/(math.pi*x))*math.exp(-t*t/(2*x)) for x in w]
        density=sum(fs[i]*math.prod(Fs[j] for j in range(len(w)) if j!=i) for i in range(len(w)))
        return math.log(t)*density
    s=densitylog(0)+densitylog(tmax)
    for j in range(1,n):
        s+=(4 if j%2 else 2)*densitylog(j*dt)
    return s*dt/3

w=[.49,.31,.20]
q=math.sqrt(w[0]*w[1]+w[1]*w[2]+w[2]*w[0])
for i in range(3):
    v=1e-4
    up=w.copy(); dn=w.copy();up[i]+=v;dn[i]-=v
    fd=(gauss_logmax(up)-gauss_logmax(dn))/(2*v)
    expected=math.atan(w[i]/q)/(math.pi*w[i])
    assert abs(fd-expected)<2e-4,(i,fd,expected)

b0=(1/3,1/3,1/3,0)
b1=(8/25,8/25,8/25,1/25)
observed=gauss_logmax(b1)-gauss_logmax(b0)
bound=.5*math.log(24/25)+1/(6*math.sqrt(2)*math.pi**2)
assert bound<0 and observed<bound,(observed,bound)
assert all(sum(sorted(b0,reverse=True)[:k])>=sum(sorted(b1,reverse=True)[:k])-1e-14 for k in range(1,4))
print('VERIFY_OK, four-axis Gaussian log difference',round(observed,10),'analytic upper bound',round(bound,10))
