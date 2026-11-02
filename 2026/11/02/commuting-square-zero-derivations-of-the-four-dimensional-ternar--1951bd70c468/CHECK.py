#!/usr/bin/env python3
"""Direct finite-field tests for square-zero commuting derivations of a four-dimensional ternary algebra."""
import itertools
from collections import Counter


def fold(v,addf):
    z=0
    for a in v:z=addf(z,a)
    return z

def product(A,B,q):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))%q for j in range(n)] for i in range(n)]

def rank(A,q):
    n=len(A);B=[row[:] for row in A];r=0
    for j in range(n):
        s=next((i for i in range(r,n) if B[i][j]),None)
        if s is None:continue
        B[r],B[s]=B[s],B[r];inv=pow(B[r][j],-1,q)
        B[r]=[(x*inv)%q for x in B[r]]
        for i in range(n):
            if i!=r and B[i][j]:
                f=B[i][j];B[i]=[(x-f*y)%q for x,y in zip(B[i],B[r])]
        r+=1
    return r

def skew_matrices(q):
    for t in itertools.product(range(q),repeat=6):
        A=[[0]*4 for _ in range(4)];k=0
        for i in range(4):
            for j in range(i+1,4):
                A[i][j]=t[k];A[j][i]=(-t[k])%q;k+=1
        yield A

def squarezero(A,q):return not any(x for row in product(A,A,q) for x in row)

def commute(A,B,q):
    C=product(A,B,q);D=product(B,A,q)
    return all(C[i][j]==D[i][j] for i in range(4) for j in range(4))

def determinant_sign(ids):
    a=list(ids);s=1
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:s=-s
    return s

def bracket(i,j,k,q):
    if len({i,j,k})<3:return (0,0,0,0)
    rem=next(h for h in range(4) if h not in (i,j,k))
    out=[0]*4;out[rem]=determinant_sign([i,j,k,rem])%q
    return out

def derivation_identity(D,q):
    for i in range(4):
      for j in range(4):
       for k in range(4):
        v=bracket(i,j,k,q)
        left=[sum(D[r][s]*v[s] for s in range(4))%q for r in range(4)]
        right=[0]*4
        for slot in range(3):
          ix=[i,j,k]
          for h in range(4):
            if not D[h][ix[slot]]:continue
            old=ix[slot];ix[slot]=h
            b=bracket(*ix,q)
            for l in range(4):right[l]=(right[l]+D[h][old]*b[l])%q
            ix[slot]=old
        if left!=right:return False
    return True

def expected_count(q,m):return (q+1)**2*(2*q-1)**m-2*q*(q+1)*q**m+q*q

def expect_rank_hist(q,m):
    ans=Counter()
    # Each coordinate has rank zero or two; count by explicit support sets.
    for mask in itertools.product((0,1),repeat=m):
        s=sum(mask);r=m-s
        if s==0:count=1
        else:
            # The active coordinates may all lie on one nilpotent line
            count=2*(q+1)*(q-1)**s
            # Mixed colors are assigned nontrivially to the active coordinates
            count+=((2**s)-2)*(q+1)**2*(q-1)**s
        ans[tuple(2*v for v in mask)]=count
    return ans

def test_prime(q):
    z=[]
    for D in skew_matrices(q):
        if squarezero(D,q):
            assert derivation_identity(D,q)
            z.append(D)
    assert len(z)==2*q*q-1
    assert Counter(rank(D,q) for D in z)==Counter({0:1,2:2*(q*q-1)})
    adj=[[commute(A,B,q) for B in z] for A in z]
    hist=Counter((rank(A,q),rank(B,q)) for i,A in enumerate(z) for j,B in enumerate(z) if adj[i][j])
    assert hist==expect_rank_hist(q,2),(q,hist,expect_rank_hist(q,2))
    assert sum(hist.values())==expected_count(q,2)
    if q<=5:
        ranks=[rank(A,q) for A in z]
        hist3=Counter((ranks[i],ranks[j],ranks[k]) for i in range(len(z)) for j in range(len(z)) for k in range(len(z)) if adj[i][j] and adj[i][k] and adj[j][k])
        assert hist3==expect_rank_hist(q,3),(q,hist3,expect_rank_hist(q,3))
        assert sum(hist3.values())==expected_count(q,3)
        print('PRIME',q,'squarezero',len(z),'pairs',sum(hist.values()),'triples',sum(hist3.values()))
    else:print('PRIME',q,'squarezero',len(z),'pairs',sum(hist.values()))

# Polynomial-arithmetic extension field F_9 = F_3[z]/(z^2+1).
def fadd(a,b):return (a%3+b%3)%3+3*((a//3+b//3)%3)
def fneg(a):return (-(a%3))%3+3*((-(a//3))%3)
def fmul(a,b):
    u,v=a%3,a//3;s,t=b%3,b//3
    return ((u*s-v*t)%3)+3*((u*t+v*s)%3)
def pmat(A,B):
    n=len(A)
    return [[fold([fmul(A[i][k],B[k][j]) for k in range(n)],fadd) for j in range(n)] for i in range(n)]
def kr(A,B):
    return [[fmul(A[i//2][j//2],B[i%2][j%2]) for j in range(4)] for i in range(4)]
def test_extension():
    q=9;Z=[[0,0],[0,0]];I=[[1,0],[0,1]]
    nil=[]
    for a,b,c in itertools.product(range(q),repeat=3):
        A=[[a,b],[c,fneg(a)]]
        if not any(x for row in pmat(A,A) for x in row):nil.append(A)
    assert len(nil)==q*q
    assert sum(bool(any(a for row in A for a in row)) for A in nil)==q*q-1
    operators=[]
    for A in nil:operators.append(kr(A,I))
    for B in nil[1:]:operators.append(kr(I,B))
    # all operators obey D^2=0 and the pair count under the tensor form
    assert len(operators)==2*q*q-1
    for D in operators: assert not any(x for row in pmat(D,D) for x in row)
    pairs=0
    for A in operators:
      for B in operators:
        P=pmat(A,B);Q=pmat(B,A)
        if P==Q:pairs+=1
    assert pairs==expected_count(q,2)
    print('EXTENSION',q,'squarezero',len(operators),'pairs',pairs)

if __name__=='__main__':
    for q in (3,5,7):test_prime(q)
    test_extension()
    print('TERNARY_LIE_SQUAREZERO_COMMUTING_OK 3_PRIME_FIELDS 1_EXTENSION_FIELD 2_TRIPLE_HISTOGRAMS')
