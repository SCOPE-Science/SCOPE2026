"""Exhaustive finite-field checks of radical-square-zero conjugacy spectra."""
from itertools import product
from collections import Counter

class Field:
    def __init__(self,q):
        self.q=q
        assert q in (2,3,4)
    def add(self,a,b):
        if self.q==4:return a^b
        return (a+b)%self.q
    def neg(self,a):
        if self.q==4:return a
        return (-a)%self.q
    def mul(self,a,b):
        if self.q!=4:return a*b%self.q
        x=0
        for i in range(2):
            if (b>>i)&1:x^=a<<i
        if x&8:x^=0b1100
        if x&4:x^=0b0111
        return x
    def inv(self,a):
        assert a
        return next(b for b in range(1,self.q) if self.mul(a,b)==1)
    def sub(self,a,b):return self.add(a,self.neg(b))

def comps(n,edges):
    parent=list(range(n))
    def root(x):
        while parent[x]!=x:x=parent[x]
        return x
    for u,v in edges:
        a,b=root(u),root(v)
        parent[a]=b
    return len({root(i) for i in range(n)})

def predicted(n,edges,q,nonzero=False):
    V=range(1,q) if nonzero else range(q)
    m=len(edges); D=Counter()
    for ds in product(V,repeat=n):
        same=[i for i,(u,v) in enumerate(edges) if ds[u]==ds[v]]
        cross=m-len(same)
        for mask in range(1<<len(same)):
            es=[edges[same[j]] for j in range(len(same)) if (mask>>j)&1]
            k=comps(n,es)
            r=n-k; b=len(es)-r
            size=q**cross*(q-1)**r
            D[size]+=(q-1)**b
    return D

def actual(n,edges,q,nonzero=False):
    f=Field(q); m=len(edges)
    verts=range(1,q) if nonzero else range(q)
    ring=list(product(range(q),repeat=m))
    units=[(z,t) for z in product(range(1,q),repeat=n) for t in ring]
    E=[(z,x) for z in product(verts,repeat=n) for x in ring]
    unseen=set(E); D=Counter()
    while unseen:
        a=next(iter(unseen));d,x=a
        orb=set()
        for lam,t in units:
            xx=tuple(f.add(f.mul(f.mul(lam[u],f.inv(lam[v])),x[j]),f.mul(f.mul(t[j],f.inv(lam[v])),f.sub(d[v],d[u]))) for j,(u,v) in enumerate(edges))
            orb.add((d,xx))
        assert len(orb)<=len(unseen)
        assert orb<=unseen
        unseen-=orb
        D[len(orb)]+=1
    return D

def tut(c,n,edges,q):
    # evaluate T_G(q+1,q) or T_G(q,q) by the subset expansion
    k0=comps(n,edges); sm=0
    for mask in range(1<<len(edges)):
        s=[e for j,e in enumerate(edges) if (mask>>j)&1]
        k=comps(n,s);b=len(s)-n+k
        sm+= (q if c=='algebra' else (q-1))**(k-k0) * (q-1)**b
    return (q if c=='algebra' else q-1)**k0*sm

cases=[('one_arrow',2,[(0,1)]),('two_parallel',2,[(0,1),(0,1)]),('path',3,[(0,1),(1,2)]),('transitive_triangle',3,[(0,1),(1,2),(0,2)]),('directed_triangle',3,[(0,1),(1,2),(2,0)])]
for q in (2,3,4):
    for name,n,edges in cases:
        if q==4 and n==3:continue
        for typ in ('algebra','units'):
            only=typ=='units'
            p=predicted(n,edges,q,only)
            a=actual(n,edges,q,only)
            assert a==p,(q,name,typ,a,p)
            assert sum(a.values())==tut(typ,n,edges,q)
            count=sum(mult*size for size,mult in a.items())
            assert count==q**len(edges)*(q-1 if only else q)**n
            print(f'q={q:>1} {name:>19} {typ:>7} classes={sum(a.values()):>4} sizes={sorted(a.items())}')
print('VERIFY_OK')
