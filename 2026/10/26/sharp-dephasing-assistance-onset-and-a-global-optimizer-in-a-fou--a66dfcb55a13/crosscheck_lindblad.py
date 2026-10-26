import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve
sx=sparse.csr_matrix(np.array([[0,1],[1,0]],dtype=complex)); sy=sparse.csr_matrix(np.array([[0,-1j],[1j,0]],dtype=complex)); sz=sparse.diags([1.,-1.],format='csr',dtype=complex); ident=sparse.eye(2,dtype=complex,format='csr'); sp=(sx+1j*sy)*.5;sm=sp.conj().T

def kprod(ops):
 res=ops[0]
 for x in ops[1:]:res=sparse.kron(res,x,format='csr')
 return res

def at(op,i,L):return kprod([op if j==i else ident for j in range(L)])
def pair(A,B,i,L):return kprod([A if j==i else B if j==i+1 else ident for j in range(L)])
def four(L,U,g,G,f):
 d=2**L;Id=sparse.eye(d,dtype=complex,format='csr')
 H=sum((pair(sx,sx,j,L)+pair(sy,sy,j,L)) for j in range(L-1))-U*sum((j+1)*at(sz,j,L) for j in range(L))
 jumps=[np.sqrt(G*(1+f)/2)*at(sp,0,L),np.sqrt(G*(1-f)/2)*at(sm,0,L),np.sqrt(G*(1-f)/2)*at(sp,L-1,L),np.sqrt(G*(1+f)/2)*at(sm,L-1,L)]+[np.sqrt(g/2)*at(sz,j,L) for j in range(L)]
 S=-1j*(sparse.kron(Id,H,format='csr')-sparse.kron(H.T,Id,format='csr'))
 for B in jumps:
  BdB=B.conj().T@B
  S=S+sparse.kron(B.conj(),B,format='csr')-sparse.kron(Id,BdB,format='csr')/2-sparse.kron(BdB.T,Id,format='csr')/2
 S=S.tolil();S[0,:]=0
 for j in range(d):S[0,j*d+j]=1
 rhs=np.zeros(d*d,complex);rhs[0]=1
 rho=spsolve(S.tocsc(),rhs).reshape((d,d),order='F')
 I=2*(pair(sx,sy,1,L)-pair(sy,sx,1,L))
 return (I@rho).diagonal().sum().real
if __name__=='__main__':
    import sympy as s
    from verify import F4, G, g, u
    F=s.lambdify((G,g,u),F4,'numpy')
    for G1,g1,u1 in [(1,.1,.1),(1,.5,2),(1,.05,.2),(2,1,.6),(.4,.08,.22)]:
        exact=float(F(G1,g1,u1))
        direct=float(four(4,u1,g1,G1,.37)/.37)
        assert abs(exact-direct)<1.e-10,(G1,g1,u1,exact,direct)
    print('PASS full 16-state Lindblad checks in five parameter regimes')
