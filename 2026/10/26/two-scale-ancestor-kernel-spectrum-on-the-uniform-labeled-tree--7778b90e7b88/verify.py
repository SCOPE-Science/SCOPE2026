"""Finite exact checks for the uniform labeled-tree ancestor matrix.

Run: python3 verify.py
"""
from fractions import Fraction
from itertools import product
from math import factorial


def distance_prob(n,k):
    fact = 1
    for i in range(k-1):
        fact *= n-2-i
    return Fraction((k+1)*fact, n**k)


def formula(n):
    h = sum((Fraction(k-1,n-2)*distance_prob(n,k) for k in range(1,n)), Fraction(0))
    j = (1-3*h)/(n-3)
    return h,j,(n-2)*h*h-(n-3)*j


def edges_of_prufer(seq,n):
    degrees=[1]*n
    for a in seq: degrees[a]+=1
    edges=[]
    for a in seq:
        leaf=next(i for i,d in enumerate(degrees) if d==1)
        edges.append((leaf,a))
        degrees[leaf]-=1; degrees[a]-=1
    ends=[i for i,d in enumerate(degrees) if d==1]
    edges.append(tuple(ends))
    return edges


def path_contains(adj, start, target, middle):
    parents={start:None}; queue=[start]
    for v in queue:
        for w in adj[v]:
            if w not in parents:
                parents[w]=v
                queue.append(w)
    t=target
    while t is not None:
        if t==middle:return True
        t=parents[t]
    return False


def split_by_middle(adj, b, marked):
    labels={}; label=0
    for t in range(len(adj)):
        if t==b or t in labels:continue
        todo=[t]; labels[t]=label
        for v in todo:
            for w in adj[v]:
                if w!=b and w not in labels:
                    labels[w]=label;todo.append(w)
        label+=1
    return len({labels[t] for t in marked})==len(marked)


def exhaustive(n):
    total=n**(n-2)
    count_h=0;count_j=0;count_by_length=[0]*n
    for seq in product(range(n),repeat=n-2):
        adj=[[] for _ in range(n)]
        for a,b in edges_of_prufer(seq,n):
            adj[a].append(b);adj[b].append(a)
        # root=0, B={1}, x=2, y=3.
        parents={0:None};queue=[0]
        for v in queue:
            for w in adj[v]:
                if w not in parents:
                    parents[w]=v;queue.append(w)
        length=0;t=2;contains=False
        while t!=0:
            if t==1:contains=True
            length+=1;t=parents[t]
        count_by_length[length]+=1
        count_h+=contains
        count_j+=split_by_middle(adj,1,(0,2,3))
    h,j,lam=formula(n)
    assert Fraction(count_h,total)==h,(n,'H')
    assert Fraction(count_j,total)==j,(n,'J')
    for k in range(1,n):
        assert Fraction(count_by_length[k],total)==distance_prob(n,k),(n,k)
    assert j>0 and lam>0
    print('PASS',n,'trees',total,'h',h,'j',j,'lambda_parallel',lam)


def main():
    for n in range(4,8):
        assert sum((distance_prob(n,k) for k in range(1,n)),Fraction(0))==1
        exhaustive(n)
    print('ALL EXACT FINITE CHECKS PASS')

if __name__=='__main__':main()
