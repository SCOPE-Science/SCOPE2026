from itertools import combinations
from collections import defaultdict

def ap_masks(n):
    out=[]
    for a in range(n):
        for c in range(a+1,n):
            if (a+c)%2==0:
                b=(a+c)//2
                if a<b<c:
                    out.append((1<<a)|(1<<b)|(1<<c))
    return sorted(set(out))

def contains_ap(mask, aps):
    return any(mask & t == t for t in aps)

def maximum_families(n):
    aps=ap_masks(n)
    verts=[m for m in range(1<<n) if contains_ap(m,aps)]
    k=len(verts)
    adj=[0]*k
    for i in range(k):
        ai=verts[i]
        bits=0
        for j in range(k):
            if i!=j and contains_ap(ai & verts[j],aps):
                bits |= 1<<j
        adj[i]=bits
    best=0; max_cliques=[]
    def bk(R,P,X):
        nonlocal best,max_cliques
        if R.bit_count()+P.bit_count()<best:
            return
        if not P and not X:
            s=R.bit_count()
            if s>best:
                best=s; max_cliques=[R]
            elif s==best:
                max_cliques.append(R)
            return
        U=P|X
        if U:
            # Pivot maximizing neighbors in P; deterministic tie by low index.
            uu=U; pivot=None; pv=-1
            while uu:
                lb=uu & -uu; u=lb.bit_length()-1; uu-=lb
                z=(P & adj[u]).bit_count()
                if z>pv: pv=z; pivot=u
            cand=P & ~adj[pivot]
        else:
            cand=P
        while cand:
            lb=cand & -cand; v=lb.bit_length()-1; cand-=lb
            bk(R|lb, P & adj[v], X & adj[v])
            P &= ~lb; X |= lb
            if R.bit_count()+P.bit_count()<best:
                return
    bk(0,(1<<k)-1,0)
    fams=[]
    for C in max_cliques:
        fams.append(frozenset(verts[i] for i in range(k) if (C>>i)&1))
    return aps,fams

def stars(n,aps):
    return {frozenset(m for m in range(1<<n) if m&t==t) for t in aps}

def pair_majority(n,aps):
    comps=defaultdict(set)
    for t in aps:
        pts=[i for i in range(n) if t>>i&1]
        for p in combinations(pts,2):
            third=next(i for i in pts if i not in p)
            comps[p].add(third)
    fams={}
    for p,C in sorted(comps.items()):
        if len(C)==3:
            pm=(1<<p[0])|(1<<p[1]); cm=sum(1<<x for x in C)
            F=frozenset(m for m in range(1<<n) if m&pm==pm and (m&cm).bit_count()>=2)
            fams[p]=(tuple(sorted(C)),F)
    return fams

EXPECTED_COUNTS={3:1,4:2,5:4,6:6,7:10,8:14,9:19,10:24}
EXPECTED_NONPR={3:0,4:0,5:0,6:0,7:1,8:2,9:3,10:4}
for n in range(3,11):
    aps,fams=maximum_families(n)
    S=stars(n,aps); M=pair_majority(n,aps)
    candidates=S | {F for _,F in M.values()}
    assert fams, n
    sizes={len(F) for F in fams}
    assert sizes=={1<<(n-3)}, (n,sizes)
    assert len(fams)==EXPECTED_COUNTS[n], (n,len(fams))
    assert len(M)==EXPECTED_NONPR[n], (n,len(M))
    assert set(fams)==candidates, (n,len(set(fams)-candidates),len(candidates-set(fams)))
    # Direct pairwise property for all candidates.
    for F in candidates:
        for A in F:
            for B in F:
                assert contains_ap(A&B,aps), (n,A,B)
    details=[([a+1,b+1],[x+1 for x in C]) for (a,b),(C,_) in M.items()]
    print(n, len(aps), len(fams), len(S), len(M), details)
print('ALL CHECKS PASSED')
