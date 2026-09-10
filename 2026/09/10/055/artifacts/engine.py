"""Exact QQ Macaulay-duality engine for socle-4 codim-3 AG algebras."""
import sympy as sp
from sympy import Matrix, Integer
X,Y,Z = sp.symbols('X Y Z')

def monoms(deg):
    res=[]
    for i in range(deg+1):
        for j in range(deg+1-i):
            k=deg-i-j
            res.append((i,j,k))
    return res

def diff_act(F, e):
    i,j,k=e; g=F
    for _ in range(i): g=sp.diff(g,X)
    for _ in range(j): g=sp.diff(g,Y)
    for _ in range(k): g=sp.diff(g,Z)
    return sp.expand(g)

def cat_mat(F, i, d=4):
    """rows=monoms(i) acting on F, cols=coeffs in monoms(d-i). Row space = W_{d-i} = image = A_i dual."""
    dom=monoms(i); tgt=monoms(d-i)
    idx={e:k for k,e in enumerate(tgt)}
    rows=[]
    for e in dom:
        g=diff_act(F,e)
        row=[Integer(0)]*len(tgt)
        if g!=0:
            for mon,cf in sp.Poly(g,X,Y,Z).as_dict().items():
                row[idx[mon]]=cf
        rows.append(row)
    return Matrix(rows), dom, tgt

def row_basis(M):
    """independent row indices + R matrix (r x t)."""
    r = M.rank()
    piv=[]
    for j in range(M.rows):
        T = M.extract(piv+[j], list(range(M.cols)))
        if T.rank()==len(piv)+1:
            piv.append(j)
        if len(piv)==r: break
    return piv, M.extract(piv, list(range(M.cols)))

def diff_matrix(d, var):
    """D: coeffs in monoms(d) -> coeffs in monoms(d-1), differentiation by var (0,1,2)."""
    if d==0: return Matrix.zeros(len(monoms(0)), len(monoms(-1)) if False else 1)  # unused
    src=monoms(d); tgt=monoms(d-1)
    idx={e:k for k,e in enumerate(tgt)}
    D=Matrix.zeros(len(src), len(tgt))
    for r,e in enumerate(src):
        f=list(e); 
        if f[var]>0:
            f[var]-=1
            D[r, idx[tuple(f)]]=e[var]
    return D

class Apolar:
    def __init__(self, F, d=4):
        self.F=F; self.d=d
        self.C={}; self.dom={}; self.tgt={}
        self.hf=[]
        for i in range(d+1):
            M,dm,tg=cat_mat(F,i,d)
            self.C[i]=M; self.dom[i]=dm; self.tgt[i]=tg
            self.hf.append(M.rank())
        # row bases R_i of W_{d-i} (subspace of k^{tgt})
        self.R={}; self.piv={}
        for i in range(d+1):
            p,R=row_basis(self.C[i])
            self.piv[i]=p; self.R[i]=R
        # transition matrices T_k^{(i)}: A_i -> A_{i+1}, coords in R-bases
        self.T={}
        for i in range(d):
            Dlist=[diff_matrix(d-i, k) for k in range(3)]
            for k in range(3):
                Ri=self.R[i]; Rj=self.R[i+1]
                Dk=Dlist[k]
                Mmat=(Rj*Rj.T)
                Tk = Mmat.LUsolve(Rj*Dk.T*Ri.T)
                self.T[(k,i)]=Tk
    def mult(self, l, i):
        """matrix of x_l: A_i -> A_{i+1}."""
        M=self.T[(0,i)]*0
        for k in range(3):
            M=M+l[k]*self.T[(k,i)]
        return M
    def Nmat(self, l):
        """13x13 nilpotent multiplication-by-l matrix in graded R-basis order."""
        offs=[0]
        for i in range(5): offs.append(offs[-1]+self.hf[i])
        N=Matrix.zeros(offs[5], offs[5])
        for i in range(4):
            M=self.mult(l,i)
            for r in range(M.rows):
                for cc in range(M.cols):
                    N[offs[i+1]+r, offs[i]+cc]=M[r,cc]
        return N
    def jordan(self, l):
        N=self.Nmat(l); n=N.rows
        kerdims=[0]
        P=N.eye(n)-N.eye(n)
        Q=N
        import copy
        # kernel dims of N^k
        kd=[]
        Nk=Matrix.eye(n)
        for k in range(1,7):
            Nk=Nk*N
            kd.append((n-Nk.rank()))
        # parts>=i counts: c_i = kd[i-1]-kd[i-2]
        c=[kd[0]]+[kd[i]-kd[i-1] for i in range(1,len(kd))]
        # block sizes: for each i, c_i blocks of size>=i -> partition conjugate
        parts=[]
        for i,cnt in enumerate(c, start=1):
            parts.append(cnt)
        # conjugate: block j size = #{i: c_i >= j}... reconstruct sizes
        # sizes: sort: number of blocks of size>=i is c_i; so sizes = for j in 1..c_1: max i with c_i>=j
        nb=c[0]
        sizes=[]
        for j in range(1,nb+1):
            s=sum(1 for x in c if x>=j)
            sizes.append(s)
        sizes.sort(reverse=True)
        assert sum(sizes)==n, (sizes,n)
        return sizes, kd
