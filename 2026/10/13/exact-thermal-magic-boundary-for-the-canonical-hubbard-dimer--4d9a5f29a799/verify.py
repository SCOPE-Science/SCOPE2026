#!/usr/bin/env python3
"""Exact four-qubit algebra and finite-sample checks for Hubbard dimer magic boundary.
Requires SymPy >= 1.12; no source downloads or external data.
"""
import sympy as s
from itertools import product
I2=s.eye(2)
X=s.Matrix([[0,1],[1,0]])
Y=s.Matrix([[0,-s.I],[s.I,0]])
Z=s.diag(1,-1)
P={'I':I2,'X':X,'Y':Y,'Z':Z}
def W(word):
    a=s.Matrix([[1]])
    for c in word:a=s.kronecker_product(a,P[c])
    return a
E=s.eye(16)
def ket(word):return E[:,int(word,2)]
u=(ket('1100')+ket('0011'))/s.sqrt(2)
v=(ket('1001')-ket('0110'))/s.sqrt(2)
d=(ket('1100')-ket('0011'))/s.sqrt(2)
r=(ket('1001')+ket('0110'))/s.sqrt(2)
B=s.Matrix.hstack(u,v,d,r)
assert s.simplify(B.T*B)==s.eye(4)
G1=-W('ZIZI');G2=-W('IZIZ');G3=W('XXXX')*W('ZZII')
LZ=W('ZZII');LX=-W('ZXIX')
for g in (G1,G2,G3):
    assert g==g.H and g*g==s.eye(16)
for a,b in product((G1,G2,G3),repeat=2):assert a*b==b*a
assert B.T*G1*B==s.eye(4)
assert B.T*G2*B==s.eye(4)
assert B.T*G3*B==s.diag(1,1,-1,-1)
assert B.T*LZ*B==s.diag(1,-1,1,-1)
assert B.T*LX*B==s.Matrix([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]])
Pi=((s.eye(16)+G1)*(s.eye(16)+G2)*(s.eye(16)+G3))/8
assert s.simplify(Pi-(u*u.T+v*v.T))==s.zeros(16)
assert s.simplify((d*d.T)**2-d*d.T)==s.zeros(16)
assert s.simplify((r*r.T)**2-r*r.T)==s.zeros(16)
# Each source eigenvector is the +/- eigenstate of a logical-qubit Hamiltonian.
q=s.symbols('q',positive=True)
g=s.sqrt(1+q*q)
dplus=q+g; dminus=q-g
assert s.simplify(dplus*dminus+1)==0
for delta,sgn in ((dplus,1),(dminus,-1)):
    a=(u+delta*v)/s.sqrt(1+delta**2)
    ax=s.simplify((a.T*LX*a)[0]);az=s.simplify((a.T*LZ*a)[0])
    assert s.simplify(ax-sgn/g)==0,(delta,ax)
    assert s.simplify(az+sgn*q/g)==0,(delta,az)
# Fully reconstruct Hubbard Hamiltonian using CAR/Jordan-Wigner operators.
raise_op=s.Matrix([[0,0],[1,0]])
lower_op=s.Matrix([[0,1],[0,0]])
def fermion_annihilator(j):
    a=s.Matrix([[1]])
    for k in range(4):a=s.kronecker_product(a,Z if k<j else lower_op if k==j else I2)
    return a
c=[fermion_annihilator(j) for j in range(4)]
hop=-(c[0].H*c[2]+c[2].H*c[0]+c[1].H*c[3]+c[3].H*c[1])
double=(c[0].H*c[0])*(c[1].H*c[1])+(c[2].H*c[2])*(c[3].H*c[3])
assert B.T*hop*B==s.Matrix([[0,-2,0,0],[-2,0,0,0],[0,0,0,0],[0,0,0,0]])
assert B.T*double*B==s.diag(1,0,1,0)
H=hop+4*q*double
for delta,ev in ((dplus,2*q-2*g),(dminus,2*q+2*g)):
    a=u+delta*v
    assert all(s.simplify(vv)==0 for vv in H*a-ev*a)
assert s.simplify(H*d-4*q*d)==s.zeros(16,1)
assert s.simplify(H*r)==s.zeros(16,1)
# Verify conditional two-state sector analytically against its energy gap.
T=s.symbols('T',positive=True)
E_minus=2*q-2*g;E_plus=2*q+2*g
assert s.simplify(E_plus-E_minus-4*g)==0
for qq in (s.Rational(1,4),s.Rational(1,2),s.Integer(1),s.Integer(2),s.Integer(7)):
    gg=s.sqrt(1+qq**2)
    dp=qq+gg;dm=qq-gg
    ap=(u+dp*v)/s.sqrt(1+dp**2)
    am=(u+dm*v)/s.sqrt(1+dm**2)
    assert s.simplify((ap.T*am)[0])==0
    for tt in (s.Rational(1,2),s.Integer(2),s.Integer(5),s.Integer(10)):
        w=s.exp(-4*gg/tt)
        sig=(ap*ap.T+w*am*am.T)/(1+w)
        x=s.simplify(s.trace(sig*LX))
        z=s.simplify(s.trace(sig*LZ))
        expect=s.tanh(2*gg/tt)
        assert abs(float(s.N(x-expect/gg,20)))<1e-12
        assert abs(float(s.N(z+qq*expect/gg,20)))<1e-12
        # Direct compare reduced 2d computational density matrix to Bloch formula.
        C=s.Matrix.hstack(u,v)
        effective=s.simplify(C.T*sig*C)
        pred=(s.eye(2)+(expect/gg)*X-(qq*expect/gg)*Z)/2
        assert all(abs(complex(s.N(vv,20)))<1e-12 for vv in effective-pred)
        boundary=float(gg/(1+qq))
        assert boundary<1
# Exact temperature-boundary substitution and derivative identities.
Lc=s.atanh(g/(1+q))
assert s.simplify((1+q)*s.tanh(Lc)/g-1)==0
assert s.simplify(s.diff(Lc,q)-(q-1)/(2*q*g))==0
assert s.simplify(s.diff(g/(1+q),q)-(q-1)/(g*(1+q)**2))==0
# For no repulsion, the logical line is the stabilizer x-axis.
assert s.limit((1+q)/g,q,0,dir='+')==1
# Critical-temperature strict increase and asymptotics follow analytically in RESULT.md;
# finite differentiation here independently checks the branch numerically.
fn=(2*g)/s.atanh(g/(1+q))
assert s.simplify(g/(1+q)-s.sqrt(1+1/q**2)/(1+1/q))==0
assert s.simplify(fn-q*fn.subs(q,1/q))==0
last=0.0
for qv in (0.00001,0.0001,0.001,0.01,0.1,0.25,0.5,1,2,4,10,100,1000):
    val=float(fn.subs(q,qv))
    assert val>last,(qv,val,last)
    last=val
print('VERIFY_OK: Clifford code, projectors, exact logical Bloch, Gibbs mixtures, boundary samples')
