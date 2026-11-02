"""Reproducible finite checks of the spectral resonance phase diagram.

Run: python3 verify.py. Uses only Python's standard library.
These checks illustrate the identities; the infinite-parameter theorem is proved in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt, isclose
from random import Random


def spectrum(s, u, z):
    c = 1 + s
    D = (c + z)**2 - 4*s*z
    return (c + z)/D + u/(4*u*u + z)


def coeffs(s, u):
    c, d = 1+s, 3*s-1
    return c+4*u, 4*u*d-16*u**3-2*c*(1-s), 16*u**3*d-c**3


def Fcrit(s):
    return 2**(2/3)*(3*s-1)**(2/3)-2*(1-s)-(1+s)**2/(3*s-1)


def u0(s):
    return ((1+s)**3/(16*(3*s-1)))**(1/3)


def bisect(f, lo, hi, steps=90):
    flo, fhi = f(lo), f(hi)
    assert flo < 0 < fhi, (lo, hi, flo, fhi)
    for _ in range(steps):
        mid = (lo+hi)/2
        if f(mid)>0:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2


def critical_u(s):
    if s<=1/3:
        return float('inf')
    r0 = u0(s)
    if Fcrit(s)<=0:
        return r0
    def disc(u):
        A,B,C=coeffs(s,u)
        return B*B+4*A*C
    # The tangency root with positive vertex is unique in (0,r0).
    lo = r0
    while True:
        lo *= .9
        if disc(lo)<0 and coeffs(s,lo)[1]>0:
            break
        assert lo>r0/10, 'bracketing failed'
    return bisect(disc, lo, r0)


def excess_sign_witness(s,u):
    if s<=1/3:
        return 0.0
    A,B,C=coeffs(s,u)
    d=3*s-1
    z=max(0.,min(d,B/(2*A)))
    return C+B*z-A*z*z


def eigenbasis_checks(kp,km,r):
    # 8-state chain with a 4-cycle and an independent binary jump process.
    states=[(j,y) for j in range(4) for y in range(2)]
    n=len(states)
    Q=[[F(0) for _ in range(n)] for _ in range(n)]
    for i,(j,y) in enumerate(states):
        for j2,y2,rate in [((j+1)%4,y,kp),((j-1)%4,y,km),(j,1-y,r)]:
            Q[i][states.index((j2,y2))]+=rate
            Q[i][i]-=rate
    assert all(sum(row)==0 for row in Q)
    assert all(sum(Q[i][j] for i in range(n))==0 for j in range(n))
    fx=[F([-1,0,1,0][j]) for j,y in states]
    gx=[F([0,1,0,-1][j]) for j,y in states]
    fy=[F(y)-F(1,2) for j,y in states]
    def act(f): return [sum(Q[i][j]*f[j] for j in range(n)) for i in range(n)]
    a,b=kp+km,kp-km
    assert act(fx)==[-a*fx[i]+b*gx[i] for i in range(n)]
    assert act(gx)==[-b*fx[i]-a*gx[i] for i in range(n)]
    assert act(fy)==[-2*r*fy[i] for i in range(n)]
    assert sum(v*v for v in fx)/n==F(1,2)
    assert sum(v*v for v in fy)/n==F(1,4)
    assert sum(fx[i]*fy[i] for i in range(n))==0
    return 8


def check():
    n=0
    rng=Random(18102026)
    for kp,km,r in [(F(19,20),F(1,20),F(3,5)),
                    (F(1),F(0),F(3,4)),
                    (F(7,5),F(2,5),F(1,7)),
                    (F(2),F(2),F(9,11))]:
        n+=eigenbasis_checks(kp,km,r)
    for i in range(320):
        s=F(rng.randrange(1,100),100)
        u=F(rng.randrange(1,100),70)
        z=F(rng.randrange(1,100),50)
        c,d=1+s,3*s-1
        D=(c+z)**2-4*s*z
        A,B,C=coeffs(s,u)
        H=4*u*(4*u*u+z)*(d-z)-c*D
        assert H==C+B*z-A*z*z
        diff=spectrum(s,u,z)-spectrum(s,u,F(0))
        assert diff==z*H/(4*u*c*(4*u*u+z)*D)
        n+=2
    sstar=bisect(Fcrit, .34, 1.)
    assert abs(sstar-.9101817562569683)<1e-12
    assert abs(sqrt(sstar)-.9540344628245713)<1e-12
    n+=2
    for s in [.2,.33,.34,.6,.9,sstar-.003,sstar+.003,.95,.98,1.]:
        uc=critical_u(s)
        if s<=1/3:
            assert all(spectrum(s,u,z)<spectrum(s,u,0) for u in [.05,.1,.5,1.,5.]
                       for z in [.01,.1,1.,10.])
            n+=20
        else:
            for u in [.95*uc,.99*uc,1.01*uc,1.05*uc]:
                w=excess_sign_witness(s,u)
                assert (w>0)==(u>uc), (s,u,uc,w)
                n+=1
    # At the directed-cycle endpoint the exact tangency polynomial factors.
    def quartic(u): return 2*u**4-2*u**3+3*u*u-1
    uc=bisect(quartic,.62,.64)
    assert abs(uc-.628329993039018)<1e-12
    assert abs(u0(1.)-.6299605249474366)<1e-12
    A,B,C=coeffs(1.,uc)
    zc=B/(2*A)
    assert abs(zc-.117166445646799)<1e-12
    assert abs(sqrt(zc)-.342295845208204)<1e-12
    assert abs(C+B*zc-A*zc*zc)<2e-12
    assert abs(spectrum(1.,uc,zc)-spectrum(1.,uc,0.))<2e-12
    n+=6
    # Compare the quartic discriminant factorization at rational arguments.
    for i in range(25):
        u=F(i+1,31)
        A,B,C=coeffs(F(1),u)
        assert B*B+4*A*C == 64*(2*u*u+2*u+1)*quartic(u)
        n+=1
    # The endpoint has a real nonzero maximum while its origin curvature is negative.
    u=.629
    assert excess_sign_witness(1.,u)>0 and coeffs(1.,u)[2]<0
    n+=1
    # For the continuous branch, the peak frequency scales like delta**(1/2).
    s=.75
    base=u0(s)
    B0=coeffs(s,base)[1]
    assert B0<0
    Cu=48*base*base*(3*s-1)
    for delta in [1e-5,1e-6,1e-7]:
        u=base+delta
        # Brute-force optimize over the positive-excess interval by golden section.
        def g(z):
            A,B,C=coeffs(s,u)
            D=(1+s+z)**2-4*s*z
            return z*(C+B*z-A*z*z)/((4*u*u+z)*D)
        lo,hi=0.,3*s-1
        for _ in range(110):
            x1=lo+(hi-lo)*.3819660112501051
            x2=hi-(hi-lo)*.3819660112501051
            if g(x1)>g(x2): hi=x2
            else:lo=x1
        zp=(lo+hi)/2
        prediction=Cu*delta/(-2*B0)
        assert abs(zp/prediction-1)<.004,(zp,prediction)
        n+=1
    # At the borderline, z_peak behaves as delta**(1/2), so omega as delta**(1/4).
    s=sstar;base=u0(s)
    A0=coeffs(s,base)[0]
    Cu=48*base*base*(3*s-1)
    for delta in [1e-5,1e-6]:
        u=base+delta
        def g(z):
            A,B,C=coeffs(s,u)
            D=(1+s+z)**2-4*s*z
            return z*(C+B*z-A*z*z)/((4*u*u+z)*D)
        lo,hi=0.,3*s-1
        for _ in range(120):
            x1=lo+(hi-lo)*.3819660112501051
            x2=hi-(hi-lo)*.3819660112501051
            if g(x1)>g(x2): hi=x2
            else:lo=x1
        zp=(lo+hi)/2
        prediction=sqrt(Cu/(3*A0))*sqrt(delta)
        assert abs(zp/prediction-1)<.03,(zp,prediction)
        n+=1
    print(f'PASS: {n} deterministic exact and floating-point checks')
    print(f'drive tricritical ratio squared s* = {sstar:.15f}')
    print(f'drive tricritical ratio = {sqrt(sstar):.15f}')
    print(f'directed-cycle onset u* = {uc:.15f}')
    print(f'directed-cycle tie frequency omega/a = {sqrt(zc):.15f}')

if __name__=='__main__':
    check()
