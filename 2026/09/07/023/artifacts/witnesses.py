"""Build explicit Gram witnesses M=3G (integer, diag 3, off +-1) for
  - Clebsch SRG(16,5,0,2): 16 lines in R^6, angle arccos(1/3)
  - Triangular T(8): 28 lines in R^7 (hence R^8), angle arccos(1/3)
Verify symmetry/diag/alphabet, exact rational LDL with pivoting (PSD+rank),
and independent float eigendecomposition. Saves matrices to artifacts.
Stdlib + numpy only (Fractions for exact part).
"""
import numpy as np, itertools
from fractions import Fraction

def clebsch_M():
    def pop(x): return bin(x).count('1')
    n=16
    A=np.zeros((n,n),dtype=int)
    for i in range(n):
        for j in range(n):
            if i!=j and (pop(i^j)==1 or pop(i^j)==4):
                A[i,j]=1
    J=np.ones((n,n),dtype=int); I=np.eye(n,dtype=int)
    S=J-I-2*A
    M=3*I+S
    return M, A

def triangular8_M():
    verts=list(itertools.combinations(range(8),2))
    n=len(verts)
    A=np.zeros((n,n),dtype=int)
    for i,v in enumerate(verts):
        for j,w in enumerate(verts):
            if i!=j and len(set(v)&set(w))==1:
                A[i,j]=1
    J=np.ones((n,n),dtype=int); I=np.eye(n,dtype=int)
    S=J-I-2*A
    M=3*I-S  # PSD side
    return M, A

def audit_matrix(M, name):
    n=M.shape[0]
    assert (M==M.T).all(), "not symmetric"
    assert set(np.diag(M).tolist())=={3}, f"diag !=3: {np.unique(np.diag(M))}"
    off=set()
    for i in range(n):
        for j in range(n):
            if i!=j: off.add(int(M[i,j]))
    assert off<={1,-1}, f"off-diag alphabet {off}"
    print(f"[{name}] n={n}: symmetric OK, diag 3 OK, off-diag alphabet {sorted(off)} OK")
    return True

def exact_ldl_rank(M, name):
    n=M.shape[0]
    A=[[Fraction(int(M[i,j])) for j in range(n)] for i in range(n)]
    perm=list(range(n))
    pivots=[]
    for k in range(n):
        best=-1; bestv=Fraction(0)
        for i in range(k,n):
            if A[i][i]>bestv: bestv=A[i][i]; best=i
        if bestv==0:
            for i in range(k,n):
                for j in range(k,n):
                    assert A[i][j]==0, f"[{name}] Schur nonzero {A[i][j]} at ({i},{j})"
            print(f"[{name}] exact LDL terminated at step {k}: {len(pivots)} positive pivots, remaining {(n-k)}x{(n-k)} Schur exactly zero")
            break
        assert bestv>0, f"[{name}] negative pivot {bestv}"
        if best!=k:
            perm[k],perm[best]=perm[best],perm[k]
            A[k],A[best]=A[best],A[k]
            for r in range(n):
                A[r][k],A[r][best]=A[r][best],A[r][k]
        piv=A[k][k]; pivots.append(piv)
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]-=A[i][k]*A[j][k]/piv
        for i in range(k+1,n):
            A[i][k]=Fraction(0); A[k][i]=Fraction(0)
    print(f"[{name}] pivots (exact Fractions): {pivots}")
    print(f"[{name}] pivot floats: {[float(p) for p in pivots]}")
    print(f"[{name}] perm: {perm}")
    print(f"[{name}] => M PSD, rank = {len(pivots)} (all pivots >0, Schur zero)")
    return pivots, perm

def float_crosscheck(M, name, rank_claim):
    eig=np.linalg.eigvalsh(M.astype(float))
    emin=float(eig.min()); emax=float(eig.max())
    n0=int((np.abs(eig)<1e-6).sum()); nneg=int((eig<-1e-8).sum())
    print(f"[{name}] float eig: min={emin:.3e}, max={emax:.3f}, #|eig|<1e-6={n0}, #eig<-1e-8={nneg}")
    print(f"[{name}] smallest 8 eigs: {np.sort(eig)[:8]}")
    assert nneg==0, "not PSD in float!"
    assert (M.shape[0]-n0)==rank_claim, f"rank mismatch: {M.shape[0]-n0} vs {rank_claim}"
    print(f"[{name}] float rank {rank_claim} consistent (n - #zeros)")
    return eig

if __name__=="__main__":
    Mc,_=clebsch_M()
    Mt,_=triangular8_M()
    for M,name,rank in [(Mc,"Clebsch16_d6",6),(Mt,"T8_28_d7",7)]:
        audit_matrix(M,name)
        piv,_=exact_ldl_rank(M,name)
        assert len(piv)==rank
        float_crosscheck(M,name,rank)
        # save integer matrix 3G
        np.savetxt(f"output/artifacts/{name}_3G.csv", M, fmt="%d", delimiter=",")
        print(f"[{name}] saved output/artifacts/{name}_3G.csv")
        print()
    print("d=8 witness: same T8_28 matrix (rank 7 <= 8) embeds in R^8 => 28 lines in R^8.")
    print("All witness audits PASSED.")
