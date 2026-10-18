"""Reproducible exact and numerical checks for the finite-cycle Lindblad mixing theorem.
Scientific assertions are independent of the analytical infinite-family proof.
"""
from fractions import Fraction
from math import cos, pi, exp, log, sqrt
import numpy as np
import sympy as sp
from scipy.linalg import expm

checks=0
def chk(ok, comment=''):
    global checks
    checks+=1
    if not ok: raise AssertionError(f'#{checks}: {comment}')

q=sp.symbols('q', real=True)
chk(sp.factor(1-4*q*(1-q)-q**4)==-(q-1)**2*(q**2+2*q-1), 'two-state crossing factor')
chk(sp.simplify((1-3*q*(1-q)-q**3)-(1-q)**3)==0, 'three-state population inequality')
chk(sp.simplify((1-2*q*(1-q)-q**2)-(1-q)**2)==0, 'four-state population inequality')
chk(sp.simplify((1-4*q*(1-q)-q**2)-(1-q)*(1-3*q))==0, 'two-state full contraction threshold')
chk(sp.simplify((1-3*q*(1-q)-q**2)-(1-q)*(1-2*q))==0, 'three-state full contraction threshold')

for n in range(2,10):
    P=np.roll(np.eye(n),1,axis=0)
    J=np.zeros((n*n,n*n))
    # column vectorization index i+n*j
    for i in range(n):
        J[((i+1)%n)+n*((i+1)%n),i+n*i] = 1.0
    one=np.eye(n*n)
    u=np.eye(n).reshape((n*n,),order='F')/n
    tr=np.eye(n).reshape((n*n,),order='F')
    Pi=np.outer(u,tr)
    a=1-cos(2*pi/n)
    for x in [.002,.1,.4,log(2),log(3),1.5,3.,7.]:
        qq=exp(-x)
        M=qq*one+(1-qq)*J
        ev=np.linalg.eigvalsh((M-Pi).T@(M-Pi))
        norm=sqrt(max(ev.max(),0))
        X=expm(x*(J-one))
        exact_norm=np.linalg.svd(X-Pi,compute_uv=False)[0]
        chk(abs(exact_norm-max(qq, exp(-a*x)))<2.e-8, 'exact semigroup norm')
        r=sqrt(max(0,1-2*a*qq*(1-qq)))
        chk(abs(norm-max(qq,r))<2.e-8, f'free operator n={n} x={x}')
        ex=max(qq,exp(-a*x))
        if n==2:
            expected=max(qq,abs(2*qq-1))
            chk(abs(norm-expected)<2.e-8)
            chk((norm>ex+1.e-8)==(x>log(3)+1.e-7), f'n2 threshold x={x}')
        elif n==3:
            chk((norm>ex+1.e-8)==(x>log(2)+1.e-7), f'n3 threshold x={x}')
        else:
            chk(norm>ex, f'n={n} strict')
        chk(np.linalg.norm((M-Pi)@tr)<1e-12,'stationarity')
        if n>=3: chk(r>exp(-a*x),'n>=3 population strict')

for n in [2,3,5,9]:
    a=1-cos(2*pi/n)
    for x in [10,14,18]:
        qq=exp(-x)
        r=sqrt(1-2*a*qq*(1-qq))
        chk(abs((1-r)/qq-a)<4*a*qq,'stiff spectral gap')

for n in [2,3,4,9]:
    P=np.roll(np.eye(n),1,axis=0)
    J=np.zeros((n*n,n*n))
    for i in range(n): J[((i+1)%n)+n*((i+1)%n),i+n*i]=1
    u=np.eye(n).reshape((n*n,),order='F')/n
    tr=np.eye(n).reshape((n*n,),order='F')
    Pi=np.outer(u,tr)
    p=np.zeros(n*n); p[0]=1
    chk(abs(np.linalg.norm(J@p-Pi@p,ord=1)-2*(1-1/n))<1.e-12,
        'sharp one-step trace-distance error')

print('PASS',checks,'symbolic and numerical checks')
