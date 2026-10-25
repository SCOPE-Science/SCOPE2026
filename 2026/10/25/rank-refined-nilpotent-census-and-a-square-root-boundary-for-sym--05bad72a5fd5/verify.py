"""Exhaustive finite checks for nilpotent-rank counts in partial-injection sandwiches."""
from itertools import combinations, permutations
from math import comb, factorial


def partial_injections(n):
    points=tuple(range(n))
    for k in range(n+1):
        for domain in combinations(points,k):
            for image in combinations(points,k):
                for arrangement in permutations(image):
                    f=[-1]*n
                    for a,b in zip(domain,arrangement):
                        f[a]=b
                    yield k,tuple(f)


def compose(f,g):
    # Map convention: first f, then g.
    return tuple(g[f[x]] if f[x]>=0 and g[f[x]]>=0 else -1 for x in range(len(f)))


def sandwich_nilpotent(f,a):
    zero=(-1,)*len(f)
    x=f
    for t in range(len(f)+4):
        if x==zero:
            return True
        x=compose(compose(x,a),f)
    return False


def theoretical(n,r,k):
    total=comb(n,k)**2*factorial(k)
    exceptional=0 if not k or not r else r*comb(n-1,k-1)**2*factorial(k-1)
    return total-exceptional


def exhaustive():
    cases=0
    elements=0
    for n in range(1,7):
        f_by_rank={k:[] for k in range(n+1)}
        for k,f in partial_injections(n):
            f_by_rank[k].append(f)
        for r in range(n+1):
            sandwich=tuple(i if i<r else -1 for i in range(n))
            for k,fs in f_by_rank.items():
                count=sum(sandwich_nilpotent(f,sandwich) for f in fs)
                want=theoretical(n,r,k)
                assert count==want,(n,r,k,count,want)
                cases+=1
                elements+=len(fs)
    return cases,elements


def check_noncanonical():
    tests=0
    for n in (3,4,5):
        fs=list(partial_injections(n))
        for r in range(0,n+1):
            maps=[g for k,g in fs if k==r]
            for a in maps[::max(1,len(maps)//5)][:6]:
                counts=[0]*(n+1)
                for k,f in fs:
                    counts[k]+=sandwich_nilpotent(f,a)
                assert counts == [theoretical(n,r,k) for k in range(n+1)],(n,r,a,counts)
                tests+=1
    return tests


def check_inclusion_exclusion():
    for n in range(1,30):
        weights=[comb(n,k)**2*factorial(k) for k in range(n+1)]
        total=sum(weights)
        assert sum((n-k)*(n-k+1)*weights[k] for k in range(n+1))==n*total
        for r in range(n+1):
            for k in range(n+1):
                assert theoretical(n,r,k)>=0
                assert theoretical(n,r,k)<=comb(n,k)**2*factorial(k)


if __name__=='__main__':
    c,e=exhaustive()
    d=check_noncanonical()
    check_inclusion_exclusion()
    print('ALL_SANDWICH_NILPOTENT_CHECKS_PASSED',c,'exhaustive rank strata',e,'evaluated elements',d,'noncanonical sandwiches')
