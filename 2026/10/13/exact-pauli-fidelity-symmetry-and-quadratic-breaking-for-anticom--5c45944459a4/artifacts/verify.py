#!/usr/bin/env python3
"""Independent matrix checks for the exact Pauli-adjoint fidelity theorem.

Requires numpy and scipy. This tests finite cases; it does not prove the theorem.
"""
import itertools
import math
import numpy as np
from scipy.linalg import expm

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]], complex)
Z = np.diag([1, -1]).astype(complex)
ONE = {'I': I, 'X': X, 'Y': Y, 'Z': Z}

def paulis(n):
    ans = {}
    for labels in itertools.product('IXYZ', repeat=n):
        label = ''.join(labels)
        value = np.array([[1]], dtype=complex)
        for letter in labels:
            value = np.kron(value, ONE[letter])
        ans[label] = value
    return ans

def traceinner(A,B):
    return float(np.trace(A.conj().T @ B).real / A.shape[0])

def anticommutes(A,B):
    return np.linalg.norm(A@B+B@A, ord='fro') < 1e-9

def compare(L_label, axes, alpha, tau):
    n = len(L_label)
    basis = paulis(n)
    L = basis[L_label]
    for a, q in axes.items():
        assert abs(q) > 0 and anticommutes(L, basis[a])
    pairs = list(axes)
    for k,a in enumerate(pairs):
        for b in pairs[:k]:
            assert anticommutes(basis[a], basis[b])
    R = sum((v*basis[k] for k,v in axes.items()), np.zeros_like(L))
    H = alpha*L+R
    omega = math.sqrt(alpha**2+sum(v*v for v in axes.values()))
    ss = math.sin(tau*omega)/omega
    cc = math.cos(tau*omega)
    U=expm(-1j*math.pi*L/4)
    E=U.conj().T@expm(-1j*tau*H)
    p = {k: abs(np.trace(M.conj().T@E)/len(L))**2 for k,M in basis.items()}
    assert abs(sum(p.values())-1)<3e-12
    p_formula={k:0.0 for k in basis}
    p_formula['I'*n]=0.5*(cc+alpha*ss)**2
    p_formula[L_label]=0.5*(cc-alpha*ss)**2
    seen=set()
    products=[]
    for k,Q in basis.items():
        if k in seen or not anticommutes(L,Q):
            continue
        Qprime=-1j*L@Q
        choices=[(b,traceinner(M,Qprime)) for b,M in basis.items()]
        choice=[(b,sgn) for b,sgn in choices if abs(abs(sgn)-1)<1e-10]
        assert len(choice)==1
        j,sgn=choice[0]
        seen.update((k,j))
        # Qprime is signed, not necessarily a canonical basis member.
        a=traceinner(Q,R)
        b=traceinner(Qprime,R)
        p_formula[k]=.5*(ss*(a+b))**2
        p_formula[j]=.5*(ss*(b-a))**2
        products.append(a*b)
    assert max(abs(p[k]-p_formula[k]) for k in basis)<2e-11, (L_label,axes,tau,p,p_formula)
    fidelity={k:sum(v*traceinner(M@Q@M,Q) for M,v in ((basis[j],w) for j,w in p.items())) for k,Q in basis.items()}
    defect={}
    for k,P in basis.items():
        UP=U@P@U.conj().T
        partners=[(j,traceinner(M,UP)) for j,M in basis.items() if abs(abs(traceinner(M,UP))-1)<1e-10]
        assert len(partners)==1
        kk=partners[0][0]
        defect[k]=fidelity[k]-fidelity[kk]
    rms=sum(d*d for d in defect.values()) / len(basis)
    expect=8*ss**4*sum(v*v for v in products)
    assert abs(rms-expect)<3e-10,(rms,expect,L_label,axes)
    return rms,expect,defect,p_formula

def main():
    configurations=[
      ('Z',{'X':0.3}, 0.7, 0.8),
      ('Z',{'X':0.3,'Y':-0.2},0.7,0.8),
      ('Z',{'X':0.3,'Y':-0.2},0.7,math.pi/math.sqrt(.49+.09+.04)),
      ('ZZ',{'XI':0.3,'YI':0.2,'ZX':0.4},0.7,1.1),
      ('ZZ',{'XI':0.3,'YZ':-0.4},0.7,.83),
      ('ZZ',{'XI':0.3,'YZ':-0.4},0.7,2.31),
    ]
    rng=np.random.default_rng(88237)
    for i in range(100):
        vals=rng.uniform(-2,2,size=4)
        if i%2:
            configurations.append(('Z',{'X':vals[0],'Y':vals[1]},vals[2],vals[3]))
        else:
            configurations.append(('ZZ',{'XI':vals[0],'YZ':vals[1]},vals[2],vals[3]))
    max_err=0.0
    for L,axes,alpha,tau in configurations:
        rms,expected,_,_=compare(L,axes,alpha,tau)
        max_err=max(max_err,abs(rms-expected))
    assert max_err<3e-10
    print('VERIFY_OK',len(configurations),'matrix experiments; max RMS-square discrepancy',format(max_err,'.3g'))

if __name__=='__main__':main()
