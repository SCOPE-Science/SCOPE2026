#!/usr/bin/env python3
"""Independent finite-field checks of the Heisenberg split-projection rank census."""
from itertools import combinations, product
from math import prod

def rank(a,q):
    if not a:return 0
    a=[list(row) for row in a]; r=0; cols=len(a[0])
    for c in range(cols):
        pivot=next((i for i in range(r,len(a)) if a[i][c]%q),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        v=pow(a[r][c],-1,q);a[r]=[(v*x)%q for x in a[r]]
        for i in range(len(a)):
            if i==r:continue
            t=a[i][c]
            if t:a[i]=[(x-t*y)%q for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r

def bracket(a,b,q,m):
    n=2*m+1
    z=sum((a[2*i]*b[2*i+1]-a[2*i+1]*b[2*i]) for i in range(m))%q
    return (0,)*(n-1)+(z,)

def all_subspaces(n,q):
    for k in range(n+1):
        for piv in combinations(range(n),k):
            free=[(i,j) for i,p in enumerate(piv) for j in range(p+1,n) if j not in piv]
            for values in product(range(q),repeat=len(free)):
                basis=[[0]*n for _ in range(k)]
                for i,p in enumerate(piv):basis[i][p]=1
                for (i,j),v in zip(free,values):basis[i][j]=v
                out=set()
                for cs in product(range(q),repeat=k):
                    out.add(tuple(sum(cs[i]*basis[i][j] for i in range(k))%q for j in range(n)))
                yield k,basis,out

def test_subalgebra_pairs(m,q):
    n=2*m+1; raw=list(all_subspaces(n,q)); known={}
    for k,basis,elems in raw:
        good=all(bracket(a,b,q,m) in elems for a,b in combinations(basis,2))
        if good:known.setdefault(k,[]).append(elems)
    got=[]
    for k in range(n+1):
        comp=known.get(n-k,[])
        got.append(sum(1 for U in known.get(k,[]) for W in comp if len(U&W)==1))
    exp=[0]*(n+1)
    def iso_count(b):
        num=prod(q**(2*m-j)-q**j for j in range(b))
        den=prod(q**b-q**j for j in range(b))
        assert num%den==0
        return num//den
    for b in range(m+1):
        v=iso_count(b)*q**(b*(2*m-b+1))
        exp[b]=v; exp[n-b]=v
    assert got==exp,(m,q,got,exp)
    print(f'PAIRS_OK m={m} q={q} subspaces={len(raw)} rank_counts={got}')

def test_operator_matrices(m,q):
    n=2*m+1
    def mv(a,x):return tuple(sum(a[i][j]*x[j] for j in range(n))%q for i in range(n))
    def matmul(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(n))%q for j in range(n)) for i in range(n))
    got=[0]*(n+1)
    for values in product(range(q),repeat=n*n):
        a=tuple(tuple(values[i*n+j] for j in range(n)) for i in range(n))
        if matmul(a,a)!=a:continue
        ok=True
        for i in range(n):
          for j in range(n):
            ei=tuple(int(x==i) for x in range(n));ej=tuple(int(x==j) for x in range(n))
            pi=mv(a,ei);pj=mv(a,ej)
            left=bracket(pi,pj,q,m)
            pbij=bracket(pi,ej,q,m);bpij=bracket(ei,pj,q,m);bij=bracket(ei,ej,q,m)
            x=tuple((pbij[k]+bpij[k]-bij[k])%q for k in range(n))
            if left!=mv(a,x):ok=False;break
          if not ok:break
        if ok:got[rank(a,q)]+=1
    assert sum(got)>0
    expected=[0]*(n+1)
    for b in range(m+1):
       num=prod(q**(2*m-j)-q**j for j in range(b))
       den=prod(q**b-q**j for j in range(b))
       v=(num//den)*q**(b*(2*m-b+1))
       expected[b]=v;expected[n-b]=v
    assert got==expected,(m,q,got,expected)
    print(f'OPERATORS_OK m={m} q={q} tested={q**(n*n)} rank_counts={got}')

if __name__=='__main__':
    for m,q in [(1,2),(1,3),(2,2)]:test_subalgebra_pairs(m,q)
    for m,q in [(1,2),(1,3)]:test_operator_matrices(m,q)
    print('VERIFY_OK')
