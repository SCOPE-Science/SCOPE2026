#!/usr/bin/env python3
import itertools, json, collections
from pathlib import Path

def suffix_has_square(w):
    n=len(w)
    for p in range(1,n//2+1):
        if w[n-2*p:n-p] == w[n-p:n]:
            return True
    return False

def direct_has_square(w):
    n=len(w)
    for i in range(n):
        for p in range(1,(n-i)//2+1):
            if w[i:i+p] == w[i+p:i+2*p]:
                return True
    return False

def engine_prefix(n):
    cur=[""]
    for _ in range(n):
        nxt=[]
        for w in cur:
            for c in "012":
                q=w+c
                if not suffix_has_square(q):
                    nxt.append(q)
        cur=sorted(nxt)
    return cur

def engine_direct(n):
    out=[]
    for t in itertools.product("012", repeat=n):
        w="".join(t)
        if not direct_has_square(w):
            out.append(w)
    return out

def irreducible(w):
    if direct_has_square(w):
        return False
    for i in range(1,len(w)-1):
        if not direct_has_square(w[:i]+w[i+1:]):
            return False
    return True

def least_square_period_a(w):
    best=None
    n=len(w)
    for i in range(n):
        for p in range(1,(n-i)//2+1):
            if w[i:i+p] == w[i+p:i+2*p]:
                best=p if best is None else min(best,p)
    return best

def least_square_period_b(w):
    n=len(w)
    for p in range(1,n//2+1):
        for i in range(0,n-2*p+1):
            if w[i:i+p] == w[i+p:i+2*p]:
                return p
    return None

def radius(w, fn):
    return max(fn(w[:i]+w[i+1:]) for i in range(1,len(w)-1))

def rename(w,p):
    d=dict(zip("012",p))
    return "".join(d[c] for c in w)

def orbit(w):
    ps=itertools.permutations("012")
    # Materialize because permutations iterator is one-shot.
    ps=list(ps)
    return {rename(z,p) for z in (w,w[::-1]) for p in ps}

root=Path(__file__).resolve().parent
cert=json.loads((root/"certificate.json").read_text(encoding="utf-8"))

A=engine_prefix(13)
B=engine_direct(13)
assert A==B
assert len(A)==cert["squarefree_count"]==342

I=sorted(w for w in A if irreducible(w))
assert len(I)==cert["irreducibly_squarefree_count"]==30

# Two independently ordered least-period scans must agree after every deletion.
for w in I:
    for i in range(1,12):
        q=w[:i]+w[i+1:]
        assert least_square_period_a(q)==least_square_period_b(q)

hist=collections.Counter(radius(w,least_square_period_a) for w in I)
assert hist=={3:18,6:12}
assert cert["radius_histogram"]=={"3":18,"6":12}

remaining=set(I)
od=[]
while remaining:
    rep=min(remaining)
    o=orbit(rep)&set(I)
    od.append((rep,len(o),radius(rep,least_square_period_a),o))
    remaining-=o
summary=[(a,b,c) for a,b,c,_ in od]
assert summary==[
    ("0102012101202",12,3),
    ("0102012102010",6,3),
    ("0102120102012",12,6),
]
assert [
    (x["representative"],x["orbit_size"],x["rho"])
    for x in cert["orbit_data"]
]==summary

rho6=set(w for w in I if radius(w,least_square_period_a)==6)
assert rho6==od[2][3]
for w in rho6:
    sites=[]
    for i in range(1,12):
        q=w[:i]+w[i+1:]
        if least_square_period_a(q)==6:
            sites.append(i+1)
            assert len(q)==12 and q[:6]==q[6:]
            assert least_square_period_b(q)==6
    assert len(sites)==1
    assert cert["rho6_words_and_unique_global_deletion_position_1_based"][w]==sites[0]

r=cert["rho6_representative_global_deletion"]
w=r["word"]; i=r["deleted_position_1_based"]-1
q=w[:i]+w[i+1:]
assert q==r["result"]=="010212010212"
assert q==r["square_root"]*2
assert least_square_period_a(q)==r["least_square_period"]==6

print(
    "VERIFY_OK length=13 squarefree=342 irreducible=30 "
    "rho_hist=3:18,6:12 orbits=3 orbit_sizes=12,6,12 "
    "global_class=0102120102012 unique_global_site_per_word=1 engines=2"
)
