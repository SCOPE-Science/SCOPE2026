from itertools import product
import numpy as np
from scipy.optimize import linprog

def norm_check(m,n,alpha,beta):
    N=m*n
    def idx(i,j):return i*n+j
    edges=[]
    for i in range(m):
        for j in range(n):
            for k in range(i+1,m):edges.append((idx(i,j),idx(k,j),float(alpha)))
            for l in range(j+1,n):edges.append((idx(i,j),idx(i,l),float(beta)))
    # inequalities +- edge difference <=d; normalize f(0,0)=0
    mat=[];rhs=[]
    for u,v,d in edges:
        z=np.zeros(N);z[u]=1;z[v]=-1
        mat.append(z);rhs.append(d)
        mat.append(-z);rhs.append(d)
    q=np.zeros((N,N))
    for i in range(m):
        for j in range(n):
            row=idx(i,j)
            for k in range(m):
                for l in range(n):
                    col=idx(k,l)
                    q[row,col]=(int(i==k and j==l)-int(j==l)/m-int(i==k)/n+1/(m*n))
    assert np.allclose(q @ q, q, atol=1e-12)
    for i in range(m):
        assert np.allclose(q[i*n:(i+1)*n, :].sum(axis=0), 0, atol=1e-12)
    for j in range(n):
        assert np.allclose(q[j::n, :].sum(axis=0), 0, atol=1e-12)
    norms=[]
    for u,v,d in edges:
        b=np.zeros(N);b[u]=1/d;b[v]=-1/d
        c=q.T@b
        opt=linprog(-c[1:],A_ub=np.array(mat)[:,1:],b_ub=np.array(rhs),bounds=[(None,None)]*(N-1),method='highs')
        if not opt.success:raise RuntimeError(opt.message)
        norms.append(-opt.fun)
    actual=max(norms)
    formula=2*min(alpha,beta)*max((n-1)/(n*alpha),(m-1)/(m*beta))
    if abs(actual-formula)>2e-8:raise AssertionError((m,n,alpha,beta,actual,formula))
    return actual

cases=list(product(range(2,6),range(2,6),[1,2,3],[1,2,3]))
for k,(m,n,a,b) in enumerate(cases):
    norm_check(m,n,a,b)
print('PASS:',len(cases),'weighted rectangles; independent edge-dual linear programs agree with formula.')
