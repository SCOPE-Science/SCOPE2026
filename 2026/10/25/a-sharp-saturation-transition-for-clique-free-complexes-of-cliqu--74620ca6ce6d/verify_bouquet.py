#!/usr/bin/env python3
"""Finite sanity checks for clique-free complexes of clique-bouquet graphs."""
from itertools import product
from collections import defaultdict
from math import comb

def face_data(t,q):
    n=t; edges=[tuple(range(t))]
    for i,c in enumerate(q):
        for _ in range(c):
            leaf=tuple(range(n,n+t-1)); n+=t-1
            edges.append((i,)+leaf)
    forbidden=[sum(1<<j for j in e) for e in edges]
    faces=defaultdict(list)
    for mask in range(1<<n):
        if all(mask&b != b for b in forbidden):
            faces[mask.bit_count()-1].append(mask)
    return n,edges,faces

def gf2_betti(faces):
    ranks={}
    for d in range(0,max(faces)+1):
        positions={v:j for j,v in enumerate(faces[d-1])}
        piv={}; r=0
        for v in faces[d]:
            col=0; cur=v
            while cur:
                bit=cur&-cur;cur-=bit
                col ^= 1<<positions[v-bit]
            while col:
                j=col.bit_length()-1
                if j not in piv:piv[j]=col;r+=1;break
                col ^= piv[j]
        ranks[d]=r
    return {d:len(faces[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in faces if d>=0 and len(faces[d])-ranks.get(d,0)-ranks.get(d+1,0)}

def main():
    tested=0;facesum=0;maxfaces=0
    for t in (3,4,5):
        maxq=2 if t==3 else 1
        for q in product(range(maxq+1),repeat=t):
            n=t+(t-1)*sum(q)
            if n>13:continue
            n,edges,faces=face_data(t,q)
            actual=gf2_betti(faces)
            expected={} if min(q)>0 else {(sum(q)+1)*(t-2):1}
            if actual!=expected:raise AssertionError((t,q,actual,expected))
            # independently confirm direct alternating face sum
            reduced_euler=sum((-1)**d*len(v) for d,v in faces.items())
            exp_euler=0 if not expected else (-1)**next(iter(expected))
            if reduced_euler!=exp_euler:raise AssertionError((t,q,reduced_euler,exp_euler))
            tested+=1;facesum+=sum(map(len,faces.values()));maxfaces=max(maxfaces,sum(map(len,faces.values())))
    print(f'CHECKED {tested} t-and-petal-vectors, {facesum} complete faces; maximal case {maxfaces} faces')
    print('GF2_BETTI_AND_EULER_OK')
if __name__=='__main__':main()
