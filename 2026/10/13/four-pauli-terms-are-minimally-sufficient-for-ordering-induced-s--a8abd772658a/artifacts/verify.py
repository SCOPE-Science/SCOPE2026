import numpy as np

I2=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],dtype=complex)
Y=np.array([[0,-1j],[1j,0]],dtype=complex)
Z=np.array([[1,0],[0,-1]],dtype=complex)
kron=np.kron
P=kron(X,I2)
Q=kron(Y,I2)
R=kron(I2,Z)
PR=P@R
QR=Q@R
Id=np.eye(4,dtype=complex)

def comm(A,B): return A@B-B@A

def exp_pauli(c,A,h):
    return np.cos(c*h)*Id-1j*np.sin(c*h)*A

def exp_herm(H,h):
    w,V=np.linalg.eigh(H)
    return (V*np.exp(-1j*h*w))@V.conj().T

a=0.7
b=-0.4
terms=[a*P,b*Q,b*QR,a*PR]
# Canonical algebraic assumptions.
assert np.linalg.norm(P@P-Id)<1e-12
assert np.linalg.norm(Q@Q-Id)<1e-12
assert np.linalg.norm(R@R-Id)<1e-12
assert np.linalg.norm(P@Q+Q@P)<1e-12
assert np.linalg.norm(P@R-R@P)<1e-12
assert np.linalg.norm(Q@R-R@Q)<1e-12
# The quadratic BCH commutator sum for the displayed order vanishes.
C=sum((comm(terms[i],terms[j]) for i in range(4) for j in range(i+1,4)),np.zeros((4,4),complex))
assert np.linalg.norm(C)<1e-12
# Sector identities: exact on R=-1, Strang on R=+1.
Pplus=(Id+R)/2
Pminus=(Id-R)/2
H=a*P+b*Q+a*PR+b*QR
for h in [0.17,0.09,0.04]:
    S=exp_pauli(a,P,h)@exp_pauli(b,Q,h)@exp_pauli(b,QR,h)@exp_pauli(a,PR,h)
    Splus=exp_pauli(a,P,h)@exp_pauli(2*b,Q,h)@exp_pauli(a,P,h)
    assert np.linalg.norm(Pplus@(S-Splus))<2e-12
    assert np.linalg.norm(Pminus@(S-Id))<2e-12
    T=exp_herm(H,h)
    assert np.linalg.norm(Pminus@(T-Id))<2e-12
# The local error has the predicted nonzero cubic coefficient.
expected=(4*abs(a*b)/3)*np.sqrt(a*a+4*b*b)
ratios=[]
for h in [2e-2,1e-2,5e-3,2.5e-3]:
    S=exp_pauli(a,P,h)@exp_pauli(b,Q,h)@exp_pauli(b,QR,h)@exp_pauli(a,PR,h)
    T=exp_herm(H,h)
    err=np.linalg.norm(S-T,2)
    ratios.append(err/h**3)
assert abs(ratios[-1]-expected)/expected < 5e-3, (ratios,expected)
# Repeated-step error is consistent with second-order global convergence.
t=0.7
scaled=[]
for r in [40,80,160]:
    h=t/r
    S=exp_pauli(a,P,h)@exp_pauli(b,Q,h)@exp_pauli(b,QR,h)@exp_pauli(a,PR,h)
    Sr=np.linalg.matrix_power(S,r)
    T=exp_herm(H,t)
    scaled.append(np.linalg.norm(Sr-T,2)*r*r)
assert max(scaled)/min(scaled) < 1.08, scaled
print('VERIFY_OK')
print('cubic_ratio', ratios[-1], 'predicted', expected)
print('global_r2_scaled', scaled)
