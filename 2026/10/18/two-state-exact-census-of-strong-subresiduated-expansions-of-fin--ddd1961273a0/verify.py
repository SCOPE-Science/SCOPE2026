#!/usr/bin/env python3
"""Independent finite checks for strong subresiduated-lattice expansion counts."""
from itertools import product, permutations
from math import comb


def recurrence(levels):
    assert levels and min(levels)>=1
    single, multiple=(1,0) if levels[0]==1 else (0,1)
    for n in levels[1:]:
        if n==1:
            single, multiple=2*single+multiple,0
        else:
            single,multiple=(n+1)*single,(2**n-n-1)*single+multiple
    return single+multiple


def orbit_recurrence(levels):
    assert levels and min(levels)>=1
    single,multiple=(1,0) if levels[0]==1 else (0,1)
    for n in levels[1:]:
        if n==1:
            single,multiple=2*single+multiple,0
        else:
            single,multiple=2*single,(n-1)*single+multiple
    return single+multiple


def orbit_count_by_signatures(levels):
    lev,lower=model(levels)
    fs=set()
    for f in idempotent_maps(levels):
        sizes=tuple(sum(lev[i]==j and f[i]==i for i in range(len(lev))) for j in range(len(levels)))
        fs.add(sizes)
    return len(fs)


def model(levels):
    lev=[]
    for i,n in enumerate(levels):
        lev.extend([i]*n)
    lower=[[j for j in range(len(lev)) if lev[j]<lev[i] or j==i] for i in range(len(lev))]
    return lev,lower


def idempotent_maps(levels):
    lev,lower=model(levels)
    for f in product(*lower):
        if all(f[f[i]]==f[i] for i in range(len(lev))) and all(lev[f[i]]<lev[f[j]] or f[i]==f[j] for i in range(len(lev)) for j in range(len(lev)) if lev[i]<lev[j]):
            yield f


def fixed_set_valid(levels,s):
    lev,lower=model(levels)
    for i in range(len(lev)):
        if i not in s:
            below=[j for j in s if j in lower[i]]
            if not below: return False
            maximal=[j for j in below if not any(j!=k and lev[j]<lev[k] for k in below)]
            if len(maximal)!=1: return False
    return True


def compare_maps(levels):
    m=list(idempotent_maps(levels))
    fs={tuple(i for i,v in enumerate(f) if i==v) for f in m}
    assert len(fs)==len(m),('distinct maps sharing fixed points',levels)
    n=sum(levels)
    all_valid={s for mask in range(1<<n) if fixed_set_valid(levels,s:=tuple(i for i in range(n) if mask>>i&1))}
    assert fs==all_valid,(levels,fs^all_valid)
    assert len(m)==recurrence(levels),(levels,len(m),recurrence(levels))
    assert orbit_count_by_signatures(levels)==orbit_recurrence(levels),(levels,orbit_count_by_signatures(levels),orbit_recurrence(levels))
    return len(m)


def orbit_count_actual(levels):
    # Independent literal action of all level permutations on the map graph.
    masks=set()
    maps=list(idempotent_maps(levels))
    for f in maps:
        masks.add(f)
    blocks=[];start=0
    for n in levels:
        blocks.append(list(range(start,start+n)))
        start+=n
    perms=[]
    for block in blocks:
        perms.append(tuple(permutations(block)))
    unseen=set(masks);count=0
    while unseen:
        f=next(iter(unseen));count+=1
        for choice in product(*perms):
            pi=tuple(x for block in choice for x in block)
            g=[None]*len(pi)
            for i in range(len(pi)):
                g[pi[i]]=pi[f[i]]
            unseen.discard(tuple(g))
    return count


def upsets(levels):
    lev,lower=model(levels)
    n=len(lev)
    out=[]
    for m in range(1<<n):
        if all((not (m>>i&1)) or (m>>j&1) for i in range(n) for j in range(n) if lev[i]<lev[j]):
            out.append(m)
    return out


def count_sublattices(levels):
    arr=upsets(levels)
    n=sum(levels);full=(1<<n)-1
    mids=[x for x in arr if x not in (0,full)]
    assert len(mids)<=12,('too large for bounded-sublattice enumeration',levels,len(mids))
    count=0
    for mask in range(1<<len(mids)):
        d={0,full}|{x for i,x in enumerate(mids) if mask>>i&1}
        if any((a|b) not in d or (a&b) not in d for a in d for b in d):continue
        box={a:max((v for v in d if v&a==v),key=int.bit_count) for a in arr}
        if all(box[a|b]==(box[a]|box[b]) for a in arr for b in arr):
            count+=1
    return count


def main():
    print('Weak-order layers: [size vectors] -> exact finite maps = strong expansions')
    candidates=[[1],[2],[1,1],[1,2],[2,1],[1,2,2],[1,2,3],[1,3,2],[1,2,1,2],
                [2,1,2],[2,2],[1,1,1,1],[1,3,3],[1,3,4], [1,2,2,2], [1,4,4]]
    for v in candidates:
        num=compare_maps(v)
        print(v,'->',num,'labeled;',orbit_recurrence(v),'isomorphism classes')
        if sum(v)<=7:
            assert orbit_count_actual(v)==orbit_recurrence(v),('literal permutation disagreement',v)
        if len(upsets(v))<=14:
            direct=count_sublattices(v)
            assert num==direct,('lattice disagreement',v,num,direct)
    checked = 0
    for total in range(1, 8):
        for mask in range(1 << (total - 1)):
            profile = []
            part = 1
            for bit in range(total - 1):
                if mask >> bit & 1:
                    profile.append(part)
                    part = 1
                else:
                    part += 1
            profile.append(part)
            compare_maps(profile)
            checked += 1
    print('ALL LAYERED PROFILES THROUGH SEVEN VERTICES VERIFIED:',checked)
    print('DIRECT-LATTICE AGREEMENT OK')
    print('DP AND FIXED-POINT BIJECTION OK')
    print('ALL UNLABELED-ORBIT RECURRENCES AGREED, INCLUDING LITERAL GROUP ACTIONS')

if __name__=='__main__': main()
