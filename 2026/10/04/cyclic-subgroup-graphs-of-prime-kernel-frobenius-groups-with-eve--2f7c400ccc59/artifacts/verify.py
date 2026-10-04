from fractions import Fraction

def order_mod(a,r):
    x=1
    for k in range(1,r):
        x=(x*a)%r
        if x==1:
            return k
    raise AssertionError

def action_generator(r,m):
    for a in range(2,r):
        if order_mod(a,r)==m:
            return a
    raise AssertionError("no action generator")

def factor(n):
    out=[]
    d=2
    while d*d<=n:
        if n%d==0:
            a=0
            while n%d==0:
                n//=d
                a+=1
            out.append((d,a))
        d+=1
    if n>1:
        out.append((n,1))
    return out

def tau(n):
    ans=1
    for p,a in factor(n):
        ans*=a+1
    return ans

def cyclic_edge_count(n):
    t=tau(n)
    s=sum(Fraction(a,a+1) for p,a in factor(n))
    return int(t*s)

def build(r,m):
    u=action_generator(r,m)
    elems=[(a,b) for a in range(r) for b in range(m)]
    e=(0,0)
    def mul(x,y):
        a,b=x
        c,d=y
        return ((a+pow(u,b,r)*c)%r,(b+d)%m)
    return elems,e,mul,u

def cyclic_subgroup(g,e,mul):
    H={e}
    x=e
    while True:
        x=mul(x,g)
        if x==e:
            break
        H.add(x)
    return frozenset(H)

def check(r,m):
    assert m>=4 and m%2==0 and (r-1)%m==0
    elems,e,mul,u=build(r,m)
    subs={cyclic_subgroup(g,e,mul) for g in elems}
    subs=list(subs)

    edges=[]
    for i,H in enumerate(subs):
        for j in range(i+1,len(subs)):
            K=subs[j]
            if H<K or K<H:
                A,B=(H,K) if H<K else (K,H)
                if not any(A<L<B for L in subs):
                    edges.append((i,j))

    t=tau(m)
    em=cyclic_edge_count(m)
    assert len(subs)==2+r*(t-1)
    assert len(edges)==1+r*em
    assert cyclic_edge_count(r*m)==t+2*em
    assert len(edges)>cyclic_edge_count(r*m)

    kernel=frozenset((a,0) for a in range(r))
    assert kernel in subs
    ki=subs.index(kernel)
    assert sum(ki in edge for edge in edges)==1

    # Explicit conjugate complements.
    complements=[]
    for s in range(r):
        gen=((1-u)*s % r,1)
        H=cyclic_subgroup(gen,e,mul)
        assert len(H)==m
        complements.append(H)
    assert len(set(complements))==r
    for i in range(r):
        for j in range(i+1,r):
            assert complements[i]&complements[j]=={e}

    # Every non-kernel nonidentity element lies in exactly one complement.
    for g in elems:
        if g==e or g in kernel:
            continue
        assert sum(g in H for H in complements)==1

    # Every cyclic subgroup other than 1 and the kernel lies in exactly one complement.
    trivial=frozenset({e})
    for H in subs:
        if H in (trivial,kernel):
            continue
        assert sum(H.issubset(K) for K in complements)==1

    return {
        "r":r,
        "m":m,
        "vertices":len(subs),
        "edges":len(edges),
        "cyclic_edges":cyclic_edge_count(r*m),
    }

rows=[check(*case) for case in [
    (5,4),(7,6),(13,4),(13,6),(17,8),(31,10)
]]
assert [x["edges"] for x in rows]==[11,29,27,53,52,125]
assert [x["cyclic_edges"] for x in rows]==[7,12,7,12,10,12]
print("VERIFY_OK")
for row in rows:
    print(row)
