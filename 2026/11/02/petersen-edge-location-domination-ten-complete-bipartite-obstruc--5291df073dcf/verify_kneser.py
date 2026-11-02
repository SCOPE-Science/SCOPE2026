#!/usr/bin/env python3
"""Exact edge-location-domination and reconfiguration certificate for the Petersen graph.

Only the Python standard library is required. All finite sets are exhaustively enumerated.
"""
from itertools import combinations, permutations
from collections import Counter, deque

v = list(combinations(range(5), 2))
e = [(i,j) for i in range(10) for j in range(i+1,10)
     if set(v[i]).isdisjoint(v[j])]
assert len(e)==15
ne = [sum(1<<j for j,(c,d) in enumerate(e) if len({a,b,c,d})==3)
      for a,b in e]

def qualifies(x):
    sig=[ne[j]&x for j in range(15) if not (x>>j)&1]
    return bool(sig) and all(sig) and len(set(sig))==len(sig)

# Every smaller cardinality, and all cardinality-five candidates, are checked.
for k in range(5):
    assert not any(qualifies(sum(1<<i for i in C))
                   for C in combinations(range(15), k))
S = [sum(1<<i for i in C) for C in combinations(range(15),5)
     if qualifies(sum(1<<i for i in C))]
assert len(S)==246
where={s:i for i,s in enumerate(S)}
A=[]
for s in S:
    nbr={where[t] for t in (s^(1<<i)^(1<<j)
                for i in range(15) if s>>i&1
                for j in range(15) if not(s>>j&1)) if t in where}
    A.append(nbr)
assert sum(map(len,A))//2 ==1470
assert Counter(map(len,A))=={11:120,12:60,13:60,20:6}

# Natural S_5 action on KG(5,2), including the 15 edge-index permutations.
vi={x:i for i,x in enumerate(v)}; ei={x:i for i,x in enumerate(e)}
permactions=[]
for p in permutations(range(5)):
    idx=[]
    for a,b in e:
        u=vi[tuple(sorted(p[i] for i in v[a]))]
        w=vi[tuple(sorted(p[i] for i in v[b]))]
        idx.append(ei[(min(u,w),max(u,w))])
    permactions.append(idx)
assert len(permactions)==120
orbindex={};orbit_sizes=[]
for s in S:
    if where[s] in orbindex:continue
    orb={sum(1<<p[i] for i in range(15) if (s>>i)&1) for p in permactions}
    assert orb <= set(S)
    k=len(orbit_sizes);orbit_sizes.append(len(orb))
    for x in orb:orbindex[where[x]]=k
assert sorted(orbit_sizes)==[6,60,60,120]
assert sorted((orbit_sizes[k],len(A[i])) for i in range(len(S))
              for k in [orbindex[i]] if S[i] == min(
                  x for x in S if orbindex[where[x]]==k)) == [(6,20),(60,12),(60,13),(120,11)]

# All possible selected-edge shapes, counted by original Petersen incidences.
double=[None]*len(S)
for i,s in enumerate(S):
    inc=Counter(a for j,(a,b) in enumerate(e) if (s>>j)&1 for a in (a,b))
    mult=Counter(inc.get(a,0) for a in range(10))
    if mult=={1:10}:continue
    assert mult=={0:1,1:8,2:1}
    double[i]=next(a for a in range(10) if inc.get(a,0)==2)
assert sum(t is None for t in double)==6

# Exhaustive all-source distances; the bound compares with Johnson distance.
pairs=Counter();distance_counts=Counter();ecc=Counter();profiles=Counter()
exception=[set() for _ in S]
for i,s in enumerate(S):
    d={i:0};Q=deque([i])
    while Q:
        x=Q.popleft()
        for y in A[x]:
            if y not in d:d[y]=d[x]+1;Q.append(y)
    assert len(d)==len(S)
    ecc[max(d.values())]+=1
    profiles[(len(A[i]),tuple(Counter(d.values()).get(j,0) for j in range(6)))]+=1
    for j in range(i+1,len(S)):
        baseline=5-(s&S[j]).bit_count()
        extra=d[j]-baseline
        assert extra in (0,1)
        pairs[extra]+=1
        distance_counts[d[j]]+=1
        if extra:
            assert double[i] is not None and double[i]==double[j]
            exception[i].add(j);exception[j].add(i)
assert pairs=={0:30045,1:90}
assert distance_counts=={1:1470,2:5100,3:9300,4:9945,5:4320}
assert ecc=={5:246}
assert profiles=={
 (11,(1,11,45,73,80,36)):120,
 (12,(1,12,36,81,84,32)):60,
 (13,(1,13,40,76,81,35)):60,
 (20,(1,20,40,70,65,50)):6}
assert Counter(map(len,exception))=={0:186,3:60}
assert all(bool(exception[i]) == (len(A[i]) == 12) for i in range(len(S)))
seen=set(); comps=[]
for i in range(len(S)):
    if i in seen or not exception[i]:continue
    comp={i};Q=deque([i]);seen.add(i)
    while Q:
        x=Q.popleft()
        for y in exception[x]:
            if y not in seen:seen.add(y);Q.append(y);comp.add(y)
    comps.append(comp)
assert len(comps)==10 and all(len(c)==6 for c in comps)
assert {double[next(iter(c))] for c in comps}==set(range(10))
for c in comps:
    assert len({double[i] for i in c})==1
    assert all(len(exception[i])==3 for i in c)
    assert not any((a in exception[b] and a in exception[c] and b in exception[c])
                   for a,b,c in combinations(c,3))
    # A 3-regular triangle-free graph of order 6 is K_{3,3}.
print('KNESER_EXACT_RECONFIGURATION_PASS')
