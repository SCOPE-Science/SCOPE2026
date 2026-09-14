"""Fast GF(p) Macaulay engine + samplers for s=6, j=8 (k=5) JDT search."""
import itertools, math
import numpy as np

P1=10**9+7; P2=10**9+9

def mons3(d):
    out=[]
    for a in range(d,-1,-1):
        for b in range(d-a,-1,-1):
            out.append((a,b,d-a-b))
    return out
MONS={d:mons3(d) for d in range(13)}
IDX={d:{m:i for i,m in enumerate(MONS[d])} for d in range(13)}

def fall(n,k):
    p=1
    for i in range(k): p*=n-i
    return p

def rk_gf(M,p):
    A=M.copy()%p; m,n=A.shape; r=0
    for c in range(n):
        piv=None
        for i in range(r,m):
            if A[i,c]%p!=0: piv=i; break
        if piv is None: continue
        A[[r,piv]]=A[[piv,r]]
        inv=pow(int(A[r,c]),-1,p)
        A[r]=(A[r]*inv)%p
        for i in range(m):
            if i!=r and A[i,c]!=0:
                A[i]=(A[i]-A[i,c]*A[r])%p
        r+=1
        if r==m: break
    return r

def row_basis_gf(C,p):
    """nonzero rows of RREF = basis of row space (h x n)."""
    A=C.copy()%p; m,n=A.shape; r=0; rows=[]
    for c in range(n):
        piv=None
        for i in range(r,m):
            if A[i,c]%p!=0: piv=i; break
        if piv is None: continue
        A[[r,piv]]=A[[piv,r]]
        inv=pow(int(A[r,c]),-1,p)
        A[r]=(A[r]*inv)%p
        for i in range(m):
            if i!=r and A[i,c]!=0:
                A[i]=(A[i]-A[i,c]*A[r])%p
        r+=1
    if r==0: return np.zeros((0,n),dtype=np.int64)
    return np.array(A[:r]%p,dtype=np.int64)

def cat_mat(F,j,d,p):
    Rd=MONS[d]; nd=len(Rd)
    if j-d<0: return np.zeros((0,nd),dtype=np.int64)
    Sd=MONS[j-d]; ns=len(Sd); ri=IDX[j-d]
    M=np.zeros((ns,nd),dtype=np.int64)
    for cj,(a,b,c) in enumerate(Rd):
        for (A,B,C),cF in F.items():
            if A>=a and B>=b and C>=c:
                k=(A-a,B-b,C-c)
                if k in ri:
                    M[ri[k],cj]=(M[ri[k],cj]+cF*fall(A,a)*fall(B,b)*fall(C,c))%p
    return M%p

from math import factorial
def mul_mat(t,u,v,l,p):
    Ru=MONS[u]; Rv=MONS[v]; iu=IDX[u]; iv=IDX[v]
    X=np.zeros((len(Rv),len(Ru)),dtype=np.int64)
    lx,ly,lz=l
    for a in range(t,-1,-1):
        for b in range(t-a,-1,-1):
            c=t-a-b
            coef=factorial(t)//(factorial(a)*factorial(b)*factorial(c))*(lx**a)*(ly**b)*(lz**c)
            if coef==0: continue
            for ju,(ua,ub,uc) in enumerate(Ru):
                key=(ua+a,ub+b,uc+c)
                jv=iv.get(key)
                if jv is not None:
                    X[jv,ju]=(X[jv,ju]+coef)%p
    return X%p

class AGfast:
    def __init__(self,F,j,p=P1):
        self.F=F; self.j=j; self.p=p
        self.Cs={}; self.Es={}; self.H=[]
        for d in range(j+1):
            C=cat_mat(F,j,d,p)
            self.Cs[d]=C
            h=rk_gf(C,p)
            self.H.append(h)
            self.Es[d]=row_basis_gf(C,p)
    def rankmat(self,l):
        j,p=self.j,self.p
        M=np.zeros((j+1,j+1),dtype=np.int64)
        for u in range(j+1):
            Eu=self.Es[u]
            for v in range(u,j+1):
                X=mul_mat(v-u,u,v,l,p)
                N=(self.Cs[v]@X@Eu.T)%p
                M[u,v]=rk_gf(N,p)
        return M
    @staticmethod
    def jdt(M,j):
        def g(u,v):
            if u<0 or v<0 or u>j or v>j: return 0
            return M[u,v]
        J=np.zeros((j+1,j+1),dtype=np.int64); ok=True
        for u in range(j+1):
            for v in range(u,j+1):
                J[u,v]=g(u,v)+g(u-1,v+1)-g(u-1,v)-g(u,v+1)
                if J[u,v]<0: ok=False
        parts=[]
        for u in range(j+1):
            for v in range(u,j+1):
                if J[u,v]!=0: parts.append((int(v-u+1),int(u),int(J[u,v])))
        return J,parts,ok

def sig_of_parts(parts):
    return tuple(sorted(parts))

def toeplitz_center(M,a=2,k=5):
    """Correct Lemma-2.15 check: center kxk block rows/cols a..a+k-1 is upper-triangular
    Toeplitz: M[u,v] depends only on v-u for u,v in block. Returns (ok, r) with r_i=M[a,a+i]."""
    C=M[a:a+k,a:a+k]
    for u in range(a,a+k):
        for v in range(u,a+k):
            if int(M[u,v])!=int(M[a,a+(v-u)]):
                return False,None
    r=tuple(int(M[a,a+i]) for i in range(k))
    return True,r

def delta_of_M(M,j,k=5,a=2):
    # r_i = M[a,a+i] (Toeplitz center first row); r_0 = s. Requires toeplitz_center ok.
    r=[int(M[a,a])]
    for i in range(1,k):
        r.append(int(M[a,a+i]))
    d=tuple(r[i-1]-r[i] for i in range(1,k))
    return tuple(r),d

def check_sym(parts,j):
    from collections import Counter
    c=Counter((p,nu) for p,nu,m in parts for _ in range(m))
    for (p,nu),m in list(c.items()):
        if c.get((p,j+1-nu-p),0)!=m: return False
    return True

# ---- samplers ----
def power_F(pts,coeffs,j):
    F={}
    for (x,y,z),c in zip(pts,coeffs):
        for a in range(j,-1,-1):
            for b in range(j-a,-1,-1):
                cc=j-a-b
                coef=math.factorial(j)//(math.factorial(a)*math.factorial(b)*math.factorial(cc))*(x**a)*(y**b)*(z**cc)*c
                F[(a,b,cc)]=F.get((a,b,cc),0)+coef
    return {k:v for k,v in F.items() if v!=0}

def no_conic(pts):
    import sympy as sp
    rows=[]
    for (x,y,z) in pts:
        rows.append([x*x,y*y,z*z,x*y,x*z,y*z])
    return sp.Matrix(rows).rank()==6

def punctual_F(j,rng):
    F={}
    for a in range(j,-1,-1):
        for b in range(j-a,-1,-1):
            c=j-a-b
            if a+b<=2:
                v=int(rng.integers(-3,4))
                if v: F[(a,b,c)]=v
    return F
