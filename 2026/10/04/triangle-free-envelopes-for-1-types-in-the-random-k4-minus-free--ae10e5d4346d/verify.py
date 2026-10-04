#!/usr/bin/env python3
from itertools import combinations

def data(n):
    pairs=list(combinations(range(n),2))
    pidx={p:i for i,p in enumerate(pairs)}
    triples=list(combinations(range(n),3))
    tidx={t:i for i,t in enumerate(triples)}
    fours=list(combinations(range(n),4))
    return pairs,pidx,triples,tidx,fours

def legal_A(n, amask):
    _,_,triples,tidx,fours=data(n)
    for Q in fours:
        c=sum((amask>>tidx[t])&1 for t in combinations(Q,3))
        if c>2: return False
    return True

def direct_poly(n, amask):
    pairs,pidx,triples,tidx,_=data(n)
    out=[0]*(len(pairs)+1)
    for lmask in range(1<<len(pairs)):
        ok=True
        for a,b,c in triples:
            old=(amask>>tidx[(a,b,c)])&1
            q=((lmask>>pidx[(a,b)])&1)+((lmask>>pidx[(a,c)])&1)+((lmask>>pidx[(b,c)])&1)
            if old+q>2:
                ok=False; break
        if ok: out[lmask.bit_count()]+=1
    return out

def conflict_poly(n, amask):
    pairs,pidx,triples,tidx,_=data(n)
    conflicts=[]
    for a,b,c in triples:
        ids=[pidx[(a,b)],pidx[(a,c)],pidx[(b,c)]]
        if (amask>>tidx[(a,b,c)])&1:
            conflicts += [(1<<ids[i])|(1<<ids[j]) for i,j in [(0,1),(0,2),(1,2)]]
        else:
            conflicts.append(sum(1<<i for i in ids))
    out=[0]*(len(pairs)+1)
    for m in range(1<<len(pairs)):
        if all((m&c)!=c for c in conflicts): out[m.bit_count()]+=1
    return out

def triangle_poly(n):
    pairs,pidx,triples,_,_=data(n)
    tris=[(1<<pidx[(a,b)])|(1<<pidx[(a,c)])|(1<<pidx[(b,c)]) for a,b,c in triples]
    out=[0]*(len(pairs)+1)
    for m in range(1<<len(pairs)):
        if all((m&t)!=t for t in tris): out[m.bit_count()]+=1
    return out

def main():
    legal_counts=[]
    checked=0
    for n in range(0,6):
        triples=list(combinations(range(n),3))
        tp=triangle_poly(n)
        legal=0
        for amask in range(1<<len(triples)):
            if not legal_A(n,amask): continue
            legal+=1; checked+=1
            a=direct_poly(n,amask)
            b=conflict_poly(n,amask)
            assert a==b
            assert all(x<=y for x,y in zip(a,tp))
            if amask==0: assert a==tp
            elif n>=3: assert a!=tp and a[2]<tp[2]
        legal_counts.append(legal)
    totals=[]
    for n in range(8): totals.append(sum(triangle_poly(n)))
    assert totals==[1,1,2,7,41,388,5789,133501]
    print('legal_parameter_structures_n0_to5=',legal_counts)
    print('checked_parameter_structures=',checked)
    print('triangle_free_totals_n0_to7=',totals)
    print('VERIFY_OK')
if __name__=='__main__': main()
