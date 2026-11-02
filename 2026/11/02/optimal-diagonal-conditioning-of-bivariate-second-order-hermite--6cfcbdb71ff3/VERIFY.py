"""Reproduce the second-chaos Gram scaling identities and numerical checks.

Requires Python 3, SymPy and NumPy. Algebraic identities are symbolic;
randomized examples are diagnostics, not a substitute for global optimality proof.
"""
import sympy as sp
import numpy as np

r = sp.symbols('r', real=True)
a = 1/(1-r**2)
b = -r/(1-r**2)
G = sp.Matrix([[2*a*a,2*a*b,2*b*b],
               [2*a*b,a*a+b*b,2*a*b],
               [2*b*b,2*a*b,2*a*a]])
D = sp.diag(1,sp.sqrt(2),1)
H = sp.simplify(D*G*D)
v1=sp.Matrix([1,sp.sqrt(2),1])/2
v2=sp.Matrix([1,-sp.sqrt(2),1])/2
v3=sp.Matrix([1,0,-1])/sp.sqrt(2)
for v,lam in [(v1,2/(1+r)**2),(v2,2/(1-r)**2),(v3,2/(1-r*r))]:
    assert all(sp.simplify(x)==0 for x in H*v-lam*v)
assert sp.simplify(G.det()-4/(1-r*r)**3)==0, 'Gram determinant failed'
# Normalized Jacobi gram: u = -sqrt(2)*r/sqrt(1+r^2)
u=-sp.sqrt(2)*r/sp.sqrt(1+r*r)
C=sp.Matrix([[1,u,r*r],[u,1,u],[r*r,u,1]])
assert all(sp.simplify(C[i,j]- (G[i,j]/sp.sqrt(G[i,i]*G[j,j])))==0 for i in range(3) for j in range(3))
assert sp.simplify(C.det()-(1-r*r)**3/(1+r*r))==0
lam_plus=(2+r*r+sp.sqrt(r**4+8*u*u))/2
lam_minus=(2+r*r-sp.sqrt(r**4+8*u*u))/2
assert sp.simplify(lam_plus*lam_minus-(1-r*r)**2/(1+r*r))==0
assert sp.simplify(lam_plus+lam_minus-(2+r*r))==0
# lplus at r->1 = 3, lminus ~ (1-r^2)^2/6, optimize ~16/(1-r^2)^2.
assert sp.limit(lam_plus,r,1,dir='-')==3
assert sp.limit((1-r*r)**2/lam_minus,r,1,dir='-')==6
assert sp.limit((lam_plus/lam_minus)*((1-r)/(1+r))**2,r,1,dir='-')==sp.Rational(9,8)
# Sample diagonal scales and compare against rigorous minimum.
rng=np.random.default_rng(20261028)
count=0
for rho in (-.97,-.73,-.31,0.0,.07,.43,.89,.995):
    mat=np.array(G.subs(r,sp.Rational(str(rho)))).astype(float)
    opt=((1+abs(rho))/(1-abs(rho)))**2
    d0=np.diag([1,np.sqrt(2),1])
    cond0=np.linalg.cond(d0@mat@d0)
    assert abs(cond0/opt-1)<2e-8, (rho,cond0,opt)
    for _ in range(400):
        dd=np.diag(np.exp(rng.normal(size=3)))
        cond=np.linalg.cond(dd@mat@dd)
        assert cond>=opt*(1-5e-8), (rho,cond,opt)
        count+=1
print(f'PASS: 5 eigen/determinant identities, Jacobi asymptotic 9/8, {count} random SPD diagonal tests')
