"""Finite-block checks for affine matrix Fock--Sobolev Toeplitz self-commutators.
These checks are supplementary and do not certify the infinite-dimensional theorem.
"""
import numpy as np

def shifts(m,L):
    J=np.zeros((L,L),dtype=complex)
    for n in range(L-1): J[n+1,n]=np.sqrt(n+m+1)
    return J

def blocks(A,B,m,L):
    J=shifts(m,L);T=np.kron(J,A)+np.kron(J.conj().T,B)
    C=T.conj().T@T - T@T.conj().T
    P=A.conj().T@A-B@B.conj().T
    Q=B.conj().T@B-A@A.conj().T
    G=P+Q
    K=B.conj().T@A-A@B.conj().T
    return C,P,Q,G,K

def run():
    rng=np.random.default_rng(173)
    assertions=0
    for m in (0,1,3,7):
      for d in (1,2,3):
       for r in range(10):
        A=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
        B=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
        L=18
        C,P,Q,G,K=blocks(A,B,m,L)
        # compare every block away from artificial top boundary (n <= L-4).
        for n in range(L-3):
         predicted=((n+m)*G+P) if n else ((m+1)*P)
         got=C[n*d:(n+1)*d,n*d:(n+1)*d]
         assert np.allclose(got,predicted,rtol=1e-11,atol=1e-9)
         assertions+=1
         if n+2 < L-2:
          target=np.sqrt((n+m+1)*(n+m+2))*K
          # row n+2, col n cross term J^2 K
          got=C[(n+2)*d:(n+3)*d,n*d:(n+1)*d]
          assert np.allclose(got,target,rtol=1e-11,atol=1e-9)
          assertions+=1
        assert abs(np.trace(G))<1e-9
        assert abs(np.trace(K))<1e-9
        assertions+=2
    # Exact nonnormal strictly hyponormal example.
    N=np.array([[0.,1.],[0.,0.]],dtype=complex)
    A=N-3*np.eye(2);B=N.conj().T-2*np.eye(2)
    for m in (0,1,4):
      C,P,Q,G,K=blocks(A,B,m,24)
      assert np.linalg.norm(G)<1e-12 and np.linalg.norm(K)<1e-12
      assert np.allclose(P,5*np.eye(2)-N-N.conj().T)
      assert np.linalg.eigvalsh(P).min()>3.999999
      for n in range(23):
        got=C[2*n:2*n+2,2*n:2*n+2]
        expected=((m+1) if n==0 else 1)*P
        assert np.allclose(got,expected,atol=1e-9,rtol=1e-11)
        assertions+=1
    print('supplementary finite assertions passed:',assertions)
if __name__=='__main__':run()
