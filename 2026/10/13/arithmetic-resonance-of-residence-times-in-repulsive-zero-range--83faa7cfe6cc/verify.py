"""Reproduce finite detailed balance and asymptotic arithmetic corrections.
Standard-library Python 3.10+; no external data or packages.
"""
from fractions import Fraction
from math import exp, log, sqrt, fsum, isclose

def g(n):
    return Fraction(4 ** (n-1)) if n else Fraction(0)

def w(n, x):
    return Fraction(x**n, 4**(n*(n-1)//2))

# Independent exact rational local-balance test of the open branch on 2 sites.
# u=log(4), h=log(4), z=1/2; x1=2, x2=8; forward=2, backward=1/2.
checks=0
for n1 in range(4):
    for n2 in range(4):
        stat=w(n1,2)*w(n2,8)
        # injection versus exit
        assert stat*1 == w(n1+1,2)*w(n2,8)*Fraction(1,2)*g(n1+1)
        checks+=1
        # one forward hop and corresponding backward hop
        if n1:
            assert stat*2*g(n1) == w(n1-1,2)*w(n2+1,8)*Fraction(1,2)*g(n2+1)
            checks+=1

# Finite fugacity identity by telescope, independently from the Gaussian step.
for u in (1.1, 4.2):
    for x in (0.3, 2.0, 12.0):
        mass=[x**m*exp(-u*m*(m-1)/2) for m in range(30)]
        mean=sum(m*mass[m] for m in range(30))/sum(mass)
        eff=sum(exp(u*(m-1))*mass[m] for m in range(1,30))/sum(mass)
        assert abs(eff-x) < 1e-8
        assert 0<=mean<30
        checks+=1

def psi(u,t):
    # theta-lattice logarithmic derivative; shifts reduce floating range.
    t=t%1.0
    numer=0.0;denom=0.0
    for m in range(-12,14):
        w=exp(-u*(m-t)**2/2)
        numer+=(m-t)*w
        denom+=w
    return numer/denom

def rho(u, h, z, k):
    t=(log(z)+h*k)/u + 0.5
    lo=max(0,int(t)-22)
    hi=max(22,int(t)+22)
    a=[(m,exp(-u*(m-t)**2/2)) for m in range(lo,hi+1)]
    return sum(m*v for m,v in a)/sum(v for _,v in a)

# Sharp rational resonance at u=8, h=8, c=1/4.
u=8.0;c=0.25;z=exp(u*(c-0.5));h=u
psi1=psi(u,c)
assert -0.134<psi1<-0.132
for k in (8,18,100):
    assert abs(rho(u,h,z,k)-(k+c+psi1))<1e-9
    checks+=1
for L in (100,300):
    total=fsum(rho(u,h,z,k) for k in range(1,L+1))
    leading=L*(L+1)/2+c*L
    # The discrepancy is constant up to negligible truncation, so slope tends to psi(c).
    assert abs((total-leading)/L-psi1)<0.003
    checks+=1

# Irrational ratio h/u=sqrt(2) has zero Cesaro mean correction.
a=sqrt(2);h=u*a
L=2200
total=fsum(rho(u,h,z,k) for k in range(1,L+1))
leading=a*L*(L+1)/2+c*L
assert abs((total-leading)/L)<0.015
checks+=1

# Rational q=3 profile is periodic in k, with a q-point theta mean.
h=u/3
avg=sum(psi(u,c+j/3) for j in range(1,4))/3
L=1800
total=fsum(rho(u,h,z,k) for k in range(1,L+1))
leading=(1/3)*L*(L+1)/2+c*L
assert abs((total-leading)/L-avg)<0.004
checks+=1

print('VERIFY_OK',checks,'rational_psi',format(psi1,'.12f'),'q3_residual_per_site',format((total-leading)/L,'.12f'))
