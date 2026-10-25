#!/usr/bin/env python3
"""Independent mod-two chain-complex calculation for the Alexander dual.
The Alexander dual consists of vertex subsets with no independent triple.
Run: python3 verify_dual.py
"""
from itertools import combinations

def independent(a,b,n):
    return min((a-b)%n,(b-a)%n)>4

def faces_by_size(n):
    groups={}
    def visit(chosen,start):
        groups.setdefault(len(chosen),[]).append(chosen)
        for v in range(start,n):
            if not any(independent(v,a,n) and independent(v,b,n) and independent(a,b,n)
                       for a,b in combinations(chosen,2)):
                visit(chosen+(v,),v+1)
    visit((),0)
    return groups

def rank_2(boundaries):
    pivots={}
    for col in boundaries:
        while col:
            i=col.bit_length()-1
            if i in pivots:col ^= pivots[i]
            else:
                pivots[i]=col
                break
    return len(pivots)

def main():
    for n in range(16,21):
        groups=faces_by_size(n)
        m=max(groups)
        sizes=[len(groups.get(k,())) for k in range(m+1)]
        ranks=[0,1]
        for k in range(2,m+1):
            prior={f:i for i,f in enumerate(groups[k-1])}
            columns=[]
            for face in groups[k]:
                b=0
                for i in range(k):b^=1<<prior[face[:i]+face[i+1:]]
                columns.append(b)
            ranks.append(rank_2(columns))
        # ranks[j] = rank of boundary C_j -> C_{j-1}, j=0,...,m-1;
        # rank of C_0 -> C_-1 is 1 in reduced chains.
        rr=ranks+[0]
        betti={k-1:sizes[k]-rr[k]-rr[k+1] for k in range(1,m+1)}
        betti={k:v for k,v in betti.items() if v}
        expected={16:{7:3},17:{5:1},18:{5:1},19:{5:1},20:{4:3}}[n]
        if betti!=expected:raise AssertionError((n,betti,expected,rr,sizes))
        print(f"n={n} dual_faces={sum(sizes)-1} by_dimension={sizes[1:]} reduced_F2_betti={betti} OK")
if __name__=='__main__':main()
