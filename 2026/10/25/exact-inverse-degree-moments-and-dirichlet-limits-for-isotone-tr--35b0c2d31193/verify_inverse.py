"""Independent finite verification of the inverse-degree laws for isotone chain maps."""
from itertools import combinations_with_replacement
from math import comb
from collections import defaultdict

def compose(f,g):
    # g after f
    return tuple(g[x] for x in f)

def rank(f):
    return len(set(f))

def inverse_count_direct(f, maps):
    total=0
    for g in maps:
        if compose(compose(f,g),f)==f and compose(compose(g,f),g)==g:
            total+=1
    return total

def prediction(f):
    lengths=[]; vals=[]
    prev=f[0];count=0
    for x in f:
        if x!=prev:
            lengths.append(count);vals.append(prev);prev=x;count=1
        else:count+=1
    lengths.append(count);vals.append(prev)
    a=1
    for x in lengths:a*=x
    for i in range(len(vals)-1):a*=vals[i+1]-vals[i]
    return a

def coeff_moments(n,r,k):
    # Dynamic coefficient convolution, independent of direct enumeration
    K=n-r
    h=[(i+1)**k for i in range(K+1)]
    def cv(a,b):
        o=[0]*(K+1)
        for i,ai in enumerate(a):
            if not ai:continue
            for j,bj in enumerate(b[:K-i+1]):o[i+j]+=ai*bj
        return o
    a=[1]+[0]*K
    for _ in range(r):a=cv(a,h)
    b=[1]+[0]*K
    for _ in range(r-1):b=cv(b,h)
    b=cv(b,[i+1 for i in range(K+1)])  # (1-z)^-2
    return a[K]*b[K]

for n in range(1,7):
    maps=list(combinations_with_replacement(range(n),n))
    hist=defaultdict(list)
    for f in maps:
        count=inverse_count_direct(f,maps)
        pred=prediction(f)
        assert count==pred,(n,f,count,pred)
        hist[rank(f)].append(count)
    for r,counts in hist.items():
        assert len(counts)==comb(n-1,r-1)*comb(n,r)
        for k in range(4):
            assert sum(v**k for v in counts)==coeff_moments(n,r,k),(n,r,k)
        assert sum(counts)==comb(n+r-1,2*r-1)**2
    print(f'n={n}, total_maps={len(maps)}, direct_pairs={len(maps)**2}, ranks={len(hist)}')
print('VERIFY_OK')
