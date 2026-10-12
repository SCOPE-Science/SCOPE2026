#!/usr/bin/env python3
import itertools,json,math
from pathlib import Path
def primitive(w):
    n=len(w)
    return not any(n%d==0 and w==w[:d]*(n//d) for d in range(1,n))
def mu(n):
    x=n;m=1;p=2
    while p*p<=x:
        if x%p==0:
            x//=p;m=-m
            if x%p==0:return 0
            while x%p==0:x//=p
        p+=1
    if x>1:m=-m
    return m
def pi(q,n):return sum(mu(d)*q**(n//d) for d in range(1,n+1) if n%d==0)
def expected(q,l):return sum(pi(q,2*l//d) for d in range(3,l+1,2) if l%d==0)
C=json.loads((Path(__file__).resolve().parent/"certificate.json").read_text())
seen=[]
for q,maxl in ((2,9),(3,6)):
    A="012"[:q]
    for l in range(1,maxl+1):
        P=["".join(t) for t in itertools.product(A,repeat=l) if primitive("".join(t))]
        deg={p:0 for p in P};ordered=0
        for p in P:
            for r in P:
                if p!=r and not primitive(p+r):deg[p]+=1;ordered+=1
        md=max(deg.values(),default=0)
        assert md<=1 and ordered==expected(q,l)
        seen.append({"alphabet_size":q,"length":l,"primitive_vertices":len(P),"ordered_edges":ordered,"max_degree":md})
assert seen==C["finite_checks"]
for d in range(3,1001,2):
    for e in range(3,1001,2):
        if d!=e:assert 2/d+2/e-2/math.lcm(d,e)<=1+1e-15
for q,maxl in ((2,8),(3,5)):
    A="012"[:q]
    for l in range(1,maxl+1):
        P=["".join(t) for t in itertools.product(A,repeat=l) if primitive("".join(t))]
        for p in P:
            for r in P:assert (not primitive(p+r))==(not primitive(r+p))
print("VERIFY_OK theorem=matching finite_checks=q2_l1..9,q3_l1..6 formula_checks=all finite cases max_degree=1 fine_wilf_pairs_odd_3..999 symmetry_checks=1")
