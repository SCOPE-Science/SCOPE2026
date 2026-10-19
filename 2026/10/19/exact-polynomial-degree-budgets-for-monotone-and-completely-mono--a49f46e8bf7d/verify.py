"""Independent finite consistency checks for an all-degree polynomial dense-output theorem.

This script supports but does not replace the analytical positivity and degree proofs.
"""
from __future__ import annotations
import math
import sympy as S
import mpmath as mp
x=S.symbols('x',real=True)
checks=0

def check(ok,msg):
    global checks
    assert bool(ok),msg
    checks+=1

# Explicit orthogonal-polynomial reproducing kernels and min-mass formulas.
for k in range(1,7):
    L=[S.legendre(j,1-2*x) for j in range(k+1)]
    K0=S.expand(sum((2*j+1)*p.subs(x,0)*p for j,p in enumerate(L)))
    K1=S.expand(sum((2*j+1)*p.subs(x,1)*p for j,p in enumerate(L)))
    for j,p in enumerate(L):
        check(S.simplify(S.integrate(K0*p,(x,0,1))-p.subs(x,0))==0,f'odd K0 k={k} j={j}')
        check(S.simplify(S.integrate(K1*p,(x,0,1))-p.subs(x,1))==0,f'odd K1 k={k} j={j}')
    check(K0.subs(x,0)==(k+1)**2,f'odd diag0 {k}')
    check(K1.subs(x,1)==(k+1)**2,f'odd diag1 {k}')
    check(K0.subs(x,1)==(-1)**k*(k+1),f'odd offdiag {k}')
    # Rational endpoint squares (alpha,beta)=(4,9): signed interpolation values.
    a,b=S.Integer(2),S.Integer((-1)**k*3)
    M=S.Matrix([[(k+1)**2,(-1)**k*(k+1)],[(-1)**k*(k+1),(k+1)**2]])
    coeff=M.inv()*S.Matrix([a,b])
    A=S.expand(coeff[0]*K0+coeff[1]*K1)
    check(A.subs(x,0)==a and A.subs(x,1)==b, f'odd A endpoints {k}')
    mass=S.simplify(S.integrate(A*A,(x,0,1)))
    target=S.Rational(13,1)/S.Integer(k*(k+2))-S.Rational(12,1)/S.Integer((k+1)*k*(k+2))
    check(mass==target,f'odd mass k={k}: {mass} {target}')
    # Weighted endpoint reproducing kernels for each parity branch.
    Bs=[S.jacobi(j,0,1,1-2*x) for j in range(k+1)]
    As=[S.jacobi(j,1,0,1-2*x) for j in range(k+1)]
    BK=S.expand(sum(2*(j+1)*p for j,p in enumerate(Bs)))
    AK=S.expand(sum(2*(j+1)*(-1)**j*p for j,p in enumerate(As)))
    m=(k+1)*(k+2)
    for p in Bs:
        check(S.simplify(S.integrate((1-x)*BK*p,(x,0,1))-p.subs(x,0))==0, f'B K {k}')
    for p in As:
        check(S.simplify(S.integrate(x*AK*p,(x,0,1))-p.subs(x,1))==0,f'A K {k}')
    check(BK.subs(x,0)==m and AK.subs(x,1)==m,f'even endpoint kernel {k}')
    check(S.simplify(S.integrate((1-x)*BK*BK,(x,0,1))-m)==0,f'even B norm {k}')
    check(S.simplify(S.integrate(x*AK*AK,(x,0,1))-m)==0,f'even A norm {k}')
    q=S.expand((1-x)*(S.Rational(2,m)*BK)**2+x*(S.Rational(3,m)*AK)**2)
    check(q.subs(x,0)==4 and q.subs(x,1)==9,f'even q endpoints {k}')
    check(S.simplify(S.integrate(q,(x,0,1))-S.Rational(13,m))==0,f'even min mass {k}')

mp.mp.dps=50

def alpha(z):return z/(-mp.expm1(-z))
def beta(z):return z/(mp.expm1(z))
def oddmass(z,k):return (alpha(z)+beta(z)-2*mp.sqrt(alpha(z)*beta(z))/(k+1))/(k*(k+2))
def evenmass(z,k):return (alpha(z)+beta(z))/((k+1)*(k+2))
def threshold(fun,k,seed):return mp.findroot(lambda z:fun(z,k)-1,seed)
roots=[]
for n in range(3,11):
    k=(n-1)//2 if n%2 else (n-2)//2
    f=oddmass if n%2 else evenmass
    rt=threshold(f,k,(n*n/6,n*n/4))
    check(rt>0 and abs(f(rt,k)-1)<mp.mpf('1e-40'),f'threshold n={n}')
    roots.append((n,rt))
    for z in (mp.mpf('0.1'),rt*mp.mpf('0.5'),rt*mp.mpf('1.5')):
        if z<rt:check(f(z,k)<1,f'allowed {n}')
        else:check(f(z,k)>1,f'forbidden {n}')
print('thresholds:',[(n,mp.nstr(r,28)) for n,r in roots])

for z in (mp.mpf('0.001'),mp.mpf('0.5'),mp.mpf('2'),mp.mpf('5'),mp.mpf('15'),mp.mpf('50')):
    ea=mp.exp(-z)
    R=z*(1-ea)/(1-(1+z)*ea)
    check(R>2,f'R>2 z={z}')
    n=int(mp.ceil(R))
    rho=R-int(mp.floor(R))
    S0=1-(1+z)*ea
    a0=ea; a1=z*ea
    j=int(mp.floor(R))
    am=S0*(j+1-R)
    ap=S0*(R-j)
    check(am>=-mp.mpf('1e-35') and ap>=-mp.mpf('1e-35'),f'weights >= 0 z={z}')
    check(abs(a0+a1+am+ap-1)<mp.mpf('1e-35'),f'endpoints CM z={z}')
    check(abs(a1+j*am+(j+1)*ap-z)<mp.mpf('1e-35'),f'slope CM z={z}')
    check(j+1==n or ap==0,f'degree CM {z}')
for z in (mp.mpf('0.1'),mp.mpf('1'),mp.mpf('5'),mp.mpf('20'),mp.mpf('100'),mp.mpf('400')):
    n=3
    while True:
        k=(n-1)//2 if n%2 else (n-2)//2
        if (oddmass(z,k) if n%2 else evenmass(z,k))<=1:
            break
        n+=1
    check(abs(n/(2*mp.sqrt(z))-1)<mp.mpf('1') if z>=100 else True,f'growth {z}')
    print('minimal monotone degree',mp.nstr(z,7),n,'CM',int(mp.ceil(z*(-mp.expm1(-z))/(1-(1+z)*mp.exp(-z)))))
print('PASSED',checks,'consistency checks')
