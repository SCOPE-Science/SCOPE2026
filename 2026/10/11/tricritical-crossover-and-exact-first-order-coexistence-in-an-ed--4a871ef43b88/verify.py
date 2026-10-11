#!/usr/bin/env python3
"""Finite symbolic and numerical diagnostics for the stated weighted-graph pressure theorem.
Run: python verify.py; requires SymPy and mpmath. No claim of exhaustive verification.
"""
import math
import sympy as sp
import mpmath as mp

K, Y, W = sp.symbols('K Y W', positive=True, real=True)
M = sp.Matrix([[sp.exp(Y), W, sp.exp(-Y)], [W, 0, W], [sp.exp(-Y), W, sp.exp(Y)]])
lam = sp.cosh(Y) + sp.sqrt(sp.sinh(Y)**2 + 1 + 2*W**2)
vec = sp.Matrix([1, 2*W/lam, 1])
assert all(sp.simplify(t) == 0 for t in M*vec-lam*vec)
P = sp.log(sp.cosh(Y) + sp.sqrt(sp.sinh(Y)**2 + K))
z = sp.sinh(Y)/sp.sqrt(sp.sinh(Y)**2+K)
assert sp.simplify(sp.diff(P,Y)-z) == 0
ratio = Y/z/sp.sqrt(K)
r_series = sp.series(ratio, Y, 0, 6).removeO().expand()
assert sp.simplify(r_series.coeff(Y,2) - (3-K)/(6*K)) == 0
assert sp.simplify(r_series.coeff(Y,4) - (7*K*K+30*K-45)/(360*K*K)) == 0

# Joint tricritical series, derived independently from the full pressure expression.
q,u,b=sp.symbols('q u b', real=True)
k=3+q*q
y=q*u
zz=sp.sinh(y)/sp.sqrt(sp.sinh(y)**2+k)
pp=sp.log(sp.cosh(y)+sp.sqrt(sp.sinh(y)**2+k))
p0=sp.log(1+sp.sqrt(k))
beta=sp.sqrt(k)*(1+b*q**4)
free=pp-p0-y*zz+beta*zz**2/2
f6=sp.simplify(sp.series(free,q,0,7).removeO().coeff(q,6))
assert sp.simplify(f6 - (b*u*u/2 +u**4/72-u**6/180)/sp.sqrt(3)) == 0

# Exact stationary sextic/coexistence/spinodal critical constants.
t=sp.symbols('t', positive=True, real=True)
branch=-t/sp.Integer(18)+t**2/sp.Integer(30)
limit_free=b*t/sp.Integer(2)+t**2/sp.Integer(72)-t**3/sp.Integer(180)
assert sp.simplify(sp.diff(limit_free,t)-b/2-t/36+t**2/60)==0
spin_t=sp.Rational(5,6)
coex_t=sp.Rational(5,4)
assert sp.simplify(sp.diff(branch,t).subs(t,spin_t))==0
assert branch.subs(t,spin_t)==-sp.Rational(5,216)
assert branch.subs(t,coex_t)==-sp.Rational(5,288)
assert sp.simplify(limit_free.subs(b,branch).subs(t,coex_t))==0

mp.mp.dps=55

def zfun(k,y):
    return mp.sinh(y)/mp.sqrt(mp.sinh(y)**2+k)
def pfun(k,y):
    return mp.log(mp.cosh(y)+mp.sqrt(mp.sinh(y)**2+k))
def rfun(k,y):
    return y/zfun(k,y)
def nfun(k,y):
    sy=mp.sinh(y)
    return sy*(sy*sy+k)-k*y*mp.cosh(y)
def cfun(k,y):
    return pfun(k,y)-pfun(k,0)-y*zfun(k,y)/2

tests=10
for tau_text in ['0.2','0.1','0.05','0.025','0.0125']:
    tau=mp.mpf(tau_text); kk=3+tau
    ys=mp.findroot(lambda v:nfun(kk,v), mp.sqrt(5*tau/6))
    yt=mp.findroot(lambda v:cfun(kk,v), mp.sqrt(5*tau/4))
    bs=rfun(kk,ys);bt=rfun(kk,yt)
    assert ys>0 and yt>ys and bs<bt<mp.sqrt(kk)
    assert abs(nfun(kk,ys))<mp.mpf('1e-38')
    assert abs(cfun(kk,yt))<mp.mpf('1e-38')
    assert abs(yt-bt*zfun(kk,yt))<mp.mpf('1e-38')
    # The stationary-state equal-pressure identity is checked directly.
    g=pfun(kk,yt)-pfun(kk,0)-yt*zfun(kk,yt)+bt*zfun(kk,yt)**2/2
    assert abs(g)<mp.mpf('1e-38')
    tests+=5
    if tau < mp.mpf('0.03'):
        assert abs(ys*ys/tau-mp.mpf(5)/6)<mp.mpf('0.005')
        assert abs(yt*yt/tau-mp.mpf(5)/4)<mp.mpf('0.005')
        assert abs((bs/mp.sqrt(kk)-1)/tau**2+mp.mpf(5)/216)<mp.mpf('0.001')
        assert abs((bt/mp.sqrt(kk)-1)/tau**2+mp.mpf(5)/288)<mp.mpf('0.001')
        tests+=4

for eps_text in ['0.2','0.1','0.05','0.025','0.0125']:
    eps=mp.mpf(eps_text); kk=3-eps; bb=mp.mpf(1)
    beta=mp.sqrt(kk)*(1+bb*eps**2)
    yy=mp.findroot(lambda v:rfun(kk,v)-beta, mp.sqrt(eps)*2)
    zz=zfun(kk,yy)
    limiting=mp.sqrt((mp.sqrt(25+1080*bb)-5)/18)
    assert yy>0 and abs(rfun(kk,yy)-beta)<mp.mpf('1e-38')
    if eps<mp.mpf('0.03'):
        assert abs(zz/mp.sqrt(eps)-limiting)<mp.mpf('0.03')
    tests+=2

# Explicit Markov kernel: checks all row sums, invariance, and its edge observable.
for kw in ['1.6','3','3.8','10']:
    for yy in ['-1.1','0','0.8']:
        kk=mp.mpf(kw); y=mp.mpf(yy); w=mp.sqrt((kk-1)/2)
        lam=mp.cosh(y)+mp.sqrt(mp.sinh(y)**2+kk)
        v=2*w/lam; rr=[mp.mpf(1),v,mp.mpf(1)]
        mm=[a*a/(2+v*v) for a in rr]
        mat=[[mp.exp(y),w,mp.exp(-y)],[w,mp.mpf(0),w],[mp.exp(-y),w,mp.exp(y)]]
        Q=[[mat[i][j]*rr[j]/(lam*rr[i]) for j in range(3)] for i in range(3)]
        assert all(abs(sum(row)-1)<mp.mpf('1e-49') for row in Q)
        assert all(abs(sum(mm[i]*Q[i][j] for i in range(3))-mm[j])<mp.mpf('1e-49') for j in range(3))
        spins=[-1,0,1]
        obs=sum(mm[i]*Q[i][j]*spins[i]*spins[j] for i in range(3) for j in range(3))
        assert abs(obs-zfun(kk,y))<mp.mpf('1e-48')
        tests+=3
print('PASS:',tests,'finite symbolic/analytic-reduction and numerical assertions; infinite claims depend on proof')
