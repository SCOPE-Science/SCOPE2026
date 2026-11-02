#!/usr/bin/env python3
"""Exact finite certificate for eight-queen batch-reconfiguration."""
import itertools
import collections
import json
import sys

N=8

def solutions():
    result=[]
    for p in itertools.permutations(range(N)):
        if len({r+p[r] for r in range(N)})==N and len({r-p[r] for r in range(N)})==N:
            result.append(p)
    return result

def graph(states,k):
    n=len(states)
    a=[[] for _ in states]
    shells=collections.Counter()
    for i in range(n):
        for j in range(i):
            d=sum(u!=v for u,v in zip(states[i], states[j]))
            shells[d]+=1
            if d<=k:
                a[i].append(j);a[j].append(i)
    for row in a:row.sort()
    return a,shells

def distance_rows(adj):
    ans=[]
    for start in range(len(adj)):
        d=[-1]*len(adj);d[start]=0;q=collections.deque([start])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]==-1:d[v]=d[u]+1;q.append(v)
        ans.append(d)
    return ans

def components(adj):
    unseen=set(range(len(adj)));out=[]
    while unseen:
        s=min(unseen);unseen.remove(s)
        q=[s]
        for x in q:
            for y in adj[x]:
                if y in unseen:unseen.remove(y);q.append(y)
        out.append(sorted(q))
    return sorted(out,key=lambda z:(-len(z),z))

def symmetry_orbit(p):
    pos=[(i,p[i]) for i in range(N)];out=set()
    for rotations in range(4):
        cur=pos
        for _ in range(rotations):cur=[(c,N-1-r) for r,c in cur]
        for reflect in (False,True):
            transformed=[(r,N-1-c) for r,c in cur] if reflect else cur
            out.add(tuple(c for r,c in sorted(transformed)))
    return out

def main():
    states=solutions()
    assert len(states)==92
    adj4,shell4=graph(states,4)
    adj5,shell=graph(states,5)
    assert shell==shell4
    assert dict(sorted(shell.items()))=={2:8,3:32,4:128,5:296,6:824,7:1272,8:1626}
    comp4=components(adj4);comp5=components(adj5)
    assert [len(c) for c in comp4]==[84,2,2,2,2]
    assert [len(c) for c in comp5]==[92]
    assert sum(map(len,adj4))//2==168 and sum(map(len,adj5))//2==464
    d5=distance_rows(adj5)
    assert all(-1 not in row for row in d5)
    paircounts=collections.Counter(d5[i][j] for i in range(92) for j in range(i))
    ecc=collections.Counter(max(row) for row in d5)
    assert paircounts=={1:464,2:2002,3:1704,4:16}
    assert ecc=={3:68,4:24}
    orbits=[];seen=set()
    for p in states:
        if p not in seen:
            orb=symmetry_orbit(p);assert orb<=set(states)
            seen.update(orb);orbits.append(orb)
    assert collections.Counter(map(len,orbits))=={8:11,4:1}
    special={states[i] for c in comp4[1:] for i in c}
    assert len(special)==8 and any(special==orb for orb in orbits)
    adjexact5=[[] for _ in states]
    for i in range(92):
        for j in adj5[i]:
            if sum(u!=v for u,v in zip(states[i],states[j]))==5:adjexact5[i].append(j)
    dex=distance_rows(adjexact5)
    assert all(-1 not in x for x in dex)
    assert collections.Counter(max(row) for row in dex)=={4:68,5:24}
    assert collections.Counter(dex[i][j] for i in range(92) for j in range(i))=={1:296,2:1178,3:1968,4:720,5:24}
    cert={
       'description':'Complete eight-queen solution and simultaneous-change adjacency certificate',
       'coordinate_convention':'Rows and columns 0..7; one column entry for each row',
       'solutions':[list(p) for p in states],
       'pair_distance_counts':{str(k):v for k,v in sorted(shell.items())},
       'neighbors_at_most_four':adj4,
       'neighbors_at_most_five':adj5,
       'distance_matrix_at_most_five':d5,
       'components_at_most_four':comp4,
       'distance_distribution_at_most_five':{str(k):v for k,v in sorted(paircounts.items())},
       'eccentricity_distribution_at_most_five':{str(k):v for k,v in sorted(ecc.items())},
       'exactly_five_distance_distribution':{str(k):v for k,v in sorted(collections.Counter(dex[i][j] for i in range(92) for j in range(i)).items())},
       'exactly_five_eccentricities':{str(k):v for k,v in sorted(collections.Counter(max(row) for row in dex).items())},
    }
    if len(sys.argv)>1:
        with open(sys.argv[1],'w',encoding='utf8') as f:json.dump(cert,f,sort_keys=True,separators=(',',':'));f.write('\n')
    print('PERMUTATION_EXHAUSTIVE_PASS')
    print('permutations=40320 solutions=92 shells='+str(dict(sorted(shell.items()))))
    print('at_most_4: edges=168 components=[84,2,2,2,2]')
    print('at_most_5: edges=464 radius=3 diameter=4 pair_distances='+str(dict(sorted(paircounts.items()))))
    print('exactly_5: edges=296 connected=1 radius=4 diameter=5')
    print('special_8_configurations_form_single_dihedral_orbit=1')
if __name__=='__main__':main()
