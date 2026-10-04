from itertools import combinations
from math import comb

def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(1, total-parts+2):
        for tail in compositions(total-first, parts-1):
            yield (first,)+tail

def build(bs):
    seq=[]; blocks=[]
    for b in bs:
        a=len(seq); seq.append(('A',a))
        B=[]
        for _ in range(b):
            v=len(seq); seq.append(('B',v)); B.append(v)
        blocks.append(([a],B))
    n=len(seq); adj=[set() for _ in range(n)]
    for i,(typ,v) in enumerate(seq):
        if typ=='B':
            for _,u in seq[:i]:
                adj[v].add(u); adj[u].add(v)
    return adj,blocks

def stalled_white(W,adj):
    W=set(W)
    return bool(W) and all(len(adj[v]&W)!=1 for v in range(len(adj)))

def skew_closure(S,adj):
    blue=set(S); allv=set(range(len(adj)))
    while True:
        white=allv-blue; forced=set()
        for v in allv:
            wn=adj[v]&white
            if len(wn)==1: forced.update(wn)
        if not forced: return blue
        blue.update(forced)

def predicted_triples(bs,blocks):
    out=set(); earlier=[]
    for j,([a],B) in enumerate(blocks):
        before=earlier+[a]
        for pair in combinations(B,2):
            for q in before:
                out.add(tuple(sorted(pair+(q,))))
        for tri in combinations(B,3): out.add(tuple(sorted(tri)))
        earlier.extend([a]+B)
    return out

graphs=subset_checks=triple_checks=maxset_checks=0
for n in range(5,12):
    for p in range(2,n//2+1):
        total=n-p
        for bs in compositions(total,p):
            if not any(b>=2 for b in bs):
                continue
            adj,blocks=build(bs); graphs+=1
            pred=predicted_triples(bs,blocks)
            actual=set()
            for k in (1,2,3):
                for W in combinations(range(n),k):
                    subset_checks+=1
                    if stalled_white(W,adj):
                        if k<3:
                            raise AssertionError((n,bs,'smaller stalled white set',W))
                        actual.add(W)
            triple_checks += len(actual)
            if actual != pred:
                raise AssertionError((n,bs,'triple mismatch',actual^pred))
            failed=[]
            for mask in range(1<<n):
                S=[v for v in range(n) if (mask>>v)&1]
                subset_checks+=1
                if len(skew_closure(S,adj))<n:
                    failed.append(tuple(S))
            m=max(map(len,failed))
            maxsets=[S for S in failed if len(S)==m]
            expected=sum(comb(b,2)*(j+1+sum(bs[:j]))+comb(b,3) for j,b in enumerate(bs))
            maxset_checks += len(maxsets)
            if m != n-3 or len(maxsets) != expected:
                raise AssertionError((n,bs,'maximum mismatch',m,len(maxsets),expected))
print(f'VERIFY_OK graphs={graphs} subset_checks={subset_checks} stalled_triples={triple_checks} maximum_sets={maxset_checks} max_order=11')
