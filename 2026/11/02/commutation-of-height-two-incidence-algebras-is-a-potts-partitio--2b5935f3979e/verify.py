#!/usr/bin/env python3
"""Independent small-instance checks for height-two incidence-algebra commutation."""
from itertools import product
from fractions import Fraction
from math import prod


def components(n, edges):
    parent = list(range(n))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for u,v in edges:
        ru,rv = root(u),root(v)
        if ru != rv:
            parent[ru] = rv
    return len({root(i) for i in range(n)})


def subset_numerator(n, edges, q):
    m=len(edges)
    return sum((q-1)**len(sub)*q**(2*components(n,sub))
               for mask in range(1<<m)
               for sub in [[edges[j] for j in range(m) if mask>>j&1]])


def color_numerator(n, edges, q):
    return sum(q**sum(color[u]==color[v] for u,v in edges)
               for color in product(range(q*q),repeat=n))


def direct_commutation(n, edges, q):
    m=len(edges)
    # Direct algebra multiplication, independent of the graph-subset formula.
    elements=list(product(range(q), repeat=n+m))
    ans=0
    for a in elements:
        for b in elements:
            equal=True
            for j,(u,v) in enumerate(edges):
                ab=(a[u]*b[n+j]+a[n+j]*b[v])%q
                ba=(b[u]*a[n+j]+b[n+j]*a[v])%q
                if ab!=ba:
                    equal=False
                    break
            ans+=equal
    return ans


def rank_of_edges(n,edges):
    return n-components(n,edges)


def leading(n,edges):
    m=len(edges)
    items=[]
    for mask in range(1<<m):
        sub=[edges[j] for j in range(m) if mask>>j&1]
        items.append((len(sub)-2*rank_of_edges(n,sub),mask))
    delta=max(k for k,_ in items)
    return m-delta,sum(k==delta for k,_ in items)


def is_forest(n,edges):
    return rank_of_edges(n,edges)==len(edges)


def forest_union_rank_brute(n,edges):
    m=len(edges)
    flags=[]
    for mask in range(1<<m):
        flags.append(is_forest(n,[edges[j] for j in range(m) if mask>>j&1]))
    maximum=0
    for mask in range(1<<m):
        if mask.bit_count()<=maximum: continue
        sub=mask
        while True:
            if flags[sub] and flags[mask^sub]:
                maximum=mask.bit_count();break
            if sub==0:break
            sub=(sub-1)&mask
    return maximum


def test():
    graphs=[
        ('empty3',3,[]),
        ('edge2',2,[(0,1)]),
        ('path3',3,[(0,2),(1,2)]),
        ('two_edges4',4,[(0,2),(1,3)]),
        ('star3',4,[(0,3),(1,3),(2,3)]),
        ('cycle4',4,[(0,2),(0,3),(1,2),(1,3)]),
        ('path5',5,[(0,3),(1,3),(1,4),(2,4)]),
        ('K23',5,[(i,j) for i in range(2) for j in range(2,5)]),
        ('K33',6,[(i,j) for i in range(3) for j in range(3,6)]),
        ('K34',7,[(i,j) for i in range(3) for j in range(3,7)]),
        ('K44',8,[(i,j) for i in range(4) for j in range(4,8)]),
    ]
    direct_cases=0; color_cases=0; matroid_cases=0
    for title,n,edges in graphs:
        m=len(edges)
        for q in (2,3):
            s=subset_numerator(n,edges,q)
            if (q*q)**n<=20000:
                assert s==color_numerator(n,edges,q),(title,q,'color')
                color_cases+=1
            if q**(n+m)<=300:
                a=direct_commutation(n,edges,q)
                assert a==q**m*s,(title,q,'algebra')
                direct_cases+=1
        exponent, coefficient=leading(n,edges)
        if m<=12:
            assert exponent==forest_union_rank_brute(n,edges),(title,exponent)
            matroid_cases+=1
        print(title, 'vertices',n,'edges',m,'large_q',f'{coefficient}q^(-{exponent})')
    print('VERIFY_OK',direct_cases,'direct algebra cases,',color_cases,
          'independent color sums,',matroid_cases,'two-forest rank checks')

if __name__=='__main__':test()
