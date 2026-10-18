#!/usr/bin/env python3
"""Exact integer enumeration for the vertex-rich faces of odd circular ladders.
No external packages; runs independently of symbolic proof or published tables.
"""
from math import comb

def central_trinomial(m):
    return sum(comb(m,2*j)*comb(2*j,j) for j in range(m//2+1))

def transfer_ct(n):
    # Matrix Laurent polynomial trace(T^(n-1)), coefficient z^0.
    # State labels are rung signs +1 and -1.
    T = {(0,0,1):1,(0,0,-1):1,(1,1,1):1,(1,1,-1):1,
         (0,1,1):1,(1,0,-1):1}
    # A[(i,j,k)] is coefficient for the length-l transfer.
    A={(0,0,0):1,(1,1,0):1}
    for _ in range(n-1):
        B={}
        for (i,j,a),v in A.items():
            for (u,w,b),mult in T.items():
                if j!=u:continue
                z=(i,w,a+b)
                B[z]=B.get(z,0)+v*mult
        A=B
    return n*sum(v for (i,j,k),v in A.items() if i==j and k==0)

def brute(n):
    # Directly construct all edge-1-Lipschitz potentials f in Z^(2n), f(a0)=0.
    # Only use graph edges, and decide facetness via BFS on tight edges.
    a=[0]*n;b=[0]*n
    target=3*n-2
    candidates=0; max_count=0; facet_count=0; other=0; invalid=0
    edges = [(i,(i+1)%n) for i in range(n)] + [(n+i,n+(i+1)%n) for i in range(n)] + [(i,n+i) for i in range(n)]
    def check():
        nonlocal candidates,max_count,facet_count,other,invalid
        val=a+b
        tight=[]
        for u,v in edges:
            d=abs(val[u]-val[v])
            assert d<=1
            if d==1: tight.append((u,v))
        candidates+=1
        if len(tight)>target:raise AssertionError((n,'too many',val))
        if len(tight)!=target:
            return
        # Independently verify that a facet's supporting vertices span its affine hyperplane.
        links=[[] for _ in range(2*n)]
        for u,v in tight:links[u].append(v);links[v].append(u)
        seen={0}; stack=[0]
        for u in stack:
            for v in links[u]:
                if v not in seen:seen.add(v);stack.append(v)
        if len(seen)==2*n:
            facet_count+=1
        else:
            invalid+=1
    def visit(i):
        if i==n-1:
            if abs(a[-1]-a[0])>1 or abs(b[-1]-b[0])>1:return
            check();return
        for u in range(a[i]-1,a[i]+2):
            for v in range(b[i]-1,b[i]+2):
                if abs(u-v)>1: continue
                a[i+1]=u;b[i+1]=v
                visit(i+1)
    for s in (-1,0,1):
        b[0]=s
        visit(0)
    return candidates,facet_count,invalid

def main():
    for n in range(3,30,2):
        expected=2*n*central_trinomial(n-1)
        via_transfer=transfer_ct(n)
        assert via_transfer==expected,(n,via_transfer,expected)
        print('TRANSFER',n,via_transfer)
    for n in (3,5,7):
        ct,ans,nonconnected=brute(n)
        expected=2*n*central_trinomial(n-1)
        assert ans==expected,(n,ct,ans,expected)
        assert nonconnected==0,(n,nonconnected)
        print('EXHAUSTIVE',n,'candidates=',ct,'maximal_connected=',ans,'nonconnected_maximal=',nonconnected)
    print('ALL INDEPENDENT CHECKS PASSED')
if __name__=='__main__': main()
