"""Supplementary checks for indexed-spectrum inversion of radial periodic Fock masks.
This is finite arithmetic evidence; the proof of the theorem is analytic.
Run: python checker.py
Requires: mpmath, sympy.
"""
import mpmath as mp
import sympy as sp
mp.mp.dps = 115
assertions=0

def ck(cond, message):
    global assertions
    assertions+=1
    if not cond: raise AssertionError(message)

def c1(L, rho, a):
    return mp.sin(mp.pi*rho)/mp.pi * mp.exp(-1j*(mp.pi*rho + 2*mp.pi*a/L))

from functools import lru_cache
@lru_cache(maxsize=32)
def delta_fourier_many(count,L,rho,a,cutoff=220):
    vals=[mp.mpf(0) for _ in range(count)]
    for m in range(1,cutoff+1):
        cm=mp.sin(mp.pi*m*rho)/(mp.pi*m)*mp.exp(-1j*(mp.pi*m*rho + 2*mp.pi*m*a/L))
        q=1/(1-2j*mp.pi*m/L)
        v=cm*q
        for n in range(count):
            vals[n]+=2*mp.re(v)
            v*=q
    return vals

def delta_fourier(n,L,rho,a,cutoff=220):
    return delta_fourier_many(max(110,n+1),L,rho,a,cutoff)[n]

def gamma_tail(n,x):
    term=mp.mpf(1)
    z=term
    for k in range(1,n+1):
        term*=x/k
        z+=term
    return mp.exp(-x)*z

def lambda_intervals(n,L,rho,a,N=260):
    length=L*rho
    accum=mp.mpf('0')
    if a+length>L:
        accum+=1-gamma_tail(n,a+length-L)
    for k in range(N):
        lo=mp.mpf(k)*L+a
        hi=lo+length
        if hi<=L*(k+1):
            accum+=gamma_tail(n,lo)-gamma_tail(n,hi)
        else:
            accum+=gamma_tail(n,lo)-gamma_tail(n,(k+1)*L)
            accum+=gamma_tail(n,(k+1)*L)-gamma_tail(n,hi)
    return accum

# Symbolic cancellation of the angle in the Hankel determinant.
a,b,q,z=sp.symbols('a b q z')
f=lambda n: a*q**n + b*z**n
D=sp.factor(f(0)*f(2)-f(1)**2)
ck(sp.simplify(D-a*b*(q-z)**2)==0,'two-frequency Hankel factorization')

for Ls,rs,astr in [('1.3','0.36','0.23'),('2.1','0.41','1.57'),('0.8','0.25','0.75')]:
    L,rho,a=map(mp.mpf,(Ls,rs,astr))
    for n in [0,1,3,7,12,18]:
        direct=lambda_intervals(n,L,rho,a)
        fourier=rho+delta_fourier(n,L,rho,a)
        # Fourier tail m>220 is O(220^(-n-1)) and is negligible from n>=3.
        if n>=7: ck(abs(direct-fourier)<mp.mpf('1e-16'),f'independent eigenvalue check {Ls} {n}')
        elif n>=3: ck(abs(direct-fourier)<mp.mpf('2e-11'),f'independent eigenvalue check {Ls} {n}')
        else: ck(abs(direct-fourier)<mp.mpf('3e-6'),f'independent eigenvalue check {Ls} {n}')
    delta=[delta_fourier(n,L,rho,a) for n in range(65)]
    r=1/mp.sqrt(1+(2*mp.pi/L)**2)
    theta=mp.atan(2*mp.pi/L)
    r2=1/mp.sqrt(1+(4*mp.pi/L)**2)
    c=c1(L,rho,a)
    for n in [12,21,35]:
        leading=2*mp.re(c*(r*mp.exp(1j*theta))**(n+1))
        ck(abs(delta[n]-leading) < 6*(r2**(n+1)),f'fourier remainder {Ls} {n}')
    H=lambda n: delta[n]*delta[n+2]-delta[n+1]**2
    for n in [22,35,47]:
        predicted=-4*abs(c)**2*r**(2*n+4)*mp.sin(theta)**2
        ck(abs(H(n)/predicted-1) < mp.mpf('0.003'),f'Hankel asymptotic {Ls} {n}')
        ck(H(n)<0,f'eventual determinant sign {Ls} {n}')
    n=55
    RR=H(n+1)/H(n)
    Lrec=2*mp.pi/mp.sqrt(1/RR-1)
    ck(abs(Lrec-L)<mp.mpf('5e-8'),f'inverse period {Ls}')
    X=delta[n]/r**(n+1)
    Xnext=delta[n+1]/r**(n+2)
    crec=mp.exp(-1j*(n+1)*theta)*mp.mpc(X/2,(X*mp.cos(theta)-Xnext)/(2*mp.sin(theta)))
    ck(abs(crec-c)<mp.mpf('1e-14'),f'inverse phase coefficient {Ls}')
    # piecewise integral exactly via periodic interval cuts
    pts=sorted(set([mp.mpf(0),L,a%L,(a+L*rho)%L]))
    exacttrace=mp.mpf(0)
    for lo,hi in zip(pts[:-1],pts[1:]):
        mid=(lo+hi)/2
        if (mid-a)%L < L*rho:
            exacttrace+=(hi-lo)/2-(hi**2-lo**2)/(2*L)
    trace_replay=sum((lambda_intervals(n,L,rho,a)-rho) if n<9 else delta[n] for n in range(65))
    ck(abs(trace_replay-exacttrace)<mp.mpf('2e-21'),f'trace identity {Ls}')

# The canonical unshifted formula has trace L rho(1-rho)/2.
for Ls,rs in [('1','0.3'),('3','0.7'),('0.5','0.5')]:
    L,rho=mp.mpf(Ls),mp.mpf(rs)
    a=mp.mpf(0)
    ds=[lambda_intervals(n,L,rho,a)-rho if n<9 else delta_fourier(n,L,rho,a) for n in range(110)]
    ck(abs(sum(ds)-L*rho*(1-rho)/2)<mp.mpf('1e-22'),f'centered trace {Ls},{rs}')

print('PASS', assertions,'supplementary assertions')
