"""Direct replay of relative-idempotent commutation in the i-Catalan monoid.
Only standard-library Python is needed.
"""
from itertools import combinations,product
from collections import Counter
from math import comb


def elements(n):
    for rank in range(n+1):
        for domain in combinations(range(n),rank):
            for image in combinations(range(n),rank):
                if all(i<=j for i,j in zip(domain,image)):
                    yield dict(zip(domain,image))


def compose(f,g):
    """g after f."""
    return {i:g[j] for i,j in f.items() if j in g}


def narayana(n,r):
    if n==0: return int(r==0)
    if not 0<=r<n:return 0
    return comb(n,r)*comb(n,r+1)//n

S=[{0:1}]
for n in range(1,10):
    S.append({r:narayana(n,r) for r in range(n)})
F=[Counter({0:1})]
for n in range(1,9):
    f=Counter(S[n]);
    for a in range(n):
        for r,x in S[a].items():
            for t,y in F[n-1-a].items():f[r+t]+=x*y
    F.append(f)

for n in range(1,9):
    el=list(elements(n))
    observed=Counter(sum(i<j for i,j in f.items()) for f in el)
    assert observed==F[n],(n,observed,F[n])
    assert len(el)==comb(2*n+2,n+1)//(n+2)
    ids=[{i:i for i in range(n) if mask&(1<<i)} for mask in range(1<<n)]
    if n<=7:
        total=0
        for f in el:
            total+=sum(compose(f,e)==compose(e,f) for e in ids)
        formula=sum(multiplicity*2**(n-r) for r,multiplicity in observed.items())
        assert total==formula,(n,total,formula)
    if n<=5:
        for arity in range(2,4 if n<=4 else 3):
            total=0
            compatible=[sum(compose(f,e)==compose(e,f) for e in ids) for f in el]
            # Direct k-tuple enumeration by composition, up to 4^n*|M|.
            for f in el:
                e_list=[e for e in ids if compose(f,e)==compose(e,f)]
                total+=sum(1 for tup in product(e_list,repeat=arity))
            formula=sum(multiplicity*(2**(arity*(n-r))) for r,multiplicity in observed.items())
            assert total==formula,(n,arity,total,formula)
print('VERIFY_OK: all rank histograms n=1..8; direct products k=1 n<=7, k=2 n<=5, k=3 n<=4')
