"""Literal finite-ring checks of equivariant commuting-idempotent enumerators."""
from itertools import product
from collections import Counter
from math import gcd


def data_for_poset(n, pairs):
    pairs=tuple(sorted(set(pairs)))
    assert all(0<=u<v<n for u,v in pairs)
    allowed={(i,i) for i in range(n)}|set(pairs)
    assert all((u,w) in allowed for u,v in allowed for v2,w in allowed if v==v2)
    basis=sorted(allowed)
    mult=[(basis.index((u,w)),i,j) for i,(u,v) in enumerate(basis)
        for j,(v2,w) in enumerate(basis) if v==v2]
    return basis,mult

def add_mul(a,b,mult,q,dim):
    c=[0]*dim
    for k,i,j in mult:
        c[k]=(c[k]+a[i]*b[j])%q
    return tuple(c)

def diag(a,basis):
    return tuple(a[j] for j,(u,v) in enumerate(basis) if u==v)

def fixed(a,basis,group_perms):
    co={e:a[k] for k,e in enumerate(basis)}
    return all(co[(perm[u],perm[v])]==co[(u,v)] for perm in group_perms for u,v in basis)

def formula(n,pairs,perms,q,t):
    # Enumerate group action orbits on vertices and strict comparable pairs.
    parent=list(range(n))
    def root(x):
        while x!=parent[x]: x=parent[x]
        return x
    def union(a,b):
        parent[root(a)]=root(b)
    for p in perms:
        for i in range(n): union(i,p[i])
    vv=sorted(set(root(i) for i in range(n)))
    edges=[]
    todo=set(pairs)
    while todo:
        x=next(iter(todo)); orb={x}; f=[x]
        while f:
            a,b=f.pop()
            for p in perms:
                y=(p[a],p[b])
                if y not in orb:orb.add(y);f.append(y)
        edges.append(x)
        todo-=orb
    res=0
    for cols in product(range(1<<t),repeat=len(vv)):
        color=dict(zip(vv,cols))
        d=sum(color[root(u)] != color[root(v)] for u,v in edges)
        res+=q**d
    return res

def exhaustive(n,pairs,q,t,perms):
    basis,mult=data_for_poset(n,pairs)
    if q**len(basis)>15000 or (t>1 and q**len(basis)>1000): return None
    els=list(product(range(q),repeat=len(basis)))
    idems=[a for a in els if add_mul(a,a,mult,q,len(basis))==a and fixed(a,basis,perms)]
    if t==1:return len(idems)
    count=0
    for a in idems:
        for b in idems:
            if add_mul(a,b,mult,q,len(basis))==add_mul(b,a,mult,q,len(basis)):
                count+=1
    return count

def main():
    cases=[
        (3,[(0,1),(1,2),(0,2)],[(0,1,2)]),
        (4,[(0,2),(0,3),(1,2),(1,3)],[(0,1,2,3)]),
        (4,[(0,2),(0,3),(1,2),(1,3)],[(1,0,3,2)]),
        (4,[(0,2),(0,3),(1,2),(1,3)],[(0,1,2,3),(1,0,3,2)]),
        (4,[(0,2),(1,2),(1,3)],[(0,1,2,3)]),
    ]
    for n,pairs,perms in cases:
        for q,t in [(2,1),(2,2),(3,1),(3,2)]:
            expected=formula(n,pairs,perms,q,t)
            observed=exhaustive(n,pairs,q,t,perms)
            if observed is not None:
                assert observed==expected,(n,pairs,perms,q,t,observed,expected)
                print('RING_OK',n,len(pairs),len(perms),q,t,observed)
    for m in range(3,6):
        # crown b_i -> t_i,t_{i+1}; b=0..m-1, t=m..2m-1
        pairs=[(i,m+i) for i in range(m)]+[(i,m+(i+1)%m) for i in range(m)]
        for s in range(m):
            perm=tuple((i+s)%m for i in range(m))+tuple(m+(i+s)%m for i in range(m))
            for q,t in [(2,1),(2,2),(3,1),(3,2)]:
                r=2**t;d=gcd(m,s)
                closed=(1+(r-1)*q)**(2*d)+(r-1)*(1-q)**(2*d)
                expected=formula(2*m,pairs,[perm],q,t)
                assert closed==expected,(m,s,q,t,closed,expected)
        print('CROWN_OK',m)
    print('VERIFY_OK_EQUIVARIANT_INCIDENCE_IDEMPOTENTS')
if __name__=='__main__':main()
