from itertools import product
from fractions import Fraction


def build_spider(lengths):
    adj=[set()]
    arms=[]
    nxt=1
    for L in lengths:
        arm=[]
        prev=0
        for _ in range(L):
            adj.append(set())
            cur=nxt; nxt+=1
            adj[prev].add(cur); adj[cur].add(prev)
            arm.append(cur); prev=cur
        arms.append(arm)
    return adj, arms


def is_power_dominating(mask, adj):
    n=len(adj)
    colored={v for v in range(n) if (mask>>v)&1}
    for v in list(colored):
        colored.update(adj[v])
    changed=True
    while changed:
        changed=False
        for v in list(colored):
            un=[u for u in adj[v] if u not in colored]
            if len(un)==1:
                colored.add(un[0]); changed=True
    return len(colored)==n


def predicted(mask, arms):
    if mask & 1:
        return True
    hit=sum(any((mask>>v)&1 for v in arm) for arm in arms)
    return hit >= len(arms)-1


def coeff_formula(lengths):
    # center-containing: x(1+x)^L
    L=sum(lengths)
    c=[0]*(L+2)
    from math import comb
    for q in range(L+1):
        c[q+1]+=comb(L,q)
    # center-free: all arms or all but one nonempty
    polys=[]
    for l in lengths:
        p=[0]*(l+1)
        for q in range(1,l+1): p[q]=comb(l,q)
        polys.append(p)
    def mul(a,b):
        z=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b): z[i+j]+=x*y
        return z
    allp=[1]
    for p in polys: allp=mul(allp,p)
    for i,x in enumerate(allp): c[i]+=x
    for skip in range(len(polys)):
        q=[1]
        for j,p in enumerate(polys):
            if j!=skip: q=mul(q,p)
        for i,x in enumerate(q): c[i]+=x
    return c


def polynomial_value(lengths,x):
    t=1+x
    L=sum(lengths)
    u=[t**l-1 for l in lengths]
    ans=x*t**L
    prod=Fraction(1)
    for v in u: prod*=v
    ans+=prod
    for i in range(len(u)):
        q=Fraction(1)
        for j,v in enumerate(u):
            if i!=j: q*=v
        ans+=q
    return ans


def partitions_fixed(n,k,lo=1):
    if k==0:
        if n==0: yield ()
        return
    for a in range(lo,n+1):
        if n-a < a*(k-1): break
        for rest in partitions_fixed(n-a,k-1,a):
            yield (a,)+rest

spider_types=0
vertex_subsets=0
for k in range(3,6):
    for lengths in product(range(1,5), repeat=k):
        if sum(lengths)>10: continue
        adj,arms=build_spider(lengths)
        n=len(adj)
        counts=[0]*(n+1)
        for mask in range(1<<n):
            vertex_subsets+=1
            truth=is_power_dominating(mask,adj)
            assert truth==predicted(mask,arms),(lengths,mask,truth)
            if truth: counts[mask.bit_count()]+=1
        assert counts==coeff_formula(lengths),(lengths,counts,coeff_formula(lengths))
        spider_types+=1

shapes=0
xs=[Fraction(1,2), Fraction(1,1), Fraction(2,1)]
for L in range(3,21):
    for k in range(3,min(6,L)+1):
        parts=list(partitions_fixed(L,k))
        if not parts: continue
        q,s=divmod(L,k)
        balanced=tuple(sorted([q+1]*s+[q]*(k-s)))
        concentrated=tuple(sorted([1]*(k-1)+[L-k+1]))
        for p in parts:
            shapes+=1
            for x in xs:
                vals={qv: polynomial_value(qv,x) for qv in parts}
                vmax=max(vals.values()); vmin=min(vals.values())
                maxs=[qv for qv,v in vals.items() if v==vmax]
                mins=[qv for qv,v in vals.items() if v==vmin]
                assert maxs==[balanced],(L,k,x,maxs,balanced)
                assert mins==[concentrated],(L,k,x,mins,concentrated)
            # don't recount values per shape; assertion repeated intentionally simple

print('VERIFY_OK')
print('spider_types_bruteforced =',spider_types)
print('vertex_subsets_checked =',vertex_subsets)
print('extremal_part_shapes_checked =',shapes)
print('extremal_evaluations_per_shape =',len(xs))
