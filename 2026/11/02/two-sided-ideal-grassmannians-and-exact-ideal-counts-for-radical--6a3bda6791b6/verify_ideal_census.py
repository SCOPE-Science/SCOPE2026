#!/usr/bin/env python3
"""Finite-field exhaustive consistency tests for two-sided ideals of radical-square-zero quiver algebras.
Only Python's standard library is required. No publication or process metadata is used.
"""
from itertools import combinations, product
from collections import Counter

class Field:
    def __init__(self, q):
        assert q in (2, 3, 4)
        self.q = q
    def add(self, x, y):
        return x ^ y if self.q == 4 else (x+y) % self.q
    def neg(self, x):
        return x if self.q == 4 else (-x) % self.q
    def mul(self, x, y):
        if self.q != 4:
            return x*y % self.q
        z=0
        for i in range(2):
            if (y>>i)&1:
                z ^= x<<i
        for i in (2,):
            if (z>>i)&1:
                z ^= 0b111 << (i-2)  # alpha^2=alpha+1
        return z
    def inv(self,x):
        assert x
        for y in range(1,self.q):
            if self.mul(x,y)==1:
                return y
        raise AssertionError

def rank(rows, F):
    if not rows:return 0
    a=[list(v) for v in rows]
    h=0
    n=len(a[0])
    for c in range(n):
        p=next((i for i in range(h,len(a)) if a[i][c]),None)
        if p is None:continue
        a[h],a[p]=a[p],a[h]
        inv=F.inv(a[h][c]); a[h]=[F.mul(inv,t) for t in a[h]]
        for i in range(h+1,len(a)):
            factor=a[i][c]
            if factor:
                a[i]=[F.add(t,F.neg(F.mul(factor,b))) for t,b in zip(a[i],a[h])]
        h+=1
        if h==len(a):break
    return h

def subspaces(n,F):
    for r in range(n+1):
        for piv in combinations(range(n),r):
            pivset=set(piv)
            free=[(i,j) for i,c in enumerate(piv) for j in range(c+1,n) if j not in pivset]
            for values in product(range(F.q), repeat=len(free)):
                rows=[[0]*n for _ in range(r)]
                for i,c in enumerate(piv): rows[i][c]=1
                for (i,j),a in zip(free,values):rows[i][j]=a
                yield rows

def action(x, b, edges, F, side):
    v=b if isinstance(b,int) else -1
    n_vertices=max((max(s,t) for s,t in edges),default=-1)+1
    if side=='left':
        if b<n_vertices:
            out=[0]*len(x)
            out[b]=x[b]
            for i,(s,t) in enumerate(edges):
                if t==b:out[n_vertices+i]=x[n_vertices+i]
            return out
        else:
            out=[0]*len(x)
            i=b-n_vertices; s,t=edges[i]
            out[b]=x[t]
            return out
    if b<n_vertices:
        out=[0]*len(x)
        out[b]=x[b]
        for i,(s,t) in enumerate(edges):
            if s==b:out[n_vertices+i]=x[n_vertices+i]
        return out
    out=[0]*len(x)
    s,t=edges[b-n_vertices]
    out[b]=x[s]
    return out

def enumerate_ideals(n_vertices, edges, F):
    N=n_vertices+len(edges)
    counts=Counter()
    for basis in subspaces(N,F):
        d=len(basis)
        if d==0:
            counts[0]+=1;continue
        success=True
        for row in basis:
            for b in range(N):
                for side in ('left','right'):
                    # action of basis element b on the row or vice versa
                    vec=[0]*N
                    if b<n_vertices:
                        vec[b]=row[b]
                        for i,(s,t) in enumerate(edges):
                            if (t if side=='left' else s)==b:
                                vec[n_vertices+i]=row[n_vertices+i]
                    else:
                        i=b-n_vertices;s,t=edges[i]
                        vec[b]=row[s if side=='left' else t]
                    if rank(basis+[vec],F)>d:
                        success=False;break
                if not success:break
            if not success:break
        if success:counts[d]+=1
    return counts

def gaussian(n,r,q):
    if r<0 or r>n:return 0
    num=den=1
    for j in range(r):
        num*=q**(n-j)-1
        den*=q**(r-j)-1
    assert num%den==0
    return num//den

def predicted(n_vertices,edges,q):
    a={(i,j):0 for i in range(n_vertices) for j in range(n_vertices)}
    for s,t in edges:a[(s,t)]+=1
    counts=Counter()
    for mask in range(1<<n_vertices):
        S={i for i in range(n_vertices) if mask&(1<<i)}
        incident=sum(v for (s,t),v in a.items() if s in S or t in S)
        polynomial=Counter({len(S)+incident:1})
        for (s,t),m in a.items():
            if s in S or t in S:continue
            new=Counter()
            for d,num in polynomial.items():
                for r in range(m+1):new[d+r]+=num*gaussian(m,r,q)
            polynomial=new
        counts.update(polynomial)
    return counts

def test():
    examples={
      'single_loop':(1,[(0,0)]),
      'two_loops':(1,[(0,0),(0,0)]),
      'parallel_2':(2,[(0,1),(0,1)]),
      'opposite_2':(2,[(0,1),(1,0)]),
      'chain_3':(3,[(0,1),(1,2)]),
      'fork_3':(3,[(1,0),(1,2)]),
      'mixed_loop_2':(2,[(0,0),(0,1)]),
      'disconnected_2':(2,[]),
    }
    cases=0
    for q in (2,3,4):
        F=Field(q)
        for name,(n,edges) in examples.items():
            if q==4 and n+len(edges)>4:continue
            actual=enumerate_ideals(n,edges,F)
            expected=predicted(n,edges,q)
            assert actual==expected, (q,name,actual,expected)
            print('OK',q,name,'dimension_counts',sorted(actual.items()))
            cases+=1
    p1=predicted(*examples['chain_3'],q=2)
    p2=predicted(*examples['fork_3'],q=2)
    assert p1==p2==Counter({0:1,1:2,2:3,3:3,4:3,5:1})
    assert sum(predicted(*examples['parallel_2'],q=2).values())==8
    assert sum(predicted(*examples['opposite_2'],q=2).values())==7
    print('VERIFY_OK_RADICAL_SQUARE_ZERO_ALL_IDEALS', cases)

if __name__=='__main__':test()
