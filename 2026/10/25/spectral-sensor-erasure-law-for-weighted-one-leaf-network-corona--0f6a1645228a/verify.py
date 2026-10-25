"""Exact-arithmetic checks of aggregate observability for pendant corona diffusion.
Scientific self-contained verifier; requires sympy >=1.10.
"""
from sympy import Matrix, eye, zeros, Rational, sqrt, simplify
from itertools import combinations

def laplacian(n, weighted_edges):
    L=zeros(n)
    for i,j,w in weighted_edges:
        L[i,i]+=w; L[j,j]+=w; L[i,j]-=w; L[j,i]-=w
    return L

def corona(L,s):
    n=L.rows
    T=zeros(2*n)
    for i in range(n):
        for j in range(n): T[i,j]=L[i,j]
        T[i,i]+=s; T[i,i+n]=-s; T[i+n,i]=-s; T[i+n,i+n]=s
    return T

def output(n,S,beta):
    C=zeros(len(S),2*n)
    for k,i in enumerate(S): C[k,i]=1; C[k,i+n]=beta
    return C

def rank_obs(A,C):
    # Krylov observability rank; exact elimination.
    O=C
    block=C
    for _ in range(1,A.rows):
        block=block*A
        O=O.col_join(block)
    return O.rank()

def base_rank(L,S):
    C=zeros(len(S),L.rows)
    for k,i in enumerate(S): C[k,i]=1
    return rank_obs(L,C)

tests=0
families=[('path3',laplacian(3,[(0,1,1),(1,2,1)]),2),('triangle3',laplacian(3,[(0,1,1),(1,2,1),(2,0,1)]),1)]
for name,L,s in families:
 n=L.rows
 A=corona(L,s)
 for S in [(0,),(0,1),(0,1,2)]:
  b=base_rank(L,S)==n
  for beta in [Rational(1,2),Rational(1),Rational(2)]:
   forbidden=any(simplify(beta-(lam+sqrt(lam**2+4*s**2))/(2*s))==0 for lam in L.eigenvals().keys())
   got=rank_obs(A,output(n,S,beta))==2*n
   assert got==(b and not forbidden), (name,S,beta,b,forbidden,got)
   tests+=1
# Exact all-module gain resonances: P3 base spectrum {0,1,3}, s=2; beta=2 kills alpha=3
L=laplacian(3,[(0,1,1),(1,2,1)])
assert rank_obs(corona(L,2),output(3,[0,1,2],2))==5
assert rank_obs(corona(L,2),output(3,[0,1,2],1))==5
assert rank_obs(corona(L,2),output(3,[0,1,2],Rational(1,2)))==6
# Cycle-six module measurement checks via double precision, not part of infinite proof.
import numpy as np
def numerical_rank(L,s,S,beta):
 A=np.array(corona(L,s),dtype=float); C=np.array(output(L.rows,S,beta),dtype=float)
 O=np.vstack([C@np.linalg.matrix_power(A,k) for k in range(A.shape[0])])
 return np.linalg.matrix_rank(O,tol=1e-5)
L=laplacian(6,[(i,(i+1)%6,1) for i in range(6)])
assert numerical_rank(L,1,[0,2],0.5)==12
assert numerical_rank(L,1,[0,3],0.5)<12
print('PASS: %d exact rank tests, 3 full-measurement resonance contrasts and 2 numerical cycle checks'%tests)
# Heterogeneous-gain law, checked through exact eigenspace restriction ranks.
def predicted_invisible(L,s,S,betas):
    out=0
    for alpha,m in L.eigenvals().items():
        E=(L-alpha*eye(L.rows)).nullspace()
        assert len(E)==m
        T=Matrix.hstack(*E)
        live=[i for i,beta in zip(S,betas) if simplify(beta-(alpha+sqrt(alpha**2+4*s**2))/(2*s))!=0]
        r_all=T.extract(list(S),list(range(m))).rank()
        r_live=T.extract(live,list(range(m))).rank() if live else 0
        out+=(m-r_all)+(m-r_live)
    return out
h_tests=0
for name,L,s in families:
    for S in [(0,),(0,1),(0,1,2)]:
        for betas in [(Rational(1,2),)*len(S), (Rational(1),)*len(S),tuple([Rational(1),Rational(2),Rational(0)][:len(S)]),tuple([Rational(2),Rational(2),Rational(1)][:len(S)])]:
            C=zeros(len(S),2*L.rows)
            for j,i in enumerate(S): C[j,i]=1; C[j,i+L.rows]=betas[j]
            actual=2*L.rows-rank_obs(corona(L,s),C)
            expected=predicted_invisible(L,s,S,betas)
            assert actual==expected,(name,S,betas,actual,expected)
            h_tests+=1
print('PASS: %d exact heterogeneous-gain invisible-dimension tests'%h_tests)
