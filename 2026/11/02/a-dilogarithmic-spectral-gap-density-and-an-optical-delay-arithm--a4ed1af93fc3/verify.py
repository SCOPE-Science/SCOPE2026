"""Standalone finite diagnostics for the frequency-gap density of a binary nondispersive wave crystal.
Proof of infinite-frequency limits is analytic in RESULT.md; this program is not an infinite certificate.
Run: python verify.py (requires Python 3 and mpmath; numpy optional).
"""
import math
import mpmath as mp
mp.mp.dps=45

def gap_general(eta):
    k=abs(eta-1)/(eta+1)
    return float(4/mp.pi**2*(mp.polylog(2,k)-mp.polylog(2,-k)))

def gap_equal(eta):
    return 2/math.pi*math.asin(abs(eta-1)/(eta+1))

def bloch_halftrace(omega, tau1, tau2, eta):
    a,b=omega*tau1,omega*tau2
    m=0.5*(eta+1/eta)
    return math.cos(a)*math.cos(b)-m*math.sin(a)*math.sin(b)

def matrix_trace(omega,tau1,tau2,eta):
    def mat(tau,imp):
        x=omega*tau
        c,s=math.cos(x),math.sin(x)
        return ((c,s/(omega*imp)),(-omega*imp*s,c))
    P,Q=mat(tau1,eta),mat(tau2,1.)
    return 0.5*(P[0][0]*Q[0][0]+P[0][1]*Q[1][0]+P[1][0]*Q[0][1]+P[1][1]*Q[1][1])

def quadrature(eta):
    k=abs(eta-1)/(eta+1)
    f=lambda t: mp.asin(k*mp.sin(t))
    return float((8/mp.pi**2)*mp.quad(f,[0,mp.pi/2]))

def torus_fraction(eta,N=1800):
    m=0.5*(eta+1/eta)
    A=(m+1)/2; B=(m-1)/2
    # 1D quadrature of the exact angular measure, independent of polylogs.
    s=0.
    for j in range(N):
        v=2*math.pi*(j+0.5)/N
        T=(1+B*math.cos(v))/A
        T=min(1.,max(-1.,T))
        s+=math.acos(T)
    return (2/math.pi)*s/N

def direct_fraction(eta,tau1,tau2,maxfrequency=50000.,step=.045):
    n=int(maxfrequency/step)
    bad=0
    for j in range(n):
        w=(j+.5)*maxfrequency/n
        bad+=abs(bloch_halftrace(w,tau1,tau2,eta))>1
    return bad/n

def test():
    count=0
    for eta in (1.05,1.2,2.,4.,10.,100.):
        G=gap_general(eta); E=gap_equal(eta)
        assert 0<E<G<1,(eta,E,G);count+=1
        assert abs(G-quadrature(eta))<1e-12;count+=1
        assert abs(G-torus_fraction(eta))<2e-6,(eta,G,torus_fraction(eta));count+=1
        assert abs(gap_general(1/eta)-G)<1e-12;count+=1
        for tau in (0.2,0.6180339887,math.sqrt(2)):
            for w in (.13,3.41,31.7):
                f=bloch_halftrace(w,tau,1.,eta)
                g=matrix_trace(w,tau,1.,eta)
                assert abs(f-g)<2e-11,(eta,w,tau,f,g)
                count+=1
    for eta in (1.2,2.,5.):
        direct=direct_fraction(eta,math.sqrt(2),1.,maxfrequency=35000.,step=.055)
        assert abs(direct-gap_general(eta))<0.004,(eta,direct,gap_general(eta))
        count+=1
        eq_direct=direct_fraction(eta,1.,1.,maxfrequency=2000.,step=.05)
        assert abs(eq_direct-gap_equal(eta))<0.002,(eta,eq_direct,gap_equal(eta))
        count+=1
    for k in (1e-3,5e-3):
        eta=(1+k)/(1-k)
        ratio=gap_general(eta)/gap_equal(eta)
        assert abs(ratio-4/math.pi)<0.0001,(k,ratio)
        count+=1
    for k in (.999,.9999):
        eta=(1+k)/(1-k)
        G=gap_general(eta)
        approx=(4/math.pi**2)*(1-k)*(1+math.log(2/(1-k)))
        assert abs((1-G)/approx-1)<0.005,(k,1-G,approx)
        count+=1
    print('PASS',count,'diagnostic assertions')
    print('eta=2 irr=',gap_general(2.),'equal=',gap_equal(2.),'delt=',gap_general(2.)-gap_equal(2.))

if __name__=='__main__':test()
