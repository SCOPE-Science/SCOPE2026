#!/usr/bin/env python3
"""Finite illustration of the directed-edge-cover theorem; standard library only."""
from itertools import combinations
P=('p',0)
X=[('x',i) for i in range(2)]
Y=[('y',i) for i in range(2)]
I=[('z',0),('z',1),('w',0)]
U=[P]+X+Y+I

def arc(a,b):
    if a==P:return True
    if a[0]=='x':return b==P or b[0]=='y'
    if a[0]=='y':return b==P or b[0]=='x'
    return b==P

def matching(A):
    left=list(A); adj={x:[y for y in A if arc(x,y)] for x in A}
    used={}
    def dfs(x,seen):
        for y in adj[x]:
            if y in seen:continue
            seen.add(y)
            if y not in used or dfs(used[y],seen):used[y]=x;return True
        return False
    return sum(dfs(x,set()) for x in left)

def tau(A):
    if any(not any(arc(x,y) for y in A) or not any(arc(y,x) for y in A) for x in A):return float('inf')
    return 2*len(A)-matching(A)

def brute(A):
    e=[(x,y) for x in A for y in A if arc(x,y)]
    for n in range(len(A),len(e)+1):
        for S in combinations(e,n):
            if all(any(a==x for a,b in S) and any(b==x for a,b in S) for x in A):return n
    return float('inf')

checks=0
for k in range(1,5):
    for A in combinations(U,k):
        assert tau(A)==brute(A),(A,tau(A),brute(A))
        checks+=1
for a,b in combinations(U,2):
    expected= (a==P or b==P or (a[0]=='x' and b[0]=='y') or (a[0]=='y' and b[0]=='x'))
    assert (tau((a,b))<=2)==expected
assert tau((P,I[0],I[1]))==4
assert tau((P,X[0],X[1]))==4
assert tau((X[0],X[1],Y[0]))==4
assert tau((X[0],X[1],Y[0],Y[1]))==4
print('VERIFY_OK finite_graphs=',checks)
