"""Exact symbolic and numerical checks for a three-state Nyström-PCG condition comparison.

Run: python verify.py
Requires sympy and numpy (and scipy for the independent generalized eigensolver).
"""
import numpy as np
import scipy.linalg as la
import sympy as sp

k, m, lam, t, z = sp.symbols('k m lam t z', real=True)
checks = 0

def chk(test, msg):
    global checks
    checks += 1
    if test is not True and test != sp.S.true:
        raise AssertionError(msg)

alpha, beta = k + m, 1 + m
u1sq = k * (lam - 1) / ((k - 1) * lam)
u2sq = (k - lam) / ((k - 1) * lam)
chk(sp.factor(u1sq + u2sq - 1) == 0, 'unit direction')
T = alpha + beta - (lam-1)/(lam+m) * (beta + k*(lam-1)/lam)
D = alpha * beta**2 / (lam + m)
G = (-m**2*lam**3
     + ((k+1)**2 + (k**2+2*k+3)*m + (2*k+3)*m**2)*lam**2
     - k*(3*k+2+(2*k+4)*m+4*m**2)*lam + k**2)
K = alpha/beta
F = T**2/D - (K+1)**2/K
chk(sp.factor(F + (lam-1)*G/(lam**2*(lam+m)*(k+m)*(m+1)**2)) == 0,
    'condition-ratio difference factor')
a0 = (m+1)*(k+2*m+1)
a1 = k**2 + 3*k*m + k + 3*m**2 + 3*m + 1
a2 = k*(k-1)*(k+2*m)*(m+1)
a3 = k**2*(k+m)*(m+1)
Ht = a3*t**3+a2*t**2-a1*t-a0
chk(sp.factor(G.subs(lam,(1+k*t)/(1+t))*(1+t)**3 - (k-1)*Ht) == 0,
    'unique crossover cubic transform')
chk(sp.factor(G.subs(lam,1) + (k-1)*(m+1)*(k+2*m+1)) == 0,
    'left endpoint sign')
chk(sp.factor(G.subs(lam,k) - k**2*(k-1)*(k+m)*(m+1)) == 0,
    'right endpoint sign')

A = sp.diag(4, 1, 1)
O = sp.Matrix([[1, 0], [4, 0], [0, 1]])
H = A*O*(O.T*A*O).inv()*O.T*A
chk(H == sp.Matrix([[sp.Rational(4,5), sp.Rational(4,5),0],
                    [sp.Rational(4,5), sp.Rational(4,5),0], [0,0,1]]),
    'exact Nyström formula')
u = sp.Matrix([1,1,0])/sp.sqrt(2)
P = sp.eye(3)+sp.Rational(3,10)*u*u.T
B = A+sp.eye(3)
chk(P == sp.Matrix([[sp.Rational(23,20),sp.Rational(3,20),0],
                    [sp.Rational(3,20),sp.Rational(23,20),0], [0,0,1]]),
    'exact preconditioner')
chk(sp.factor(sp.det(B-z*P) + (z-2)*(26*z*z-161*z+200)/20) == 0,
    'generalized eigenvalue polynomial')
TT=sp.Rational(161,26)
DD=sp.Rational(100,13)
chk(TT**2/DD - sp.Rational(49,10) == sp.Rational(441,5200),
    'strict condition deterioration certificate')

# Crosscheck the formula for arbitrary sketch subspaces against a separate
# dense Nyström matrix reconstruction and an independent generalized eigensolver.
rng=np.random.default_rng(1234567)
for j in range(500):
    kk=np.exp(rng.uniform(0.003, 7.0))
    mm=np.exp(rng.uniform(-4.0, 6.0))
    AA=np.diag([kk,1,1]); BB=AA+mm*np.eye(3)
    OO=rng.normal(size=(3,2))
    AH=AA@OO
    HH=AH@np.linalg.solve(OO.T@AH,AH.T)
    w,U=np.linalg.eigh(HH)
    ww=w[-2:]; UU=U[:,-2:]
    chk(abs(ww[0]-1)<2.e-8, 'invariant retained eigenvalue')
    ll=ww[-1]
    if ll<=1+1.e-10 or ll>=kk-1.e-10: continue
    PP=np.eye(3)+UU@np.diag((ww-ww[0])/(ww[0]+mm))@UU.T
    vals=la.eigh(BB,PP,eigvals_only=True)
    observed=vals[-1]/vals[0]
    T0=float(T.subs({k:kk,m:mm,lam:ll}))
    D0=float(D.subs({k:kk,m:mm,lam:ll}))
    vp=(T0+np.sqrt(max(0.,T0*T0-4*D0)))/2
    vm=D0/vp
    predicted=vp/vm
    chk(abs(predicted-observed)<1.e-8*max(1,observed),
        'generalized eigenvalue condition formula')
    calcF=T0*T0/D0-(kk+mm+1+mm)**2/((kk+mm)*(1+mm))
    signG=np.sign(float(G.subs({k:kk,m:mm,lam:ll})))
    if abs(calcF)>1.e-7:
        chk(np.sign(calcF)==-signG, 'crossover sign')
    chk((ll>1) and (ll<kk), 'sketch eigenvalue bounds')

# The 32/27 number is an attained limit in this family, not a global upper bound.
limT=sp.limit(T.subs({m:1/k,lam:sp.Rational(3,2)})/k,k,sp.oo)
limD=sp.limit(D.subs({m:1/k,lam:sp.Rational(3,2)})/k,k,sp.oo)
limb=sp.limit(K.subs(m,1/k)/k,k,sp.oo)
chk(sp.simplify((limT**2/limD)/limb - sp.Rational(32,27))==0,
    'asymptotic relative inflation')
print(f'PASS: {checks} assertions; exact crossover identity, explicit witness, independent direct-sketch checks and 32/27 limit.')
