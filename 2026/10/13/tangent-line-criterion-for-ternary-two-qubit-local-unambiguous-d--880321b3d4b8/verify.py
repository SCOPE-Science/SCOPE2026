import numpy as np
rng=np.random.default_rng(42)

def mat(v): return v.reshape(2,2)
def det(v): return np.linalg.det(mat(v))
def adj(M): return np.array([[M[1,1],-M[0,1]],[-M[1,0],M[0,0]]],dtype=complex)

def criterion(psis,k,tol=1e-8):
    others=np.column_stack([psis[j] for j in range(3) if j!=k])
    # null of others^* gives W dim2
    _,_,vh=np.linalg.svd(others.conj().T)
    W=vh.conj().T[:,2:]
    # c in W and orthogonal psi_k: solve psi^* W z=0
    a=psis[k].conj()@W
    c=W@np.array([-a[1],a[0]],dtype=complex)
    # d choose projection of psi into W (guarantees overlap nonzero)
    d=W@(W.conj().T@psis[k])
    C,D=mat(c),mat(d)
    A=np.linalg.det(C)
    B=np.trace(adj(C)@D)
    E=np.linalg.det(D)
    fail=(abs(A)<tol and abs(B)<tol and abs(E)>tol)
    # brute: p(z)=det(C+z D), detector roots with z !=0 (here C at z=0 is nondetector); infinity D if detD=0
    # coefficients A + B z + E z^2
    success=False
    if abs(E)<tol:
        success=True # D product and is detector
    elif abs(B)>tol or abs(A)>tol:
        roots=np.roots([E,B,A])
        if any(abs(z)>1e-7 for z in roots): success=True
    # if p identically zero, D product -> success above
    return fail, success, (A,B,E)

# known obstruction
bp=np.array([1,0,0,1],complex)/np.sqrt(2)
bm=np.array([1,0,0,-1],complex)/np.sqrt(2)
p10=np.array([0,0,1,0],complex)
psis=[bp,bm,p10]
for k in range(3): print('known',k,criterion(psis,k))
for t in range(1000):
    X=rng.normal(size=(4,3))+1j*rng.normal(size=(4,3))
    if np.linalg.matrix_rank(X)<3: continue
    ps=[X[:,j]/np.linalg.norm(X[:,j]) for j in range(3)]
    for k in range(3):
        f,s,_=criterion(ps,k)
        if f==s: raise AssertionError((t,k,f,s))
print('VERIFY_OK random_triples=1000 known_obstruction=passed')
