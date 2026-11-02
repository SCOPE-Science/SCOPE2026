#!/usr/bin/env python3
"""Exact, standalone checks for nonpalindromic 3-mer universal cycles."""
from fractions import Fraction
from math import factorial
from collections import defaultdict


def bareiss_det(a):
    a=[list(map(int,r)) for r in a]
    n=len(a)
    if n==0:return 1
    sign=1;last=1
    for k in range(n-1):
        if a[k][k]==0:
            j=next((j for j in range(k+1,n) if a[j][k]!=0),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator%last==0
                a[i][j]=numerator//last
            a[i][k]=0
        last=pivot
    return sign*a[-1][-1]


def closed_formula(q):
    if q==2:return 1,1
    assert q>=3
    tau=q**(q*(q-1)//2+q-3)*(q-2)**((q-1)*(q-2)//2)*(q-1)**(q-1)
    return tau,tau*factorial(q-2)**(q*q)


def graph(q):
    v=[(a,b) for a in range(q) for b in range(q)]
    vindex={v:i for i,v in enumerate(v)}
    edges=[(a,b,c) for a in range(q) for b in range(q) for c in range(q) if a!=c]
    A=[[0]*len(v) for _ in v]
    for a,b,c in edges:A[vindex[a,b]][vindex[b,c]]+=1
    return v,edges,A


def tree_count(q):
    v,e,A=graph(q)
    d=q-1
    L=[[(d if i==j else 0)-A[i][j] for j in range(q*q)] for i in range(q*q)]
    return bareiss_det([row[:-1] for row in L[:-1]])


def brute_tours(q):
    # Count edge-identified Euler circuits beginning with unique edge (0,0,1).
    v,e,A=graph(q)
    if len(e)>18:raise ValueError('brute only q <= 3')
    ei={word:i for i,word in enumerate(e)}
    start=(0,0,1);first=ei[start]
    adj=defaultdict(list)
    for a,b,c in e:adj[a,b].append((ei[a,b,c],(b,c)))
    end=(0,0); count=0
    path=[start]
    def visit(u,used):
        nonlocal count
        if len(path)==len(e):
            if u==end:
                # Word's consecutive circular 3-mers are exactly the edge set
                letters=tuple(x[0] for x in path)
                windows={(letters[i], letters[(i+1)%len(letters)], letters[(i+2)%len(letters)]) for i in range(len(letters))}
                assert windows==set(e)
                count+=1
            return
        for j,v in adj[u]:
            if not ((used>>j)&1):
                path.append(e[j]);visit(v,used|(1<<j));path.pop()
    visit((start[1],start[2]),1<<first)
    return count

if __name__=='__main__':
    for q in range(2,7):
        tau,uc=closed_formula(q)
        det=tree_count(q)
        assert det==tau,(q,det,tau)
        print('q',q,'vertices',q*q,'edges',q*q*(q-1),'tau',tau,'cycles',uc,'det_ok')
        if q<=3:
            brute=brute_tours(q)
            assert brute==uc,(q,brute,uc)
            print('direct_circuit_count',brute)
    print('VERIFY_OK')
