"""Direct numerical cross-checks of the Pauli-transfer block-separability criterion.
Requires Python >=3.10 and NumPy. Finite tests do not establish the theorem.
"""
import itertools
import numpy as np

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
SIGMA = [I, X, Y, Z]


def matrices(weights):
    return [np.sqrt(w)*v for w,v in zip(weights,SIGMA)]


def transfer_power(z, weights, ell):
    p0,p1,p2,p3 = weights
    lam = [p0+p1-p2-p3, p0-p1+p2-p3, p0-p1-p2+p3]
    out = np.trace(z)*I/2
    for L, S in zip(lam, SIGMA[1:]):
        out += (L**ell)*np.trace(S@z)*S/2
    return out


def block_product(mats, depth):
    return [np.linalg.multi_dot(a) if len(a)>1 else a[0]
            for a in itertools.product(mats,repeat=depth)]


def matrix_for_blocks(weights, ell, n=1, m=1):
    mats=matrices(weights)
    A=block_product(mats,n)
    C=block_product(mats,m)
    E=[[transfer_power(U@I/2@V.conj().T, weights, ell) for V in C] for U in C]
    out=np.zeros((len(A)*len(C),len(A)*len(C)),complex)
    for i,S in enumerate(A):
        for j,U in enumerate(C):
            for k,T in enumerate(A):
                for h,V in enumerate(C):
                    out[i*len(C)+j,k*len(C)+h]=np.trace(S@E[j][h]@T.conj().T)
    return out


def physical_partial_transpose(state, da, dc):
    return state.reshape(da,dc,da,dc).transpose(0,3,2,1).reshape(da*dc,da*dc)


def embedding(mats, n):
    return np.array([M.flatten() for M in block_product(mats,n)])


def check(weights, ell,n,m):
    assert all(x>0 for x in weights) and abs(sum(weights)-1)<1e-10
    lam=[weights[0]+weights[1]-weights[2]-weights[3],
         weights[0]-weights[1]+weights[2]-weights[3],
         weights[0]-weights[1]-weights[2]+weights[3]]
    assert max(map(abs,lam))<1
    rho=matrix_for_blocks(weights,ell,n,m)
    assert abs(np.trace(rho)-1)<5e-10
    assert np.linalg.eigvalsh(rho).min()>-5e-10
    G1=embedding(matrices(weights),n)
    G2=embedding(matrices(weights),m)
    assert np.linalg.matrix_rank(G1)==4
    assert np.linalg.matrix_rank(G2)==4
    left=np.linalg.pinv(np.kron(G1,G2))
    omega=left@rho@left.conj().T
    expected=np.zeros((16,16),complex)
    for ao in range(2):
      for ai in range(2):
       for ci in range(2):
        for co in range(2):
         r=8*ao+4*ai+2*ci+co
         for bo in range(2):
          for bi in range(2):
           for di in range(2):
            for do in range(2):
             c=8*bo+4*bi+2*di+do
             basis=np.zeros((2,2),complex);basis[ci,di]=1
             q=transfer_power(basis,weights,ell)
             expected[r,c]=(ao==bo)*(co==do)*q[ai,bi]/2
    assert np.max(abs(omega-expected))<1e-8
    pt=physical_partial_transpose(rho,4**n,4**m)
    min_eig=np.linalg.eigvalsh(pt).min()
    criterion=sum(abs(l)**ell for l in lam)-1
    if criterion>1e-8: assert min_eig < -1e-11,(weights,ell,n,m,min_eig,criterion)
    if criterion< -1e-8: assert min_eig > -1e-10,(weights,ell,n,m,min_eig,criterion)
    return criterion,min_eig

if __name__ == '__main__':
    tested=0
    wset=[(.70,.10,.10,.10),(.82,.06,.06,.06),(.40,.30,.20,.10),
          (.10,.15,.25,.50),(.26,.24,.23,.27),(.91,.03,.03,.03)]
    for w in wset:
      for ell in range(1,9):
        check(w,ell,1,1)
        tested+=1
    for w in wset[:3]:
      for ell in range(1,4):
        check(w,ell,2,1)
        tested+=1
    print('PASS',tested,'direct density/partial-transpose tests, including 2-site blocks')
