from itertools import product
from math import prod
from collections import Counter

# Independent generic cycle-convex-hull evaluator: components of selected graph.
def flower(lengths, extra_leaves=0):
    adj=[set()]
    blocks=[]
    for ell in lengths:
        vs=[]
        for _ in range(ell-1):
            vs.append(len(adj));adj.append(set())
        path=[0]+vs+[0]
        for a,b in zip(path,path[1:]):
            adj[a].add(b);adj[b].add(a)
        blocks.append(vs)
    for t in range(extra_leaves):
        p=len(adj);adj.append(set());parent=p-1 if t else blocks[0][0]
        adj[parent].add(p);adj[p].add(parent)
    return adj, blocks

def hull(mask,adj):
    n=len(adj)
    while True:
        comps=[-1]*n; label=0
        for i in range(n):
            if mask>>i&1 and comps[i]<0:
                stack=[i];comps[i]=label
                while stack:
                    v=stack.pop()
                    for w in adj[v]:
                        if mask>>w&1 and comps[w]<0:
                            comps[w]=label;stack.append(w)
                label+=1
        new=0
        for v in range(n):
            if mask>>v&1:continue
            cs=[comps[w] for w in adj[v] if mask>>w&1]
            if len(cs)>len(set(cs)):new|=1<<v
        if not new:return mask
        mask|=new

def actual_poly(lengths,leaves=0):
    adj,blocks=flower(lengths,leaves)
    N=len(adj);H=[hull(s,adj) for s in range(1<<N)]
    counterR=Counter();counterHe=Counter();counterRa=Counter();sets=[]
    for s in range(1<<N):
        bits=[v for v in range(N) if s>>v&1]
        rank=all(not(H[s&~(1<<v)]>>v&1) for v in bits)
        if rank:counterR[len(bits)]+=1
        if s:
            inter=(1<<N)-1
            for v in bits: inter&=H[s&~(1<<v)]
            helly=(inter==0)
        else:helly=False
        if helly:counterHe[len(bits)]+=1
        radon=True
        if rank:
            q=(s-1)&s
            while q:
                other=s^q
                if H[q]&H[other]:radon=False;break
                q=(q-1)&s
        else:radon=False
        if radon:counterRa[len(bits)]+=1
        if rank and not(helly or not s): print('RNOTH',lengths,s)
        if rank and not radon: print('RNOTRAD',lengths,s)
        if len(bits)>=N-len(lengths) and rank:sets.append(bits)
    return counterR,counterHe,counterRa,sets

def predicted(lengths,leaves):
    polys=[[1]+[0]*((sum(lengths)-len(lengths)+leaves)+1) for _ in []]
    n=1+sum(e-1 for e in lengths)+leaves
    result=Counter()
    for mask in range(1<<n):
        center=mask&1
        all_periph_counts=[]
        start=1
        full=0
        for e in lengths:
            k=e-1
            c=sum(mask>>i&1 for i in range(start,start+k))
            if c==k:full+=1
            start+=k
        good = (full==0) if center else (full<=1)
        if good:result[mask.bit_count()]+=1
    return result


def coefficient_formula(lengths, leaves):
    # Expand the closed generating expression without enumerating vertex subsets.
    def mul(a,b):
        out=Counter()
        for i, ai in a.items():
            for j, bj in b.items():out[i+j]+=ai*bj
        return out
    q=[Counter({0:1})]
    aa=[]
    from math import comb
    for ell in lengths:
        m=ell-1
        aa.append(Counter({j:comb(m,j) for j in range(m)}))
    def product(factors):
        out=Counter({0:1})
        for a in factors:out=mul(out,a)
        return out
    all_nonfull=product(aa)
    base=mul(Counter({0:1,1:1}),all_nonfull)
    for i, ell in enumerate(lengths):
        term=mul(Counter({ell-1:1}),product([v for j,v in enumerate(aa) if i!=j]))
        base.update(term)
    return mul(base,Counter({j:comb(leaves,j) for j in range(leaves+1)}))

if __name__=='__main__':
 cases=[((3,),0),((4,),0),((3,3),0),((3,4),0),((4,4),0),((3,3,3),0),((3,3,4),0),((3,4,4),0),((4,4,4),0),((3,3,3,3),0),((3,4,4),1),((4,4,4),2)]
 for lengths, leaves in cases:
    a,b,c,S=actual_poly(lengths,leaves)
    p=predicted(lengths,leaves)
    assert a==p,(lengths,leaves,a,p)
    f=coefficient_formula(lengths,leaves)
    assert a==f,(lengths,leaves,a,f)
    assert all(b[i]==a[i] for i in a if i>0),(lengths,leaves,a,b)
    assert c==a,(lengths,leaves,a,c)
    rank=max(a)
    k=len(lengths);n=1+sum(e-1 for e in lengths)+leaves
    assert rank==n-k,(lengths,leaves,rank,n-k)
    num=prod(e-1 for e in lengths)+sum(prod(lengths[j]-1 for j in range(k) if j!=i) for i in range(k))
    assert a[rank]==num,(lengths,leaves,a[rank],num)
    print(f'PASS lengths={lengths} leaves={leaves} n={n} rank={rank} opt_count={num} all_sets={sum(a.values())} poly={dict(sorted(a.items()))}')
 print('VERIFY_OK')
