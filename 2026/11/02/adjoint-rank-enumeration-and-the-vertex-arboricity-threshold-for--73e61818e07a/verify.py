#!/usr/bin/env python3
"""Direct finite-field checks of adjoint-rank enumeration for radical-square-zero quiver algebras."""
from itertools import product,combinations
from collections import Counter


def add(a,b,q):
    return (a^b) if q == 4 else (a+b)%q

def neg(a,q):
    return a if q == 4 else (-a)%q

def mul(a,b,q):
    if q!=4: return (a*b)%q
    r=0
    for _ in range(2):
        if b&1: r^=a
        b >>= 1
        a <<= 1
        if a&4:a^=7
    return r

def inv(a,q):
    assert a
    return next(b for b in range(1,q) if mul(a,b,q)==1)

def rref_rank(rows,q):
    if not rows:return 0
    mat=[row[:] for row in rows]; r=0
    for j in range(len(mat[0])):
        k=next((i for i in range(r,len(mat)) if mat[i][j]!=0),None)
        if k is None: continue
        mat[r],mat[k]=mat[k],mat[r]
        u=inv(mat[r][j],q); mat[r]=[mul(u,x,q) for x in mat[r]]
        for i in range(len(mat)):
            if i==r or mat[i][j]==0: continue
            coeff=neg(mat[i][j],q)
            mat[i]=[add(x,mul(coeff,y,q),q) for x,y in zip(mat[i],mat[r])]
        r+=1
        if r==len(mat):break
    return r

def number_components(v,edges):
    parent=list(range(v))
    def find(i):
        while i!=parent[i]:
            parent[i]=parent[parent[i]];i=parent[i]
        return i
    for u,w in edges:
        ru,rw=find(u),find(w)
        if ru!=rw:parent[ru]=rw
    return len({find(i) for i in range(v)})

def predict_rank(v,edges,a,x):
    equal=[j for j,(u,w) in enumerate(edges) if a[u]==a[w]]
    support=[edges[j] for j in equal if x[j]]
    return len(edges)-len(equal)+v-number_components(v,support)

def brute_rank(v,edges,coords,q):
    m=len(edges); N=v+m; a=coords[:v]; x=coords[v:]
    # Use multiplication of two elements in the radical-square-zero quotient of the path algebra.
    def mult(B,C):
        out=[mul(B[i],C[i],q) for i in range(v)]+[0]*m
        for j,(s,t) in enumerate(edges):
            out[v+j]=add(mul(B[s],C[v+j],q),mul(B[v+j],C[t],q),q)
        return out
    rows=[[0]*N for _ in range(N)]
    for col in range(N):
        unit=[0]*N;unit[col]=1
        left=mult(coords,unit);right=mult(unit,coords)
        for row in range(N):
            rows[row][col]=add(left[row],neg(right[row],q),q)
    return rref_rank(rows,q)

def graph_hist(v,edges,q):
    m=len(edges); hist=Counter()
    for a in product(range(q),repeat=v):
        eq=[j for j,(u,w) in enumerate(edges) if a[u]==a[w]]
        ne=m-len(eq)
        for bits in product((0,1),repeat=len(eq)):
            sup=[edges[eq[i]] for i,b in enumerate(bits) if b]
            rank=ne+v-number_components(v,sup)
            hist[rank]+=q**ne*(q-1)**sum(bits)
    return hist

def tutte_cp_count(v,edges,q):
    m=len(edges)
    return q**m*sum((q-1)**len(S)*q**(2*number_components(v,S))
                     for size in range(m+1) for S in combinations(edges,size))

def arboricity(v,edges):
    for colors in range(1,v+1):
        for a in product(range(colors),repeat=v):
            H=[e for e in edges if a[e[0]]==a[e[1]]]
            if len(H)-v+number_components(v,H)==0: return colors
    return v

def run_one(name,v,edges,q):
    hist=graph_hist(v,edges,q)
    hist_brute=Counter()
    for coords in product(range(q),repeat=v+len(edges)):
        rank=brute_rank(v,edges,coords,q)
        assert rank==predict_rank(v,edges,coords[:v],coords[v:]),(name,q,coords,rank)
        hist_brute[rank]+=1
    assert hist==hist_brute,(name,q,hist,hist_brute)
    cp=sum(q**(v+len(edges)-rank)*count for rank,count in hist.items())
    cp_tutte=tutte_cp_count(v,edges,q)
    assert cp==cp_tutte,(name,q,cp,cp_tutte)
    va=arboricity(v,edges)
    assert (max(hist)==len(edges))==(q>=va),(name,q,va,max(hist))
    assert sum(hist.values())==q**(v+len(edges))
    print(f'{name}: q={q}; |A|={q**(v+len(edges))}; rank_hist={dict(sorted(hist.items()))}; commuting_pairs={cp}; va={va}; OK')

def main():
    tests=[
      ('one-arrow',2,[(0,1)],2),
      ('P3-forward',3,[(0,1),(1,2)],2),
      ('P3-fork',3,[(1,0),(1,2)],2),
      ('P3-fork',3,[(1,0),(1,2)],4),
      ('triangle',3,[(0,1),(1,2),(2,0)],3),
      ('parallel-pair',2,[(0,1),(0,1)],3),
      ('K4',4,[(i,j) for i in range(4) for j in range(i+1,4)],2),
      ('K5',5,[(i,j) for i in range(5) for j in range(i+1,5)],2),
    ]
    for args in tests:run_one(*args)
    print('VERIFY_OK',len(tests),'direct exhaustive configurations')
if __name__=='__main__':main()
