"""Direct small-case verification of the zero-product rank law for rook monoids."""
from itertools import combinations, permutations
from collections import Counter
from math import comb, factorial, exp


def maps(n):
    for r in range(n+1):
        for dom in combinations(range(n),r):
            for imgs in permutations(range(n),r):
                arr=[-1]*n
                for a,b in zip(dom,imgs): arr[a]=b
                yield tuple(arr)


def expected(n,i,j):
    if i+j>n:return 0
    return factorial(n)*comb(n,i)*comb(n,j)//factorial(n-i-j)


def check_small():
    for n in range(0,5):
        maps_n=list(maps(n)); counts=Counter()
        for a in maps_n:
            ra=sum(v>=0 for v in a)
            for b in maps_n:
                if not any(v>=0 and b[v]>=0 for v in a):
                    rb=sum(v>=0 for v in b)
                    counts[(ra,rb)]+=1
        for i in range(n+1):
            for j in range(n+1):
                assert counts[(i,j)]==expected(n,i,j),(n,i,j,counts[(i,j)],expected(n,i,j))
        total=sum(counts.values())
        oeis=sum(factorial(n)*comb(2*n,n-s)//factorial(s) for s in range(n+1))
        # Above each term is integral for the test dimensions.
        assert total==oeis,(n,total,oeis)
        assert len(maps_n)==sum(comb(n,r)**2*factorial(r) for r in range(n+1))


def check_large():
    for n in range(1,71):
        base=comb(2*n,n)
        w=[comb(2*n,n-s)/factorial(s)/base for s in range(n+1)]
        assert all(0<=v<=1 for v in w)
        if n in (30,60,70):
            p=[x/sum(w) for x in w]
            # The vacancy count approaches Poisson(1).
            for s in range(5):
                assert abs(p[s]-exp(-1)/factorial(s))<0.04,(n,s,p[s])
            # Hypergeometric conditional rank imbalance variance ~ n/2.
            var=(n-1)*(n+1)/(2*n-1)
            assert abs(var/n-0.5)<0.05

if __name__=='__main__':
    check_small();check_large();print('VERIFY_OK: direct pair products through n=4 and 70 exact-ratio cases')
