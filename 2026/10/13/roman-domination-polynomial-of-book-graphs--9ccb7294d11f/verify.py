from itertools import product
from collections import defaultdict


def add(*ps):
    out=defaultdict(int)
    for p in ps:
        for k,v in p.items(): out[k]+=v
    return {k:v for k,v in out.items() if v}

def scale(p,c): return {k:c*v for k,v in p.items() if c*v}
def mul(p,q):
    out=defaultdict(int)
    for i,a in p.items():
        for j,b in q.items(): out[i+j]+=a*b
    return dict(out)
def power(p,n):
    r={0:1}; b=p
    while n:
        if n&1:r=mul(r,b)
        b=mul(b,b); n//=2
    return r
def shift(p,s): return {k+s:v for k,v in p.items()}

def formula(n):
    one={0:1,1:1}
    A={2:3,3:2,4:1}
    A0={2:2,3:1}
    B={1:1,2:3,3:2,4:1}
    tri={0:1,1:1,2:1}
    return add(
        mul(power(one,2),power(A,n)),
        scale(mul(one,power(A0,n)),-2),
        {2*n:1},
        scale(shift(mul(one,power(B,n)),2),2),
        shift(power(tri,2*n),4),
    )

def graph(n):
    # vertices: u=0, v=1, a_i=2+2i, b_i=3+2i
    N=2*n+2
    adj=[set() for _ in range(N)]
    def edge(x,y): adj[x].add(y); adj[y].add(x)
    edge(0,1)
    for i in range(n):
        a=2+2*i; b=a+1
        edge(0,a); edge(a,b); edge(b,1)
    return adj

def rdf(adj,lab):
    return all(lab[v]!=0 or any(lab[w]==2 for w in adj[v]) for v in range(len(adj)))

total_assignments=total_rdfs=coefficient_checks=minimum_checks=total_checks=0
for n in range(1,6):
    adj=graph(n); hist=defaultdict(int)
    for lab in product((0,1,2), repeat=len(adj)):
        total_assignments += 1
        if rdf(adj,lab):
            hist[sum(lab)] += 1
            total_rdfs += 1
    hist=dict(hist); f=formula(n)
    keys=set(hist)|set(f)
    coefficient_checks += len(keys)
    assert hist==f, (n,hist,f)
    mw=min(hist); mc=hist[mw]
    expw=3 if n==1 else 4
    expc=4 if n==1 else (5 if n==2 else 1)
    assert (mw,mc)==(expw,expc), (n,mw,mc)
    minimum_checks += 1
    total_formula=4*(6**n)-4*(3**n)+1+4*(7**n)+(9**n)
    assert sum(hist.values())==total_formula
    total_checks += 1
print(f'VERIFY_OK n_range=1..5 labelings={total_assignments} rdf_functions={total_rdfs} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} total_checks={total_checks} max_order=12')
