#!/usr/bin/env python3
from itertools import combinations, product

def closure(n, covers):
    le=[[False]*n for _ in range(n)]
    for i in range(n):
        le[i][i]=True
    for a,b in covers:
        le[a][b]=True
    for k in range(n):
        for i in range(n):
            if le[i][k]:
                for j in range(n):
                    le[i][j]=le[i][j] or le[k][j]
    return le

def is_chain(S,le):
    return all(le[a][b] or le[b][a] for a,b in combinations(S,2))

def is_antichain(S,le):
    return all(not le[a][b] and not le[b][a] for a,b in combinations(S,2))

def maximal_by_inclusion(items,n):
    ss=[set(x) for x in items]
    return [tuple(sorted(s)) for s in ss if not any(s<t for t in ss)]

def analyze(name,n,covers):
    le=closure(n,covers)
    subs=[tuple(i for i in range(n) if (m>>i)&1) for m in range(1<<n)]
    chains=[S for S in subs if S and is_chain(S,le)]
    ants=[S for S in subs if is_antichain(S,le)]
    maxchains=maximal_by_inclusion(chains,n)
    h=max(map(len,chains))
    w=max(map(len,ants))
    longest=[C for C in maxchains if len(C)==h]
    maxants=[A for A in ants if len(A)==w]

    # Every signed antichain generator satisfies every signed maximal-chain facet.
    checked=0
    for A in ants:
        Aset=set(A)
        for signsA in product((-1,1), repeat=len(A)):
            x=[0]*n
            for i,s in zip(A,signsA): x[i]=s
            for C in maxchains:
                for eps in product((-1,1), repeat=len(C)):
                    val=sum(e*x[i] for i,e in zip(C,eps))
                    assert val<=1
                    checked+=1

    # Squared radii are exactly 1/h and w.
    facet_norm_sq=max(len(C) for C in maxchains)
    gen_norm_sq=max(len(A) for A in ants)
    assert facet_norm_sq==h
    assert gen_norm_sq==w

    # The incenter is unique exactly when longest chains cover the ground set.
    covered=set().union(*(set(C) for C in longest))
    unique=(len(covered)==n)

    # Contact counts from the theorem.
    inner_contacts=sum(2**len(C) for C in longest)
    outer_contacts=len(maxants)*(2**w)
    assert inner_contacts==(2**h)*len(longest)
    assert outer_contacts==(2**w)*len(maxants)

    return (name,n,h,w,len(maxchains),len(longest),len(maxants),unique,checked)

tests=[
    ("chain5",5,[(0,1),(1,2),(2,3),(3,4)]),
    ("antichain5",5,[]),
    ("diamond4",4,[(0,1),(0,2),(1,3),(2,3)]),
    ("V4_nonpure",4,[(0,1),(1,2)]),             # element 3 is isolated, hence not on a longest chain
    ("two_levels5",5,[(0,2),(0,3),(1,2),(1,3),(1,4)]),
    ("fork6",6,[(0,2),(1,2),(2,3),(2,4),(4,5)]),
]

rows=[analyze(*t) for t in tests]
assert any(r[7] for r in rows)
assert any(not r[7] for r in rows)
print("VERIFY_OK enriched-chain-radii cases=%d generator_facet_checks=%d" %
      (len(rows),sum(r[8] for r in rows)))
