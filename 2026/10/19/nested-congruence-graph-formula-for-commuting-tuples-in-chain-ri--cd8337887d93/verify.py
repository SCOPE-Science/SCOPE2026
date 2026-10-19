"""Literal multiplication validation of the nested congruence formula.

No theorem-side commutator simplifications are used for brute results.
"""
from itertools import product
from collections import Counter


def ring(p,ell,kind):
    size=p**ell
    def to_digits(x):
        z=[]
        for _ in range(ell):z.append(x%p);x//=p
        return z
    if kind=='integer':
        return size, lambda a,b:(a+b)%size,lambda a,b:(a*b)%size
    digs=[to_digits(j) for j in range(size)]
    def pack(ds):return sum((v%p)*p**i for i,v in enumerate(ds))
    def add(a,b):return pack([x+y for x,y in zip(digs[a],digs[b])])
    def mult(a,b):
        da,db=digs[a],digs[b]
        return pack([sum(da[h]*db[j-h] for h in range(j+1)) for j in range(ell)])
    return size,add,mult

def brute(v,edges,p,ell,kind,t):
    size,add,mult=ring(p,ell,kind)
    els=list(product(range(size), repeat=v+len(edges)))
    def multiply(a,b):
        da,za=a[:v],a[v:]; db,zb=b[:v],b[v:]
        d=tuple(mult(x,y) for x,y in zip(da,db))
        z=tuple(add(mult(da[s],zb[j]),mult(za[j],db[tar])) for j,(s,tar) in enumerate(edges))
        return d+z
    n=len(els)
    # Product-based commuting relation, no use of valuation criterion.
    adj=[0]*n
    for i,a in enumerate(els):
        bmask=0
        for j,b in enumerate(els):
            if multiply(a,b)==multiply(b,a):bmask|=1<<j
        adj[i]=bmask
    # Number of ordered commuting tuples equals sum over compatible choices.
    from functools import lru_cache
    full=(1<<n)-1
    @lru_cache(None)
    def F(mask,k):
        if k==0:return 1
        out=0
        rest=mask
        while rest:
            bit=rest&-rest
            i=bit.bit_length()-1
            out+=F(mask&adj[i],k-1)
            rest-=bit
        return out
    return F(full,t)

def components(v,edges):
    parent=list(range(v))
    def root(a):
        while parent[a]!=a:a=parent[a]
        return a
    for a,b in edges:
        parent[root(a)]=root(b)
    return len({root(j) for j in range(v)})

def predicted(v,edges,p,ell,t):
    q=p;m=len(edges)
    weights=[1]+[q**((t-1)*j)-q**((t-1)*(j-1)) for j in range(1,ell+1)]
    total=0
    for ranks in product(range(ell+1),repeat=m):
        term=1
        for a in ranks:term*=weights[a]
        for h in range(1,ell+1):
            term*=q**(t*components(v,[edge for edge,j in zip(edges,ranks) if j>=h]))
        total+=term
    return q**(ell*m)*total

def run():
    cases=[
        (2,[(0,1)],2,2,'integer',3),
        (2,[(0,1)],2,2,'polynomial',3),
        (2,[(0,1),(0,1)],2,2,'integer',2),
        (2,[(0,1),(0,1)],2,2,'polynomial',2),
        (3,[(0,1),(1,2)],2,2,'integer',2),
        (3,[(0,1),(1,2)],2,2,'polynomial',2),
        (2,[(0,1)],2,3,'integer',2),
        (2,[(0,1)],2,3,'polynomial',2),
        (2,[(0,1)],3,2,'integer',2),
        (2,[(0,0)],2,2,'integer',2),
        (2,[(0,1)],2,2,'integer',1),
        (2,[(1,0)],2,2,'polynomial',2),
    ]
    for v,edges,p,ell,kind,t in cases:
        n=brute(v,edges,p,ell,kind,t)
        th=predicted(v,edges,p,ell,t)
        assert n==th,(v,edges,p,ell,kind,t,n,th)
        print('CHAIN_CASE_OK',v,edges,p,ell,kind,t,n,flush=True)
    print('VERIFY_OK_NESTED_CHAIN_QUIVER',flush=True)
if __name__=='__main__':run()
