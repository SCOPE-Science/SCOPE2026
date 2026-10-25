"""Exact check for consecutive-label cycle-boundary tails in uniform permutations.
Scientific tests compare independent permutation enumeration with weighted run compositions.
"""
from itertools import permutations, combinations
from math import factorial, comb
from collections import Counter


def group_partitions(k):
    if k == 0:
        yield ()
        return
    for p in group_partitions(k-1):
        yield p + ((k-1,),)
        for i in range(len(p)):
            yield p[:i] + (p[i] + (k-1,),) + p[i+1:]


def allowed_partitions(r):
    return [p for p in group_partitions(r) if all(not any(i in z and i+1 in z for z in p) for i in range(r-1))]


def compositions(n,r):
    for cuts in combinations(range(1,n),r-1):
        pts=(0,)+cuts+(n,)
        yield tuple(pts[i+1]-pts[i] for i in range(r))


def weighted_count(n, d):
    r=d+1
    if r>n:return 0
    partitions=allowed_partitions(r)
    tot=0
    fac=[factorial(i) for i in range(n)]
    for parts in compositions(n,r):
        for blocks in partitions:
            weight=1
            for block in blocks:
                weight*=fac[sum(parts[i] for i in block)-1]
            tot+=weight
    return tot


def brute(n):
    arr=Counter()
    for p in permutations(range(n)):
        labels=[-1]*n;c=0
        for i in range(n):
            if labels[i]<0:
                j=i
                while labels[j]<0:
                    labels[j]=c;j=p[j]
                c+=1
        d=sum(labels[i]!=labels[i+1] for i in range(n-1))
        arr[d]+=1
    return arr


def main():
    checks=0
    for n in range(1,9):
        counts=brute(n)
        for d in range(n):
            got=weighted_count(n,d)
            assert got==counts[d],(n,d,got,counts[d]);checks+=1
        assert sum(counts.values())==factorial(n)
        print('n',n,'boundary counts',list(counts[d] for d in range(n)))
    for n in (12,20,30,50):
        vals=[]
        for d in range(min(4,n)):
            count=weighted_count(n,d)
            scale=n if d%2==0 else n*n
            val=scale*count/factorial(n)
            vals.append((d,round(val,6),'limit', 1 if d%2==0 else d+1))
            checks+=1
        print('n',n,'scaled tails',vals)
    print('ALL EXACT CHECKS PASS:',checks)

if __name__=='__main__': main()
