from itertools import product

def commute_bruteforce(q,n,edges):
    m=len(edges)
    elems=list(product(range(q), repeat=n+m))
    def commutes(x,y):
        d=x[:n]; xi=x[n:]; s=y[:n]; eta=y[n:]
        for j,(u,v) in enumerate(edges):
            if ((d[u]-d[v])*eta[j]-(s[u]-s[v])*xi[j])%q:
                return False
        return True
    return sum(commutes(x,y) for x in elems for y in elems)

def k_components(n, edges, mask):
    p=list(range(n))
    def find(a):
        while p[a]!=a:
            p[a]=p[p[a]]; a=p[a]
        return a
    def union(a,b):
        a,b=find(a),find(b)
        if a!=b: p[b]=a
    for i,(u,v) in enumerate(edges):
        if mask>>i & 1: union(u,v)
    return len({find(i) for i in range(n)})

def formula(q,n,edges):
    m=len(edges)
    S=0
    for mask in range(1<<m):
        r=mask.bit_count()
        S += (q-1)**r * q**(2*k_components(n,edges,mask))
    return q**m*S

cases=[
    (2,2,[(0,1)]),
    (3,2,[(0,1)]),
    (2,2,[(0,1),(0,1)]),
    (2,3,[(0,1),(1,2)]),
    (3,3,[(0,1),(1,2)]),
    (2,3,[(0,1),(1,2),(0,2)]),
    (2,3,[(0,1),(1,2),(2,0)]),
]
for q,n,e in cases:
    b=commute_bruteforce(q,n,e)
    f=formula(q,n,e)
    assert b==f,(q,n,e,b,f)
    print('case',q,n,e,'commuting_pairs',b)
for q in (2,3,5):
    for r in range(1,7):
        e=[(0,1)]*r
        C=formula(q,2,e)
        den=q**(2*(2+r))
        num_expected = den//(q*q) + (q*q-1)*den//(q**(r+2))
        assert C==num_expected,(q,r,C,num_expected)
print('VERIFY_OK')
