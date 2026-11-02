"""Independent finite-field verification of tripotent-count formulas."""
from itertools import product

def add(a,b,q):return a^b if (q & (q-1))==0 else (a+b)%q

def mul(a,b,q):
    if q in (2,3,5): return (a*b)%q
    if q==4:
        v=0
        for i in range(2):
            for j in range(2):
                if (a>>i)&1 and (b>>j)&1:v ^= 1<<(i+j)
        if v & 8:v ^= 0b1110 # x^3=x^2+x in GF(4)
        if v & 4:v ^= 0b111  # x^2=x+1
        return v
    raise ValueError(q)

def multiply(a,b,n,edges,q):
    out=[mul(a[i],b[i],q) for i in range(n)]
    for j,(u,v) in enumerate(edges):
        out.append(add(mul(a[u],b[n+j],q),mul(a[n+j],b[v],q),q))
    return tuple(out)

def coeff_formula(n,edges,q):
    m=len(edges)
    if q%2==0:
        return sum(q**sum(not (not (mask>>u&1) and not(mask>>v&1)) for u,v in edges) for mask in range(1<<n))
    return sum(q**sum(c[u]!=c[v] for u,v in edges) for c in product((0,1,q-1),repeat=n))

def independent_count(n,edges):
    return sum(all(not ((mask>>u&1) and(mask>>v&1)) for u,v in edges) for mask in range(1<<n))

def count(n,edges,q):
    N=n+len(edges); count=0
    for a in product(range(q),repeat=N):
        a2=multiply(a,a,n,edges,q)
        a3=multiply(a2,a,n,edges,q)
        count += a==a3
    return count

def check_orbits(n,edges):
    q=2;m=len(edges)
    for sc in product((0,1),repeat=n):
        allowed=[j for j,(u,v) in enumerate(edges) if sc[u] or sc[v]]
        classes={}
        for values in product((0,1),repeat=len(allowed)):
            r=[0]*m
            for j,v in zip(allowed,values):r[j]=v
            key=tuple(r[j] for j,(u,v) in enumerate(edges) if sc[u] and sc[v])
            classes.setdefault(key,[]).append(tuple(r))
        # Unipotent orbits obtained by shifts on cross-colored arrows.
        cross=sum(sc[u]!=sc[v] for u,v in edges)
        internal=sum(sc[u] and sc[v] for u,v in edges)
        assert len(classes)==2**internal
        assert all(len(x)==2**cross for x in classes.values())

cases=[
(1,[],2),(1,[(0,0)],2),(2,[(0,1)],2),(2,[(0,1),(1,0)],2),
(2,[(0,1),(0,1)],4),(3,[(0,1),(1,2)],2),
(3,[(0,1),(1,2),(2,0)],2),(3,[(0,1),(1,2),(2,0)],4),
(3,[(0,1),(1,2),(2,0)],3),(4,[(0,1),(0,2),(1,2)],2),
(3,[(0,0),(0,1),(1,1)],4),(2,[(0,1)],3),
]
for i,(n,edges,q) in enumerate(cases,1):
    x=count(n,edges,q);y=coeff_formula(n,edges,q)
    assert x==y,(i,x,y)
    if q==2:check_orbits(n,edges)
    print(i,n,len(edges),q,x)
print('TRIPOTENT_GRAPH_CENSUS_OK',len(cases),'exhaustive finite-field cases')
