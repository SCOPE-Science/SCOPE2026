"""Reproducible checks for the symmetric half-turn orbits of a two-harmonic nontwist map.
All algebraic identities required in the proof are established separately in RESULT.md.
The numerical tests below are non-exhaustive cross-checks, not an infinite proof.
"""
import math
import sympy as S
import numpy as np

q,h,c,gam,k,r=S.symbols('q h c gam k r',real=True)
A=S.Matrix([[q,-h],[c*q,1-c*h]])
B=S.Matrix([[q,h],[-c*q,1-c*h]])
assert S.simplify(S.det(A)-q)==0
assert S.simplify(S.det(B*A)-q*q)==0
assert S.simplify(S.trace(B*A)-(1+q*q+(c*h)**2+2*(q-1)*c*h))==0
assert S.simplify(r*(r+2)**2-(2*r+1)**2-(r**3-1))==0
s=S.symbols('s',positive=True)
f=(1-3*s)**2/(s*(1-s))
assert S.factor(S.diff(f,s)) == (s+1)*(3*s-1)/(s*s*(s-1)**2)
u=S.symbols('u',real=True)
assert S.trigsimp(S.sin(u)+S.sin(3*u)-4*S.sin(u)*S.cos(u)**2)==0
assert S.trigsimp(S.diff(4*S.sin(u)*S.cos(u)**2,u)-4*S.cos(u)*(1-3*S.sin(u)**2))==0
print('six symbolic identities: PASS')

def param(a, gam):
    rho=math.sqrt(1-1/(2*a))
    H=gam/(math.pi*(2*a-1)*(2-gam))
    D=H*math.sqrt(H*H+8)
    s0=(6+H*H-D)/(2*(9+H*H))
    s1=(6+H*H+D)/(2*(9+H*H))
    assert 0<s0<1/3<s1<1
    getb=lambda s:(2-gam)*rho/(4*math.sqrt(s)*(1-s))
    fold=getb(1/3)
    out,inside=getb(s0),getb(s1)
    assert fold<out<inside
    return rho,fold,out,inside

def F(x,a,gam,b):
    I,theta=x
    G=lambda theta:math.sin(2*math.pi*theta)+math.sin(6*math.pi*theta)
    I1=(1-gam)*I-b*G(theta)
    t1=(theta+a*(1-I1*I1))%1
    return np.array([I1,t1])

def jac(x,a,gam,b):
    I,th=x
    g=math.sin(2*math.pi*th)+math.sin(6*math.pi*th)
    gp=2*math.pi*math.cos(2*math.pi*th)+6*math.pi*math.cos(6*math.pi*th)
    I1=(1-gam)*I-b*g
    return np.array([[1-gam,-b*gp],[-2*a*I1*(1-gam),1+2*a*I1*b*gp]])

def orbits(a,gam,b):
    rho, fold, _,_=param(a,gam)
    if b<=fold:return []
    level=(2-gam)*rho/b
    roots=np.roots([4,0,-4,level])
    ts=sorted([float(z.real) for z in roots if abs(z.imag)<1e-10 and 0<z.real<1])
    assert len(ts)==2
    items=[]
    for t in ts:
        for U in (math.asin(t),math.pi-math.asin(t)):
            x=np.array([rho,U/(2*math.pi)])
            y=F(x,a,gam,b)
            z=F(y,a,gam,b)
            assert np.linalg.norm(y-np.array([-rho,(x[1]+0.5)%1]))<1e-11
            assert np.linalg.norm(z-x)<1e-11
            M=jac(y,a,gam,b)@jac(x,a,gam,b)
            ev=np.linalg.eigvals(M)
            gp=2*math.pi*math.cos(U)+6*math.pi*math.cos(3*U)
            kval=2*a*rho*b*gp
            assert abs(np.trace(M)-(1+(1-gam)**2+kval*kval-2*gam*kval))<2e-10
            assert abs(np.linalg.det(M)-(1-gam)**2)<2e-10
            sink=max(abs(ev))<1-1e-10
            assert sink==(0<kval<2*gam)
            items.append((t,U,sink,kval,ev))
    return items

N=0
for a,gam in ((.55,.8),(.6,.8),(.65,.9),(.75,.5)):
    rho, b0, bo, bi=param(a,gam)
    print('a=%.3f gamma=%.3f b0=%.12f b_outer=%.12f b_inner=%.12f'%(a,gam,b0,bo,bi))
    for b,ns in ((b0*0.9,0),((b0+bo)/2,2),((bo+bi)/2,1),(bi*1.08,0)):
        rows=orbits(a,gam,b)
        if b<b0: assert not rows
        else: assert len(rows)==4 and sum(z[2] for z in rows)==ns
        N+=len(rows)
        print('  b=%.12f  half-turn-orbits=%d  sinks=%d'%(b,len(rows),sum(z[2] for z in rows)))
print('All independent finite-orbit checks: PASS, evaluated cycle orbits:',N)
