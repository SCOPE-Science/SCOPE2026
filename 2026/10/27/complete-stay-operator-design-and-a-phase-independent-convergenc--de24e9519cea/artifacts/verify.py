"""Finite-dimensional checks for balanced-ray Kraus completions.

Run: python verify.py  (requires NumPy and SymPy).
The universal result is proved analytically, not by these tests.
"""
import numpy as np
import sympy as s

# Rational example: L and R share only the line of e1; stationary ray is balanced.
L=s.Matrix([[s.Rational(1,4),s.Rational(1,4)],[0,s.Rational(1,4)]])
R=s.Matrix([[s.Rational(1,4),0],[0,0]])
C=s.eye(2)-L.T*L-R.T*R
beta=C[0,0]
assert beta==s.Rational(7,8)
assert C.det()>0
b=s.sqrt(beta)
c=C[0,1]/b
d=s.sqrt(C[1,1]-c**2)
B=s.Matrix([[b,c],[0,d]])
assert s.simplify(L.T*L+R.T*R+B.T*B-s.eye(2))==s.zeros(2)
assert s.simplify(sum([L[0,0]**2,R[0,0]**2,B[0,0]**2])-1)==0
eta=s.simplify(L[1,1]**2+R[1,1]**2+B[1,1]**2)
assert eta==s.Rational(209,224),eta
assert s.simplify(1-L[0,1]**2-R[0,1]**2-abs(C[0,1])**2/beta)==eta

def chan(rho):
    return L*rho*L.T+R*rho*R.T+B*rho*B.T
rho=s.Matrix([[0,0],[0,1]])
for n in range(2):
    assert s.simplify(rho[1,1]-eta**n)==0,(n,rho[1,1])
    rho=chan(rho)
# Complex two-phase family for the same C: theta changes the phase of b,
# phi independently changes the phase of d; the complement population rate is fixed.
cn=np.array(C,float)
ln=np.array(L,float)
rn=np.array(R,float)
for theta in [0.1,0.4,1.5,2.8]:
 for phi in [0.2,1.7,3.6]:
    bb=float(s.sqrt(beta))*np.exp(1j*theta)
    uu=cn[0,1]/np.conj(bb)
    dd=np.sqrt(cn[1,1]-abs(uu)**2)*np.exp(1j*phi)
    bn=np.array([[bb,uu],[0,dd]],dtype=complex)
    assert np.allclose(ln.T@ln+rn.T@rn+bn.conj().T@bn,np.eye(2),atol=1e-12)
    assert abs((abs(ln[1,1])**2+abs(rn[1,1])**2+abs(dd)**2)-float(eta))<1e-12
print('PASS: exact Kraus identities, unique-ray population rate, and 12 complex phase completions; eta=209/224')
