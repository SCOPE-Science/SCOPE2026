#!/usr/bin/env python3
"""Standalone finite-case tests of the mathematical statement in RESULT.md."""
from itertools import product, permutations
from math import factorial, gcd


def dsu(n):
    parent=list(range(n))
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]]
            i=parent[i]
        return i
    def union(i,j):
        ri,rj=root(i),root(j)
        if ri!=rj: parent[ri]=rj;return True
        return False
    return root,union


def cyclic_cases(p,m):
    lam=next(a for a in range(2,p) if pow(a,m,p)==1 and all(pow(a,j,p)!=1 for j in range(1,m)))
    G=list(product(range(p),range(m)))
    pos={g:i for i,g in enumerate(G)}
    def mul(x,y):return ((x[0]+pow(lam,x[1],p)*y[0])%p,(x[1]+y[1])%m)
    def inv(x):return ((-pow(lam,(-x[1])%m,p)*x[0])%p,(-x[1])%m)
    def conj(x,y):return mul(mul(inv(y),x),y)
    n=len(G)
    tab=[[pos[conj(x,y)] for y in G] for x in G]
    root,union=dsu(n)
    for x,y,z,t in product(range(n),repeat=4):
        left=tab[tab[x][y]][tab[z][t]]
        right=tab[tab[x][z]][tab[y][t]]
        union(left,right)
    while True:
        changed=False
        for a,b in product(range(n),repeat=2):
            if root(a)!=root(b):continue
            for x in range(n):
                changed|=union(tab[a][x],tab[b][x])
                changed|=union(tab[x][a],tab[x][b])
        if not changed:break
    classes={}
    for i,g in enumerate(G):classes.setdefault(root(i),[]).append(g)
    cls=list(classes.values())
    assert len(cls)==p+m-1,(p,m,len(cls))
    assert all(len(c)==1 for c in cls if c[0][1]==0)
    assert all(len(c)==p for c in cls if c[0][1]!=0)
    lookup={g:i for i,c in enumerate(cls) for g in c}
    qt=[[lookup[conj(c[0],d[0])] for d in cls] for c in cls]
    A=[i for i,c in enumerate(cls) if c[0][1]==0]
    T=[i for i,c in enumerate(cls) if c[0][1]!=0]
    assert all(qt[i][j]==i for i in T for j in range(len(cls)))
    assert all(qt[i][j]==i for i in A for j in A)
    cnt=0
    for ar in permutations(A):
        for tr in permutations(T):
            f={**dict(zip(A,ar)),**dict(zip(T,tr))}
            if all(f[qt[i][j]]==qt[f[i]][f[j]] for i in range(len(cls)) for j in range(len(cls))):cnt+=1
    k=(p-1)//m
    phi=sum(gcd(u,m)==1 for u in range(m))
    assert cnt==m**k*factorial(k)*phi,(p,m,cnt,m**k*factorial(k)*phi)
    assert p+m-1==len(cls)
    print('PASS prime group',p,m,'classes',len(cls),'automorphisms',cnt)


def collision():
    # Alpha=[[0,-1],[1,-1]] over Z/4, alpha^3=I and alpha-I invertible.
    def a(v,mod):return ((-v[1])%mod,(v[0]-v[1])%mod)
    for mod in (2,4):
        V=list(product(range(mod),repeat=2))
        assert all(a(a(a(x,mod),mod),mod)==x for x in V)
        for j in (1,2):
            assert [x for x in V if (a(x,mod) if j==1 else a(a(x,mod),mod))==x]==[(0,0)]
    # A four-dimensional elementary-abelian group vs an exponent-4 group,
    # both of cardinality sixteen; both admit fixed-point-free order-three maps.
    def quotient_table(mod, blocks):
        K=list(product(range(mod),repeat=2*blocks))
        zero=(0,)*(2*blocks)
        def rot(x):
            y=[]
            for i in range(blocks):y.extend(a(x[2*i:2*i+2],mod))
            return tuple(y)
        def powrot(x,j):
            for _ in range(j%3):x=rot(x)
            return x
        def add(x,y):return tuple((a+b)%mod for a,b in zip(x,y))
        def neg(x):return tuple((-a)%mod for a in x)
        def mul(x,y):return (add(x[0],powrot(y[0],x[1])),(x[1]+y[1])%3)
        def inv(x):return (neg(powrot(x[0],-x[1])),-x[1]%3)
        def conj(x,y):return mul(mul(inv(y),x),y)
        labels={zero:0};count=0
        for x in K:
            if x in labels:continue
            for j in range(3):labels[powrot(x,j)]=1+3*count+j
            count+=1
        assert len(labels)==len(K) and count==5
        reps=[None]*len(K)
        for x,i in labels.items():reps[i]=(x,0)
        reps.extend([(zero,1),(zero,2)])
        def qclass(x):return labels[x[0]] if x[1]==0 else len(K)+x[1]-1
        table=tuple(tuple(qclass(conj(x,y)) for y in reps) for x in reps)
        return table
    assert quotient_table(4,1)==quotient_table(2,2)
    print('PASS distinct-kernel collision |K|=16, m=3, matching 18-element quotient tables')

if __name__=='__main__':
    for p,m in ((3,2),(5,2),(5,4),(7,2),(7,3),(7,6)):
        cyclic_cases(p,m)
    collision()
    print('VERIFY_OK')
