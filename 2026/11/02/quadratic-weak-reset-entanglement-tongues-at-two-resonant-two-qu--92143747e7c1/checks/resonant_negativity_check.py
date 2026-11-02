"""Exact algebra and numerical checks for a two-qubit reset-gate resonance.

Run with Python 3, NumPy, SciPy, and SymPy.
This code checks specific finite algebraic identities and numerical samples;
it does not independently establish publication priority.
"""
import numpy as np
import sympy as sp
from scipy.linalg import eigh

I = sp.I
s = sp.sqrt(2)
p, c = sp.symbols('p c', real=True)
H = sp.Matrix([
    [2-s, 2-s, -I-s, I-s],
    [2-s, 2-s, I-s, -I-s],
    [I-s, -I-s, 2+s, 2+s],
    [-I-s, I-s, 2+s, 2+s],
])
spectrum = (-2, 0, 2, 8)
E = sp.eye(4)
projectors = []
for j, lam in enumerate(spectrum):
    P = E
    for k, mu in enumerate(spectrum):
        if k != j:
            P = P * (H - mu*E) / (lam - mu)
    projectors.append(P.applyfunc(sp.simplify))
assert sp.simplify(sum(projectors, sp.zeros(4)) - E) == sp.zeros(4)
assert sp.simplify(sum((v * Q for v, Q in zip(spectrum, projectors)), sp.zeros(4)) - H) == sp.zeros(4)
seed = sp.zeros(4)
seed[0, 0] = 1
z = sp.Matrix([0, 0, 1, 1]) / sp.sqrt(2)
A0_expected = sp.Matrix([[3,1,0,0],[1,3,0,0],[0,0,1,-1],[0,0,-1,1]])/8

def pt(A):
    return sp.Matrix(4,4,lambda a,b:A[2*(a//2)+(b%2), 2*(b//2)+(a%2)])

def phase(d, mult):
    return (1, I, -1, -I)[(mult*d//2) % 4]

for mult in (1, 3):
    rho_exact = sp.zeros(4)
    B0, B1, B2 = (sp.zeros(4), sp.zeros(4), sp.zeros(4))
    for i, li in enumerate(spectrum):
        for j, lj in enumerate(spectrum):
            d = li - lj
            q = phase(d, mult)
            pair = projectors[i] * seed * projectors[j]
            rho_exact += (p/(1-(1-p)*q)) * pair
            if q == 1:
                h0, h1, h2 = 1, I*d*c, -d*d*c*c-I*d*c
            else:
                h0, h1, h2 = 0, 1/(1-q), -q/(1-q)**2
            B0 += h0*pair
            B1 += h1*pair
            B2 += h2*pair
    A = pt(rho_exact).applyfunc(sp.cancel)
    determinant = sp.factor(A.det(method='domain-ge'))
    expected_det = -p**2 * (1-p)**3 / (16 * (2-p) * ((1-p)**2+1)**2)
    assert sp.simplify(determinant - expected_det) == 0
    A0, A1, A2 = [pt(M).applyfunc(sp.simplify) for M in (B0, B1, B2)]
    assert A0 == A0_expected
    assert sp.simplify((z.T*A1*z)[0]) == 0
    zz = z*z.T
    # Moore-Penrose inverse, since A0 is Hermitian and has kernel span{z}.
    A0_plus = A0*(A0+zz).inv()**2
    direct = sp.simplify((z.T*A2*z)[0])
    mixing = sp.simplify((z.T*A1*A0_plus*A1*z)[0])
    assert direct == 8*c**2
    assert mixing == 4*c**2 + sp.Rational(1,4)
    assert sp.simplify(direct-mixing-(4*c**2-sp.Rational(1,4))) == 0
    print('resonance theta =', ('pi/4' if mult==1 else '3pi/4'),
          '| exact determinant and second-order coefficient: PASS')

H_np = np.array(H.evalf(),dtype=complex)
eigenvalues, U = eigh(H_np)
seed_np = np.zeros((4,4),complex); seed_np[0,0] = 1
b = U.conj().T[:,0]
P_np = np.outer(b,b.conj())

def stationary(p_value, theta):
    phases = np.exp(1j*theta*(eigenvalues[:,None]-eigenvalues[None,:]))
    rho_eig = p_value*P_np/(1-(1-p_value)*phases)
    return U@rho_eig@U.conj().T

def pt_np(A):
    return A.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)

for mult in (1,3):
    for c_value in (-0.4,-0.2,0.0,0.2,0.4):
        target = 4*c_value**2 - 0.25
        for p_value in (0.01,0.005,0.002):
            theta = mult*np.pi/4+c_value*p_value**2
            actual = np.linalg.eigvalsh(pt_np(stationary(p_value,theta)))[0]/p_value**2
            assert abs(actual-target) < 0.0075
    print('resonance',mult,'| finite reset/detuning samples: PASS')

# Check the stationary spectral resolvent against independent channel iteration.
prob = 0.12; theta = np.pi/4+0.2*prob**2
u = U@np.diag(np.exp(1j*theta*eigenvalues))@U.conj().T
state = seed_np.copy()
for _ in range(400):
    state = prob*seed_np+(1-prob)*u@state@u.conj().T
assert np.linalg.norm(state-stationary(prob,theta)) < 1e-12
print('independent iterative stationary channel: PASS')
