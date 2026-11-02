#!/usr/bin/env python3
"""Reproduce finite counts for Boolean algebras with LFI operators.
This implementation uses direct truth-table enumeration for small carriers and
independent orbit and permutation-power computations for arbitrary displayed cases.
"""
from itertools import permutations, product
from math import factorial, prod

def positions(m):
    return [(a,j) for a in range(1<<m) for j in range(m) if a & (1<<j)]

def other_positions(m):
    return [(a,j) for a in range(1<<m) for j in range(m) if not(a & (1<<j))]

def act(p, a, j):
    b=0
    for x in range(len(p)):
        if (a>>x)&1: b|=1<<p[x]
    return (b,p[j])

def cycles_on(p,sites):
    sites=set(sites); unseen=set(sites); count=0
    while unseen:
        x=next(iter(unseen));count+=1;y=x
        while y in unseen:
            unseen.remove(y);y=act(p,*y)
        assert y==x
    return count

def formula_orbit(p):
    m=len(p); r=1;perm=tuple(range(m))
    powers=[perm]
    def compose(q,p): return tuple(q[p[i]] for i in range(m))
    q=p
    while q!=perm:
        powers.append(q);q=compose(p,q)
    r=len(powers)
    fix=0
    for q in powers:
        f=sum(q[i]==i for i in range(m))
        visited=set(); cyc=0
        for i in range(m):
            if i in visited: continue
            cyc+=1;j=i
            while j not in visited: visited.add(j);j=q[j]
        fix+= f*2**(cyc-1)
    assert fix%r==0
    return fix//r

def orbit_counts(m):
    ps=list(permutations(range(m)))
    coeff={q:0 for q in (2,4,6)}
    dist={}
    for p in ps:
        inside=cycles_on(p,positions(m))
        outside=cycles_on(p,other_positions(m))
        formula=formula_orbit(p)
        assert inside==outside==formula,(m,p,inside,outside,formula)
        dist[inside]=dist.get(inside,0)+1
        for q in coeff: coeff[q]+=q**inside
    assert all(k%factorial(m)==0 for k in coeff.values())
    return {q:k//factorial(m) for q,k in coeff.items()},dist

def truth_counts(m):
    """Enumerate all actual unary-operation pairs for m <= 2, no Burnside input."""
    sites=[(a,j) for a in range(1<<m) for j in range(m)]
    allowed=[]
    for a,j in sites:
        allowed.append(((0,0),(0,1),(1,0)) if a>>j&1 else ((1,0),(1,1)))
    allcnt=ciw=classical=both=0
    contradiction_distribution={}
    fixed={p:0 for p in permutations(range(m))}
    for table in product(*allowed):
        rows=dict(zip(sites,table))
        # Ground truth check of the identities by reconstructing the operations.
        neg=[];cons=[];mask=(1<<m)-1
        for a in range(1<<m):
            n=c=0
            for j in range(m):
                nb,cb=rows[a,j]
                n|=nb<<j;c|=cb<<j
            assert a|n==mask and (a&n&c)==0
            neg.append(n);cons.append(c)
        allcnt+=1
        t=sum(bool(a & neg[a] & (1<<j)) for a in range(1<<m) for j in range(m))
        contradiction_distribution[t]=contradiction_distribution.get(t,0)+1
        if all(cons[a]==mask ^ (a&neg[a]) for a in range(1<<m)):
            ciw+=1
        if all(neg[a]==mask^a for a in range(1<<m)):
            classical+=1
        if all(cons[a]==mask ^(a&neg[a]) and neg[a]==mask^a for a in range(1<<m)):
            both+=1
        for p in fixed:
            if all(rows[act(p,*s)]==rows[s] for s in sites):fixed[p]+=1
    L=m*2**(m-1)
    assert (allcnt,ciw,classical,both)==(6**L,2**L,4**L,1)
    from math import comb
    assert contradiction_distribution=={t: comb(L,t)*2**(2*L-t) for t in range(L+1)}
    assert sum(fixed.values())%factorial(m)==0
    return {'all':allcnt,'ciw':ciw,'classical':classical,'both':both,'orbit':sum(fixed.values())//factorial(m),'fixed':fixed}

for m in range(1,6):
    res,dist=orbit_counts(m)
    L=m*2**(m-1)
    assert res[6]*factorial(m)==sum(mult*6**o for o,mult in dist.items())
    assert res[4]*factorial(m)==sum(mult*4**o for o,mult in dist.items())
    assert res[2]*factorial(m)==sum(mult*2**o for o,mult in dist.items())
    if m<=2:
        direct=truth_counts(m)
        assert direct['orbit']==res[6]
        for p,v in direct['fixed'].items():
            assert v==6**formula_orbit(p)
        print('DIRECT',m,direct['all'],direct['ciw'],direct['classical'],direct['orbit'])
    print('ORBIT',m,'L',L,'all',res[6],'ciw',res[2],'classical',res[4], 'orbit_multiplicities',sorted(dist.items()))
print('ALL_CHECKS_OK')
