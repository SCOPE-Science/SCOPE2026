"""Standalone exhaustive small-instance verification of simultaneous domination on rook graphs.

Every tested subset is evaluated from independent row/column adjacency masks,
not from the theorem's occupancy criteria.
"""
from itertools import combinations
from math import comb, factorial


def closed_and_complement_open(m,n):
    V=[(i,j) for i in range(m) for j in range(n)]
    c=[];o=[]
    for (i,j) in V:
        c.append(sum(1<<z for z,(a,b) in enumerate(V) if i==a or j==b))
        o.append(sum(1<<z for z,(a,b) in enumerate(V) if i!=a and j!=b))
    return V,c,o


def direct(m,n,D,c,o):
    bits=sum(1<<z for z in D)
    return all(bits & nb for nb in c) and all(bits & nb for nb in o)


def theorem_number(m,n):
    assert 2<=m<=n
    if m==2:return 4,comb(n,2)**2
    a=n**m-n-m*n*(n-1)
    return m,(2*a-factorial(m)) if m==n else a


def theorem_indicator(m,n,D):
    W={(z//n,z%n) for z in D}
    if m==2:
        return len(W)==4 and all(sum(i==a for i,j in W)==2 for a in range(2))
    if len(W)!=m:return False
    rows=all(sum(a==i for a,b in W)==1 for i in range(m))
    cols=all(sum(b==j for a,b in W)==1 for j in range(n)) if n==m else False
    if rows:
        c=[sum(b==j for a,b in W) for j in range(n)]
        if max(c)<=m-2:return True
    if cols:
        r=[sum(a==i for a,b in W) for i in range(m)]
        if max(r)<=m-2:return True
    return False


def main():
    pairs=[(2,n) for n in range(2,9)] + [(3,n) for n in range(3,7)] + [(4,n) for n in range(4,7)] + [(5,n) for n in range(5,7)]
    trials=0
    for m,n in pairs:
        V,c,o=closed_and_complement_open(m,n)
        k,target=theorem_number(m,n)
        num=0
        for r in range(k+1):
            for D in combinations(range(m*n),r):
                ok=direct(m,n,D,c,o)
                if r<k:
                    assert not ok,(m,n,r,D)
                else:
                    assert ok==theorem_indicator(m,n,D),(m,n,D,ok)
                    num+=ok
                trials+=1
        assert num==target,(m,n,target,num)
        print(f'{m}x{n}: minimum={k}, exact minimizers={num}')
    print(f'ALL PASS: {len(pairs)} parameter pairs; {trials} subsets checked independently.')

if __name__=='__main__':main()
