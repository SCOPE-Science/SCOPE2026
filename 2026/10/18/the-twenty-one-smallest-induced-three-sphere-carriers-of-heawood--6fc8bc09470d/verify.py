#!/usr/bin/env python3
"""Exact simplicial and induced-carrier verification for the Heawood independence complex.
Requires only the Python 3 standard library.
"""
from itertools import combinations
from collections import Counter,deque

V=tuple(range(14))
A=[set() for _ in V]
for p in range(1,8):
    for l in range(1,8):
        if ((p & l).bit_count() % 2)==0:
            a=p-1;b=l+6
            A[a].add(b);A[b].add(a)
assert sum(map(len,A))==42
F={d:[] for d in range(7)}
for k in range(1,15):
    for t in combinations(V,k):
        if all(j not in A[i] for i,j in combinations(t,2)):
            F[k-1].append(t)
assert [len(F[d]) for d in range(7)]==[14,70,154,147,56,14,2]
IDX={d:{t:i for i,t in enumerate(F[d])} for d in F}
M={d:{t:sum(1<<i for i in t) for t in F[d]} for d in F}
D3={t:sum(1<<IDX[2][f] for f in combinations(t,3)) for t in F[3]}
D4={t:sum(1<<IDX[3][f] for f in combinations(t,4)) for t in F[4]}

class GF2Basis:
    def __init__(self,other=None): self.p={} if other is None else other.p.copy()
    def reduce(self,v):
        while v:
            h=v.bit_length()-1
            if h not in self.p: return v
            v^=self.p[h]
        return 0
    def insert(self,v):
        v=self.reduce(v)
        if v:
            self.p[v.bit_length()-1]=v
            return True
        return False
    def __len__(self): return len(self.p)

def morse(face_tuples,order,expected):
    FF=set(map(frozenset,face_tuples))
    U=set(FF);pairs=[]
    for v in order:
        lower=sorted((t for t in U if v not in t and t|{v} in U),key=lambda f:(len(f),tuple(sorted(f))))
        for lo in lower:
            hi=lo|{v}
            if lo in U and hi in U:
                U.remove(lo);U.remove(hi);pairs.append((lo,hi))
    assert Counter(len(t)-1 for t in U)==Counter(expected)
    assert len(pairs)*2+len(U)==len(FF)
    oriented={(a,b) for a,b in pairs};out={v:[] for v in FF};indeg={v:0 for v in FF}
    for hi in FF:
        for x in hi:
            lo=hi-{x}
            if lo not in FF:continue
            src,dst=(lo,hi) if (lo,hi) in oriented else (hi,lo)
            out[src].append(dst);indeg[dst]+=1
    q=deque(t for t in FF if not indeg[t]);count=0
    while q:
        a=q.popleft();count+=1
        for b in out[a]:
            indeg[b]-=1
            if indeg[b]==0:q.append(b)
    assert count==len(FF),('cyclic matching',count,len(FF))
    return len(pairs)

assert morse(sum((F[d] for d in F),[]),V,{0:1,3:6})==225
full4=GF2Basis()
for v in D4.values():full4.insert(v)
assert len(full4)==44
hits=[];gen=[]
for k in (9,10):
    for W in combinations(V,k):
        mask=sum(1<<i for i in W)
        C3=[q for q in F[3] if M[3][q]&mask==M[3][q]]
        C4=[q for q in F[4] if M[4][q]&mask==M[4][q]]
        bb3=GF2Basis()
        for q in C3: bb3.insert(D3[q])
        bb4=GF2Basis()
        for q in C4: bb4.insert(D4[q])
        beta=len(C3)-len(bb3)-len(bb4)
        assert beta>=0
        if k==9: assert beta==0
        elif beta:
            assert beta==1
            hits.append(W)
            # Exact GF(2) kernel vectors of boundary in global simplex coordinates.
            echelon={};cycles=[]
            for q in C3:
                col=D3[q];chain=1<<IDX[3][q]
                while col:
                    h=col.bit_length()-1
                    if h in echelon:
                        old_col,old_chain=echelon[h]
                        col^=old_col;chain^=old_chain
                    else:
                        echelon[h]=(col,chain)
                        break
                if col==0: cycles.append(chain)
            found=next((z for z in cycles if bb4.reduce(z)!=0),None)
            assert found is not None
            assert full4.reduce(found)!=0,('non-surviving',W)
            gen.append(found)
assert len(hits)==21
expected=[]
for p,q in combinations(range(7),2):
    avoiding=[l for l in range(7) if l+7 not in A[p] and l+7 not in A[q]]
    assert len(avoiding)==2
    excluded={p,q}|{l+7 for l in avoiding}
    expected.append(tuple(i for i in V if i not in excluded))
assert sorted(hits)==sorted(expected)
for W in hits:
    subset={t for d in F for t in F[d] if all(i in W for i in t)}
    assert morse(subset,W,{0:1,3:1})==69
allimage=GF2Basis(full4)
for z in gen:allimage.insert(z)
assert len(allimage)-len(full4)==6
print('VERIFY_OK 2002_NINE_ZERO 21_TEN_SPHERES 21_NONZERO_MAPS SPAN_6')
