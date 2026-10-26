#!/usr/bin/env python3
"""Independent finite checks of singleton rainbow domination on balanced multipartite graphs.

Every direct test enumerates all named 0..k vertex assignments and checks the
literal open-neighborhood condition. This is a finite test, not a general proof.
"""
from itertools import combinations, product
from math import comb, factorial


def formula(r,m,k):
    n=r*m
    if k>(r-1)*m:
        return n,k**n
    q,s=divmod(k,m)
    if s==0:
        return k,comb(r,q)*factorial(k)
    h=r-q
    def double_count():
        choices=list(combinations(range(h),2))
        total=0
        for pairs in product(choices,repeat=s):
            load=[0]*h
            for i,j in pairs:
                load[i]+=1;load[j]+=1
            ways=1
            for d in load:
                for t in range(d):ways*=m-t
            total+=ways
        return comb(r,q)*factorial(k)//factorial(s)*total
    def full_count():
        # Number of onto mappings from selected vertices to k named colours.
        onto=sum((-1)**j*comb(k,j)*(k-j)**((q+1)*m) for j in range(k+1))
        return comb(r,q+1)*onto
    if 2*s<m:
        return q*m+2*s,double_count()
    if 2*s>m:
        return (q+1)*m,full_count()
    return q*m+2*s,double_count()+full_count()


def matches_classification(a,r,m,k):
    n=r*m
    if k>(r-1)*m:
        return all(x>0 for x in a)
    q,s=divmod(k,m)
    parts=[a[i*m:(i+1)*m] for i in range(r)]
    full=[p for p in parts if all(x>0 for x in p)]
    full_colors=[x for p in full for x in p]
    partial=[p for p in parts if any(x==0 for x in p)]
    if s==0:
        return len(full)==q and len(set(full_colors))==k and all(all(x==0 for x in p) for p in partial)
    good_a=(len(full)==q and len(set(full_colors))==q*m)
    if good_a:
        rest=set(range(1,k+1))-set(full_colors)
        occ={c:[] for c in rest}
        for pi,p in enumerate(partial):
            for x in p:
                if x>0:
                    if x not in rest:good_a=False
                    else:occ[x].append(pi)
        good_a=good_a and all(len(loc)==2 and loc[0]!=loc[1] for loc in occ.values())
    good_b=(len(full)==q+1 and set(full_colors)==set(range(1,k+1)) and
            all(all(x==0 for x in p) for p in partial))
    return (good_a if 2*s<m else good_b if 2*s>m else (good_a or good_b))


def brute(r,m,k):
    n=r*m
    neighbors=[tuple(j for j in range(n) if i//m!=j//m) for i in range(n)]
    best=n+1
    ways=0
    examined=0
    optimal_target=formula(r,m,k)[0]
    for a in product(range(k+1),repeat=n):
        examined+=1
        w=sum(v>0 for v in a)
        if w>best:continue
        good=True
        for v in range(n):
            if a[v]==0 and len({a[u] for u in neighbors[v] if a[u]>0})!=k:
                good=False;break
        if not good:continue
        if w==optimal_target:
            assert matches_classification(a,r,m,k),(r,m,k,a)
        if w<best:best=w;ways=0
        ways+=1
    return best,ways,examined


def main():
    count=0;assignments=0
    for r in (2,3,4):
        for m in (1,2,3,4):
            if r*m>8:continue
            for k in range(1,min(5,(r-1)*m+2)):
                expected=formula(r,m,k)
                actual=brute(r,m,k)
                assert actual[:2]==expected, (r,m,k,actual,expected)
                count+=1; assignments+=actual[2]
    # A nine-vertex example with one full part and duplicated leftover colour.
    expected=formula(3,3,4)
    actual=brute(3,3,4)
    assert actual[:2]==expected,(expected,actual)
    count+=1;assignments+=actual[2]
    print(f'VERIFY_OK cases={count} exhaustive_labelings={assignments}')
    print('EXAMPLE r=3 m=3 k=4: minimum='+str(expected[0])+' count='+str(expected[1]))
    for r,m,k in ((3,5,6),(4,5,12),(5,3,10),(2,7,4)):
        print(f'SYMBOLIC_CASE r={r} m={m} k={k} gamma={formula(r,m,k)[0]} optimal_functions={formula(r,m,k)[1]}')

if __name__=='__main__':main()
