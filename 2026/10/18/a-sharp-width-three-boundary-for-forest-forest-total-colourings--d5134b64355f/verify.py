#!/usr/bin/env python3
"""Standalone finite checks for a width-three generalized forest-total-colouring theorem.
Only standard Python is required. The all-order proof is contained in RESULT.md.
"""
from itertools import combinations
from math import ceil

C5_V = [0,2,1,3,3,3,3,1,3]
C5_E = {
 (0,1):1,(0,2):3,(0,3):2,(0,4):1,(0,5):2,(0,6):1,(0,7):3,(0,8):2,
 (1,4):0,(1,5):1,(1,6):0,(1,7):3,(1,8):0,
 (2,4):2,(2,5):0,(2,6):2,(2,7):0,(2,8):2,
 (3,4):1,(3,5):0,(3,6):0,(3,7):2,(3,8):1
}

def graph(a,b):
    n=1+a+b
    A=set(range(1,a+1)); B=set(range(a+1,n))
    edges={tuple(sorted((u,v))) for u in range(n) for v in range(u+1,n)
           if u==0 or v==0 or ((u in A and v in B) or (u in B and v in A))}
    return n,A,B,edges

def forest(n, edges):
    parent=list(range(n))
    def root(x):
        while parent[x]!=x:
            x=parent[x]
        return x
    for x,y in edges:
        rx,ry=root(x),root(y)
        if rx==ry:return False
        parent[rx]=ry
    return True

def solution(a,b):
    n,A,B,E=graph(a,b)
    if a==3 and 2<=b<=5:
        V=C5_V[:n]; ec={e:c for e,c in C5_E.items() if e in E};k=4
    else:
        k=3 if a==1 else 4 if a==2 else 5
        V=[0]+[1]*a+[2]*b
        ec={}
        for e in E:
            x,y=e
            if x==0 or y==0:
                other=y if x==0 else x
                ec[e]=2 if other in A else 1
            else:
                rank=x-1 if x in A else y-1
                ec[e]=0 if rank==0 else rank+2
    return k,V,ec

def predicted(a,b):
    return 3 if a==1 else 4 if a==2 or b<=5 else 5

def check(a,b):
    n,A,B,E=graph(a,b)
    k,V,C=solution(a,b)
    assert k==predicted(a,b),(a,b,k)
    assert len(V)==n and set(C)==E
    assert all(0<=z<k for z in V) and all(0<=z<k for z in C.values())
    assert all(c!=V[u] and c!=V[v] for (u,v),c in C.items())
    for c in range(k):
        vc={u for u in range(n) if V[u]==c}
        assert forest(n, [e for e in E if e[0] in vc and e[1] in vc]), (a,b,c,'vertex')
        assert forest(n,[e for e,d in C.items() if d==c]), (a,b,c,'edge')
    edge_count=len(E)
    lower=ceil((edge_count+n)/(n-1))
    assert lower==k, (a,b,lower,k)
    if (a,b)==(3,5):
        assert sum(len([e for e in E if C[e]==c]) for c in range(k))==23
        assert all(sum(d==c for d in C.values())==n-1-sum(v==c for v in V) for c in range(k))
    return len(E)

def main():
    trials=0; edges=0
    for a in range(1,4):
        for b in range(max(a,1),201):
            edges+=check(a,b);trials+=1
    print('CHECKS_PASSED instances=%d all_graph_edges=%d special_K_1_3_5=23 saturation=YES' %(trials,edges))
if __name__=='__main__':main()
