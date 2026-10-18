"""Reproduce exact Schatten moment identities and spectral optimality for rooted broom integration.
Run: python tree_hardy_checker.py. Requires Python 3, numpy, sympy.
All tests are independent of any stored numerical results.
"""
from fractions import Fraction as F
import math
import numpy as np
import sympy as sp

passed = 0
def check(ok, label):
    global passed
    assert ok, label
    passed += 1

x,m=sp.symbols('x m', real=True)
b=1-x
p2=sp.factor(x*x/sp.Integer(2)+m*x*b+m*b*b/2)
p4=sp.expand(x**4/sp.Integer(6)+sp.Rational(2,3)*m*x**3*b+m*m*x*x*b*b+sp.Rational(2,3)*m*x*b**3+m*b**4/sp.Integer(6))
check(sp.simplify(p2 - (m-(m-1)*x*x)/2)==0,'S2 formula')
check(sp.factor(sp.diff(p4,x)-sp.Rational(2,3)*x*(m-1)*((6*m-1)*x*x-9*m*x+3*m))==0,'S4 derivative')
check(sp.factor(p4.subs(x,0)-m/sp.Integer(6))==0,'S4 star endpoint')
check(sp.factor(p4.subs(x,1)-sp.Rational(1,6))==0,'S4 path endpoint')

def p4opt(M):
    return (9*M-math.sqrt(3*M*(3*M+4)))/(2*(6*M-1))

def kroot(M,a,L=1):
    d=2*a-L
    def f(k):
        return .5*((M+1)*math.cos(k*L)-(M-1)*math.cos(k*d))
    lo=0.; hi=math.pi/(2*L)
    for _ in range(80):
        q=(lo+hi)/2
        if f(q)>0:lo=q
        else:hi=q
    return (lo+hi)/2

def moment_quadrature(M,a,L=1,N=100):
    b=L-a
    points=[]
    if a>0:
        for i in range(N):points.append((-1,(i+.5)*a/N,a/N))
    if b>0:
        for j in range(M):
            for i in range(N):points.append((j,(i+.5)*b/N,b/N))
    E=np.array([z[0] for z in points],int)
    T=np.array([z[1] for z in points],float)
    W=np.array([z[2] for z in points],float)
    is_stem=(E[:,None]==-1)|(E[None,:]==-1)
    same=(E[:,None]==E[None,:])
    K=np.where(is_stem, np.where((E[:,None]==-1)&(E[None,:]==-1),np.minimum(T[:,None],T[None,:]),np.where(E[:,None]==-1,T[:,None],T[None,:])), np.where(same,a+np.minimum(T[:,None],T[None,:]),a))
    moment2=np.dot(K.diagonal(),W)
    moment4=np.sum(K*K*(W[:,None]*W[None,:]))
    B=K*np.sqrt(W[:,None]*W[None,:])
    top=np.linalg.eigvalsh(B)[-1]
    return moment2,moment4,math.sqrt(top)

for M in (2,3,5,10,50):
    check(0<p4opt(M)<.5,'S4 interior')
    for aa in (.02,.17,.50,.73,.98):
        check(kroot(M,.5)<kroot(M,aa)+2e-13,'op maximizer')
        check(abs(kroot(M,.5)-2*math.atan(1/math.sqrt(M)))<2e-14,'operator formula')
        check(float(sp.diff(p4,x).subs({m:M,x:.5}))<0,'S4 derivative midpoint')
        check(float(sp.diff(p4,x).subs({m:M,x:p4opt(M)/2}))>0,'S4 derivative before')
        check(float(sp.diff(p4,x).subs({m:M,x:(p4opt(M)+1)/2}))<0,'S4 derivative after')
        if aa not in (.5,): check(kroot(M,.5)<kroot(M,aa),'strict operator maximum')

for M,aa in ((2,.25),(3,.5),(4,.3),(5,.65)):
    p2n,p4n,pn=moment_quadrature(M,aa,N=42)
    check(abs(p2n-float(p2.subs({x:aa,m:M})))<2e-12,'independent S2 quadrature')
    check(abs(p4n-float(p4.subs({x:aa,m:M})))<2e-4,'independent S4 quadrature')
    check(abs(pn-1/kroot(M,aa))<2e-3,'independent Nyström operator norm')

# Exact moment kernel (independent rational midpoint quadrature, tests continuum formula convergence).
def exact_discrete(M,aa,N):
    aa=F(aa); bb=1-aa
    points=[]
    for i in range(N):points.append((-1,(F(i)+F(1,2))*aa/N,aa/N))
    for j in range(M):
        for i in range(N):points.append((j,(F(i)+F(1,2))*bb/N,bb/N))
    M2=F(0);M4=F(0)
    for edge,x1,w in points:
        M2+= w*(x1 if edge==-1 else aa+x1)
        for other,y1,v in points:
            z=min(x1,y1) if edge==-1 and other==-1 else (x1 if edge==-1 else (y1 if other==-1 else aa+(min(x1,y1) if edge==other else F(0))))
            M4+=w*v*z*z
    return M2,M4

for mm,rat in [(2,F(1,2)),(3,F(1,3)),(4,F(3,5))]:
    q2,q4=exact_discrete(mm,rat,12)
    check(abs(q2-F(str(p2.subs({x:sp.Rational(rat.numerator,rat.denominator),m:mm}))))<F(1,500),'exact rational S2 quadrature')
    check(abs(q4-F(str(p4.subs({x:sp.Rational(rat.numerator,rat.denominator),m:mm}))))<F(1,100),'exact rational S4 quadrature')

print(f'PASS {passed} checks; S4 optimal fraction m=3: {p4opt(3):.12f}; S_infty midpoint m=3: {1/kroot(3,.5):.12f}')
