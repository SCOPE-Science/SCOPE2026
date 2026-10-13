from itertools import product
from fractions import Fraction

def canonical(seq):
    remap={}; nxt=0; out=[]
    for x in seq:
        if x not in remap:
            remap[x]=nxt; nxt+=1
        out.append(remap[x])
    # partition canonical independent of traversal label, canonical relabel is enough
    return tuple(out)

def fat(seq):
    n=len(seq); colors=sorted(set(seq)); k=len(colors)
    if k==1: return (True,Fraction(0),Fraction(1))
    # infer alpha,beta from each incidence; require common values
    aval=None; bval=None
    for v in range(n):
        deg=2
        counts={c:0 for c in colors}
        for u in ((v-1)%n,(v+1)%n): counts[seq[u]]+=1
        for c in colors:
            val=Fraction(counts[c],deg)
            if c==seq[v]:
                if bval is None: bval=val
                elif bval!=val: return (False,None,None)
            else:
                if aval is None: aval=val
                elif aval!=val: return (False,None,None)
    return (True,aval,bval)

def refines(a,b):
    # partition a finer than b: equal a-color => must imply equal b-color
    mp={}
    for x,y in zip(a,b):
        if x in mp and mp[x]!=y: return False
        mp[x]=y
    return True

def predicted(n):
    parts=[]
    parts.append(tuple(0 for _ in range(n)))
    if n%2==0:
        parts.append(canonical(tuple(i%2 for i in range(n))))
    if n%4==0:
        parts.append(canonical(tuple((i//2)%2 for i in range(n))))
        parts.append(canonical(tuple(((i+1)//2)%2 for i in range(n))))
    if n%3==0:
        parts.append(canonical(tuple(i%3 for i in range(n))))
    return set(parts)

total_labeled=0
total_fat_partitions=0
for n in range(3,13):
    found={}
    for k in (1,2,3):
        for seq in product(range(k), repeat=n):
            total_labeled+=1
            if set(seq)!=set(range(k)): continue
            ok,a,b=fat(seq)
            if ok:
                c=canonical(seq)
                found[c]=(a,b)
    if set(found)!=predicted(n):
        print('FOUND',n,found)
        print('PRED',predicted(n))
        raise SystemExit(('classification mismatch',n))
    total_fat_partitions += len(found)
    irreduc=[]
    for p in found:
        if not any(q!=p and len(set(q))>len(set(p)) and refines(q,p) for q in found):
            irreduc.append(p)
    expected=1+2*(n%4==0)+(n%6==0)
    if len(irreduc)!=expected:
        raise SystemExit(('irreducible mismatch',n,len(irreduc),expected))
    print(f'n={n}: FAT_partitions={len(found)} irreducible={len(irreduc)} expected={expected}')
print(f'ALL CHECKS PASSED; n_range=3..12; labeled_colorings_checked={total_labeled}; FAT_partitions={total_fat_partitions}')
