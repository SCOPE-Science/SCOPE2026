"""Matrix-level tests of the finite-dwell two-ray qubit channel."""
import math
import numpy as np
from scipy.linalg import expm

I = np.eye(2, dtype=complex)
X = np.array([[0,1],[1,0]],complex)
Y = np.array([[0,-1j],[1j,0]],complex)
Z = np.array([[1,0],[0,-1]],complex)
PAULI = [X,Y,Z]
L1 = X + 1j / math.sqrt(2) * Y
U = -1j*(X+Z)/math.sqrt(2)
L2 = U @ L1 @ U.conj().T

def lindbladian(L):
    A = L.conj().T @ L
    return np.kron(L.conj(), L) - (np.kron(I,A)+np.kron(A.T,I))/2

def vector(a):
    return np.array(a,dtype=complex).reshape(4,order='F')

def matrix(v):
    return v.reshape((2,2),order='F')

def apply(superop,a):
    return matrix(superop@vector(a))

def choi(superop):
    out = np.zeros((4,4),complex)
    for i in range(2):
        for j in range(2):
            e = np.zeros((2,2),complex)
            e[i,j]=1
            out += np.kron(e,apply(superop,e))/2
    return out

def pt_b(m):
    return m.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)

def bloch(a):
    return np.array([np.trace(a@p).real for p in PAULI])

def f_drift(h):
    v=math.exp(-h)
    k=2*math.sqrt(2)/3
    w=k*(-math.expm1(-3*h))/(-math.expm1(-4*h))
    return np.array([w,0,v*w])

def f_symmetric(h):
    v=math.exp(-h)
    k=2*math.sqrt(2)/3
    den=-math.expm1(-4*h)
    x=k*math.exp(-h/2)*(-math.expm1(-3*h))/den
    z=k*(-math.expm1(-3*h/2))*(1+math.exp(-5*h/2))/den
    return np.array([x,0,z])

def eb_threshold(r):
    d=math.sqrt(max(0,1-np.dot(r,r)))
    return d/(2+d)

def reset_choi(a,r):
    tau=(I+sum(r[i]*PAULI[i] for i in range(3)))/2
    return a*np.outer(np.array([1,0,0,1])/math.sqrt(2),np.array([1,0,0,1])/math.sqrt(2))+(1-a)*np.kron(I/2,tau)

D1=lindbladian(L1)
D2=lindbladian(L2)
checks=0
for h in [0.003,0.015,0.05,0.14,0.25,0.48,0.7,1.1,2.5]:
    E1=expm(h*D1);E2=expm(h*D2)
    standard=E2@E1
    symmetric=expm(h/2*D1)@E2@expm(h/2*D1)
    for label,S,r in [('standard',standard,f_drift(h)),('symmetric',symmetric,f_symmetric(h))]:
        a=math.exp(-4*h)
        tau=(I+sum(r[i]*PAULI[i] for i in range(3)))/2
        assert np.max(np.abs(apply(S,I/2)-((1-a)*tau+a*I/2)))<1e-12
        checks+=1
        for p in PAULI:
            assert np.max(np.abs(apply(S,p)-a*p))<1e-12
            checks+=1
        assert np.max(np.abs(choi(S)-reset_choi(a,r)))<2e-12
        checks+=1
        assert abs(np.dot(r,r))<1
        checks+=1
        t=eb_threshold(r)
        n=math.ceil(math.log(1/t)/(4*h))
        for k in [max(0,n-1),n,n+1]:
            Sk=np.linalg.matrix_power(S,k)
            mineig=np.linalg.eigvalsh(pt_b(choi(Sk)))[0]
            cond=math.exp(-4*h*k)<=t
            if cond: assert mineig>-2e-10,(label,h,k,mineig)
            else: assert mineig<2e-10,(label,h,k,mineig)
            checks+=1
        if label=='standard':
            v=math.exp(-h)
            analytic=(1-v)**2*(v*v+4*v+1)/(9*(1+v)**2*(1+v*v))
            assert abs(1-np.dot(r,r)-analytic)<2e-13
            checks+=1
    if h<.015:
        assert abs(np.linalg.norm(f_drift(h)-np.array([1/math.sqrt(2),0,1/math.sqrt(2)])) - 0.5*h)<.1*h
    checks+=1
for h in [1e-2,5e-3,1e-3,5e-4]:
    rd=f_drift(h); rs=f_symmetric(h)
    n=np.array([1/math.sqrt(2),0,1/math.sqrt(2)])
    assert abs((1-np.dot(rd,rd))/h**2-1/12)<2e-4
    assert abs((1-np.dot(rs,rs))/h**2-1/12)<2e-4
    assert abs(np.linalg.norm(rd-n)/h-.5)<0.004
    assert abs(np.linalg.norm(rs-n)/h**2-math.sqrt(37)/24)<.01
    checks+=4
print('PASS',checks,'direct Lindblad, Choi, threshold, and asymptotic checks')
