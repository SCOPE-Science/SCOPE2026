"""Standalone small-field verification of the characteristic-two graphical-group torsion formulas.
Python 3 standard library only. Run: python verify.py
"""
from itertools import combinations
from collections import Counter
from math import comb

def mul(a,b,e):
    if e==1: return a&b
    if e==2:
        p=0
        for j in range(2):
            if b>>j&1: p^=a<<j
        if p&8: p^=0b111<<1
        if p&4: p^=0b111
        return p
    raise ValueError(e)

def decode(t,n,e):
    mask=(1<<e)-1
    return tuple((t>>(e*i))&mask for i in range(n))

def cocycle(x,y,edges,e):
    return tuple(mul(x[i],y[j],e) for i,j in edges)

def square(x,edges,e):
    return cocycle(x,x,edges,e)

def commutator(x,y,edges,e):
    u=cocycle(x,y,edges,e)
    v=cocycle(y,x,edges,e)
    return tuple(a^b for a,b in zip(u,v))

def gaussian_binom(N,r):
    if r<0 or r>N: return 0
    top=1; bot=1
    for k in range(r):
        top*=2**N-2**k
        bot*=2**r-2**k
    return top//bot

def subspaces(d):
    # Distinct binary subspaces by unique reduced row-echelon bases.
    for r in range(d+1):
        for pivots in combinations(range(d),r):
            free=[(i,j) for i in range(r) for j in range(pivots[i]+1,d) if j not in pivots]
            for mask in range(1<<len(free)):
                rows=[1<<p for p in pivots]
                for k,(i,j) in enumerate(free):
                    if (mask>>k)&1:rows[i]|=1<<j
                yield tuple(rows)

def independent_sets(n,edges):
    for S in range(1<<n):
        if all(not ((S>>i&1) and (S>>j&1)) for i,j in edges):
            yield S

def expected_subgroups(n,edges,e):
    cnt=Counter()
    for S in independent_sets(n,edges):
        t=S.bit_count()
        for r in range(e*t+1):
            exact=sum((-1)**(t-j)*comb(t,j)*gaussian_binom(e*j,r) for j in range(t+1))
            cnt[r]+=exact
    return cnt

def expected_class_strata(n,edges,q):
    m=len(edges); out=Counter()
    for S in independent_sets(n,edges):
        neighbor=0
        for i,j in edges:
            if S>>i&1: neighbor|=1<<j
            if S>>j&1: neighbor|=1<<i
        deg=neighbor.bit_count()
        out[deg]+=(q-1)**S.bit_count()*q**(m-deg)
    return out

def check(n,q):
    e=q.bit_length()-1
    N=(n*(n-1))//2
    graphs=0
    for mask in range(1<<N):
        pairs=list(combinations(range(n),2))
        edges=tuple(pairs[j] for j in range(N) if mask>>j&1)
        m=len(edges)
        verts=[decode(x,n,e) for x in range(q**n)]
        inv=[x for x in verts if not any(square(x,edges,e))]
        indep=list(independent_sets(n,edges))
        predicted=q**m*sum((q-1)**S.bit_count() for S in indep)
        assert q**m*len(inv)==predicted,(n,q,edges,'involutions')
        actual_classes=Counter()
        for x in inv:
            image={commutator(x,y,edges,e) for y in verts}
            assert len(image)&(len(image)-1)==0
            actual_classes[(len(image).bit_length()-1)//e]+=q**m//len(image)
        assert actual_classes==expected_class_strata(n,edges,q),(n,q,edges,'classes',actual_classes,expected_class_strata(n,edges,q))
        actual_subgroups=Counter()
        for basis in subspaces(e*n):
            U=[0]
            for b in basis: U += [z^b for z in U]
            ok=all(not any(square(decode(z,n,e),edges,e)) for z in U)
            if ok:
                # The preimage of the subspace is an elementary abelian group.
                assert all(not any(commutator(decode(a,n,e),decode(b,n,e),edges,e)) for a in U for b in U)
                actual_subgroups[len(basis)]+=1
        want=expected_subgroups(n,edges,e)
        assert actual_subgroups==want,(n,q,edges,'subgroups',actual_subgroups,want)
        alpha=max(S.bit_count() for S in indep)
        mx=sum(S.bit_count()==alpha for S in indep)
        assert actual_subgroups[e*alpha]==mx
        graphs+=1
    return graphs

if __name__=='__main__':
    runs=[(2,2),(3,2),(4,2),(2,4),(3,4)]
    graph_count=sum(check(n,q) for n,q in runs)
    print(f'VERIFY_OK {graph_count} independent graph-field cases: group-square, conjugacy, F2-subspace census')
