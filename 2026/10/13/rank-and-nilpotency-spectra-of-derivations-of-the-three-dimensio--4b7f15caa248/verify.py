#!/usr/bin/env python3
import itertools
from collections import Counter

def invp(a,p): return pow(a,p-2,p)
def rank_mod(M,p):
    A=[row[:] for row in M]; m=len(A); n=len(A[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]%p),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        z=invp(A[r][c]%p,p)
        A[r]=[(z*x)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%p:
                f=A[i][c]%p
                A[i]=[(A[i][j]-f*A[r][j])%p for j in range(n)]
        r+=1
        if r==m: break
    return r

def mmul(A,B,p):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%p for j in range(len(B[0]))] for i in range(len(A))]
def iszero(A): return all(x==0 for row in A for x in row)
def nil_index(M,p):
    P=[row[:] for row in M]
    for k in range(1,5):
        if iszero(P): return k
        P=mmul(P,M,p)
    return None

def Dmat(a,b,c,d,u,v,p):
    return [[a,c,0],[b,d,0],[u,v,(a+d)%p]]

def expected(q):
    return {0:1,1:(q-1)*(q+1)**2,2:q*(q-1)*(2*q**3+2*q**2-1),3:q**3*(q-1)*(q**2-q-1)}
def expected_nil(q):
    return {1:1,2:(q-1)*(q+1)**2,3:q*(q-1)**2*(q+1)}

def check_param_prime(p):
    rh=Counter(); nh=Counter()
    for vals in itertools.product(range(p), repeat=6):
        M=Dmat(*vals,p)
        rh[rank_mod(M,p)]+=1
        ni=nil_index(M,p)
        if ni is not None: nh[ni]+=1
    assert dict(rh)==expected(p),(p,rh,expected(p))
    assert dict(nh)==expected_nil(p),(p,nh,expected_nil(p))
    assert sum(nh.values())==p**4
    print('prime parameter',p,dict(rh),dict(nh))

def bracket(x,y,p):
    # basis x,y,z; [x,y]=z
    return [0,0,(x[0]*y[1]-x[1]*y[0])%p]
def mv(M,x,p): return [sum(M[i][j]*x[j] for j in range(3))%p for i in range(3)]
def add(x,y,p): return [(x[i]+y[i])%p for i in range(3)]
def derivation(M,p):
    E=[[1,0,0],[0,1,0],[0,0,1]]
    for x in E:
      for y in E:
        lhs=mv(M,bracket(x,y,p),p)
        rhs=add(bracket(mv(M,x,p),y,p),bracket(x,mv(M,y,p),p),p)
        if lhs!=rhs:return False
    return True

def brute_all_maps(p):
    rh=Counter(); n=0
    for vals in itertools.product(range(p), repeat=9):
        M=[list(vals[0:3]),list(vals[3:6]),list(vals[6:9])]
        if derivation(M,p):
            n+=1; rh[rank_mod(M,p)]+=1
    assert n==p**6
    assert dict(rh)==expected(p)
    print('all linear maps',p,'derivations',n,'ranks',dict(rh))

# GF(4), a^2=a+1, represented 0,1,a,a+1 as 0..3 bits
class GF4:
    q=4
    def add(self,a,b): return a^b
    def mul(self,a,b):
        r=0; aa=a; bb=b
        for _ in range(2):
            if bb&1:r^=aa
            bb>>=1; aa<<=1
            if aa&4: aa^=0b111
        return r&3
    def inv(self,a):
        if a==0: raise ZeroDivisionError
        for b in range(1,4):
            if self.mul(a,b)==1:return b
        raise AssertionError
F=GF4()
def rank_f4(M):
    A=[row[:] for row in M]; r=0; m=len(A); n=len(A[0])
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        z=F.inv(A[r][c]); A[r]=[F.mul(z,x) for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                f=A[i][c]
                A[i]=[F.add(A[i][j],F.mul(f,A[r][j])) for j in range(n)]
        r+=1
    return r
def mmul_f4(A,B): return [[F.add(F.add(F.mul(A[i][0],B[0][j]),F.mul(A[i][1],B[1][j])),F.mul(A[i][2],B[2][j])) for j in range(3)] for i in range(3)]
def nil_index_f4(M):
    P=[row[:] for row in M]
    for k in range(1,5):
        if iszero(P):return k
        P=mmul_f4(P,M)
    return None
def check_f4():
    rh=Counter(); nh=Counter()
    for a,b,c,d,u,v in itertools.product(range(4),repeat=6):
        M=[[a,c,0],[b,d,0],[u,v,F.add(a,d)]]
        rh[rank_f4(M)]+=1
        ni=nil_index_f4(M)
        if ni is not None:nh[ni]+=1
    assert dict(rh)==expected(4),(rh,expected(4))
    assert dict(nh)==expected_nil(4),(nh,expected_nil(4))
    print('GF4 parameter',dict(rh),dict(nh))

for p in (2,3,5,7): check_param_prime(p)
for p in (2,3): brute_all_maps(p)
check_f4()
print('VERIFY_OK')
