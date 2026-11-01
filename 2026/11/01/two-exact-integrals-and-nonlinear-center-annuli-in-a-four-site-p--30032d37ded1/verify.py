"""Reproduce algebraic reductions and invariant identities for a four-site phase oscillator ring."""
import math
import random
import sympy as sp
import numpy as np

v,z,p,a=sp.symbols('v z p a',real=True)
F=sp.Matrix([-2*sp.sin(v)*sp.cos(z)*sp.cos(p+a),
             -2*sp.sin(z)*sp.cos(v)*sp.cos(a-p),
             -4*sp.cos(a)*sp.sin(p)*sp.cos(v)*sp.cos(z)])
H=sp.log(sp.sin(v))+sp.log(sp.sin(z))-sp.log(sp.sin(p))
J=sp.log(sp.sin(v))-sp.log(sp.sin(z))+p*sp.tan(a)
vars=(v,z,p)
assert sp.trigsimp(sum(sp.diff(H,t)*F[i] for i,t in enumerate(vars)))==0
assert sp.trigsimp(sum(sp.diff(J,t)*F[i] for i,t in enumerate(vars)))==0
cross=sp.Matrix([sp.diff(H,t) for t in vars]).cross(sp.Matrix([sp.diff(J,t) for t in vars]))
assert all(sp.trigsimp(F[i]-2*sp.cos(a)*sp.sin(p)*sp.sin(v)*sp.sin(z)*cross[i])==0 for i in range(3))
M=F.jacobian(vars).subs({v:sp.pi/2,z:sp.pi/2})
assert sp.simplify(M[0,1]-2*sp.cos(p+a))==0
assert sp.simplify(M[1,0]-2*sp.cos(a-p))==0
assert sp.simplify(M[2,2])==0
rng=random.Random(20261029)
for _ in range(280):
    al=rng.uniform(.06,1.48); vv=rng.uniform(.06,3.08); zz=rng.uniform(.06,3.08); pp=rng.uniform(.06,3.08)
    theta=np.array([vv,pp+zz,-vv,pp-zz],dtype=float)
    original=np.array([math.sin(theta[(i-1)%4]-theta[i]+al)+math.sin(theta[(i+1)%4]-theta[i]+al) for i in range(4)])
    derived=np.array([(original[0]-original[2])/2,(original[1]-original[3])/2,(original[1]+original[3]-original[0]-original[2])/2])
    rhs=np.array([float(x) for x in F.subs({a:al,v:vv,z:zz,p:pp})])
    assert max(abs(derived-rhs))<4e-14
    dH=derived[0]/math.tan(vv)+derived[1]/math.tan(zz)-derived[2]/math.tan(pp)
    dJ=derived[0]/math.tan(vv)-derived[1]/math.tan(zz)+math.tan(al)*derived[2]
    assert abs(dH)<1e-12 and abs(dJ)<1e-12
    # Normal stability threshold at central equilibrium.
    phi0=rng.uniform(.05,3.08)
    det=4*math.cos(phi0+al)*math.cos(al-phi0)
    assert (det<0)==(abs(math.cos(phi0))<math.sin(al))
print('PASS: two exact conservation identities, Nambu factor, central Jacobian, 280 independent four-phase numeric reductions')
