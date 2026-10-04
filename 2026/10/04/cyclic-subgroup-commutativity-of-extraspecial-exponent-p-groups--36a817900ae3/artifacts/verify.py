from itertools import product

def addv(a,b,p):
    return tuple((x+y)%p for x,y in zip(a,b))

def dot(a,b,p):
    return sum(x*y for x,y in zip(a,b)) % p

def mul(g,h,p,n):
    x,y,z=g
    u,v,w=h
    return (addv(x,u,p), addv(y,v,p), (z+w+dot(x,v,p))%p)

def inv(g,p,n):
    x,y,z=g
    return (tuple((-a)%p for a in x), tuple((-a)%p for a in y), (-z+dot(x,y,p))%p)

def power(g,k,p,n):
    e=((0,)*n,(0,)*n,0)
    x=e
    for _ in range(k):
        x=mul(x,g,p,n)
    return x

def cyclic(g,p,n):
    e=((0,)*n,(0,)*n,0)
    H={e}
    x=e
    while True:
        x=mul(x,g,p,n)
        if x==e:
            break
        H.add(x)
    return frozenset(H)

def setprod(H,K,p,n):
    return frozenset(mul(h,k,p,n) for h in H for k in K)

def formula(p,n):
    N=(p**(2*n)-1)//(p-1)
    R=(p**(2*n-1)-1)//(p-1)
    return p*p*N*R+4*p*N+4, (p*N+2)**2, N, R

def check(p,n):
    vecs=list(product(range(p), repeat=n))
    elems=[(x,y,z) for x in vecs for y in vecs for z in range(p)]
    e=((0,)*n,(0,)*n,0)

    assert len(elems)==p**(2*n+1)
    for g in elems:
        assert mul(g,inv(g,p,n),p,n)==e
        assert power(g,p,p,n)==e

    subs={cyclic(g,p,n) for g in elems}
    num,den,N,R=formula(p,n)
    assert len(subs)==p*N+2

    Z=frozenset({((0,)*n,(0,)*n,z) for z in range(p)})
    assert Z in subs
    noncentral=[H for H in subs if H not in (frozenset({e}),Z)]
    assert len(noncentral)==p*N

    def normalize(v):
        for a in v:
            if a%p:
                inva=pow(a,-1,p)
                return tuple((inva*x)%p for x in v)
        raise AssertionError("zero vector")

    counts={}
    for H in noncentral:
        g=next(x for x in H if x!=e)
        L=normalize(g[0]+g[1])
        counts[L]=counts.get(L,0)+1
    assert len(counts)==N
    assert set(counts.values())=={p}

    total_pairs=0
    partner_counts={}
    for H in subs:
        c=0
        for K in subs:
            if setprod(H,K,p,n)==setprod(K,H,p,n):
                total_pairs+=1
                c+=1
        partner_counts[H]=c

    assert total_pairs==num, (p,n,total_pairs,num)
    assert len(subs)**2==den
    assert partner_counts[frozenset({e})]==len(subs)
    assert partner_counts[Z]==len(subs)
    assert set(partner_counts[H] for H in noncentral)=={p*R+2}

    if n==1:
        assert (num,den)==(
            p**3+5*p**2+4*p+4,
            (p**2+p+2)**2,
        )

for case in [(3,1),(3,2),(5,1),(5,2)]:
    check(*case)

print("VERIFY_OK")
