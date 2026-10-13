"""Finite-dimensional cross-checks for the rank-deficient photon coincidence theorem.

Dependencies: Python 3, numpy. Every finite check is illustrative; the theorem
for arbitrary photon number follows from the separate algebraic proof.
"""
from itertools import permutations
from math import factorial, sqrt
import numpy as np


def gram_from_vectors(vecs):
    V=np.column_stack(vecs)
    return V.conj().T@V


def amplitudes(U):
    n=U.shape[0]
    ps=list(permutations(range(n)))
    A=np.array([np.prod([U[p[j],j] for j in range(n)]) for p in ps],complex)
    return ps,A


def coincidence_two_ways(U,vecs):
    n=len(vecs)
    ps,A=amplitudes(U)
    # Direct internal-tensor final amplitude as a sum over all path assignments.
    v=np.stack([x/np.linalg.norm(x) for x in vecs])
    tensor=np.zeros((v.shape[1],)*n,complex)
    for p,a in zip(ps,A):
        product=v[p.index(0)]
        for k in range(1,n):
            product=np.multiply.outer(product,v[p.index(k)])
        tensor+=a*product
    P_direct=np.vdot(tensor,tensor).real
    # Alternative Gram-of-permutations double sum, not tensor materialization.
    G=gram_from_vectors([x/np.linalg.norm(x) for x in vecs])
    P_gram=0j
    for p,a in zip(ps,A):
        for q,b in zip(ps,A):
            g=1.+0j
            for k in range(n):
                g*=G[q.index(k),p.index(k)]
            P_gram+=np.conj(b)*a*g
    return P_direct,P_gram.real


def householder(n):
    w=np.arange(1,n+1,dtype=float)
    return np.eye(n)-2*np.outer(w,w)/np.dot(w,w)


def check():
    tests=0
    for n in (3,4,5):
        basis=np.eye(n-1)
        vecs=[basis[j].astype(complex) for j in range(n-1)]
        vecs.append(np.arange(1,n,dtype=float).astype(complex))
        for U in (np.eye(n),householder(n),
                  np.linalg.qr(np.arange(n*n).reshape(n,n)+np.eye(n)*7.0)[0]):
            p,q=coincidence_two_ways(U,vecs)
            assert abs(p-q)<1e-10,(n,p,q)
            assert p>1e-12,(n,p)
            tests+=1
        # Exact duplicate pair admits an embedded HOM dip.
        vecs[-1]=vecs[-2].copy()
        B=np.eye(n,dtype=complex)
        B[-2:,-2:]=np.array([[1,1],[1,-1]],complex)/sqrt(2)
        p,q=coincidence_two_ways(B,vecs)
        assert abs(p)<1e-12 and abs(q)<1e-12,(n,p,q)
        tests+=1
    # Check the algebraic van der Waerden separation in the stated range.
    for n in range(3,26):
        # Logarithms avoid overflow in a certificate check only.
        from math import lgamma,log
        assert 2*lgamma(n+1) > n*log(n)
    # Inspect the n=3 Gram quotient and its explicit spectral gap.
    n=3; e=np.eye(2,dtype=complex)
    vecs=[e[0],e[1],(e[0]+e[1])/sqrt(2)]
    ps,A=amplitudes(householder(n)); G=gram_from_vectors(vecs)
    J=np.array([[np.prod([G[q.index(k),p.index(k)] for k in range(n)])
                 for q in ps] for p in ps],complex)
    eigen=np.linalg.eigvalsh(J)
    assert abs(eigen[0])<1e-11 and eigen[1]>1e-8,eigen
    P_direct,P_gram=coincidence_two_ways(householder(n),vecs)
    bound=eigen[1]*(factorial(n)/n**n -1/factorial(n))
    assert P_direct+1e-11>=bound>0,(P_direct,bound)
    print('VERIFY_OK direct_tensor_gram='+str(tests)
          +' HOM_boundary=3 positive_orbit_quotient=passed'
          +' finite_factorial_gap=passed')

if __name__=='__main__':
    check()
