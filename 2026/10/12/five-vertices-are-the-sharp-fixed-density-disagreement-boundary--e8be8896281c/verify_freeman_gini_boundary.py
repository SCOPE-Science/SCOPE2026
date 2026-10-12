#!/usr/bin/env python3
from itertools import combinations, permutations
from collections import defaultdict

def connected(n, edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    seen={0}
    stack=[0]
    while stack:
        u=stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v); stack.append(v)
    return len(seen)==n

def degree_sequence(n, edges):
    d=[0]*n
    for u,v in edges:
        d[u]+=1; d[v]+=1
    return tuple(sorted(d))

def freeman_num(ds):
    n=len(ds)
    return n*max(ds)-sum(ds)

def gini_unordered_num(ds):
    return sum(abs(a-b) for a,b in combinations(ds,2))

def canonical_code(n, edges):
    E={tuple(sorted(e)) for e in edges}
    best=None
    for p in permutations(range(n)):
        bits=[]
        for i,j in combinations(range(n),2):
            bits.append("1" if tuple(sorted((p[i],p[j]))) in E else "0")
        s="".join(bits)
        if best is None or s<best:
            best=s
    return best

connected_labeled={}
connected_unlabeled={}
reversals=[]

for n in range(2,6):
    poss=list(combinations(range(n),2))
    classes={}
    records=[]
    for mask in range(1<<len(poss)):
        if mask.bit_count() < n-1:
            continue
        edges=[poss[i] for i in range(len(poss)) if (mask>>i)&1]
        if not connected(n, edges):
            continue
        ds=degree_sequence(n, edges)
        code=canonical_code(n, edges)
        classes.setdefault(code, (ds, edges))
        records.append((len(edges), ds, code, edges))
    connected_labeled[n]=len(records)
    connected_unlabeled[n]=len(classes)

    by_m=defaultdict(dict)
    for m,ds,code,edges in records:
        by_m[m][code]=(ds,edges)

    for m, cm in by_m.items():
        vals=list(cm.values())
        for (ds1,e1),(ds2,e2) in combinations(vals,2):
            dc=freeman_num(ds1)-freeman_num(ds2)
            dg=gini_unordered_num(ds1)-gini_unordered_num(ds2)
            if dc*dg<0:
                reversals.append((n,m,ds1,ds2,freeman_num(ds1),freeman_num(ds2),
                                  gini_unordered_num(ds1),gini_unordered_num(ds2),e1,e2))

assert connected_labeled == {2:1,3:4,4:38,5:728}
assert connected_unlabeled == {2:1,3:2,4:6,5:21}

assert len(reversals)==1, reversals
r=reversals[0]
assert r[0]==5 and r[1]==6
pair={r[2],r[3]}
assert pair=={(2,2,2,2,4),(1,2,3,3,3)}

A=(2,2,2,2,4)
B=(1,2,3,3,3)
assert freeman_num(A)==8
assert freeman_num(B)==3
assert gini_unordered_num(A)==8
assert gini_unordered_num(B)==10

# Exact normalized values:
# Freeman degree centralization = freeman_num / ((n-1)(n-2))
# Degree Gini = unordered absolute-difference sum / (n * sum(degrees))
n=5
assert (freeman_num(A), (n-1)*(n-2)) == (8,12)
assert (freeman_num(B), (n-1)*(n-2)) == (3,12)
assert (gini_unordered_num(A), n*sum(A)) == (8,60)
assert (gini_unordered_num(B), n*sum(B)) == (10,60)

# Each reversing degree sequence is realized by exactly one unlabeled graph.
poss=list(combinations(range(5),2))
iso_by_seq=defaultdict(set)
example_by_seq={}
for mask in range(1<<len(poss)):
    if mask.bit_count()!=6:
        continue
    edges=[poss[i] for i in range(len(poss)) if (mask>>i)&1]
    if not connected(5,edges):
        continue
    ds=degree_sequence(5,edges)
    if ds in (A,B):
        code=canonical_code(5,edges)
        iso_by_seq[ds].add(code)
        example_by_seq.setdefault(ds,edges)
assert len(iso_by_seq[A])==1
assert len(iso_by_seq[B])==1

# Direct first-layer degree-sequence census at n=5,m=6.
seqs=set()
for mask in range(1<<len(poss)):
    if mask.bit_count()!=6:
        continue
    edges=[poss[i] for i in range(len(poss)) if (mask>>i)&1]
    if connected(5,edges):
        seqs.add(degree_sequence(5,edges))
assert seqs == {
    (1,2,2,3,4),
    (1,2,3,3,3),
    (2,2,2,2,4),
    (2,2,2,3,3),
}

print("VERIFY_OK")
print("connected_labeled", connected_labeled)
print("connected_unlabeled", connected_unlabeled)
print("unique_reversal", reversals[0][:8])
print("example_A_edges", example_by_seq[A])
print("example_B_edges", example_by_seq[B])
