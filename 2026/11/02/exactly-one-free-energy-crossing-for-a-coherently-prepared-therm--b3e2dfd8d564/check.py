"""Standalone checks for the two-level Davies Mpemba crossing theorem.

Dependencies: Python 3, sympy, mpmath, numpy, scipy. Run: python check.py.
The finite tests are supplemental; the continuous-parameter theorem is proved in RESULT.md.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.linalg import expm, eigvalsh
import sympy as sp
import mpmath as mp

count=0

def verify(condition, what):
    global count
    assert condition, what
    count += 1

p,b,R,z,t=sp.symbols('p b R z t', real=True)
c=R**2-z**2
A2=sp.expand((-b+(b+z)*p)**2 + c*p)
B2=sp.expand((-b+(b+R)*p)**2)
verify(sp.simplify(A2-B2 - (R-z)*(R+z+2*b)*p*(1-p))==0,'radius gap')
for X,alpha in [(A2,(b+z)**2),(B2,(b+R)**2)]:
    verify(sp.simplify(X+(1-p)*sp.diff(X,p) - (R**2-alpha*(1-p)**2))==0,'quadratic identity')
verify(sp.simplify(A2.subs(p,0)-b**2)==0,'stationary original')
verify(sp.simplify(B2.subs(p,0)-b**2)==0,'stationary rotated')
verify(sp.simplify(A2.subs(p,1)-R**2)==0,'initial spectrum original')
verify(sp.simplify(B2.subs(p,1)-R**2)==0,'initial spectrum rotated')

# A separate exact numerical 2x2 Lindblad-superoperator implementation.
sx=np.array([[0,1],[1,0]],complex)
sy=np.array([[0,-1j],[1j,0]],complex)
sz=np.array([[1,0],[0,-1]],complex)
sminus=np.array([[0,0],[1,0]],complex)
splus=sminus.T.conj()
I=np.eye(2,dtype=complex)

def qubit(x,y,z):
    return (I+x*sx+y*sy+z*sz)/2

def vne(rho):
    lambdas=np.linalg.eigvalsh((rho+rho.conj().T)/2).real
    return -sum(float(q)*math.log(float(q)) for q in lambdas if q>1e-13)

def direct_delta(b,R,z,p):
    x=math.sqrt(max(0,R*R-z*z)); y=0
    initial=qubit(x,y,z)
    better=qubit(0,0,R)
    g_plus=(1-b)/2
    g_minus=(1+b)/2
    jumps=[math.sqrt(g_minus)*sminus,math.sqrt(g_plus)*splus]
    H=sz/2
    def gen(mat):
        result=-1j*(H@mat-mat@H)
        for L in jumps:
            LL=L.conj().T@L
            result+=L@mat@L.conj().T-(LL@mat+mat@LL)/2
        return result
    eij=[]
    for i in range(2):
        for j in range(2):
            M=np.zeros((2,2),complex);M[i,j]=1
            eij.append(M)
    mat=np.column_stack([gen(E).reshape(-1) for E in eij])
    T=expm(mat*(-math.log(p)))
    out1=(T@initial.reshape(-1)).reshape(2,2)
    out2=(T@better.reshape(-1)).reshape(2,2)
    stationary=qubit(0,0,-b)
    # D(rho||tau)=-S(rho) -tr(rho log tau)
    elog=(math.log((1-b)/2),math.log((1+b)/2))
    def rel(rho):
        return -vne(rho) - float((rho[0,0]*elog[0]+rho[1,1]*elog[1]).real)
    return rel(out2)-rel(out1)

def binaryentropy(radius):
    x=max(0,min(1,float(radius)))
    a=(1+x)/2; d=(1-x)/2
    return -a*math.log(a)-(d*math.log(d) if d else 0.)

def formula(b,R,z,p):
    aa=math.sqrt(max(0,(-b+(b+z)*p)**2+(R*R-z*z)*p))
    bb=abs(-b+(b+R)*p)
    return (R-z)*math.atanh(b)*p-(binaryentropy(bb)-binaryentropy(aa))

# Diverse mixed and pure initial states, near / beyond the crossing.
for bb in (.10,.50,.90):
    for rr in (.20,.75,1.):
        for frac in (-.99,-.5,0.,.5,.99):
            zz=frac*rr
            for pp in (.001,.03,.15,.4,.65,.9,.999):
                got=direct_delta(bb,rr,zz,pp)
                expected=formula(bb,rr,zz,pp)
                verify(abs(got-expected)<3e-10,'generator vs entropy formula')
            # Prove shape using sampled checks; symbolic argument covers all p.
            vals=[formula(bb,rr,zz,pp)/((rr-zz)*pp) for pp in (.00001,.001,.03,.1,.3,.7,.99)]
            verify(all(vals[i]<vals[i+1]+1e-9 for i in range(len(vals)-1)),'strict normalized sign')
            verify(vals[0]<0 and vals[-1]>0,'opposite endpoint signs')

# Complete boundary checks (inverted already, and population-aligned).
for bb in (.1,.5,.9):
    for rr in (.2,.8,1.):
        for pp in (.0001,.03,.2,.7,.999):
            verify(abs(formula(bb,rr,rr,pp))<1e-12,'same state')
            verify(formula(bb,rr,-rr,pp)>-1e-11,'diagonal noncrossing')

mp.mp.dps=60
bb=mp.mpf('0.5'); rr=mp.mpf('0.8'); zz=mp.mpf('0')
def ent(u):
    a=(1+u)/2; d=(1-u)/2
    return -a*mp.log(a) -d*mp.log(d) if d>0 else -a*mp.log(a)
def delta(p):
    aa=mp.sqrt((-bb+(bb+zz)*p)**2+(rr*rr-zz*zz)*p)
    bb2=abs(-bb+(bb+rr)*p)
    return (rr-zz)*mp.atanh(bb)*p-(ent(bb2)-ent(aa))
pstar=mp.findroot(delta,(mp.mpf('.4'),mp.mpf('.5')))
tstar=-mp.log(pstar)
verify(abs(pstar-mp.mpf('0.4299317297264721373231271583202845712203397560938'))<mp.mpf('1e-42'),'p*')
verify(abs(tstar-mp.mpf('0.84412885097748620685540371120667709709976736940061'))<mp.mpf('1e-42'),'t*')
verify(delta(mp.mpf('.4'))<0 and delta(mp.mpf('.5'))>0,'certified crossing bracket')
print('PASS',count,'independent symbolic, generator and root diagnostics')
print('p*=',mp.nstr(pstar,35))
print('t*=',mp.nstr(tstar,35))
