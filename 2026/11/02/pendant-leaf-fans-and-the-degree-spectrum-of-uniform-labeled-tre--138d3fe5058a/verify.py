from fractions import Fraction
from itertools import product
from math import comb
import heapq

def p(n,r):
    if r<1 or r>n-1:return Fraction(0)
    if n==2:return Fraction(int(r==1))
    return Fraction(comb(n-2,r-1)*(n-1)**(n-r-1),n**(n-2))

def mean_fan(n,k):
    assert n>=k+2 and k>=2
    return Fraction(comb(n,k)*(n-k)**(n-k-1),n**(n-2))

def delta(n,k,r):
    m=n-k
    return k*int(r==1)+(m-1)*p(m,r)+p(m,r-k)-n*p(n,r)

def degrees_leafneighbors(n,pr):
    d=[1]*n
    for v in pr:d[v]+=1
    nei=[[] for _ in range(n)]
    heap=[v for v in range(n) if d[v]==1];heapq.heapify(heap)
    for v in pr:
        leaf=heapq.heappop(heap)
        nei[v].append(leaf);nei[leaf].append(v)
        d[leaf]-=1;d[v]-=1
        if d[v]==1:heapq.heappush(heap,v)
    u=heapq.heappop(heap);v=heapq.heappop(heap)
    nei[u].append(v);nei[v].append(u)
    dd=list(map(len,nei))
    return dd,[sum(dd[j]==1 for j in nei[v]) for v in range(n)]

assertions=0; trees=0
for n in range(4,9):
    tot=n**(n-2)
    sums_D=[0]*n
    sum_S={k:0 for k in range(2,n-1)}
    sum_SD={(k,r):0 for k in range(2,n-1) for r in range(1,n)}
    for pr in product(range(n),repeat=n-2):
        trees+=1
        dd,lleaves=degrees_leafneighbors(n,pr)
        ds=[dd.count(r) for r in range(n)]
        for r in range(1,n):sums_D[r]+=ds[r]
        for k in range(2,n-1):
            fan=sum(comb(t,k) for t in lleaves if t>=k)
            sum_S[k]+=fan
            for r in range(1,n):sum_SD[(k,r)]+=fan*ds[r]
    for k in range(2,n-1):
        E=mean_fan(n,k)
        assert Fraction(sum_S[k],tot)==E
        assertions+=1
        for r in range(1,n):
            cv=Fraction(sum_SD[(k,r)],tot)-Fraction(sum_S[k]*sums_D[r],tot**2)
            expected=E*delta(n,k,r)
            assert cv==expected,(n,k,r,cv,expected)
            assertions+=1
    print('n',n,'trees',tot,'cumulative assertions',assertions)
print('PASS',trees,'trees',assertions,'independent equalities')
