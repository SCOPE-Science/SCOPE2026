#!/usr/bin/env python3
"""Exact finite checks for reflection traces on ordinary 3-cut complexes of cycle powers."""
from itertools import combinations
from math import comb, gcd


def distance(i,j,n):
    d=(i-j)%n
    return min(d,n-d)


def good(n,p,vertices):
    return all(sum(distance(u,v,n)>p for v in vertices if v!=u)<=1 for u in vertices)


def orbits(n,a):
    seen=set(); result=[]
    for v in range(n):
        if v not in seen:
            o=tuple(sorted({v,(a-v)%n}))
            seen.update(o);result.append(o)
    return result


def dual_fixed_sum(n,p,a,return_components=False):
    orbs=orbits(n,a)
    states=[((),(),1)]
    for i,o in enumerate(orbs):
        new=list(states)
        for indices,T,w in states:
            if good(n,p,T+o):new.append((indices+(i,),T+o,-w))
        states=new
    z=sum(w for _,_,w in states)
    if not return_components:return z,len(states)
    faces={I for I,T,w in states}
    graph=[set() for _ in orbs]
    for I in faces:
        if len(I)==2:
            i,j=I;graph[i].add(j);graph[j].add(i)
    seen=set(); components=[]
    for i in range(len(orbs)):
        if i in seen:continue
        queue=[i];seen.add(i);com=set()
        while queue:
            u=queue.pop();com.add(u)
            for v in graph[u]:
                if v not in seen:seen.add(v);queue.append(v)
        components.append(com)
    return z,len(states),orbs,faces,components


def ref_trace(n,p,a):
    m=n//2
    if n%2: return (-1)**m*(2*p-1-m)
    if a%2: return (-1)**m*(2*p-1-m)
    return (-1)**(m-1)*(2*p+1-m)


def direct_cut_trace(n,p,a):
    triple_masks=[]
    for T in combinations(range(n),3):
        if not good(n,p,T):
            triple_masks.append(sum(1<<v for v in T))
    orb=orbits(n,a)
    ans=0
    for mask in range(1<<len(orb)):
        subset=0; pair_count=0
        for i,o in enumerate(orb):
            if mask>>i & 1:
                pair_count+=len(o)==2
                for v in o:subset|=1<<v
        if any(subset & t==0 for t in triple_masks):
            term=(-1)**(subset.bit_count()+pair_count)
            ans+=term
    return (-1)**(n-3)*ans


def check():
    fold_cases=0; face_cases=0; direct_cases=0
    for p in range(2,9):
        for n in range(6*p-3,6*p+9):
            for a in (0,1) if n%2==0 else (0,):
                z,states,orb,faces,comps=dual_fixed_sum(n,p,a,True)
                assert (-1)**sum(len(o)==2 for o in orb)*z==ref_trace(n,p,a),(p,n,a,z)
                assert z==1-len(comps)
                # The only nontrivial connected pieces are local cones, or two cones bridged
                # by a single edge when the reflection fixes opposite vertices.
                for C in comps:
                    if len(C)==1:continue
                    if n%2==0 and a%2==0 and C==set(range(0,p+1))|set(range(n//2-p,n//2+1)):
                        A=set(range(0,p+1));B=set(range(n//2-p,n//2+1))
                        for I in faces:
                            if len(I)<1 or not (set(I)<=C):continue
                            if set(I)<={0,n//2}:continue
                            if set(I)<=A:assert 0 in I or tuple(sorted(I+(0,))) in faces
                            elif set(I)<=B:assert n//2 in I or tuple(sorted(I+(n//2,))) in faces
                            else:raise AssertionError(('unexpected bridge simplex',p,n,a,I))
                    else:
                        apex_candidates=[i for i in C if all(i in I or tuple(sorted(I+(i,))) in faces for I in faces if set(I)<=C)]
                        assert apex_candidates,(p,n,a,C)
                fold_cases+=1;face_cases+=len(faces)
                if n<=18:
                    c=direct_cut_trace(n,p,a)
                    assert c==ref_trace(n,p,a),(p,n,a,c,ref_trace(n,p,a))
                    direct_cases+=1
    print('VERIFY_OK orbit_cases=%s orbit_faces=%s direct_cut_cases=%s'%(fold_cases,face_cases,direct_cases))
if __name__=='__main__':check()
