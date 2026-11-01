#!/usr/bin/env python3
"""Finite checks for fixed loci of total two-cut Hamming complexes.
Only Python standard library. No external data; comparisons use graph nonedges.
"""
from itertools import product, permutations
from collections import defaultdict
from math import comb

def test_case(n, q, homology=False, character=False):
    words = list(product(range(q), repeat=n))
    def hist(w):
        return tuple(w.count(c) for c in range(q))
    groups = defaultdict(list)
    for w in words:
        groups[hist(w)].append(w)
    types = sorted(groups)
    T = len(types)
    index = {x:i for i,x in enumerate(types)}
    u = {i for i,x in enumerate(types) if max(x)!=n}
    c = {i for i,x in enumerate(types) if max(x)==n}
    assert len(c)==q and T==comb(n+q-1,q-1)
    full=(1<<T)-1
    pairmasks=set()
    for i,v in enumerate(words):
        for w in words[i+1:]:
            if sum(a!=b for a,b in zip(v,w))>=2:
                pairmasks.add((1<<index[hist(v)])|(1<<index[hist(w)]))
    pairmasks = sorted(pairmasks)
    faces=[]
    for mask in range(1<<T):
        direct=any((mask&p)==0 for p in pairmasks)
        expected = any(not (mask>>i)&1 for i in u) or sum(not (mask>>i)&1 for i in c)>=2
        assert direct==expected, (n,q,mask,direct,expected)
        if direct:faces.append(mask)
    assert 0 in faces
    faces_set=set(faces)
    dual={mask for mask in range(1<<T) if (full^mask) not in faces_set}
    assert dual=={0}|{1<<i for i in c}
    d=T-3
    ranks={}
    if homology:
        chain=defaultdict(list)
        for m in faces:
            if m: chain[m.bit_count()-1].append(m)
        for k,lst in chain.items():
            if k==0:
                ranks[k]=1
                continue
            rows={m:i for i,m in enumerate(chain[k-1])}
            pivots={}
            for m in lst:
                bits=0
                mm=m
                while mm:
                    b=mm&-mm
                    mm-=b
                    bits^=1<<rows[m^b]
                while bits:
                    p=bits.bit_length()-1
                    if p in pivots: bits^=pivots[p]
                    else:
                        pivots[p]=bits
                        break
            ranks[k]=len(pivots)
        betti={k:len(lst)-ranks.get(k,0)-ranks.get(k+1,0) for k,lst in chain.items()}
        assert {k:v for k,v in betti.items() if v}=={d:q-1}, (n,q,betti)
    nc=0
    if character:
        for perm in permutations(range(q)):
            induced = []
            for t in types:
                trans=[0]*q
                for a,count in enumerate(t):trans[perm[a]]=count
                induced.append(index[tuple(trans)])
            sign_total=(-1)**sum(induced[i]>induced[j] for i in range(T) for j in range(i+1,T))
            fix=sum(perm[i]==i for i in range(q))
            Lef=-1
            for m in faces:
                if not m: continue
                old=[i for i in range(T) if (m>>i)&1]
                new=[induced[i] for i in old]
                if set(new)!=set(old):continue
                ori=(-1)**sum(new[i]>new[j] for i in range(len(new)) for j in range(i+1,len(new)))
                Lef+=((-1)**(len(old)-1))*ori
            predicted=((-1)**d)*sign_total*(fix-1)
            assert Lef==predicted,(n,q,perm,Lef,predicted)
            nc+=1
    return (n,q,len(words),T,len(faces),len(pairmasks),d,ranks.get(d,0),nc)

if __name__=='__main__':
    checks=[(2,2),(3,2),(4,2),(5,2),(6,2), (2,3),(3,3),(4,3), (2,4),(3,4), (2,5)]
    records=[]
    for n,q in checks:
        records.append(test_case(n,q,homology=(comb(n+q-1,q-1)<=10),character=(comb(n+q-1,q-1)<=10)))
    for rec in records: print('PASS n,q,words,orbits,faces,nonedge-orbit-sets,topdim,top_boundary_rank,characters=',rec)
    print('ALL_OK',len(records),'cases',sum(r[4] for r in records),'quotient faces',sum(r[-1] for r in records),'integral-character-Lefschetz comparisons')
