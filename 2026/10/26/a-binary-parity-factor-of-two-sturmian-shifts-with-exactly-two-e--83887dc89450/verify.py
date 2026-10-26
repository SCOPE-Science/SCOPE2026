"""Reproducible finite checks for parity factors of independent Sturmian shifts.
Numerical tests corroborate, but do not prove, the unrestricted statements.
"""
import cmath
from math import sqrt, pi, floor

alpha=sqrt(2)-1
beta=sqrt(3)-1
assert 0<alpha<1 and 0<beta<1

def mech(theta,n,x=0.0,side=0):
    # for exact singular intercept x=0, use symbolic one-sided convention
    if x==0 and n in (-1,0) and side in (-1,1):
        return int(n==0) if side==-1 else int(n==-1)
    return floor((n+1)*theta+x)-floor(n*theta+x)

rng=range(-50,51)
u_minus=[mech(alpha,n,side=-1) for n in rng]
u_plus=[mech(alpha,n,side=1) for n in rng]
v_minus=[mech(beta,n,side=-1) for n in rng]
v_plus=[mech(beta,n,side=1) for n in rng]
assert [n for n in rng if mech(alpha,n,side=-1)!=mech(alpha,n,side=1)]==[-1,0]
assert [n for n in rng if mech(beta,n,side=-1)!=mech(beta,n,side=1)]==[-1,0]
assert [a^b for a,b in zip(u_minus,v_minus)]==[a^b for a,b in zip(u_plus,v_plus)]
assert [a^b for a,b in zip(u_minus,v_plus)]==[a^b for a,b in zip(u_plus,v_minus)]
assert [a^b for a,b in zip(u_minus,v_minus)]!=[a^b for a,b in zip(u_minus,v_plus)]

x,y=0.19,0.37
N=30000
signs=[(-1)**(mech(alpha,n,x)^mech(beta,n,y)) for n in range(N)]
def empirical(freq):
    return sum(signs[n]*cmath.exp(-2j*pi*n*freq) for n in range(N))/N

def fourier1(theta):
    return (1-cmath.exp(2j*pi*theta))/(1j*pi)
ca=fourier1(alpha)*(1-2*beta)
cb=fourier1(beta)*(1-2*alpha)
phase_a=empirical(alpha)/ca
phase_b=empirical(beta)/cb
assert abs(phase_a-cmath.exp(2j*pi*x))<0.008,(phase_a,x)
assert abs(phase_b-cmath.exp(2j*pi*y))<0.008,(phase_b,y)
print('VERIFY_OK: two exact singular-pair XOR identities; distinct mixed branch;')
print('  30,000 finite-prefix samples for each independent Fourier phase recovery;')
print('  numeric errors:',round(abs(phase_a-cmath.exp(2j*pi*x)),7),round(abs(phase_b-cmath.exp(2j*pi*y)),7))
