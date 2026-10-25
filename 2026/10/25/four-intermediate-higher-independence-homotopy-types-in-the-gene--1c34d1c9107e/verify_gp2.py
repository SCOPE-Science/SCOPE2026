#!/usr/bin/env python3
"""Standalone integer discrete-Morse certificate for higher independence complexes.

Usage: python3 verify_gp2.py
Only Python's standard library is required.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

ORDERS = {
    6: [11,10,8,1,7,9,2,3,5,4,0,6],
    7: [9,13,12,2,1,8,7,10,3,5,4,0,11,6],
    8: [10,8,7,9,15,2,1,6,14,3,5,4,12,0,11,13],
    9: [17,16,15,4,9,0,7,3,8,6,10,1,12,5,14,2,13,11],
}
EXPECTED = {
    6: (810, {0:1,3:3,4:1}),
    7: (2269,{0:1,5:1}),
    8: (6711,{0:1,5:7}),
    9: (20800,{0:1,5:4}),
}

def graph(n):
    adj = [0] * (2*n)
    for i in range(n):
        for u,v in ((i,(i+1)%n),(n+i,n+(i+2)%n),(i,n+i)):
            assert u!=v
            adj[u]|=1<<v
            adj[v]|=1<<u
    assert all(x.bit_count()==3 for x in adj)
    return adj

def faces_of(n):
    adj=graph(n)
    out=[]
    for m in range(1<<(2*n)):
        # Components of size <=2 iff every induced vertex degree <=1.
        s=m;good=True
        while s:
            bit=s&-s;s-=bit
            i=bit.bit_length()-1
            if (adj[i]&m).bit_count()>1:
                good=False;break
        if good:out.append(m)
    assert out[0]==0
    return out

def matching(n,faces):
    # Deterministic sequential toggles; the face-poset DAG is checked below.
    remaining=set(faces)-{0}
    pairs=[]
    for v in ORDERS[n]:
        b=1<<v
        for lo in sorted((x for x in remaining if not x&b),
                         key=lambda m:(m.bit_count(),m)):
            hi=lo|b
            if lo in remaining and hi in remaining:
                remaining.remove(lo);remaining.remove(hi)
                pairs.append((lo,hi))
    return pairs,remaining

def acyclic_hasse(n, faces, pairs):
    # Each cover relation is directed upward except matched covers, reversed.
    face_set=set(faces)-{0}
    pair_set=set(pairs)
    indeg={m:0 for m in face_set}
    out={m:[] for m in face_set}
    for hi in face_set:
        bits=hi
        while bits:
            b=bits&-bits;bits-=b
            lo=hi^b
            if lo==0:continue
            a,z=(hi,lo) if (lo,hi) in pair_set else (lo,hi)
            out[a].append(z);indeg[z]+=1
    queue=deque(m for m,d in indeg.items() if d==0)
    reached=0
    while queue:
        x=queue.popleft();reached+=1
        for y in out[x]:
            indeg[y]-=1
            if indeg[y]==0:queue.append(y)
    assert reached==len(face_set),f'cyclic matching for n={n}'
    return sum(len(v) for v in out.values())

def boundary(m):
    items=[];initial=m;k=0
    while m:
        b=m&-m;m-=b
        items.append((initial^b, (-1)**k));k+=1
    return items

def check_integral_morse(n,pairs,crit):
    assert n==6
    lower_to_upper={lo:hi for lo,hi in pairs if lo.bit_count()==4}
    degree_three={m for m in crit if m.bit_count()==4}
    degree_four={m for m in crit if m.bit_count()==5}
    assert len(degree_three)==3 and len(degree_four)==1
    @lru_cache(None)
    def propagate(lo):
        # Coefficient of each critical 3-cell in gradient reduction of lo.
        if lo in degree_three:return {lo:1}
        if lo not in lower_to_upper:return {}
        hi=lower_to_upper[lo]
        incid=dict(boundary(hi))
        assert abs(incid[lo])==1
        total=defaultdict(int)
        for other,a in incid.items():
            if other==lo:continue
            for target,c in propagate(other).items():
                total[target]-=incid[lo]*a*c
        return {k:v for k,v in total.items() if v}
    result=defaultdict(int)
    top=next(iter(degree_four))
    for lo,a in boundary(top):
        for k,c in propagate(lo).items():result[k]+=a*c
    assert all(v==0 for v in result.values())
    return top,sorted(degree_three),[result.get(k,0) for k in sorted(degree_three)]

def main():
    for n in sorted(ORDERS):
        faces=faces_of(n)
        expected_count,expected_critical=EXPECTED[n]
        assert len(faces)==expected_count
        face_set=set(faces)
        assert len(face_set)==len(faces)
        assert set(ORDERS[n])==set(range(2*n))
        pairs,critical=matching(n,faces)
        assert len(set(x for p in pairs for x in p))==2*len(pairs)
        assert all(hi in face_set and lo in face_set and
                   (hi^lo).bit_count()==1 and (lo&hi)==lo
                   for lo,hi in pairs)
        assert 2*len(pairs)+len(critical)==len(faces)-1
        counts=dict(Counter(m.bit_count()-1 for m in critical))
        assert counts==expected_critical,(n,counts)
        covers=acyclic_hasse(n,faces,pairs)
        output=f'n={n}: {len(faces)-1} nonempty faces; {len(pairs)} pairs; '+str(counts)+f'; {covers} directed Hasse edges'
        if n==6:
            top,lower,coeffs=check_integral_morse(n,pairs,critical)
            output+=f'; signed Morse boundary {top}->{lower} = {coeffs}'
        print(output)
    print('ALL FOUR CERTIFICATES PASS')

if __name__=='__main__':main()
