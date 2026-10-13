"""Reproducible finite-field checks for nilpotent derivations of quadratic jets.
Pure Python, no third-party modules. All exhaustive tests labeled explicitly.
"""
import itertools
import math
from collections import Counter

def mm(A,B,q):
    return [[sum(x*y for x,y in zip(row,col))%q for col in zip(*B)] for row in A]

def rank(M,p):
    if not M:return 0
    A=[list(x) for x in M]; m,n=len(A),len(A[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]%p),None)
        if piv is None:continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c]%p,-1,p)
        A[r]=[(z*inv)%p for z in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%p:
                a=A[i][c]%p
                A[i]=[(v-a*w)%p for v,w in zip(A[i],A[r])]
        r+=1
    return r

def monomials(d):return [(i,j) for i in range(d) for j in range(i,d)]

def induced(P,q):
    d=len(P); mon=monomials(d); ix={m:i for i,m in enumerate(mon)}
    M=[[0]*len(mon) for _ in mon]
    for col,(i,j) in enumerate(mon):
        for a in range(d):
            pair=tuple(sorted((a,j))); M[ix[pair]][col]=(M[ix[pair]][col]+P[a][i])%q
            pair=tuple(sorted((i,a))); M[ix[pair]][col]=(M[ix[pair]][col]+P[a][j])%q
    return M

def D_matrix(P,Q,q):
    d=len(P);N=len(Q); S=induced(P,q)
    M=[[0]*(d+N) for _ in range(d+N)]
    for i in range(d):
        for j in range(d): M[i][j]=P[i][j]
    for i in range(N):
        for j in range(d): M[d+i][j]=Q[i][j]
        for j in range(N): M[d+i][d+j]=S[i][j]
    return M

def rref_null_basis(A,p):
    if not A:return []
    B=[row[:] for row in A];m,n=len(B),len(B[0]); pivs=[];r=0
    for c in range(n):
        s=next((i for i in range(r,m) if B[i][c]%p),None)
        if s is None:continue
        B[r],B[s]=B[s],B[r]
        inv=pow(B[r][c]%p,-1,p)
        B[r]=[v*inv%p for v in B[r]]
        for i in range(m):
            if i!=r and B[i][c]%p:
                u=B[i][c]
                B[i]=[(v-u*w)%p for v,w in zip(B[i],B[r])]
        pivs.append(c);r+=1
    out=[]
    for f in range(n):
        if f in pivs:continue
        v=[0]*n;v[f]=1
        for i,c in enumerate(pivs): v[c]=-B[i][f]%p
        out.append(v)
    return out

def qbin(n,k,q):
    if not 0<=k<=n:return 0
    return math.prod(q**n-q**i for i in range(k))//math.prod(q**k-q**i for i in range(k)) if k else 1

def glm(k,q):return math.prod(q**k-q**i for i in range(k))

def matrix_rank_count(a,b,k,q):return qbin(a,k,q)*qbin(b,k,q)*glm(k,q)

def square_zero_P_count(d,r,q):return qbin(d,r,q)*qbin(d-r,r,q)*glm(r,q)

def formula(d,q):
    N=d*(d+1)//2;h0=Counter()
    for k in range(min(d,N)+1):h0[k]+=matrix_rank_count(N,d,k,q)
    if q%2:
        return h0
    for r in range(1,d//2+1):
        h=r*(d-r);t=d-2*r;s=N-2*h;E=(d-r)*N-t*h
        for k in range(min(t,s)+1):
            h0[r+h+k]+=square_zero_P_count(d,r,q)*q**(E-t*s)*matrix_rank_count(s,t,k,q)
    return h0

def derivation_exhaust(d,p,limit=None):
    N=d*(d+1)//2; coeffs=d*d+N*d
    if limit is not None and p**coeffs>limit: return None
    actual=Counter()
    for pp in itertools.product(range(p),repeat=d*d):
        P=[list(pp[i*d:(i+1)*d]) for i in range(d)]
        S=induced(P,p)
        if any(any(z for z in row) for row in mm(P,P,p)) or any(any(z for z in row) for row in mm(S,S,p)):
            continue
        # Linear equations S Q + Q P =0 with flattened row-major Q variables
        constraints=[]
        for i in range(N):
          for j in range(d):
            row=[0]*(N*d)
            for a in range(N):row[a*d+j]=(row[a*d+j]+S[i][a])%p
            for b in range(d):row[i*d+b]=(row[i*d+b]+P[b][j])%p
            constraints.append(row)
        basis=rref_null_basis(constraints,p)
        if not basis: assignments=[()]
        else:assignments=itertools.product(range(p),repeat=len(basis))
        for coefs in assignments:
            v=[sum(t*b[i] for t,b in zip(coefs,basis))%p for i in range(N*d)]
            Q=[v[i*d:(i+1)*d] for i in range(N)]
            D=D_matrix(P,Q,p)
            assert all(all(z==0 for z in row) for row in mm(D,D,p))
            actual[rank(D,p)]+=1
    return actual

def canonical_checks():
    # P has one size-two chain and one singleton on V=F_2^3.
    d=3;p=2;N=6
    P=[[0,1,0],[0,0,0],[0,0,0]]
    S=induced(P,p)
    assert rank(S,p)==2
    constraints=[]
    for i in range(N):
      for j in range(d):
        row=[0]*(N*d)
        for a in range(N):row[a*d+j]=(row[a*d+j]+S[i][a])%p
        for b in range(d):row[i*d+b]=(row[i*d+b]+P[b][j])%p
        constraints.append(row)
    basis=rref_null_basis(constraints,p)
    assert len(basis)==10
    actual=Counter()
    for bits in itertools.product(range(p),repeat=len(basis)):
      v=[sum(c*b[j] for c,b in zip(bits,basis))%p for j in range(N*d)]
      Q=[v[i*d:(i+1)*d] for i in range(N)]
      D=D_matrix(P,Q,p)
      assert all(all(z==0 for z in row) for row in mm(D,D,p))
      actual[rank(D,p)]+=1
    assert actual==Counter({3:256,4:768})
    print('CANONICAL',d,p,dict(actual))
    # Characteristic-two general block rank on a second canonical type.
    d=4;p=2;P=[[0]*d for _ in range(d)];P[0][1]=1;P[2][3]=1
    assert rank(P,p)==2 and rank(induced(P,p),p)==4
    print('CANONICAL',d,p,'rank P=2, rank Sym2(P)=4')

def test():
    for d,p in [(2,2),(2,3)]:
        got=derivation_exhaust(d,p,limit=2**28)
        want=formula(d,p)
        print('EXHAUST',d,p,'got',dict(sorted(got.items())),'formula',dict(sorted(want.items())))
        assert got==want
    canonical_checks()
    for d,q in [(2,2),(2,3),(2,4),(3,2),(3,4),(4,2),(4,3),(5,2)]:
        f=formula(d,q)
        N=d*(d+1)//2
        if q%2:
            assert sum(f.values())==q**(d*N)
        else:
            expected=sum(square_zero_P_count(d,r,q)*q**((d-r)*N-(d-2*r)*r*(d-r)) for r in range(d//2+1))
            assert sum(f.values())==expected
        print('NORMALIZED',d,q,sorted(f.items()))
    print('VERIFY_OK_QUADRATIC_JET_DIFFERENTIALS')

if __name__=='__main__':test()
