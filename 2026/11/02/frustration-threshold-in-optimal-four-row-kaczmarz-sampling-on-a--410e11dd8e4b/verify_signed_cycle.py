#!/usr/bin/env python3
"""Checks finite certificates for the four-row signed-cycle Kaczmarz theorem.
Requires Python 3, NumPy, SciPy, and SymPy. Finite tests are not an infinite proof.
"""
from fractions import Fraction
import numpy as np
import sympy as sp
from scipy.optimize import root, minimize

N = 0

def ck(cond, message):
    global N
    N += 1
    if not bool(cond):
        raise AssertionError(message)


def data(t, w=sp.Rational(1, 10)):
    t, w = sp.sympify(t), sp.sympify(w)
    C = sp.diag(5, 6, 7, 8)
    for i,j,v in [(0,1,w),(1,2,w),(2,3,w),(3,0,-t*w)]:
        C[i,j] = C[j,i] = v
    if t <= sp.Rational(1,3):
        alpha, beta = 1-t, 2
        X = sp.ones(4)
    else:
        c = sp.sqrt((1+t)/(4*t))
        alpha, beta = 2*t*c, 2*c
        T = lambda k: sp.chebyshevt(k,c)
        X = sp.Matrix(4,4,lambda i,j:T(abs(i-j)))
    q = sp.Matrix([C[i,i]+w*(alpha if i in (0,3) else beta) for i in range(4)])
    S = sp.diag(*q)-C
    return C, q, S, X

for t in [sp.Rational(1,10), sp.Rational(1,5), sp.Rational(1,3),
          sp.Rational(4,5), sp.Rational(9,7), sp.Rational(25,11)]:
    C,q,S,X = data(t)
    ck(all(sp.simplify((S*X)[i,j])==0 for i in range(4) for j in range(4)),f'complementary slackness {t}')
    ck(sp.simplify(sum(q)-sp.trace(C*X))==0,f'dual equality {t}')
    ck(all(X[i,i]==1 for i in range(4)),f'dual diagonal {t}')
    for Z, name in [(S,'slack'),(X,'dual')]:
        for mask in range(1,16):
            inds=[i for i in range(4) if mask&(1<<i)]
            det = sp.simplify(Z.extract(inds,inds).det())
            ck(det.is_nonnegative or det>=0,f'{name} principal minor {mask} at {t}: {det}')
    ck(all(i>0 for i in q),f'positive weights {t}')

# Explicit unit-normalized Gram at t=1: 4x4 skew-holonomy cycle squares to 2 I.
w = sp.Rational(1,4)
a = (1+sp.sqrt(1+8*w*w))/2
C = sp.diag(a,a,a,a)
for i,j,v in [(0,1,w),(1,2,w),(2,3,w),(3,0,-w)]:C[i,j]=C[j,i]=v
G = C.inv()
ck(all(sp.simplify(G[i,i]-1)==0 for i in range(4)),'explicit unit rows')
q = sp.Matrix([a+sp.sqrt(2)*w]*4)
ck(all(sp.simplify(v)==0 for v in (sp.diag(*q)-C)*sp.Matrix([1,sp.sqrt(2)/2,0,-sp.sqrt(2)/2])), 'explicit dual kernel')
# Numeric normalized-row instances at t values across the threshold.
for t in (.1, .2, 1/3, .4, .8, 1., 2., 10.):
    w=.15
    E=np.zeros((4,4))
    for i,j,v in ((0,1,w),(1,2,w),(2,3,w),(3,0,-t*w)): E[i,j]=E[j,i]=v
    def normalize_err(z):
        C0=np.diag([z[0],z[1],z[1],z[0]])+E
        if np.linalg.eigvalsh(C0)[0] <= 0: return np.array([100,100])
        inv=np.linalg.inv(C0)
        return np.array([inv[0,0]-1,inv[1,1]-1])
    fit=root(normalize_err,[1+w*w*(1+t*t),1+2*w*w],tol=1e-11)
    ck(fit.success or np.linalg.norm(fit.fun)<1e-9,f'normalized fit {t}')
    C0=np.diag([fit.x[0],fit.x[1],fit.x[1],fit.x[0]])+E
    G=np.linalg.inv(C0)
    ck(max(abs(np.diag(G)-1))<1e-9, f'unit row Gram {t}')
    ck(np.linalg.eigvalsh(C0)[0]>0, f'SPD {t}')
    if t<=1/3: ab=[1-t,2,2,1-t]
    else:
        c=np.sqrt((1+t)/(4*t));ab=[2*t*c,2*c,2*c,2*t*c]
    q=np.diag(C0)+w*np.array(ab)
    S=np.diag(q)-C0
    ck(np.linalg.eigvalsh(S)[0]>-1e-9,f'slack PSD {t}')
    p=q/sum(q)
    lam=np.linalg.eigvalsh(np.diag(np.sqrt(p))@G@np.diag(np.sqrt(p)))[0]
    ck(abs(lam-1/sum(q))<1e-9,f'primal eigen equality {t}')
    rng=np.random.default_rng(int(t*1000)+3)
    for _ in range(100):
        randomp=rng.dirichlet(np.ones(4))
        lamrandom=np.linalg.eigvalsh(np.diag(np.sqrt(randomp))@G@np.diag(np.sqrt(randomp)))[0]
        ck(lamrandom<=lam+1e-9,f'competitor {t}')
print(f'PASS {N} grouped exact and numerical assertions')
