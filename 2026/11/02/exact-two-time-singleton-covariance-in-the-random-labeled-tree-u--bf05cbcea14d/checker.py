"""Reproduce exact two-time isolate-count moments for a uniform labeled tree.
Only standard-library exact fractions are used for finite assertions.
"""
from fractions import Fraction as F
from itertools import product
from math import exp

def p1(n,j):
    assert n >= 4 and 2 <= j < n
    return F(n-j,n) * F(n-1,n)**(j-2)

def q_old(n,j,k):
    assert n >= 4 and 2 <= j <= k < n
    return F((n-j)*(n-k), n*n) * F(n-1,n)**(k-j) * F(n-2,n)**(j-3)

def q_new(n,j,k):
    assert n >= 4 and 2 <= j < k < n
    return F((n-j-1)*(n-k), n*n) * F(n-1,n)**(k-j-1) * F(n-2,n)**(j-2)

def cov(n,j,k):
    assert n >= 4 and 2 <= j <= k < n
    return j*p1(n,k)+j*(j-1)*q_old(n,j,k) + (j*(k-j)*q_new(n,j,k) if k>j else 0) - j*k*p1(n,j)*p1(n,k)

def prufer_edges(pr):
    n=len(pr)+2
    deg=[1]*n
    for v in pr: deg[v]+=1
    edges=[]
    for v in pr:
        w=deg.index(1)
        edges.append((w,v));deg[w]-=1;deg[v]-=1
    z=[i for i,d in enumerate(deg) if d==1]
    edges.append(tuple(z))
    return edges

def iso(edges,j):
    marked=set(range(j))
    for u,v in edges:
        if u<j and v<j:
            marked.discard(u);marked.discard(v)
    return len(marked)

def boundary_kernel(s,t):
    assert 0 < s <= t < 1
    return s*(1-t)*exp(-t)*(1-(1-s)*exp(-s)+s*(2-s)*(1-t)*exp(-s))

def test():
    ct=0
    for n in range(4,8):
        trees=[prufer_edges(pr) for pr in product(range(n),repeat=n-2)]
        for j in range(2,n):
            obs=sum(iso(es,j) for es in trees)
            assert F(obs,len(trees)) == j*p1(n,j); ct+=1
            for k in range(j,n):
                moment=F(sum(iso(es,j)*iso(es,k) for es in trees),len(trees))
                pred = j*p1(n,k) + j*(j-1)*q_old(n,j,k) + (j*(k-j)*q_new(n,j,k) if j<k else 0)
                assert moment==pred, (n,j,k,moment,pred);ct+=1
    for n in range(4,80):
        for j in range(2,n):
            for k in range(j,n):
                assert cov(n,j,k)>0, (n,j,k,cov(n,j,k));ct+=1
    for (s,t) in [(0.2,0.2),(0.2,0.4),(0.35,0.8),(0.7,0.9)]:
        n=20000;j=int(n*s);k=int(n*t)
        obs=float(cov(n,j,k))/n;expv=boundary_kernel(s,t)
        assert abs(obs-expv) < 0.00015, (s,t,obs,expv)
        ct+=1
    print('PASS exact enumeration, covariance positivity tests, asymptotic kernel:',ct,'assertions')
if __name__=='__main__':test()
