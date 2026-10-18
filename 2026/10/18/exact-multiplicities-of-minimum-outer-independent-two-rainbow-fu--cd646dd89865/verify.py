#!/usr/bin/env python3
"""Independent finite checks for the stated optimal OI2RD-count formula."""
from itertools import permutations, product, combinations
from math import comb, factorial

def formula(m,n):
    assert 2<=m<=n
    B=m*n-m
    s=1<<B
    for k in range(1,m+1):
        u=k*(m+n-k-1)
        s+=(-1)**k*comb(m,k)*(1<<(B-u+1))
    return (factorial(n)//factorial(n-m))*s

def direct_by_singleton_colorings(m,n):
    N=m*n
    cells=list(product(range(m),range(n)))
    total=0
    for chosen_cols in permutations(range(n),m):
        holes={(i,chosen_cols[i]) for i in range(m)}
        nonzero=[(i,j) for i,j in cells if (i,j) not in holes]
        nb=[[v for v,(a,b) in enumerate(nonzero) if (a==i or b==chosen_cols[i])] for i in range(m)]
        for colors in product((1,2),repeat=len(nonzero)):
            if all(any(colors[v]==1 for v in ns) and any(colors[v]==2 for v in ns) for ns in nb):
                total+=1
    return total

def full_brute(m,n):
    cells=list(product(range(m),range(n)))
    all_neigh=[ [j for j,(a,b) in enumerate(cells) if j!=i and (a==r or b==c)] for i,(r,c) in enumerate(cells)]
    N=m*n
    best=N*2+1
    count=0
    for labels in product((0,1,2,3),repeat=N):
        wt=sum((x==1 or x==2)+2*(x==3) for x in labels)
        if wt>best:continue
        holes=[i for i,x in enumerate(labels) if x==0]
        if any(j in holes for i in holes for j in all_neigh[i]):continue
        if not all(any(labels[j]&1 for j in all_neigh[i]) and any(labels[j]&2 for j in all_neigh[i]) for i in holes):continue
        if wt<best: best=wt;count=1
        elif wt==best:count+=1
    return best,count

def main():
    cases=[(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(4,4)]
    for m,n in cases:
        a=formula(m,n)
        b=direct_by_singleton_colorings(m,n)
        assert a==b,(m,n,a,b)
        print('MATCH',m,n,a)
    for m,n in [(2,2),(2,3),(3,3)]:
        a=full_brute(m,n)
        assert a==(m*n-m,formula(m,n)),(m,n,a)
        print('FULL',m,n,a)
    print('VERIFICATION_OK min_color_cases=9 full_4_label_cases=3')
if __name__=='__main__':main()
