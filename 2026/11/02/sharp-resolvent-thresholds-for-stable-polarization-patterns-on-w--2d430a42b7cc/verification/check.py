"""Exact finite checks for a weighted-graph clipped-sign opinion theorem.

All arithmetic uses fractions.Fraction. This tests linear-algebra certificates
for finite graphs, not the analytic quantifiers in the theorem.
"""
from fractions import Fraction as Q
from itertools import product, combinations
from math import comb

def solve(A, y):
    n=len(A)
    m=[[Q(z) for z in row]+[Q(y[i])] for i,row in enumerate(A)]
    for j in range(n):
        k=next(k for k in range(j,n) if m[k][j])
        m[j],m[k]=m[k],m[j]
        d=m[j][j]
        m[j]=[z/d for z in m[j]]
        for i in range(n):
            if i!=j:
                t=m[i][j]
                if t: m[i]=[u-t*v for u,v in zip(m[i],m[j])]
    return [row[-1] for row in m]

def laplacian(n,edges):
    L=[[Q(0) for _ in range(n)] for _ in range(n)]
    for i,j,w in edges:
        w=Q(w)
        assert w>0 and i!=j
        L[i][i]+=w;L[j][j]+=w
        L[i][j]-=w;L[j][i]-=w
    return L

def kernel(L,b):
    n=len(L)
    A=[[L[i][j]+(b if i==j else 0) for j in range(n)] for i in range(n)]
    cols=[solve(A,[b*int(i==j) for i in range(n)]) for j in range(n)]
    return [[cols[j][i] for j in range(n)] for i in range(n)]

def dot(M,x):return [sum((a*b for a,b in zip(row,x)),Q(0)) for row in M]

def candidate_count(H,eps):
    n=len(H); count=0
    for s in product((-1,1),repeat=n):
        x=dot(H,s)
        if all(Q(si)*xi>eps for si,xi in zip(s,x)): count+=1
    return count

def all_signs_iff(H,eps):
    n=len(H)
    return candidate_count(H,eps)==2**n, all(H[i][i]>(1+eps)/2 for i in range(n))

def bipartite_form(p,q,w,b,eps):
    n=p+q; total=Q(0)
    for k in range(p+1):
        for ell in range(q+1):
            S=Q(2*k-p,p);T=Q(2*ell-q,q)
            U=((b+p*w)*S+q*w*T)/(b+n*w)
            V=(p*w*S+(b+q*w)*T)/(b+n*w)
            up=(q*w*V+b)/(b+q*w); um=(q*w*V-b)/(b+q*w)
            vp=(p*w*U+b)/(b+p*w); vm=(p*w*U-b)/(b+p*w)
            if ((k==0 or up>eps) and (k==p or um<-eps)
                and (ell==0 or vp>eps) and (ell==q or vm<-eps)):
                total+=comb(p,k)*comb(q,ell)
    return total

def run():
    checks=0
    for n in range(2,8):
        # Paths, cycles (when n>=3), stars, and complete graphs
        kinds=[[(i,i+1,Q(1)) for i in range(n-1)],
               [(0,i,Q(1)) for i in range(1,n)],
               [(i,j,Q(1)) for i in range(n) for j in range(i+1,n)]]
        if n>=3:kinds.append([(i,(i+1)%n,Q(1)) for i in range(n)])
        for edges in kinds:
            L=laplacian(n,edges)
            for b in (Q(1,2),Q(2),Q(5)):
                eps=Q(1,20)
                H=kernel(L,b)
                for row in H: assert sum(row)==1 and all(v>0 for v in row)
                assert all(H[i][j]==H[j][i] for i in range(n) for j in range(n))
                aa,bb=all_signs_iff(H,eps)
                assert aa==bb
                for i in range(n):
                    sign=[1]*n;sign[i]=-1
                    x=dot(H,sign)
                    plateau=all(Q(z)*xx>eps for z,xx in zip(sign,x))
                    assert plateau==(H[i][i]>(1+eps)/2)
                checks+=1
    for p in range(1,5):
      for q in range(1,5):
       n=p+q
       edges=[(i,j,Q(1)) for i in range(p) for j in range(p,n)]
       L=laplacian(n,edges)
       for b in (Q(1,2),Q(2),Q(5)):
        H=kernel(L,b);eps=Q(1,20)
        ha=(b*b+b*n+q)/((b+q)*(b+n))
        hb=(b*b+b*n+p)/((b+p)*(b+n))
        assert all(H[i][i]==ha for i in range(p))
        assert all(H[j][j]==hb for j in range(p,n))
        assert candidate_count(H,eps)==bipartite_form(p,q,Q(1),b,eps)
        checks+=1
    p,q,b,eps=1,5,Q(2),Q(1,10)
    L=laplacian(6,[(0,j,Q(1)) for j in range(1,6)])
    H=kernel(L,b)
    assert H[0][0]==Q(3,8) and H[1][1]==Q(17,24)
    assert dot(H,[1,-1,1,1,1,1])==[Q(3,4),-Q(5,12),Q(11,12),Q(11,12),Q(11,12),Q(11,12)]
    assert dot(H,[-1,1,1,1,1,1])==[Q(1,4)]+[Q(3,4)]*5
    assert eps<b/(b+5)
    print('PASS:',checks,'exact graph/parameter instances; plateau census, symmetries, isolated-dissenter criterion, explicit star witness')
if __name__=='__main__':run()
