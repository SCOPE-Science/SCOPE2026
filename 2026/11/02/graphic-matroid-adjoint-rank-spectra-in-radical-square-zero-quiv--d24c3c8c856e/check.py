"""Independent finite-field checks of adjoint-rank formulas for height-two incidence algebras.
No external dependencies. Run: python check.py
"""
from collections import Counter
from itertools import product
from math import comb


def add(a,b,q):
    return (a^b) if q == 4 else ((a+b)%q)

def neg(a,q):
    return a if q == 4 else ((-a)%q)

def mul(a,b,q):
    if q!=4: return (a*b)%q
    t=0
    while b:
        if b&1: t^=a
        b>>=1
        a<<=1
        if a&4: a^=7 # x^2 + x + 1
    return t

def rank(A,q):
    if not A: return 0
    A=[row[:] for row in A]
    h=len(A); w=len(A[0]); r=0
    for j in range(w):
        i=next((i for i in range(r,h) if A[i][j]!=0),None)
        if i is None: continue
        A[r],A[i]=A[i],A[r]
        pivot=A[r][j]
        inv=next(t for t in range(1,q) if mul(pivot,t,q)==1)
        for c in range(j,w): A[r][c]=mul(A[r][c],inv,q)
        for i in range(r+1,h):
            coeff=A[i][j]
            if coeff:
                for c in range(j,w):
                    A[i][c]=add(A[i][c],neg(mul(coeff,A[r][c],q),q),q)
        r+=1
        if r==h:break
    return r

def components(n,edges):
    parent=list(range(n))
    def find(a):
        while parent[a]!=a:
            a=parent[a]
        return a
    for u,v in edges:
        u=find(u);v=find(v)
        if u!=v: parent[v]=u
    return len({find(i) for i in range(n)})

def predicted(n,edges,lam,x):
    different=0; F=[]
    for (u,v),weight in zip(edges,x):
        if lam[u]!=lam[v]: different+=1
        elif weight: F.append((u,v))
    return different+n-components(n,F)

def exact(n,edges,lam,x,q):
    mat=[];e=len(edges)
    for i,(u,v) in enumerate(edges):
        row=[0]*(n+e)
        row[u]=neg(x[i],q)
        row[v]=x[i]
        row[n+i]=add(lam[u],neg(lam[v],q),q)
        mat.append(row)
    return rank(mat,q)

def count_poly(n,edges,q):
    cnt=Counter()
    for z in product(range(q),repeat=n+len(edges)):
        lam=z[:n];x=z[n:]
        got=exact(n,edges,lam,x,q)
        expect=predicted(n,edges,lam,x)
        assert got==expect,(n,edges,q,z,got,expect)
        cnt[got]+=1
    return [cnt[j] for j in range(len(edges)+1)]

def flagged(n,edges,q):
    # An independent three-state subset expansion depending only on the cycle matroid.
    e=len(edges);rE=n-components(n,edges);out=[0]*(e+1)
    for state in product(range(3),repeat=e):
        F=[edges[i] for i,s in enumerate(state) if s==1]
        S=[edges[i] for i,s in enumerate(state) if s==2]
        rF=n-components(n,F)
        rFS=n-components(n,F+S)
        base=(q-1)**len(F)*q**(rE-rFS)*q**(e-len(F)-len(S))
        shift=rF+e-len(F)-len(S)
        for j in range(len(S)+1):
            out[shift+j]+=base*comb(len(S),j)*(-q)**j
    return out

def multiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def forest_formula(e,q):
    return [comb(e,j)*(q*q-1)**j for j in range(e+1)]

def cycle_formula(length,q):
    out=[]
    for j in range(length+1):
        num=comb(length,j)*((q*q-1)**j+(q-1)*(-1)**j)
        assert num%q==0
        out.append(num//q)
    out[length-1]+=(q-1)**length
    out[length]-=(q-1)**length
    return out

star=[(0,1),(0,2),(0,3)]
path=[(0,1),(1,2),(2,3)]
square=[(0,1),(1,2),(2,3),(3,0)]
cycle6=[(i,(i+1)%6) for i in range(6)]
square_leaf=square+[(0,4)]
double_square=square+[(0,4),(4,5),(5,6),(6,0)]
triangle=[(0,1),(1,2),(2,0)]
cycle5=[(i,(i+1)%5) for i in range(5)]
disjoint=[(0,1),(2,3)]
configs=[(4,star,2),(4,star,3),(4,star,4),(4,path,2),(4,path,3),
         (4,square,2),(4,square,3),(4,square,4),(6,cycle6,2),
         (5,square_leaf,2),(7,double_square,2),
         (3,triangle,2),(3,triangle,3),(3,triangle,4),
         (5,cycle5,2),(4,disjoint,3),
         (4,[(1,0),(2,1),(3,2),(0,3)],3)]
for n,edges,q in configs:
    # Each ordered edge records the arrow orientation, even for odd cycles.
    # Reversing an arrow changes signs, not the asserted rank distribution.
    counts=count_poly(n,edges,q)
    cc=components(n,edges)
    assert all(t%q**cc==0 for t in counts)
    inner=[t//q**cc for t in counts]
    assert inner==flagged(n,edges,q),(n,edges,q,inner,flagged(n,edges,q))
    assert sum(inner)==q**(n+len(edges)-cc)
    if len(edges)==n-cc: assert inner==forest_formula(len(edges),q)
    if edges==square: assert inner==cycle_formula(4,q)
    if edges==cycle6: assert inner==cycle_formula(6,q)
    if edges==triangle: assert inner==cycle_formula(3,q)
    if edges==cycle5: assert inner==cycle_formula(5,q)
    if edges==square_leaf:
        assert inner==multiply(cycle_formula(4,q),forest_formula(1,q))
    print('CHECK',q,n,len(edges),'inner_ranks',inner)
print('INCIDENCE_ADJOINT_MATROID_CYCLE_OK',len(configs))
