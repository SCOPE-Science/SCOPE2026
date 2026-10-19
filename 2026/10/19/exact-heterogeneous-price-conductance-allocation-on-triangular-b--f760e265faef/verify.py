"""Numerical and exact cross-checks for priced resistance minimization on triangle bouquets.
Run: python verify.py  (Python 3 with numpy, scipy, sympy).
"""
import math
import random
import numpy as np
from scipy.optimize import minimize
import sympy as sp

CHECKS=0

def check(p, message=''):
    global CHECKS
    CHECKS+=1
    if not p:
        raise AssertionError(message or str(CHECKS))

n,t,w=sp.symbols('n t w',positive=True)
f=(2+t*w)*(2*(n-1)+2*(n-2)*w)/(1+2*w)
p=sp.factor(sp.diff(f,w)*(1+2*w)**2)
check(sp.simplify(p- (2*(n-1)*t-4*n +4*t*(n-2)*(w+w**2)))==0, str(p))
sc=sp.sqrt(n*(4-t)/(t*(n-2)))
wstar=(sc-1)/2
g=2*(n-2)+t+sp.sqrt(n*(n-2)*t*(4-t))
zsym=sp.symbols('zsym',positive=True)
fs=sp.factor(f.subs(w,(zsym-1)/2))
check(sp.simplify(fs- (2*(n-2)+t+t*(n-2)*zsym) + (t*(n-2)*zsym**2 - n*(4-t))/(2*zsym))==0)
check(abs(float(f.subs({n:5,t:1,w:(sp.sqrt(5)-1)/2}))-float(g.subs({n:5,t:1})))<1e-12)
tcrit=2*n/(n-1)
check(sp.simplify(sc.subs(t,tcrit)-1)==0)
check(sp.simplify(g.subs({n:5,t:sp.Rational(5,2)})-16)==0)


def opt(m, prices, B):
    N=2*m+1
    tc=2*N/(N-1)
    x=[]; y=[]; z=[]; gvals=[]
    for price in prices:
        if price>=tc:
            ratio=0.0
            val=4*(N-1)
        else:
            ratio=(math.sqrt(N*(4-price)/(price*(N-2)))-1)/2
            val=2*(N-2)+price+math.sqrt(N*(N-2)*price*(4-price))
        gvals.append(val)
        x.append(ratio)
    G=sum(math.sqrt(v) for v in gvals)
    for price, ratio, val in zip(prices,x,gvals):
        b=B*math.sqrt(val)/G
        base=b/(2+price*ratio)
        z.append(b)
        y.append(ratio*base)
    a=[zi/(2+pi*ri) for zi,pi,ri in zip(z,prices,x)]
    return a,y,G*G/B,z


def lap(m,as_,bs_,cs_):
    N=2*m+1
    L=np.zeros((N,N))
    for i in range(m):
        u,v=2*i+1,2*i+2
        for x,y,wgt in [(0,u,as_[i]),(0,v,bs_[i]),(u,v,cs_[i])]:
            L[x,x]+=wgt; L[y,y]+=wgt
            L[x,y]-=wgt; L[y,x]-=wgt
    return L


def K_exact(m, aa,bb,cc):
    N=2*m+1
    S=0.0
    for a,b,c in zip(aa,bb,cc):
        delta=a*b+a*c+b*c
        S+=((N-1)*(a+b)+2*(N-2)*c)/delta
    return S


def K_lap(m,aa,bb,cc):
    L=lap(m,aa,bb,cc)
    N=L.shape[0]
    # Kirchhoff index: N*Tr((L+11^T/N)^-1) - N.
    return N*(np.trace(np.linalg.inv(L+np.ones((N,N))/N))-1)

r=random.Random(1729)
for m in range(2,8):
    for trial in range(12):
        aa=[r.uniform(.03,3) for _ in range(m)]
        bb=[r.uniform(.03,3) for _ in range(m)]
        cc=[r.uniform(0,3) for _ in range(m)]
        f1=K_exact(m,aa,bb,cc)
        f2=K_lap(m,aa,bb,cc)
        check(abs(f1-f2)<=1e-8*max(1,f1), f'Kirchhoff decomposition m={m} trial={trial}: {f1} {f2}')

for m in range(2,7):
    tc=2*(2*m+1)/(2*m)
    prices=([tc-1.3,tc-.2,tc+.05,2*tc,tc] *2)[:m]
    B=3.0 + m
    a,c,K,z=opt(m,prices,B)
    check(abs(sum(2*ai+ti*ci for ai,ci,ti in zip(a,c,prices))-B)<1e-10)
    check(abs(K_exact(m,a,a,c)-K)<1e-9*max(1,K))
    check(abs(K_lap(m,a,a,c)-K)<1e-9*max(1,K))
    for j,tprice in enumerate(prices):
        check((c[j] <= 1e-12)==(tprice>=tc))
    # Independent full-Laplacian evaluation for random nonsymmetric feasible arrays.
    co=np.array([q for tt in prices for q in (1,1,tt)])
    for run in range(80):
        raw=np.array([r.uniform(.04,2.0) for _ in range(3*m)])
        raw=B*raw/np.dot(co,raw)
        rival=K_lap(m,raw[::3],raw[1::3],raw[2::3])
        check(rival+1e-9>=K, f'Rival improves optimum m={m}, run={run}, {rival} < {K}')
    # Independent numerical constrained minimization, using a positive parameterization.
    # The strict global result does not rely on its success.
    M=3*m
    init=np.array([p for ai,ci in zip(a,c) for p in (ai,ai,max(ci,1e-7))])
    init=B*init/np.dot(co,init)
    def fun(v):
        return K_exact(m,v[::3],v[1::3],v[2::3])
    cons={'type':'eq', 'fun':lambda v: np.dot(v,co)-B, 'jac':lambda v:co}
    bnds=[(1e-9,None) if k%3 in (0,1) else (0,None) for k in range(M)]
    sol=minimize(fun,init,method='SLSQP',bounds=bnds,constraints=[cons],options={'maxiter':350,'ftol':1e-10})
    check(abs(sol.fun-K)<1e-6*max(1,K),f'Numerical minimizer {m} {sol.fun} {K}: {sol.message}')
    for tt,b in zip(prices,z):
        check(b>0)

# Direct rational effective resistances for exact ordinary weights
for m in range(2,5):
    NN=2*m+1
    for case in range(4):
        aa=[sp.Rational(i+2+case,5) for i in range(m)]
        bb=[sp.Rational(i+2*case+4,7) for i in range(m)]
        cc=[sp.Rational(i+case+1,11) for i in range(m)]
        X=sp.zeros(NN,NN)
        for i,(a,b,c) in enumerate(zip(aa,bb,cc)):
            u,v=2*i+1,2*i+2
            for ii,jj,wt in [(0,u,a),(0,v,b),(u,v,c)]:
                X[ii,ii]+=wt;X[jj,jj]+=wt;X[ii,jj]-=wt;X[jj,ii]-=wt
        Q=(X+sp.ones(NN,NN)/NN).inv()
        actual=NN*(sp.trace(Q)-1)
        theoretical=sum(((NN-1)*(a+b)+2*(NN-2)*c)/(a*b+a*c+b*c) for a,b,c in zip(aa,bb,cc))
        check(actual==theoretical)
print(f'PASS: {CHECKS} exact symbolic, exact rational, and numerical checks')
