#!/usr/bin/env python3
import itertools

def profiles(n, last=2, prefix=()):
    if n == 0:
        if len(prefix) >= 2:
            yield prefix
        return
    for x in range(last, n + 1):
        if x >= 2:
            yield from profiles(n - x, x, prefix + (x,))

def part_map(parts):
    ans=[]
    for i,a in enumerate(parts):
        ans.extend([i]*a)
    return ans

def valid(parts, lab):
    po=part_map(parts)
    n=len(lab)
    pos=[x>0 for x in lab]
    for v in range(n):
        if pos[v] and not any(pos[u] and po[u]!=po[v] for u in range(n)):
            return False
    for v,x in enumerate(lab):
        if x<3:
            active=0
            total=x
            for u in range(n):
                if po[u]!=po[v]:
                    total += lab[u]
                    if lab[u]>0:
                        active += 1
            if total < active+3:
                return False
    return True

def predicted(parts):
    return 7 if min(parts)==2 else 8

def brute(parts):
    n=sum(parts)
    target=predicted(parts)
    found=False
    for lab in itertools.product(range(5), repeat=n):
        w=sum(lab)
        if w>target:
            continue
        if valid(parts,lab):
            if w<target:
                raise AssertionError((parts,'counterexample',w,lab))
            found=True
            break
    if not found:
        raise AssertionError((parts,'no target witness'))

def construction(parts):
    po=part_map(parts)
    n=sum(parts)
    lab=[0]*n
    if min(parts)==2:
        i=parts.index(2)
        inds=[v for v,p in enumerate(po) if p==i]
        j=0 if i!=0 else 1
        c=next(v for v,p in enumerate(po) if p==j)
        lab[inds[0]]=3; lab[inds[1]]=2; lab[c]=2
    else:
        a=next(v for v,p in enumerate(po) if p==0)
        b=next(v for v,p in enumerate(po) if p==1)
        lab[a]=4; lab[b]=4
    assert sum(lab)==predicted(parts)
    assert valid(parts,lab), (parts,lab)

count=0
for n in range(4,9):
    for p in profiles(n):
        brute(p); count+=1

construction_count=0
for n in range(4,31):
    for p in profiles(n):
        construction(p); construction_count+=1

print(f'ALL CHECKS PASSED; exhaustive_profiles={count}; exhaustive_orders=4..8; construction_profiles={construction_count}; construction_orders=4..30')
