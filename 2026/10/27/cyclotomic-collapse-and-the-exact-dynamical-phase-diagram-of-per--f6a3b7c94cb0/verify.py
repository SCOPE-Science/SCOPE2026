"""Finite algebra diagnostics for cyclotomic periodic shifts.

These tests do not prove the infinite-dimensional statements.
"""
import cmath
import numpy as np

def check():
    total=0
    for q in range(2,9):
        zeta=cmath.exp(2j*cmath.pi/q)
        for N in [2*q,3*q,4*q+1]:
            k=np.arange(N)
            for phase in [0.2,0.9,1.8]:
                a=(0.3+0.2*q)*cmath.exp(1j*phase)
                weights=np.array([(0.8+0.16*(j+1))*cmath.exp(1j*(phase+0.13*j)) for j in range(q)],dtype=complex)
                D=np.diag(a*zeta**k)
                B=np.zeros((N,N),dtype=complex)
                for j in range(N-1): B[j,j+1]=weights[j%q]
                T=D+B
                W=np.prod(weights)
                assert np.allclose(np.linalg.matrix_power(T,q),a**q*np.eye(N)+np.linalg.matrix_power(B,q),atol=1e-7,rtol=1e-7)
                total+=1
                Q=np.linalg.matrix_power(B,q)
                for j in range(N-q):
                    assert abs(Q[j,j+q]-W)<1e-7
                    total+=1
                weights2=np.array([w*cmath.exp(1j*(j+1)*0.23) for j,w in enumerate(weights)],dtype=complex)
                # A phase-conserving tuple with the same product modulus.
                s=np.ones(N,dtype=complex)
                for j in range(N-1): s[j+1]=s[j]*weights2[j%q]/weights[j%q]
                assert max(abs(s))<10 and min(abs(s))>0.1
                B2=np.zeros((N,N),dtype=complex)
                for j in range(N-1): B2[j,j+1]=weights2[j%q]
                S=np.diag(s)
                assert np.allclose(np.linalg.solve(S,T@S),D+B2,atol=1e-7)
                total+=1
    print(f'PASS: {total} finite algebraic assertions (cyclotomic identity, periodic product, similarity).')
if __name__=='__main__': check()
