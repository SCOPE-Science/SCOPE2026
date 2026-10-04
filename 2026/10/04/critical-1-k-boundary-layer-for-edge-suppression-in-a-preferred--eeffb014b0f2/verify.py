#!/usr/bin/env python3
import cmath, math


def scatter_coeffs(k):
    den = k*k + 3.0
    s0 = (k*k - 1.0) / den
    s1 = 2.0*(k + 1.0) / den
    s2 = 2.0*(1.0 - k) / den
    return s0, s1, s2


def amplitudes(k, l2, theta):
    phi = k*l2
    q = cmath.exp(1j*(phi-theta))
    r = cmath.exp(-1j*(phi+theta))
    D = k*k*(q-r) + 2.0*k*(q*r-1.0) + (2.0*q*r-q-3.0*r+2.0)
    a = 2.0*(k+1.0)*(q-1.0)/D
    b = 2.0*(k-1.0)*(r-1.0)/D
    s0,s1,s2 = scatter_coeffs(k)
    d = s1*a + s2*b*q + s0
    return a,b,d,q,r


def norm2(A,B,k,L):
    cross = A*B.conjugate()*(1.0-cmath.exp(-2j*k*L))/(2j*k)
    return L*(abs(A)**2+abs(B)**2) + 2.0*cross.real


def critical_k(n,l2,xi):
    disc = (n*math.pi)**2 + 4.0*l2*xi
    assert disc > 0
    return (n*math.pi + math.sqrt(disc))/(2.0*l2)


def check_scattering(k,l2,theta):
    a,b,d,q,r = amplitudes(k,l2,theta)
    s0,s1,s2 = scatter_coeffs(k)
    vin = [a,b*q,1.0+0j]
    out = [
        s0*vin[0]+s1*vin[1]+s2*vin[2],
        s2*vin[0]+s0*vin[1]+s1*vin[2],
        s1*vin[0]+s2*vin[1]+s0*vin[2],
    ]
    target=[b,a*r,d]
    return max(abs(x-y) for x,y in zip(out,target))


def check_case(parity,theta,xi,l1,l2,ns):
    eps = 1 if parity==0 else -1
    denom = eps*xi - 2.0*math.sin(theta)
    assert abs(denom) > 0.15
    A = (eps-cmath.exp(1j*theta))/(1j*denom)
    limit_ratio=(l2/l1)*abs(A)**2
    errors=[]
    for n in ns:
        assert n%2==parity
        k=critical_k(n,l2,xi)
        a,b,d,q,r=amplitudes(k,l2,theta)
        assert check_scattering(k,l2,theta) < 2e-12
        ng=norm2(a,b,k,l2)
        nf=norm2(1.0+0j,d,k,l1)
        ratio=ng/nf
        amp_err=max(abs(a-A),abs(b-A),abs(d-1.0))
        errors.append((k,abs(ratio-limit_ratio),amp_err))
    # asymptotic errors should be small at the largest index and improve overall.
    assert errors[-1][1] < 0.02*max(1.0,abs(limit_ratio))
    assert errors[-1][2] < 0.03*max(1.0,abs(A))
    assert errors[-1][1] < errors[0][1]
    return limit_ratio, errors


def mesoscopic_k(n,l2,alpha):
    # Solve l2*k = n*pi + alpha/sqrt(k) by Newton iteration.
    k=n*math.pi/l2
    for _ in range(20):
        f=l2*k-n*math.pi-alpha/math.sqrt(k)
        fp=l2+0.5*alpha*k**(-1.5)
        k-=f/fp
    return k


def check_mesoscopic(theta,l1,l2,alpha,ns):
    ratios=[]
    for n in ns:
        k=mesoscopic_k(n,l2,alpha)
        a,b,d,q,r=amplitudes(k,l2,theta)
        ng=norm2(a,b,k,l2)
        nf=norm2(1.0+0j,d,k,l1)
        ratios.append(ng/nf)
    assert ratios[-1] < 0.2*ratios[0]
    assert ratios[-1] < 0.02
    return ratios


def main():
    c1=check_case(0,0.7,2.0,0.8,1.3,[20,40,80,160,320])
    c2=check_case(1,-0.5,1.8,1.1,0.9,[21,41,81,161,321])
    meso=check_mesoscopic(0.6,0.8,1.3,1.2,[20,40,80,160,320])
    print('critical-even limit_ratio',repr(c1[0]))
    print('critical-even errors',[(round(k,6),e1,e2) for k,e1,e2 in c1[1]])
    print('critical-odd limit_ratio',repr(c2[0]))
    print('critical-odd errors',[(round(k,6),e1,e2) for k,e1,e2 in c2[1]])
    print('mesoscopic ratios',meso)
    print('VERIFY_OK')

if __name__=='__main__':
    main()
