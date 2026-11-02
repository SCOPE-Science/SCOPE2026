"""Finite numerical linear-program tests for signed adjacency norms and heat contractions."""
from itertools import combinations
import numpy as np
from scipy.optimize import linprog
from scipy.linalg import expm

def graph(n):
    V=list(combinations(range(n),2)); m=len(V)
    A=np.array([[int(not (set(u)&set(v))) for v in V] for u in V],dtype=int)
    assert (np.diag(A)==0).all()
    return V,A

def kr_norm(d,A):
    m=len(d)
    ed=np.transpose(np.nonzero(np.triu(A,1)))
    mat=np.zeros((2*len(ed),m))
    for ix,(u,v) in enumerate(ed):
        mat[2*ix,u]=1;mat[2*ix,v]=-1
        mat[2*ix+1,u]=-1;mat[2*ix+1,v]=1
    out=linprog(-d,A_ub=mat,b_ub=np.ones(len(mat)),bounds=[(0,0)]+[(None,None)]*(m-1),method='highs')
    if not out.success: raise RuntimeError(out.message)
    return -out.fun

def exact_formula(n,alpha,beta):
    if n==5:return max(abs(alpha)+3*abs(beta),4*abs(beta))
    return abs(alpha-beta)+2*(n-4)*abs(beta)

checks=0
for n in range(5,10):
    V,A=graph(n)
    u,v=next((i,j) for i in range(len(V)) for j in range(i+1,len(V)) if A[i,j])
    d=np.eye(len(V))[u]-np.eye(len(V))[v]
    for alpha,beta in [(-3,-1),(-1,1),(0,1),(1,1),(2,1),(4,-3),(1,0),(2,3),(-1,0),(0,0)]:
        value=kr_norm(alpha*d+beta*A@d,A)
        predicted=exact_formula(n,alpha,beta)
        assert abs(value-predicted)<1.e-8, (n,alpha,beta,value,predicted)
        checks+=1
    k=(n-2)*(n-3)//2
    L=k*np.eye(len(V))-A
    for t in [0,.007,.08,.23,1.1]:
        H=expm(-t*L)
        value=kr_norm(H@d,A)
        a=np.exp(-(k-1)*t); b=np.exp(-(k+n-3)*t)
        pred=(5*a-2*b)/3 if n==5 else (3*(n-4)*a-2*(n-5)*b)/(n-2)
        assert abs(value-pred)<2.e-8,(n,t,value,pred)
        checks+=1
    print('n',n,'signed/heat passed',flush=True)
print('CHECK_OK signed_and_heat_lp_checks',checks)
