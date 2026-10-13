#!/usr/bin/env python3
from itertools import combinations

def supports(a):
    r=len(a)
    full=(1<<r)-1
    ws={}
    for m in range(1,full):
        z=1
        for i,x in enumerate(a):
            if m>>i&1:
                z*=x
        ws[m]=z
    return ws

def complement_pairs(r):
    full=(1<<r)-1
    out=[]
    seen=set()
    for m in range(1,full):
        if m in seen: continue
        c=full^m
        seen.add(m); seen.add(c)
        out.append((m,c))
    return out

def expected(a):
    ws=supports(a)
    pairs=complement_pairs(len(a))
    alpha=sum(max(ws[x],ws[y]) for x,y in pairs)
    tau=sum(ws[x]==ws[y] for x,y in pairs)
    return alpha,tau

def exhaustive_pairs(a):
    ws=supports(a)
    pairs=complement_pairs(len(a))
    best=-1
    count=0
    examples=[]
    for bits in range(1<<len(pairs)):
        fam=[]
        wt=0
        for j,(x,y) in enumerate(pairs):
            z=y if (bits>>j)&1 else x
            fam.append(z); wt+=ws[z]
        ok=True
        for x,y in combinations(fam,2):
            if x&y==0:
                ok=False; break
        if not ok:
            continue
        if wt>best:
            best=wt; count=1; examples=[tuple(sorted(fam))]
        elif wt==best:
            count+=1
            if len(examples)<3:
                examples.append(tuple(sorted(fam)))
    return best,count,examples

def formula_alt(q):
    a=[x-1 for x in q]
    ws=supports(a)
    N=1
    P=1
    for x in q: N*=x
    for x in a: P*=x
    N=N-P-1
    full=(1<<len(q))-1
    abs_sum=sum(abs(ws[m]-ws[full^m]) for m in ws)
    val_num=2*N+abs_sum
    assert val_num%4==0
    return val_num//4

def alikhani_r3(a):
    a=sorted(a,reverse=True)
    n1,n2,n3=a
    return n1*n2+n1*n3+max(n1,n2*n3)

tests=[
    (3,3),
    (3,5),
    (3,3,3),
    (7,5,5),
    (3,4,7),
    (3,3,3,3),
    (3,3,4,4),
    (3,4,5,7),
    (3,3,3,3,3),
    (3,3,3,4,5),
]
for q in tests:
    a=[x-1 for x in q]
    alpha,tau=expected(a)
    assert alpha==formula_alt(q)
    if len(q)<=5:
        b,c,_=exhaustive_pairs(a)
        assert b==alpha
        assert c==(1<<tau)
    if len(q)==3:
        assert alpha==alikhani_r3(a)
    print("q=",q,"alpha=",alpha,"ties=",tau,"max_families=",1<<tau)

# Symbolic-sized checks beyond exhaustive pair selection.
for q in [
    (3,3,3,3,3,3),
    (3,4,5,7,8,9),
    (5,5,5,5,5,5,5),
]:
    alpha,tau=expected([x-1 for x in q])
    assert alpha==formula_alt(q)
    print("large q=",q,"alpha=",alpha,"ties=",tau,"max_families=",1<<tau)

print("VERIFY_OK")
