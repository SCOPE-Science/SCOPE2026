#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter, defaultdict


def boston_rounds(profile):
    n=len(profile)
    unmatched=set(range(n)); available=set(range(n)); assignment=[None]*n
    # Common strict priority 0 > 1 > ... > n-1.
    for r in range(n):
        apps=defaultdict(list)
        for i in sorted(unmatched):
            apps[profile[i][r]].append(i)
        for s in sorted(available):
            if apps[s]:
                i=min(apps[s])
                assignment[i]=s
                unmatched.remove(i)
                available.remove(s)
    assert not unmatched and not available
    return tuple(assignment)


def boston_events(profile):
    # Independent implementation: process the (round,school) event grid, with
    # acceptance final and only still-unmatched agents eligible at each event.
    n=len(profile)
    assignment=[-1]*n; used=[False]*n
    inv=[[0]*n for _ in range(n)]
    for i,p in enumerate(profile):
        for r,s in enumerate(p): inv[i][r]=s
    for r in range(n):
        for s in range(n):
            if used[s]: continue
            candidates=[i for i in range(n) if assignment[i] < 0 and inv[i][r]==s]
            if candidates:
                i=min(candidates)
                assignment[i]=s; used[s]=True
    assert all(x>=0 for x in assignment) and all(used)
    return tuple(assignment)


def profitable(profile, i, mechanism=boston_rounds):
    n=len(profile); prefs=list(permutations(range(n)))
    truthful=mechanism(profile)
    rank={s:r for r,s in enumerate(profile[i])}
    good=[]
    for rep in prefs:
        if rep==profile[i]: continue
        q=list(profile); q[i]=rep
        out=mechanism(tuple(q))
        if rank[out[i]] < rank[truthful[i]]:
            good.append((rep,out[i]))
    return truthful[i], tuple(good)


def manipulators(profile, mechanism=boston_rounds):
    return tuple(i for i in range(len(profile)) if profitable(profile,i,mechanism)[1])

# Exact boundary for n<=2 and cross-implementation agreement.
for n in (1,2):
    prefs=list(permutations(range(n)))
    for prof in product(prefs, repeat=n):
        assert boston_rounds(prof)==boston_events(prof)
        assert manipulators(prof)==()

n=3; prefs=list(permutations(range(n)))
counts=Counter(); direct_bad=[]
for prof in product(prefs, repeat=n):
    assert boston_rounds(prof)==boston_events(prof)
    m=manipulators(prof)
    counts[m]+=1
    if m:
        direct_bad.append(prof)
        assert len(m)==1
        i=m[0]
        got, good=profitable(prof,i)
        rank={s:r for r,s in enumerate(prof[i])}
        assert rank[got]==2
        assert {rank[x[1]] for x in good}=={1}
        expected={rep for rep in prefs if rep[0]==prof[i][1]}
        assert {rep for rep,_ in good}==expected

assert counts==Counter({():180,(1,):24,(2,):12})
assert len(direct_bad)==36

# School-relabeling quotient. Since student 0 has a strict order, normalizing
# that order to (0,1,2) gives one representative from every orbit.
def relabel(prof,sigma):
    return tuple(tuple(sigma[s] for s in p) for p in prof)

def canonical(prof):
    return min(relabel(prof,s) for s in permutations(range(3)))

classes={}
for prof in product(prefs, repeat=3):
    c=canonical(prof)
    m=manipulators(prof)
    if c in classes: assert classes[c]==m
    else: classes[c]=m
assert len(classes)==36
assert Counter(classes.values())==Counter({():30,(1,):4,(2,):2})

bad=sorted((c,m) for c,m in classes.items() if m)
expected=[
 (((0,1,2),(0,1,2),(0,1,2)),(2,)),
 (((0,1,2),(0,1,2),(1,0,2)),(1,)),
 (((0,1,2),(0,1,2),(1,2,0)),(1,)),
 (((0,1,2),(0,2,1),(0,2,1)),(2,)),
 (((0,1,2),(0,2,1),(2,0,1)),(1,)),
 (((0,1,2),(0,2,1),(2,1,0)),(1,)),
]
assert bad==expected

# Every orbit has size six: verified directly, and structurally forced by the
# strict ranking of highest-priority student 0.
for c in classes:
    orbit={relabel(c,s) for s in permutations(range(3))}
    assert len(orbit)==6

print('VERIFY_OK')
print('n1_manipulable_profiles',0)
print('n2_manipulable_profiles',0)
print('n3_total_profiles',216)
print('n3_nonmanipulable',180)
print('n3_middle_priority_only',24)
print('n3_lowest_priority_only',12)
print('n3_manipulable_total',36)
print('n3_manipulability_probability','1/6')
print('n3_school_relabel_classes',36)
print('n3_manipulable_classes',6)
print('class_split_middle_lowest','4+2')
print('each_failure_truthful_third_to_second',True)
print('each_failure_exactly_two_profitable_reports',True)
