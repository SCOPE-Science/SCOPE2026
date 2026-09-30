from itertools import combinations
from math import comb


def vertices(a,b):
    return [('A',i) for i in range(a)] + [('B',j) for j in range(b)]


def same_part_pairs(S, part):
    L=[v for v in S if v[0]==part]
    return list(combinations(L,2))


def can_match(omitted, pairs):
    # Explicit path-slot matching. An omitted A vertex may be the internal
    # vertex of any selected B-B geodesic, and symmetrically for B.
    adj={u:list(range(len(pairs))) for u in omitted}
    owner={}
    def aug(u, seen):
        for k in adj[u]:
            if k in seen:
                continue
            seen.add(k)
            if k not in owner or aug(owner[k], seen):
                owner[k]=u
                return True
        return False
    return all(aug(u,set()) for u in omitted)


def is_strong(a,b,S):
    S=set(S)
    V=vertices(a,b)
    if len(S)<2:
        return False
    omitA=[v for v in V if v not in S and v[0]=='A']
    omitB=[v for v in V if v not in S and v[0]=='B']
    return (can_match(omitA, same_part_pairs(S,'B')) and
            can_match(omitB, same_part_pairs(S,'A')))


def is_minimal_strong(a,b,S):
    S=set(S)
    if not is_strong(a,b,S):
        return False
    return all(not is_strong(a,b,S-{v}) for v in list(S))


def predicted_value(a,b):
    assert 1 <= a <= b
    if a==b==1:
        return 2
    if a==1:
        return b
    return b+1


def predicted_patterns(a,b):
    if a==b==1:
        return {(1,1)}
    if a==1:
        return {(0,b)}
    if a<b:
        return {(2,b-1)}
    n=a
    if n==2:
        return {(1,2),(2,1)}
    if n==3:
        return {(2,2)}
    if n==4:
        return {(2,3),(3,2)}
    if n==5:
        return {(2,4),(3,3),(4,2)}
    return {(2,n-1),(n-1,2)}


def predicted_count(a,b):
    return sum(comb(a,s)*comb(b,t) for s,t in predicted_patterns(a,b))


types=0
subsets=0
minimal_sets=0
max_sets=0
for a in range(1,8):
    for b in range(a,9):
        V=vertices(a,b)
        mins=[]
        for mask in range(1 << len(V)):
            S={V[i] for i in range(len(V)) if (mask>>i)&1}
            subsets += 1
            if is_minimal_strong(a,b,S):
                mins.append(S)
        assert mins, (a,b)
        mx=max(map(len,mins))
        assert mx==predicted_value(a,b), (a,b,mx,predicted_value(a,b))
        maxmins=[S for S in mins if len(S)==mx]
        got={(sum(v[0]=='A' for v in S),sum(v[0]=='B' for v in S))
             for S in maxmins}
        assert got==predicted_patterns(a,b), (a,b,got,predicted_patterns(a,b))
        assert len(maxmins)==predicted_count(a,b), (a,b,len(maxmins),predicted_count(a,b))
        types += 1
        minimal_sets += len(mins)
        max_sets += len(maxmins)
print('VERIFY_OK', 'types',types,'subsets',subsets,'minimal_sets',minimal_sets,'max_sets',max_sets)
