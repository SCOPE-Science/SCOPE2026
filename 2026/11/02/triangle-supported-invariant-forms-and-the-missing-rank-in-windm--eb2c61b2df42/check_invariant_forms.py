#!/usr/bin/env python3
"""Independent finite-field checks for triangle-supported invariant Lie forms.
Python 3 standard library only. No imported research-package modules.
"""
from itertools import product, combinations
from collections import Counter
from math import comb

class Field:
    def __init__(self, q):
        assert q in (2,3,4,5)
        self.q=q
    def add(self,a,b): return a^b if self.q==4 else (a+b)%self.q
    def sub(self,a,b): return a^b if self.q==4 else (a-b)%self.q
    def mul(self,a,b):
        if self.q!=4: return a*b%self.q
        z=0
        for i in range(2):
            for j in range(2):
                if (a>>i)&1 and (b>>j)&1: z ^= 1<<(i+j)
        for bit in (3,2):
            if (z>>bit)&1:z ^= 0b111<<(bit-2)
        return z
    def inv(self,a):
        assert a
        return next(b for b in range(1,self.q) if self.mul(a,b)==1)

def rank_f(mat,F):
    if not mat:return 0
    a=[row[:] for row in mat];n=len(a);m=len(a[0]);r=0
    for c in range(m):
        p=next((i for i in range(r,n) if a[i][c]!=0),None)
        if p is None:continue
        a[p],a[r]=a[r],a[p]
        inv=F.inv(a[r][c]);a[r]=[F.mul(inv,v) for v in a[r]]
        for i in range(r+1,n):
            f=a[i][c]
            if f:a[i]=[F.sub(x,F.mul(f,y)) for x,y in zip(a[i],a[r])]
        r+=1
        if r==n:break
    return r

def triples(edges,n):
    E=set(edges)
    return [x for x in combinations(range(n),3) if all(tuple(sorted(y)) in E for y in combinations(x,2))]

def graph_lie(n,edges):
    es=[tuple(sorted(e)) for e in edges]
    assert len(es)==len(set(es)) and all(i<j for i,j in es)
    return es

def pair_index(d):return {(i,j):k for k,(i,j) in enumerate(combinations_with_replacement_range(d))}
def combinations_with_replacement_range(d):
    return ((i,j) for i in range(d) for j in range(i,d))

def constraint_rank(n,edges,q):
    F=Field(q);e=len(edges);d=n+e;ind=pair_index(d);eqs=[]
    # Bilinear invariance B([i,j],k)=B(i,[j,k]) for vertex triples.
    for i in range(n):
      for j in range(n):
       for k in range(d):
        row=[0]*len(ind)
        if i!=j and tuple(sorted((i,j))) in edges:
            p=edges.index(tuple(sorted((i,j))))+n
            t=ind[min(p,k),max(p,k)]
            row[t]=F.add(row[t],1 if i<j else F.sub(0,1))
        if k<n and j!=k and tuple(sorted((j,k))) in edges:
            p=edges.index(tuple(sorted((j,k))))+n
            t=ind[min(i,p),max(i,p)]
            row[t]=F.sub(row[t],1 if j<k else F.sub(0,1))
        if any(row):eqs.append(row)
    return len(ind)-rank_f(eqs,F)

def star_windmill(t):
    # Hub zero; triangles indexed 1+2j,2+2j.
    n=2*t+1
    edges=[]
    for j in range(t):
        a=1+2*j;b=a+1
        edges += [(0,a),(0,b),(a,b)]
    return n,edges

def form_matrix(n,edges,A,weights,F):
    tri=triples(edges,n); E=len(edges);d=n+E
    b=[[0]*d for _ in range(d)]
    for i in range(n):
      for j in range(n): b[i][j]=A[i][j]
    for val,(u,v,w) in zip(weights,tri):
        # B([u,v],w)= T(u,v,w) for positive order u<v<w,
        # B([u,w],v)= -T(u,v,w), B([v,w],u)= T(u,v,w)
        for (edge,vert,sig) in [((u,v),w,1),((u,w),v,-1),((v,w),u,1)]:
            h=n+edges.index(edge); b[h][vert]=b[vert][h]=val if sig==1 else F.sub(0,val)
    return b

def enumerate_hist(t,q):
    F=Field(q);n,edges=star_windmill(t);tri=triples(edges,n)
    pairs=list(combinations_with_replacement_range(n))
    out=Counter()
    for coefficients in product(range(q),repeat=len(pairs)):
      A=[[0]*n for _ in range(n)]
      for (i,j),v in zip(pairs,coefficients):A[i][j]=A[j][i]=v
      for weights in product(range(q),repeat=t):
        B=form_matrix(n,edges,A,weights,F)
        out[rank_f(B,F)]+=1
    return dict(sorted(out.items()))


def gl_order(n,q):
    z=1
    for i in range(n):z*=q**n-q**i
    return z

def sp_order(s,q):
    z=q**(s*s)
    for i in range(1,s+1):z*=q**(2*i)-1
    return z

def nondegenerate_symmetric_count(j,q):
    # Classification of nondegenerate symmetric bilinear forms.
    if j==0:return 1
    g=gl_order(j,q)
    if j%2:
        return g//sp_order((j-1)//2,q)
    s=j//2
    if q%2==0:
        return g//sp_order(s,q) + g//(q**(2*s-1)*sp_order(s-1,q))
    order_plus=2*q**(s*(s-1))*(q**s-1)
    order_minus=2*q**(s*(s-1))*(q**s+1)
    for i in range(1,s):
        order_plus*=q**(2*i)-1
        order_minus*=q**(2*i)-1
    return g//order_plus + g//order_minus

def gaussian_binom(n,k,q):
    if not 0<=k<=n:return 0
    u=v=1
    for i in range(k):u*=q**(n-i)-1;v*=q**(k-i)-1
    return u//v


def nonsingular_symmetric_product(j,q):
    if j%2==0:
        s=j//2
        result=q**(s*(s+1))
        for i in range(1,s+1):result*=q**(2*i-1)-1
        return result
    s=(j-1)//2
    result=q**(s*(s+1))
    for i in range(s+1):result*=q**(2*i+1)-1
    return result

def theoretical_symmetric_rank_hist(d,q):
    return {j:gaussian_binom(d,j,q)*nonsingular_symmetric_product(j,q) for j in range(d+1)}

def theoretical_windmill_hist(t,q):
    n=2*t+1;N=n*(n+1)//2;h=Counter()
    for k in range(t+1):
        r=0 if k==0 else 2*k+1
        d=n-r
        weight=comb(t,k)*(q-1)**k*q**(N-d*(d+1)//2)
        for j,v in theoretical_symmetric_rank_hist(d,q).items():
            h[2*r+j]+=weight*v
    return dict(sorted((j,v) for j,v in h.items() if v))

def symmetric_rank_hist(d,q):
    F=Field(q);pairs=list(combinations_with_replacement_range(d))
    h=Counter()
    for coefficients in product(range(q),repeat=len(pairs)):
      A=[[0]*d for _ in range(d)]
      for (i,j),v in zip(pairs,coefficients):A[i][j]=A[j][i]=v
      h[rank_f(A,F)]+=1
    return h

def predicted_hist(t,q):
    n=2*t+1;N=n*(n+1)//2
    h=Counter()
    for k in range(t+1):
        r=0 if k==0 else 2*k+1
        d=n-r
        M=comb(t,k)*(q-1)**k*q**(N-d*(d+1)//2)
        for sr,v in symmetric_rank_hist(d,q).items():
            h[2*r+sr]+=M*v
    return dict(sorted(h.items()))

def test():
    F=Field(2)
    examples=[('empty_4',4,[]),('path_3',3,[(0,1),(1,2)]),('triangle',3,[(0,1),(0,2),(1,2)]),('cycle_4',4,[(0,1),(1,2),(2,3),(0,3)]),('bowtie',*star_windmill(2)),('tetrahedron',4,list(combinations(range(4),2)))]
    for name,n,edges in examples:
        edges=graph_lie(n,edges)
        dim_expected=n*(n+1)//2+len(triples(edges,n))
        for q in (2,3):
            actual=constraint_rank(n,edges,q)
            assert actual==dim_expected,(name,q,dim_expected,actual)
        print('INVARIANT_SPACE',name,'n',n,'e',len(edges),'triangles',len(triples(edges,n)),'dimension',dim_expected)
    cases=[(1,2),(1,3),(1,4),(2,2)]
    for t,q in cases:
        actual=enumerate_hist(t,q)
        predicted=predicted_hist(t,q)
        assert actual==predicted,(t,q,actual,predicted)
        closed=theoretical_windmill_hist(t,q)
        assert actual==closed,(t,q,actual,closed)
        n=2*t+1;N=n*(n+1)//2
        assert sum(actual.values())==q**(N+t)
        assert actual[max(actual)]==q**N*(q-1)**t
        print('WINDMILL',t,'field',q,'rank_hist',actual)
    for q in (2,3,4):
        for d in (1,2,3):
            assert dict(symmetric_rank_hist(d,q))==theoretical_symmetric_rank_hist(d,q)
            for j in range(d+1):assert nonsingular_symmetric_product(j,q)==nondegenerate_symmetric_count(j,q)
    assert symmetric_rank_hist(4,2)==theoretical_symmetric_rank_hist(4,2)
    print('TRIANGLE_INVARIANT_FORM_RANK_ENUMERATOR_OK',len(examples)*2,len(cases))
if __name__=='__main__':test()
