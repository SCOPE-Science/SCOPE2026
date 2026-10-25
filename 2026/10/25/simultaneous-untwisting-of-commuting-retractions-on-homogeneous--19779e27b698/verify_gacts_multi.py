"""Direct finite group-labelled map checks of simultaneous idempotent commutation.
All computations use pure Python and compare with an independent base-map weighted count.
"""
from itertools import product,permutations


def cyclic(q):
    return tuple(range(q)), lambda a,b:(a+b)%q, 0

def klein():
    return tuple(range(4)), lambda a,b:a^b, 0

def symmetric_three():
    p=list(permutations(range(3))); pos={x:i for i,x in enumerate(p)}
    return tuple(range(6)),lambda a,b:pos[tuple(p[a][p[b][i]] for i in range(3))],pos[(0,1,2)]

def idem(n,G):
    elems,mul,one=G
    for f in product(range(n),repeat=n):
        if any(f[f[i]]!=f[i] for i in range(n)):continue
        other=[i for i in range(n) if i not in set(f)]
        for assign in product(elems,repeat=len(other)):
            w=[one]*n
            for i,a in zip(other,assign):w[i]=a
            yield (f,tuple(w))

def comp(A,B,G):
    mul=G[1]; f,a=A; h,b=B
    return tuple(f[h[i]] for i in range(len(f))), tuple(mul(b[i],a[h[i]]) for i in range(len(f)))

def profile(n,G,k):
    E=list(idem(n,G)); sz=len(E); adj=[0]*sz; imgs=[]
    for i,(f,a) in enumerate(E):
        imgs.append(sum(1<<v for v in set(f)))
        for j in range(i+1):
            if comp(E[i],E[j],G)==comp(E[j],E[i],G):
                adj[i]|=1<<j
                if i!=j:adj[j]|=1<<i
    out={}
    def walk(mask,depth,meet):
        if depth==k:
            r=meet.bit_count();out[r]=out.get(r,0)+1;return
        available=mask
        while available:
            low=available & -available
            j=low.bit_length()-1
            available-=low
            walk(mask & adj[j],depth+1,meet & imgs[j])
    walk((1<<sz)-1,0,(1<<n)-1)
    return out,sz

def gauge_check(n,G,k):
    E=list(idem(n,G)); mul=G[1]; group,_,one=G
    inv={a:next(b for b in group if mul(a,b)==one and mul(b,a)==one) for a in group}
    identity=(tuple(range(n)),(one,)*n)
    adj=[[i for i,B in enumerate(E) if comp(A,B,G)==comp(B,A,G)] for A in E]
    tested=0
    def visit(indices,allowed):
        nonlocal tested
        if len(indices)==k:
            P=identity
            for i in indices:P=comp(P,E[i],G)
            D=(tuple(range(n)),P[1]); Di=(D[0],tuple(inv[x] for x in P[1]))
            assert comp(D,Di,G)==identity
            for i in indices:
                base=E[i][0]
                assert comp(comp(D,E[i],G),Di,G)==(base,(one,)*n)
            tested+=1;return
        for i in allowed:
            visit(indices+(i,),[j for j in allowed if j in adj[i]])
    visit(tuple(),list(range(len(E))))
    return tested

def run():
    cases=[(2,cyclic(2),4),(3,cyclic(6),4),(3,symmetric_three(),4),
           (4,cyclic(4),3),(4,klein(),3)]
    for n,G,k in cases:
        direct,size=profile(n,G,k)
        ground,_=profile(n,cyclic(1),k)
        expected={c:count*len(G[0])**(n-c) for c,count in ground.items()}
        assert direct==expected,(n,len(G[0]),k,direct,expected)
        print('PASS n=%d group_size=%d arity=%d idempotents=%d tuples=%d ranks=%s' %
              (n,len(G[0]),k,size,sum(direct.values()),sorted(direct.items())))
    tested=gauge_check(3,symmetric_three(),3)
    assert tested==8137,tested
    print('PASS direct simultaneous gauge untwisting for %d S3 triples'%tested)
    print('VERIFY_OK simultaneous higher-arity group-labelled idempotents')

if __name__=='__main__':run()
