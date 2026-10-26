"""Finite-field exhaustive verification for the transvection-commutator similarity law.

Uses only the Python standard library. GF(4) is represented with x^2+x+1.
Each nonidentity transvection is enumerated once as an outer-product matrix.
"""
from itertools import product
from collections import Counter

class Field:
    def __init__(self,q):
        self.q=q
        assert q in (2,3,4,5,7)
    def add(self,x,y):
        return x^y if self.q==4 else (x+y)%self.q
    def neg(self,x):
        return x if self.q==4 else (-x)%self.q
    def sub(self,x,y):
        return self.add(x,self.neg(y))
    def mul(self,x,y):
        if self.q!=4: return (x*y)%self.q
        z=0
        for j in range(2):
            if (y>>j)&1: z^=x<<j
        for j in (2,):
            if (z>>j)&1: z^=0b111 << (j-2)
        return z
    def dot(self,u,v):
        w=0
        for x,y in zip(u,v): w=self.add(w,self.mul(x,y))
        return w
    def sq(self,x): return self.mul(x,x)

def ident(n):
    return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))

def matmul(A,B,F):
    n=len(A); out=[[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k]:
                for j in range(n):
                    out[i][j]=F.add(out[i][j],F.mul(A[i][k],B[k][j]))
    return tuple(map(tuple,out))

def matadd(A,B,F,neg=False):
    return tuple(tuple(F.sub(a,b) if neg else F.add(a,b) for a,b in zip(x,y)) for x,y in zip(A,B))

def rank(A,F):
    m=[list(x) for x in A]; n=len(m); r=0
    for j in range(n):
        pivot=next((i for i in range(r,n) if m[i][j]),None)
        if pivot is None:continue
        m[r],m[pivot]=m[pivot],m[r]
        inv=next(k for k in range(1,F.q) if F.mul(k,m[r][j])==1)
        m[r]=[F.mul(inv,z) for z in m[r]]
        for i in range(n):
            if i!=r and m[i][j]:
                s=m[i][j]
                m[i]=[F.sub(a,F.mul(s,b)) for a,b in zip(m[i],m[r])]
        r+=1
    return r

def all_transvections(n,F):
    xs=range(F.q)
    matrices={}
    for u in product(xs,repeat=n):
        if not any(u):continue
        for phi in product(xs,repeat=n):
            if not any(phi) or F.dot(u,phi):continue
            mat=tuple(tuple(F.add(int(i==j),F.mul(u[i],phi[j])) for j in range(n)) for i in range(n))
            matrices[mat]=1
    return list(matrices)

def expected(q,n):
    N=(q**n-1)*(q**(n-1)-1)//(q-1)
    eye=(q**(n-1)-1)+q*(q**(n-2)-1)**2//(q-1)
    trans=2*q**(n-1)*(q**(n-2)-1)
    each=q**(2*n-3)
    assert eye+trans+(q-1)*each==N
    return N,eye,trans,each

def test(q,n):
    F=Field(q); I=ident(n)
    E=tuple(tuple(F.add(int(i==j),int(i==0 and j==1)) for j in range(n)) for i in range(n))
    Einv=tuple(tuple(F.sub(int(i==j),int(i==0 and j==1)) for j in range(n)) for i in range(n))
    N,ei,tr,each=expected(q,n)
    Blist=all_transvections(n,F)
    assert len(Blist)==N,(q,n,len(Blist),N)
    observed=Counter(); splits=Counter()
    for B in Blist:
        Binv=matadd(I,matadd(B,I,F,True),F,True)  # 2I-B
        C=matmul(matmul(matmul(E,B,F),Einv,F),Binv,F)
        C1=matadd(C,I,F,True)
        rr=rank(C1,F)
        # trace((E-I)(B-I)) = phi_B(e1) * e2*(u_B) = t
        EN=matadd(E,I,F,True); BN=matadd(B,I,F,True)
        Z=matmul(EN,BN,F)
        t=0
        for i in range(n):t=F.add(t,Z[i][i])
        assert all(matmul(B,Binv,F)[i]==I[i] for i in range(n))
        if t:
            assert rr==2,(q,n,'rank',t,rr)
            ct=0
            for i in range(n):ct=F.add(ct,C1[i][i])
            assert ct==F.sq(t),(q,n,'trace',ct,t)
            # The nontrivial two-dimensional block has polynomial X^2-(2+t^2)X+1.
            # Hence the full matrix satisfies (K-I)(K^2-(2+t^2)K+I)=0.
            coeff=F.add(F.add(1,1),F.sq(t))
            K2=matmul(C,C,F)
            scalarK=tuple(tuple(F.mul(coeff,x) for x in row) for row in C)
            polynomial=matadd(matadd(K2,scalarK,F,True),I,F)
            assert matmul(C1,polynomial,F)==tuple(tuple(0 for _ in range(n)) for _ in range(n))
            observed[('t',t)]+=1
        elif C==I:
            observed['identity']+=1
        else:
            assert rr==1,(q,n,'r1',rr)
            assert matmul(C1,C1,F)==tuple(tuple(0 for _ in range(n)) for _ in range(n))
            observed['transvection']+=1
    assert observed['identity']==ei,(q,n,'eye',observed['identity'],ei)
    assert observed['transvection']==tr,(q,n,'trans',observed['transvection'],tr)
    for t in range(1,q):
        assert observed[('t',t)]==each,(q,n,t,observed[('t',t)],each)
        roots=[x for x in range(q) if F.add(F.sub(F.sq(x),F.mul(F.add(1,F.add(1,F.sq(t))),x)),1)==0]
        if len(roots)==0:splits['irreducible']+=1
        elif len(roots)==1:splits['repeated']+=1
        else:
            assert len(roots)==2
            splits['split']+=1
    if q==4 or q==2:
        assert splits['repeated']==0
        assert splits['split']==q//2-1
        assert splits['irreducible']==q//2
    elif q%2:
        delta=2 if q%4==1 else 0 # chi(-1) for odd prime q
        assert splits['repeated']==delta
        assert splits['split']==(q-3-delta)//2
        assert splits['irreducible']==(q+1-delta)//2
    print(f'q={q} n={n} N={N} identity={ei} transvection={tr} each-nonzero-t={each} split={splits["split"]} nonsplit={splits["irreducible"]} repeated={splits["repeated"]}')
    return N

if __name__=='__main__':
    total=0
    for q,n in [(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2),(4,3),(5,2),(5,3),(7,2),(7,3)]:
        total+=test(q,n)
    print(f'ALL_TRANSVECTION_COMMUTATOR_COUNTS_PASSED: cases=12 B_matrices={total}')
