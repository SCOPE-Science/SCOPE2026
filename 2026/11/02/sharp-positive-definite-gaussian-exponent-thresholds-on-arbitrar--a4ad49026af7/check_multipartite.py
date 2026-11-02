"""Exact-rational and numerical reproducibility checks for the multipartite distance theorem.
Uses only the Python standard library. Finite tests corroborate, not replace, the proof.
"""
from fractions import Fraction as F
from math import log2
from itertools import combinations

def partitions(n, minimum=1):
    if n==0:
        yield ()
    for k in range(minimum,n+1):
        for tail in partitions(n-k,k):
            yield (k,)+tail

def root(parts):
    parts=tuple(sorted(parts,reverse=True))
    if parts[0]==1:return 1.0
    if parts[0]==parts[1]:return 1/parts[0]
    a=1/parts[0]; b=1/parts[1]; a0=a
    def f(t):
        h=sum(1/(1/s-t) for s in parts[1:])
        return t-a0-1/h
    for _ in range(75):
        m=(a+b)/2
        if f(m)>0:b=m
        else:a=m
    return (a+b)/2

def form_matrix(parts,t):
    # Compute -B^T D B for standard basis b_i=e_i-e_last, exactly in Q.
    inv=F(1)/(1-t)
    colors=[i for i,n in enumerate(parts) for _ in range(n)]
    N=len(colors)
    def dist(i,j):
        if i==j:return F(0)
        return inv if colors[i]==colors[j] else F(1)
    return [[-dist(i,j)+dist(i,N-1)+dist(N-1,j) for j in range(N-1)] for i in range(N-1)]

def rank_q(M):
    if not M:return 0
    M=[row[:] for row in M];nr=len(M); nc=len(M[0]); k=0
    for j in range(nc):
        pivot=next((i for i in range(k,nr) if M[i][j]),None)
        if pivot is None:continue
        M[k],M[pivot]=M[pivot],M[k]
        d=M[k][j]
        for l in range(j,nc): M[k][l]/=d
        for i in range(k+1,nr):
            r=M[i][j]
            if r:
                for l in range(j,nc):M[i][l]-=r*M[k][l]
        k+=1
        if k==nr:break
    return k

def positive_definite(M):
    M=[row[:] for row in M]
    N=len(M)
    for i in range(N):
        d=M[i][i]
        if d<=0:return False
        for j in range(i+1,N):
            for k in range(j,N):
                M[j][k]-=M[i][j]*M[i][k]/d
                M[k][j]=M[j][k]
    return True

def sign_witness(parts,t):
    # Strictly positive distance power quadratic beyond the endpoint.
    q=[t-F(1,s) for s in parts]
    if q[1]>=0:
        S=[F(1),F(-1)]+[F(0)]*(len(parts)-2)
    else:
        weights=[F(1)/(F(1,s)-t) for s in parts[1:]]
        tot=sum(weights)
        S=[F(1)]+[-w/tot for w in weights]
    return sum(qi*si*si for qi,si in zip(q,S))

def run():
    checked=0; exact_end=0; count_strict=0; irrational_ex=0
    for N in range(3,11):
        for pp in partitions(N):
            if len(pp)<2 or all(s==1 for s in pp):continue
            parts=tuple(sorted(pp,reverse=True));tstar=root(parts)
            tbelow=F(int(tstar*1000000)-3,1000000)
            if tbelow<=0:tbelow=F(0)
            tabove=F(int(tstar*1000000)+3,1000000)
            if tabove>=1:tabove=F(999999,1000000)
            assert positive_definite(form_matrix(parts,tbelow)),('below',parts,tbelow,tstar)
            assert sign_witness(parts,tabove)>0,('above',parts,tabove,tstar)
            checked+=1;count_strict+=1
            if parts[0]==parts[1]:
                tc=F(1,parts[0]);N0=sum(parts)
                expected_null=sum(1 for p in parts if p==parts[0])-1
                assert rank_q(form_matrix(parts,tc))==(N0-1-expected_null),('endpoint',parts)
                exact_end+=1
            if parts==(3,2,1):
                # Secular equation is 9t^2 -11t+3=0.
                from math import sqrt
                assert abs(tstar-(11-sqrt(13))/18)<1e-12
                irrational_ex+=1
    for p in [(2,1),(3,1),(2,1,1),(2,2),(3,3),(3,2,1),(4,3,2,1)]:
        t=root(p)
        print('PARTS',p,'T',format(t,'.12g'),'P',format(-log2(1-t),'.12g'))
    print('PASS',checked,'distinct noncomplete multipartite profiles; exact endpoint ranks',exact_end,
          'strict-inside tests',count_strict,'irrational example',irrational_ex)

if __name__=='__main__':run()
