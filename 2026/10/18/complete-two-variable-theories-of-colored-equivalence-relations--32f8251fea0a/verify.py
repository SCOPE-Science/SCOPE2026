"""Reproducibility checks for two-variable logic on colored equivalence structures.
Only finite test cases are used here; the all-cardinality statement is proved in RESULT.md.
"""
from itertools import product
from collections import defaultdict

def partitions(n):
    def rec(prefix, hi):
        if len(prefix) == n:
            yield tuple(prefix)
        else:
            for k in range(hi+2):
                yield from rec(prefix+[k], max(hi,k))
    return rec([0], 0) if n else iter(())

def profile(P, C, q):
    groups=defaultdict(lambda:[0]*q)
    for group,color in zip(P,C):
        groups[group][color]+=1
    out=defaultdict(int)
    for numbers in groups.values():
        out[tuple(min(2,c) for c in numbers)]+=1
    return tuple(sorted((key, min(2,n)) for key,n in out.items()))

def all_structures(q, max_n):
    for n in range(1,max_n+1):
        for p in partitions(n):
            for colors in product(range(q), repeat=n):
                yield p,colors

def atomic(p,c,a,b):
    if a is None and b is None: return ('nil',)
    if a is None: return ('y', c[b])
    if b is None: return ('x', c[a])
    return ('xy',c[a],c[b], a==b, p[a]==p[b])

def signature_partition(structures, rounds):
    # Every state with zero, one, or two pebbles, independently of which variable is free.
    states=[]
    for si,(p,c) in enumerate(structures):
        nn=len(p)
        for a in [None,*range(nn)]:
            for b in [None,*range(nn)]:
                states.append((si,a,b))
    index={s:i for i,s in enumerate(states)}
    atoms=[atomic(*structures[si],a,b) for si,a,b in states]
    def intern(keys):
        d={};res=[]
        for x in keys:
            if x not in d: d[x]=len(d)
            res.append(d[x])
        return res
    cur=intern(atoms)
    for _ in range(rounds):
        keys=[]
        for i,(si,a,b) in enumerate(states):
            n=len(structures[si][0]);
            x=tuple(sorted({cur[index[(si,t,b)]] for t in range(n)}))
            y=tuple(sorted({cur[index[(si,a,t)]] for t in range(n)}))
            keys.append((atoms[i],x,y))
        cur=intern(keys)
    result=[]
    for si in range(len(structures)):
        result.append(cur[index[(si,None,None)]])
    return result, len(set(cur))

def check_case(q, max_n, rounds=6):
    structs=list(all_structures(q,max_n))
    profiles=[profile(p,c,q) for p,c in structs]
    labels,count=signature_partition(structs,rounds)
    group_a=defaultdict(set);group_b=defaultdict(set)
    for p,lab in zip(profiles, labels):
        group_a[p].add(lab);group_b[lab].add(p)
    assert all(len(v)==1 for v in group_a.values()), 'same profile distinguished by a formula'
    assert all(len(v)==1 for v in group_b.values()), 'different profiles not distinguished at given rank'
    return dict(q=q,n=max_n,structures=len(structs),profiles=len(group_a),qrank=rounds,rank_states=count)

def direct_combinatorial_check(q):
    profiles=list(product(range(3),repeat=q))
    profiles.remove((0,)*q)
    assert len(profiles)==3**q-1
    s=sum(sum(p) for p in profiles)
    assert s==q*3**q
    return dict(q=q,local_profiles=len(profiles),theory_count=3**len(profiles)-1,maximum_minimal_size=2*s)

if __name__=='__main__':
    for q in [1,2,3]:
        print('FORMULA', direct_combinatorial_check(q))
    for args in [(1,6),(2,5)]:
        print('EF', check_case(*args,rounds=6))
    print('COLORED_EQUIVALENCE_FO2_VERIFY_OK')
