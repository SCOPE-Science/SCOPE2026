from itertools import combinations
from math import comb, gcd

def states(k,H):
    for bars in combinations(range(H+k-1),k-1):
        bounds=(-1,)+bars+(H+k-1,)
        yield tuple(bounds[i+1]-bounds[i]-1 for i in range(k))

def update(g,c):
    k=len(g)
    return tuple(g[i]-min(c,g[i])+min(c,g[(i+1)%k]) for i in range(k))

def tau(g,c):
    for t in range(len(g)+1):
        if all(v>=c for v in g):return t
        g=update(g,c)
    raise AssertionError('not stabilized')

def formula(k,c):
    L=k-1
    return k*c*comb((c+1)*L+c,L)//((c+1)*L+c)

cases=0
for c in range(1,4):
    for k in range(2,7):
        for surplus in (0,1,2):
            H=k*c+surplus
            if comb(H+k-1,k-1)>100000:continue
            top=sum(tau(g,c)==k-1 for g in states(k,H))
            want=formula(k,c)
            assert top==want,(k,c,H,top,want)
            assert all(tau(g,c)<=k-1 for g in states(k,H))
            cases+=1
print('VERIFY_OK cases=',cases)
