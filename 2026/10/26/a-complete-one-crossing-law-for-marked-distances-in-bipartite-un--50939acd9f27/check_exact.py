#!/usr/bin/env python3
"""Exact verification of marked-distance tail comparisons in bipartite spanning trees."""
from fractions import Fraction
from itertools import combinations
from math import prod

checks = 0

def check(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)

def falling(n, k):
    if k < 0:
        raise ValueError('negative length')
    return prod(n-j for j in range(k))

def tail(a, b, k):
    """Probability two marked vertices in the a-part are distance at least 2*k."""
    if k <= 1:
        return Fraction(1)
    if k > min(a-1,b):
        return Fraction(0)
    return Fraction(falling(a-2,k-1)*falling(b-1,k-1), (a*b)**(k-1))

def path_mass(a,b,k):
    if k < 1 or k > min(a-1,b):
        return Fraction(0)
    count = falling(a-2,k-1)*falling(b,k)
    numerator = (k+1)*b + k*a-k*(k+1)
    return Fraction(count*numerator, a**k*b**(k+1))

def connected_tree(edges, size):
    parent = list(range(size))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u,v in edges:
        u,v=find(u),find(v)
        if u == v:
            return False
        parent[u] = v
    return len({find(i) for i in range(size)}) == 1

def tree_distance(edges, size, u=0, v=1):
    adj=[[] for _ in range(size)]
    for x,y in edges:
        adj[x].append(y);adj[y].append(x)
    visited={u}; layer=[u]; d=0
    while layer:
        if v in layer:return d
        next_layer=[]
        for w in layer:
            for z in adj[w]:
                if z not in visited:
                    visited.add(z);next_layer.append(z)
        layer=next_layer;d+=1
    raise AssertionError('tree is disconnected')

# Algebraic normalization and forest-path count, without a numerical tolerance.
for a in range(2,19):
    for b in range(1,19):
        check(tail(a,b,1)==1, f'base a={a} b={b}')
        check(sum((path_mass(a,b,k) for k in range(1,min(a-1,b)+1)),Fraction(0))==1,
              f'normalization a={a} b={b}')
        for k in range(1,min(a-1,b)+1):
            check(path_mass(a,b,k)==tail(a,b,k)-tail(a,b,k+1),
                  f'path mass a={a} b={b} k={k}')

# Independently enumerate spanning trees without using the forest-inclusion theorem.
for a in range(2,6):
    for b in range(1,6):
        size=a+b
        if size>8:
            continue
        edges=[(x,a+y) for x in range(a) for y in range(b)]
        counts={}; total=0
        for chosen in combinations(edges,size-1):
            if not connected_tree(chosen,size):
                continue
            total+=1
            k=tree_distance(chosen,size)//2
            counts[k]=counts.get(k,0)+1
        check(total==a**(b-1)*b**(a-1), f'spanning-tree total a={a} b={b}')
        for k in range(1,min(a-1,b)+1):
            check(Fraction(counts.get(k,0),total)==path_mass(a,b,k),
                  f'enumerated path mass a={a} b={b} k={k}')

# Exact pairwise factor difference and exhaustive finite trichotomy checks.
for n in range(4,61):
    for u in range((n+1)//2,n-1):
        for v in range(u+1,n):
            H=u*v-2*(n-1)*(u+v-n)
            positive_at_first = H>0
            special=(n%2==0 and u==n//2 and v==n//2+1)
            max_k=min(u-1,n-u)
            inequalities=[]
            for k in range(2,max_k+1):
                left=tail(v,n-v,k);right=tail(u,n-u,k)
                inequalities.append((left>right)-(left<right))
                if k<=n-v:
                    j=k-1
                    fv=Fraction((v-j-1)*(n-v-j),v*(n-v))
                    fu=Fraction((u-j-1)*(n-u-j),u*(n-u))
                    H_j=u*v-(u+v-n)*(j+1)*(n-j)
                    factor_difference=Fraction((v-u)*H_j,u*v*(n-u)*(n-v))
                    check(fv-fu==factor_difference,
                          f'factor identity n={n} u={u} v={v} j={j}')
            if H<=0:
                check(all(x<=0 for x in inequalities),
                      f'dominance n={n} u={u} v={v}')
            elif special:
                check(all(x>=0 for x in inequalities),
                      f'special dominance n={n} u={u} v={v}')
            else:
                check(inequalities[0]>0 and inequalities[-1]<0,
                      f'incomparability n={n} u={u} v={v}')
                negative_seen=False
                for x in inequalities:
                    if x<0:negative_seen=True
                    check(not(negative_seen and x>0),
                          f'multiple crossing n={n} u={u} v={v}')
            check(positive_at_first == (tail(v,n-v,2)>tail(u,n-u,2)),
                  f'first-factor classification n={n} u={u} v={v}')

# Sharp first-order barrier for non-comparability.
for n in range(4,11):
    for u in range((n+1)//2,n-1):
        for v in range(u+1,n):
            special=(n%2==0 and u==n//2 and v==n//2+1)
            H=u*v-2*(n-1)*(u+v-n)
            check(special or H<=0, f'premature crossing n={n} u={u} v={v}')
check(tail(7,4,2)-tail(6,5,2)==Fraction(1,420),'n=11 first tail')
check(tail(6,5,3)-tail(7,4,3)==Fraction(17,2450),'n=11 second tail')
print(f'PASS: {checks} exact assertions')
