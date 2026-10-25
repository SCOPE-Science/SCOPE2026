"""Independent finite checks of normality and labelled partition enumeration.
Run: python checker.py
"""
from functools import lru_cache
from itertools import product
from math import comb

@lru_cache(None)
def parts(n):
    if n == 0:
        return ((),)
    result=[]
    for p in parts(n-1):
        result.append(p+((n-1,),))
        for j in range(len(p)):
            a=list(p); a[j]=a[j]+(n-1,)
            result.append(tuple(a))
    return tuple(result)

def cells(p,n):
    return tuple(next(frozenset(b) for b in p if x in b) for x in range(n))

def normal_local(collection,n):
    cells_by_agent=[cells(p,n) for p in collection]
    for w in range(n):
        common=set(range(n))
        for C in cells_by_agent: common.intersection_update(C[w])
        if not any(set(C[w])==common for C in cells_by_agent): return False
    return True

def brute_distribution(collection,n):
    C=[cells(p,n) for p in collection]
    def op(w,assignment):
        return any(all(assignment>>x & 1 for x in A[w]) for A in C)
    for w in range(n):
        for P in range(1<<n):
            for Q in range(1<<n):
                if op(w,P) and op(w,Q) and not op(w,P&Q): return False
    return True

def bell(n):return len(parts(n))
def stirling(n,t):
    if n==t==0:return 1
    if n<=0 or t<=0:return 0
    return stirling(n-1,t-1)+t*stirling(n-1,t)
def h(t,r):
    return sum((-1)**j*comb(t,j)*sum((-1)**k*comb(j,k)*bell(t-k) for k in range(j+1))**r for j in range(t+1))
def predicted(n,r):return sum(stirling(n,t)*h(t,r) for t in range(n+1))

if __name__=='__main__':
    for n,r in [(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(2,3),(3,3),(4,3),(3,4)]:
        got=sum(normal_local(P,n) for P in product(parts(n),repeat=r))
        exp=predicted(n,r)
        print(f'n={n} agents={r}: observed={got} predicted={exp}, ambient={bell(n)**r}')
        assert got==exp
    for n,r in [(2,2),(3,2),(3,3)]:
        for P in product(parts(n),repeat=r):
            assert normal_local(P,n)==brute_distribution(P,n)
        print(f'n={n} agents={r}: local-vs-all-valuations PASS')
    print('All checks passed.')
