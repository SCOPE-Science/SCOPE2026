"""Exact independent graph-spectral checks for the symmetric edge polytope of a complete bipartite graph."""
from itertools import product, combinations
from collections import Counter
from math import prod
from sympy import Matrix, symbols, factor, binomial

def polytope_vertices(p,q):
    verts=[]; labels=[]
    for sign in (1,-1):
        for i in range(p):
            for j in range(q):
                v=[0]*(p+q);v[i]=sign;v[p+j]=-sign
                verts.append(v);labels.append((sign,i,j))
    return Matrix(verts),labels

def edge_rule(a,b):
    s,i,j=a;t,k,l=b
    return (i==k) != (j==l) if s==t else (i!=k and j!=l)

def laplacian(p,q):
    V,labels=polytope_vertices(p,q);N=len(labels)
    L=Matrix.zeros(N,N)
    for k,l in combinations(range(N),2):
        if edge_rule(labels[k],labels[l]):
            L[k,l]=L[l,k]=-1;L[k,k]+=1;L[l,l]+=1
    assert all(L[i,i]==p*q-1 for i in range(N))
    return L

def eigen_exponents(p,q):
    d=p*q
    values=[(0,1),(d,d-1),(2*(p-1)*(q-1),1),(p*(q-2)+2,q-1),(q*(p-2)+2,p-1),(d+2,(p-1)*(q-1))]
    exponents=Counter()
    for lam,mult in values: exponents[lam]+=mult
    return exponents

def expected_charpoly(p,q,t):
    e=eigen_exponents(p,q)
    return prod((t-lam)**m for lam,m in e.items())

def expected_tree(p,q):
    d=p*q
    return (p-1)*(q-1)*d**(d-2)*(p*(q-2)+2)**(q-1)*(q*(p-2)+2)**(p-1)*(d+2)**((p-1)*(q-1))

def check(p,q):
    L=laplacian(p,q);N=2*p*q;t=symbols('t')
    if N<=24:
        cp=L.charpoly(t).as_expr()
        assert factor(cp-expected_charpoly(p,q,t))==0,(p,q,'charpoly')
        trees=L[:-1,:-1].det(method='domain-ge')
        assert trees==expected_tree(p,q),(p,q,'Kirchhoff',trees)
    assert sum(eigen_exponents(p,q).values())==N
    assert sum(eig*m for eig,m in eigen_exponents(p,q).items())==N*(p*q-1)
    assert min(e for e,m in eigen_exponents(p,q).items() if e>0)==p*q-2*max(p,q)+2
    return N

if __name__=='__main__':
    cases=[(p,q) for p in range(2,6) for q in range(2,6)]
    print('EXACT_MATRICES',[(p,q,check(p,q)) for p,q in cases])
    try:
        import numpy as np
        from scipy.optimize import linprog
        ncheck=0
        for p,q in [(2,2),(2,3),(3,2),(3,3)]:
            verts,labels=polytope_vertices(p,q)
            arr=np.array(verts.tolist(),dtype=float)
            for x,y in combinations(range(len(labels)),2):
                # Exposed pair iff there exists c with c.(v_x-v_y)=0 and all others
                # c.(v_x-v_z)>=1. Homogeneity makes this necessary and sufficient.
                z=[k for k in range(len(labels)) if k!=x and k!=y]
                result=linprog(np.zeros(p+q),A_ub=arr[z]-arr[x],b_ub=-np.ones(len(z)),
                               A_eq=[arr[x]-arr[y]],b_eq=[0.],bounds=[(None,None)]*(p+q),method='highs')
                if bool(result.success)!=bool(edge_rule(labels[x],labels[y])):
                    raise AssertionError((p,q,x,y,result.status,labels[x],labels[y]))
                ncheck+=1
        print('LP_PAIRWISE_EXPOSED_CHECKS',ncheck)
    except ImportError:
        print('scipy unavailable, LP checks omitted')
    print('ALL_CHECKS_PASS')
