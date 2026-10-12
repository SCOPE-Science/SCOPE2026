#!/usr/bin/env python3
"""Independently validate complete finite cases for the barbell packing-isolation classification.
Uses Python standard library; reads seed_table.csv next to this file.
"""
import csv,itertools,pathlib

HERE=pathlib.Path(__file__).resolve().parent
BAD={(5,5,0),(5,5,1),(3,5,2),(5,5,3),(5,5,4),(5,5,7)}

def graph(a,b,d):
    # Construction independent of the finite-case search program.
    arcs=[]
    def ring(v):
        for j in range(len(v)):arcs.append((v[j],v[(j+1)%len(v)]))
    ring(list(range(a)))
    if d==0:
        ring([0]+list(range(a,a+b-1)))
        n=a+b-1
    else:
        trail=[0]+list(range(a,a+d))
        arcs.extend(zip(trail,trail[1:]))
        ring([trail[-1]]+list(range(a+d,a+d+b-1)))
        n=a+b+d-1
    edges={tuple(sorted(x)) for x in arcs}
    assert len(edges)==n+1
    N=[{i} for i in range(n)]
    for u,v in edges:
        N[u].add(v);N[v].add(u)
    return n,edges,N

def is_valid(S,edges,N):
    S=set(S)
    # Closed neighborhoods disjoint iff a 2-packing.
    for u,v in itertools.combinations(S,2):
        if N[u]&N[v]:return False
    dominated=set()
    for v in S:dominated.update(N[v])
    return all(u in dominated or v in dominated for u,v in edges)

def exhaust_negative(a,b,d):
    n,edges,N=graph(a,b,d)
    count_packing=0;count_valid=0
    near=[sum(1<<w for w in N[v]) for v in range(n)]
    for mask in range(1<<n):
        chosen=[];covered=0
        valid=True
        for v in range(n):
            if mask>>v&1:
                if covered&near[v]:valid=False;break
                covered|=near[v];chosen.append(v)
        if not valid:continue
        count_packing+=1
        if all(((covered>>u)&1) or ((covered>>v)&1) for u,v in edges):count_valid+=1
    return count_packing,count_valid

def main():
    seen=set();yes=0;no=0;stats=[]
    with (HERE/'seed_table.csv').open(newline='',encoding='utf-8') as stream:
        reader=csv.DictReader(stream)
        assert reader.fieldnames==['a','b','d','result','vertices']
        for row in reader:
            a,b,d=(int(row[k]) for k in ('a','b','d'))
            key=(a,b,d)
            assert 3<=a<=b<=8 and 0<=d<=10 and key not in seen
            seen.add(key)
            n,edges,N=graph(a,b,d)
            if row['result']=='YES':
                assert key not in BAD
                S=[int(v) for v in row['vertices'].split(';')]
                assert len(S)==len(set(S)) and all(0<=v<n for v in S)
                assert is_valid(S,edges,N),('failed witness',key,S)
                yes+=1
            else:
                assert row['result']=='NO' and row['vertices']=='' and key in BAD
                p,q=exhaust_negative(a,b,d)
                assert q==0,('negative case has witness',key)
                stats.append((key,p,q))
                no+=1
    expected={(a,b,d) for d in range(11) for a in range(3,9) for b in range(a,9)}
    assert seen==expected and yes==225 and no==6
    print('verified_cases',len(seen),'positive_witnesses',yes,'exhaustively_negative',no)
    for key,p,q in stats:print('negative',key,'packing_subsets',p,'isolating_packings',q)
    print('FINITE_BASE_CERTIFICATE_OK')

if __name__=='__main__':main()
