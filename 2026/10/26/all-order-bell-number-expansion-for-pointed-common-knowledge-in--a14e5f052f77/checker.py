"""Independent small-size enumeration for pointed common-knowledge probability."""
from fractions import Fraction
from itertools import product
from math import comb

def partitions(n):
    if n == 0:
        yield ()
        return
    def generate(prefix, top):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for x in range(top + 2):
            yield from generate(prefix + [x], max(top, x))
    yield from generate([0], 0)

def component_size(q):
    n=len(q[0]); d=list(range(n))
    def root(x):
        while d[x]!=x: x=d[x]
        return x
    for part in q:
        leaders={}
        for v,a in enumerate(part):
            if a in leaders: d[root(v)]=root(leaders[a])
            else: leaders[a]=v
    return sum(root(i)==root(0) for i in range(n))

def check(n,r):
    arr=list(partitions(n)); B=[sum(1 for _ in partitions(k)) for k in range(n+1)]
    A=[b**r for b in B]; C=[0]*(n+1)
    for k in range(1,n+1):
        C[k]=A[k]-sum(comb(k-1,j-1)*C[j]*A[k-j] for j in range(1,k))
    observed=[0]*(n+1)
    for q in product(arr, repeat=r): observed[component_size(q)] += 1
    expected=[0]+[comb(n-1,k-1)*C[k]*A[n-k] for k in range(1,n+1)]
    assert observed==expected,(n,r,observed,expected)
    probability=Fraction(sum(observed[k]*2**(n-k) for k in range(1,n+1)),(B[n]**r)*2**n)
    exact= sum((Fraction(comb(n-1,k-1)*C[k]*A[n-k],A[n])*Fraction(1,2**k) for k in range(1,n+1)),Fraction(0))
    assert probability==exact
    return (n,r,B[n]**r,tuple(observed[1:]),str(exact))

if __name__=='__main__':
    for r in (2,3):
        for n in range(1,7 if r==2 else 5):
            print(*check(n,r))
