#!/usr/bin/env python3
"""Finite verification of preimage-extension theorem for cycle/copy automata."""
from collections import deque, Counter
from math import gcd

def E(S,n,d):
    return [i for i in range(n) if not (S>>i)&1 and (S>>((i+d)%n))&1]

def inv_a(S,n):
    return (S>>1)|((S&1)<<(n-1))

def inv_b(S,d):
    return (S&~1)|((S>>d)&1)

def bfs(S,n,d):
    z=deque([(S,0)]); vis={S}; k=S.bit_count()
    while z:
        V,dist=z.popleft()
        for U in (inv_a(V,n),inv_b(V,d)):
            if U.bit_count()>k:
                return dist+1
            if U not in vis:
                vis.add(U);z.append((U,dist+1))
    return None

def graph_A(n,d,t):
    parent=list(range(n));size=[1]*n
    def find(x):
        while parent[x]!=x:
            x=parent[x]
        return x
    for i in range(t):
        x,y=find(i),find((i+d)%n)
        if x!=y:
            parent[y]=x;size[x]+=size[y]
    p=1
    for i in range(n):
        if parent[i]==i: p*=size[i]+1
    return p

def main():
    num=0; profiles=0
    for n in range(2,11):
        for d in range(1,n):
            counts=Counter()
            for S in range(1,(1<<n)-1):
                ch=E(S,n,d)
                expected=1+min(ch) if ch else None
                got=bfs(S,n,d)
                assert got==expected,(n,d,S,expected,got)
                counts[got]+=1
                num+=1
            if gcd(n,d)==1:
                A=[graph_A(n,d,t) if t<n else 2 for t in range(n+1)]
                assert all(counts[k]==A[k-1]-A[k] for k in range(1,n+1)),(n,d,counts,A)
                assert counts[n]==n-1,(n,d,counts)
                for s in range(1,n):
                    winners=[S for S in range(1,(1<<n)-1) if S.bit_count()==s and E(S,n,d)==[n-1]]
                    want=sum(1<<((n-1+j*d)%n) for j in range(1,s+1))
                    assert winners==[want],(n,d,s,winners,want)
                if d==1:
                    assert all(counts[k]==k*2**(n-k-1) for k in range(1,n)),(n,counts)
            profiles+=1
    print(f'PASS all n=2..10 and 1<=d<n: {profiles} automata, {num} tested nontrivial subsets; exact BFS, directed-chord, forest product, unique worst sets')
if __name__=='__main__':main()
