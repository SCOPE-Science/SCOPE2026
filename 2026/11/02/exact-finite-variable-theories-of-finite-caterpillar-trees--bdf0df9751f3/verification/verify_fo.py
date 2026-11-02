#!/usr/bin/env python3
"""Independent finite k-pebble partition refinement for small caterpillars.
No theorem is assumed by the refinement algorithm."""
from itertools import product
from collections import defaultdict

def adjacency(word):
    if word == ('SINGLE',): return [set()]
    if word == ('EDGE',): return [{1},{0}]
    m=len(word); n=m+sum(word); out=[set() for _ in range(n)]
    def edge(u,v):out[u].add(v);out[v].add(u)
    for i in range(m-1):edge(i,i+1)
    p=m
    for i,b in enumerate(word):
        for _ in range(b):edge(i,p);p+=1
    return out

def canonical(word): return min(tuple(word),tuple(word[::-1]))

def predicted(a,b,k):
    if a==('SINGLE',) or b==('SINGLE',): return a==b if k>=2 else True
    if a==('EDGE',) or b==('EDGE',): return a==b if k>=2 else True
    if k==2:return (len(a)==1)==(len(b)==1)
    if len(a)!=len(b):return False
    aa=tuple(min(x,k) for x in a);bb=tuple(min(x,k) for x in b)
    return canonical(aa)==canonical(bb)

def run(words,k):
    gs=[adjacency(w) for w in words]; offsets=[]; data=[];total=0
    for g in gs:
        n=len(g); offsets.append(total)
        tuples=list(product(range(n),repeat=k));data.append((n,g,tuples))
        total+=len(tuples)
    def compact(sigs):
        codes={};out=[]
        for sig in sigs:
            if sig not in codes:codes[sig]=len(codes)
            out.append(codes[sig])
        return out,len(codes)
    initial=[]
    for n,g,tuples in data:
        for t in tuples:
            initial.append(tuple((t[i]==t[j],t[j] in g[t[i]]) for i in range(k) for j in range(i+1,k)))
    colors,c=compact(initial)
    assert len(colors)==total
    for iteration in range(60):
        signatures=[]
        for (n,g,tuples),off in zip(data,offsets):
            strides=[n**(k-j-1) for j in range(k)]
            for idx,t in enumerate(tuples):
                sig=[colors[off+idx]]
                for j in range(k):
                    s=strides[j]; base=idx-t[j]*s
                    sig.append(tuple(sorted(set(colors[off+base+a*s] for a in range(n)))))
                signatures.append(tuple(sig))
        colors,newc=compact(signatures)
        if newc==c:break
        c=newc
    types=[]
    for i,(n,g,ts) in enumerate(data):
        off=offsets[i];types.append(set(colors[off:off+len(ts)]))
    checked=0
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            observed=bool(types[i]&types[j]);exp=predicted(words[i],words[j],k)
            if observed!=exp:raise AssertionError(f'FAIL {words[i]}, {words[j]}, k={k}: obs={observed},exp={exp}')
            checked+=1
    print(f'FO^{k}: {len(words)} models, {checked} pairs, {iteration+1} refinements, {c} final tuple types, ALL PASS')
    return checked

if __name__=='__main__':
    words=[]
    for m in range(1,5):
        alphs=[range(2,5)] if m==1 else [range(1,5)]+[range(0,3)]*(m-2)+[range(1,5)]
        for b in product(*alphs):
            if sum(b)+m>10:continue
            if tuple(b)==canonical(b):words.append(b)
    words=[('SINGLE',),('EDGE',)]+sorted(set(words))
    print('Models:',len(words),'vertices max:',max(len(adjacency(w)) for w in words))
    p2=run(words,2)
    p3=run(words,3)
    chosen=[('SINGLE',),('EDGE',),(1,1),(1,2),(1,3),(1,4),(2,2),(2,3),(2,4),(3,3),(3,4),(1,0,1),(1,0,2),(1,0,3),(1,0,4)]
    p4=run(chosen,4)
    print('VERIFIED',p2+p3+p4,'pairwise logical classifications')
