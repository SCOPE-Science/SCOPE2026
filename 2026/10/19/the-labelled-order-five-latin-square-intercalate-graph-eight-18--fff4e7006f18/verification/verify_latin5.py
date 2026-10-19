#!/usr/bin/env python3
"""Exhaustive labelled order-five Latin-square intercalate graph certificate.

With --certificate FILE, write lex-sorted 26-byte records: 25 symbols in
row-major order (values 0,..,4) and one component tag. Tag zero denotes a
vertex with no intercalates; nonzero tags 1,..,8 enumerate the mobile
components by their lexicographically least square.
"""
import argparse
import collections
import itertools
import hashlib
import json

N=5
P=list(itertools.permutations(range(N)))
options=[[p for p in P if p[0]==r] for r in range(N)]
reduced=[]

def extend(rows, masks):
    if len(rows)==N:
        reduced.append(bytes(x for row in rows for x in row))
        return
    r=len(rows)
    for p in options[r]:
        if all(not masks[c]&(1<<p[c]) for c in range(N)):
            extend(rows+[p],[masks[c]|1<<p[c] for c in range(N)])

extend([tuple(range(N))],[1<<c for c in range(N)])
assert len(reduced)==56
squares=[]
for b in reduced:
    for rows in itertools.permutations((1,2,3,4)):
        for sym in P:
            squares.append(bytes(sym[b[5*r+c]] for r in (0,)+rows for c in range(5)))
assert len(squares)==161280 and len(set(squares))==len(squares)
index={b:i for i,b in enumerate(squares)}
parent=list(range(len(squares)))
size=[1]*len(squares)
def root(i):
    while parent[i]!=i:
        parent[i]=parent[parent[i]]
        i=parent[i]
    return i
def unite(i,j):
    i=root(i);j=root(j)
    if i!=j:
        if size[i]<size[j]:i,j=j,i
        parent[j]=i;size[i]+=size[j]

def neighbours(b):
    for r in range(5):
        for s in range(r+1,5):
            for c in range(5):
                for t in range(c+1,5):
                    a=5*r+c;d=5*s+t;v=5*r+t;w=5*s+c
                    if b[a]==b[d] and b[v]==b[w]:
                        q=bytearray(b)
                        q[a],q[v]=q[v],q[a]
                        q[w],q[d]=q[d],q[w]
                        yield bytes(q)

def odd(p):
    return sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))%2

def parity(b):
    return (sum(odd(b[5*r:5*r+5]) for r in range(5))%2,
        sum(odd([b[5*r+c] for r in range(5)]) for c in range(5))%2,
        sum(odd([next(c for c in range(5) if b[5*r+c]==k) for r in range(5)]) for k in range(5))%2)

degree=collections.Counter()
pop=collections.Counter()
for i,b in enumerate(squares):
    d=0
    for q in neighbours(b):
        unite(i,index[q]);d+=1
    degree[d]+=1
    pop[(parity(b),d)]+=1

components=collections.defaultdict(list)
for i,b in enumerate(squares):components[root(i)].append(i)
component_sizes=collections.Counter(map(len,components.values()))
assert degree=={0:17280,4:144000}
assert component_sizes=={1:17280,18000:8}
parity_mobile=collections.Counter()
parity_frozen=collections.Counter()
mobile=[]
for v in components.values():
    if len(v)>1:
        pars={parity(squares[i]) for i in v}
        assert len(pars)==1
        parity_mobile[pars.pop()]+=1
        mobile.append((min(squares[i] for i in v),v))
    else:parity_frozen[parity(squares[v[0]])]+=1
assert set(parity_mobile.values())=={2}
assert set(parity_frozen.values())=={4320}
mobile.sort(key=lambda z:z[0])
tags=[0]*len(squares)
for t,(_,v) in enumerate(mobile,1):
    for i in v:tags[i]=t
h=hashlib.sha256()
args=argparse.ArgumentParser()
args.add_argument('--certificate',default='latin5_components.bin')
out=args.parse_args().certificate
with open(out,'wb') as f:
    for b in sorted(squares):
        rec=b+bytes((tags[index[b]],))
        f.write(rec);h.update(rec)
report={'reduced_squares':56,'labelled_squares':len(squares),
 'degree_distribution':{str(k):v for k,v in sorted(degree.items())},
 'edges':sum(k*v for k,v in degree.items())//2,
 'component_size_distribution':{str(k):v for k,v in sorted(component_sizes.items())},
 'component_count':len(components),
 'mobile_components_per_parity':{str(k):v for k,v in sorted(parity_mobile.items())},
 'isolated_per_parity':{str(k):v for k,v in sorted(parity_frozen.items())},
 'component_representatives':[''.join(map(str,s)) for s,_ in mobile],
 'certificate_sha256':h.hexdigest(),'certificate_bytes':26*len(squares)}
print(json.dumps(report,sort_keys=True,indent=2))
