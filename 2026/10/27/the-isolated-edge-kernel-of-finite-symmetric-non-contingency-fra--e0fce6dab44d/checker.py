from itertools import combinations
from math import comb, factorial
from collections import defaultdict, Counter

def edges(n):return [(u,v) for u in range(n) for v in range(u+1,n)]
def neighbors(n,edge_mask):
    rows=[0]*n
    for i,(u,v) in enumerate(edges(n)):
        if edge_mask>>i&1:rows[u]|=1<<v;rows[v]|=1<<u
    return rows

def canonical(n,mask):
    rows=neighbors(n,mask)
    for i,(u,v) in enumerate(edges(n)):
        if mask>>i&1 and rows[u].bit_count()==rows[v].bit_count()==1:
            mask^=1<<i
    return mask

def signature(n,mask):
    rows=neighbors(n,mask)
    return tuple(tuple(1 if (row & pv)==0 or (row & pv)==row else 0 for pv in range(1<<n)) for row in rows)

def matching(n,k):return factorial(n)//(2**k*factorial(k)*factorial(n-2*k))
def quotient_formula(n):return sum((-1)**k*matching(n,k)*2**comb(n-2*k,2) for k in range(n//2+1))
def M(s):return sum(matching(s,k) for k in range(s//2+1))
def no_isolated_no_two_component(m):
    return sum((-1)**i*comb(m,i)*quotient_formula(m-i) for i in range(m+1))

checks=0
for n in range(1,7):
    groups=defaultdict(list); sig2can={}; qcounts=Counter()
    for mask in range(1<<comb(n,2)):
        c=canonical(n,mask); sig=signature(n,mask)
        assert sig2can.setdefault(sig,c)==c
        groups[c].append(mask)
        checks+=1
    assert len(sig2can)==len(groups)==quotient_formula(n)
    for can,lifts in groups.items():
        iso=sum(row==0 for row in neighbors(n,can))
        assert len(lifts)==M(iso)
        qcounts[iso]+=1
        checks+=1
    assert dict(qcounts)=={s:comb(n,s)*no_isolated_no_two_component(n-s) for s in range(n+1) if no_isolated_no_two_component(n-s)}
    assert sum(len(v) for v in groups.values())==2**comb(n,2)
    assert sum(qcounts[s]*M(s) for s in qcounts)==2**comb(n,2)
    print(n,len(groups),dict(sorted(qcounts.items())),max(map(len,groups.values())),sum(map(len,groups.values())))
print('ALL_CHECKS_OK',checks)
