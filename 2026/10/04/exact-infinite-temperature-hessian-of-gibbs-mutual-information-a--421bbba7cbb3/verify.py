#!/usr/bin/env python3
import math
import numpy as np

I2=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],dtype=complex)
Y=np.array([[0,-1j],[1j,0]],dtype=complex)
Z=np.array([[1,0],[0,-1]],dtype=complex)

def kron(a,b): return np.kron(a,b)

def ptrace_b(M):
    T=M.reshape(2,2,2,2)
    return np.trace(T,axis1=1,axis2=3)

def ptrace_a(M):
    T=M.reshape(2,2,2,2)
    return np.trace(T,axis1=0,axis2=2)

def entropy(rho):
    vals=np.linalg.eigvalsh((rho+rho.conj().T)/2).real
    vals=np.clip(vals,1e-300,None)
    return float(-np.sum(vals*np.log(vals)))

def gibbs(H,beta):
    w,V=np.linalg.eigh(H)
    u=np.exp(-beta*(w-w.min()))
    return (V*u)@V.conj().T/u.sum()

def mutual_information(rho):
    return entropy(ptrace_b(rho))+entropy(ptrace_a(rho))-entropy(rho)

def hint(H):
    tr=np.trace(H).real
    return H-kron(ptrace_b(H)/2,I2)-kron(I2,ptrace_a(H)/2)+(tr/4)*np.eye(4)

# Deterministic noncommuting Hamiltonian with both local and interaction pieces.
H=(0.7*kron(X,I2)-0.4*kron(I2,Z)+0.3*kron(X,Z)
   -0.2*kron(Y,Y)+0.5*kron(Z,X)+0.11*np.eye(4))
K=hint(H)
assert np.linalg.norm(ptrace_b(K)) < 1e-12
assert np.linalg.norm(ptrace_a(K)) < 1e-12
coef=float(np.trace(K@K).real/8.0)
ratios=[]
for beta in (0.02,0.01,0.005,0.0025):
    ratios.append(mutual_information(gibbs(H,beta))/(beta*beta))
# First-order convergence of ratio to coefficient is sufficient here.
assert abs(ratios[-1]-coef) < 3e-3, (ratios,coef)
assert abs(ratios[-1]-coef) < abs(ratios[0]-coef), (ratios,coef)

# Pauli crossing coefficient: local pieces must drop out.
pauli_cross={('X','Z'):0.3,('Y','Y'):-0.2,('Z','X'):0.5}
coef_pauli=0.5*sum(c*c for c in pauli_cross.values())
assert abs(coef-coef_pauli) < 1e-12, (coef,coef_pauli)

# Exact one-bond Ising formula and quadratic limit.
def ising_exact(x):
    return x*math.tanh(x)-math.log(math.cosh(x))
for x in (0.1,0.05,0.02,0.01):
    assert ising_exact(x) > 0
assert abs(ising_exact(0.01)/(0.01**2)-0.5) < 3e-5
# m bonds add exactly.
m=7; x=0.13
assert abs(m*ising_exact(x) - sum(ising_exact(x) for _ in range(m))) < 1e-15
print('VERIFY_OK')
