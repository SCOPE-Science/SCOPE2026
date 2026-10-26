"""Reproduce exact rational Stieltjes identity and numerical mixed-qubit trace-kernel spectra."""
from fractions import Fraction as F
from math import sqrt, isclose, pi, sin, cos


def mul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def conjtranspose(a):
    return [[a[j][i].conjugate() for j in range(2)] for i in range(2)]


def rho_half(q,theta):
    plus,minus=sqrt((1+q)/2),sqrt((1-q)/2)
    avg,delta=(plus+minus)/2,(plus-minus)/2
    z=complex(cos(theta),sin(theta))
    return [[avg,delta*z.conjugate()],[delta*z,avg]]


def rho(q,theta):
    z=complex(cos(theta),sin(theta))
    return [[.5,.5*q*z.conjugate()],[.5*q*z,.5]]


def spectral_power_trace(q,i,j,r):
    h=rho_half(q,i*pi/2)
    a=mul(mul(h,rho(q,j*pi/2)),conjtranspose(h))
    tr=(a[0][0]+a[1][1]).real
    det=(a[0][0]*a[1][1]-a[0][1]*a[1][0]).real
    disc=max(0,tr*tr-4*det)
    return ((tr+sqrt(disc))/2)**r+((tr-sqrt(disc))/2)**r


def explicit(q,r):
    u=q*sqrt(2-q*q)
    d=((1+q)**(2*r)+(1-q)**(2*r))/4**r
    a=((1+u)**r+(1-u)**r)/4**r
    b=2*(1-q*q)**r/4**r
    return d,a,b


def rational_stieltjes(q,s):
    a=(1+q)**2
    b=(1-q)**2
    c=1-q*q
    u2=q*q*(2-q*q)
    g=1/(s+a)+1/(s+b)+2/(s+c)-4*(s+1)/((s+1)**2-u2)
    gfact=8*q**4*s*(s+q*q-1)/((s+c)*(s+a)*(s+b)*((s+1)**2-u2))
    assert g==gfact
    return g

n_exact=0
for qn in range(1,10):
    q=F(qn,10)
    for sn in range(1,31):
        s=F(sn,17)
        rational_stieltjes(q,s)
        n_exact+=1
    assert (1+q)**2*(1-q)**2*(1-q*q)**2==((1-q*q)**2)**2

n_spectral=0
for q in (.035,.15,.42,.8,.99):
    for r in (.25,.5,.75,.91,1.):
        d,a,b=explicit(q,r)
        for i in range(4):
            for j in range(4):
                sep=(i-j)%4
                want=(d,a,b,a)[sep]
                got=spectral_power_trace(q,i,j,r)
                assert isclose(got,want,rel_tol=2e-10,abs_tol=2e-12),(q,r,i,j,got,want)
                n_spectral+=1
        lam=d+b-2*a
        if r<1:
            assert lam<-1e-10
            assert d-b>0
        else:
            assert abs(lam)<1e-10
        for dimension in (2,3,6):
            scaled=(2/dimension)**(2*r)*lam
            assert (scaled<0 if r<1 else abs(scaled)<1e-10)

# Quartic coefficient is -2*r*r*(1-r*r)/(3*dimension**(2*r)).
for r in (.25,.5,.75):
    q=.02
    d,a,b=explicit(q,r)
    lam=d+b-2*a
    coefficient=-4**(-r)*2*r*r*(1-r*r)/3
    assert abs(lam/q**4-coefficient)/abs(coefficient)<.01

print(f"PASS exact Stieltjes rational identities={n_exact}; independent 2x2 matrix-power checks={n_spectral}; quartic and dimensional checks passed")
