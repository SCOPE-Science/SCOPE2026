"""Finite checks for cusp-symbol and lacunary Hardy-weight identities.
The script does not certify asymptotic or infinite-dimensional assertions.
Uses only the Python standard library.
"""
from fractions import Fraction
from math import cos, exp, gamma, log, pi
import cmath

checks=0
TH=Fraction(1,2)
M=70
# Taylor coefficients for F_n(z)=[1-(1-z)^theta]^n.
F=[[Fraction(0) for _ in range(M+1)] for n in range(7)]
F[0][0]=Fraction(1)
for n in range(1,7):
    for m in range(M):
        F[n][m+1]=((m-n*TH)*F[n][m]+n*TH*F[n-1][m])/(m+1)
        assert F[n][m+1]>=0
        checks+=1
# Compare the exact recurrence to truncated polynomial convolution.
p=[Fraction(0)]*(M+1)
p[1]=TH
for m in range(2,M+1):
    p[m]=p[m-1]*(m-1-TH)/m
for n in range(2,7):
    for m in range(M+1):
        direct=sum(p[k]*F[n-1][m-k] for k in range(1,m+1))
        assert direct==F[n][m]
        checks+=1
# Approximate finite norms, with an intentionally finite Taylor cutoff.
M2=8192
N2=45
T=.5
G=[0.]*(M2+1)
G[0]=1.
for n in range(1,N2+1):
    H=[0.]*(M2+1)
    for m in range(M2):
        H[m+1]=((m-n*T)*H[m]+n*T*G[m])/(m+1)
    G=H
    if n in (8,16,32,45):
        a=sum(x*x for x in G)
        b=a-sum((1.-(j**-2.))*G[j]*G[j] for j in (2,4,8,16,32,64,128,256,512,1024,2048,4096,8192))
        assert b>0.92*a and b<=a
        # The proven limiting constant for theta=1/2 is 1/pi.
        assert abs(a*n*n-1./pi)<0.04
        checks+=3
# Numerically check the boundary-modulus local scaling for several theta values.
for theta in (0.3,0.5,0.7):
    q=2*cos(pi*theta/2)
    for t in (1.e-4,1.e-6,1.e-8):
        z=1-(1-cmath.exp(1j*t))**theta
        ratio=(1-abs(z)**2)/(t**theta)
        assert abs(ratio/q-1)<0.04
        checks+=1
# Exact endpoint summability comparison for geometric levels.
for theta in (.4,.5,.8):
    crit=1/theta
    for alpha,gamma in ((crit-.25,3),(crit,-2),(crit,-1),(crit,-.5),(crit,0),(crit,1),(crit+.25,-3)):
        vals=[(2.**j)**(alpha-crit)*(log(exp(1.)+2.**j))**gamma for j in range(48,73)]
        if alpha>crit or (alpha==crit and gamma>0):
            assert vals[-1]>vals[0]
        elif alpha==crit and gamma==0:
            assert max(vals)-min(vals)<1e-11
        else:
            assert vals[-1]<vals[0]
        checks+=1
print('CUSPIDAL_LACUNARY_FINITE_OK',checks)
