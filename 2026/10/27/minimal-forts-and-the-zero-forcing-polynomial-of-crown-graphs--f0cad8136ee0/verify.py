"""Independent direct-definition test for forts and standard zero forcing on crown graphs."""
from collections import Counter
from itertools import combinations
from math import comb

def expected(n):
    return {2*n:1, 2*n-1:2*n, 2*n-2:n*(2*n-1),
            2*n-3:n*n*(n-1), 2*n-4:n*(n-1)*(n-2)*(n+1)//4}

for n in range(3,8):
    # allow O(1) membership in the independently calculated set
    vertices=range(2*n)
    full=(1<<(2*n))-1
    neighbors=[]
    for v in vertices:
        if v<n:neighbors.append(sum(1<<(n+j) for j in range(n) if j!=v))
        else:neighbors.append(sum(1<<i for i in range(n) if i!=v-n))
    zero_set=set()
    forts=[]
    for mask in range(full+1):
        if mask and all((neighbors[v]&mask).bit_count()!=1 for v in vertices if not(mask>>v&1)):
            forts.append(mask)
        blue=mask
        while True:
            adds=0
            for v in vertices:
                if blue>>v&1:
                    w=neighbors[v]&(full^blue)
                    if w.bit_count()==1:adds|=w
            if not adds:break
            blue|=adds
        if blue==full:zero_set.add(mask)
    cand=set()
    for c in combinations(range(n),3):
        cand.add(sum(1<<v for v in c))
        cand.add(sum(1<<(v+n) for v in c))
    for i,j in combinations(range(n),2):
        cand.add((1<<i)|(1<<j)|(1<<(n+i))|(1<<(n+j)))
    # A minimal fort contains no smaller nonempty fort.
    observed={f for f in forts if not any(g!=f and f&g==g for g in forts)}
    assert observed==cand, ('minimal forts',n)
    counts=Counter(mask.bit_count() for mask in zero_set)
    assert counts==expected(n), ('coefficients',n,counts,expected(n))
    for mask in range(full+1):
        A={i for i in range(n) if not(mask>>i&1)}
        B={i for i in range(n) if not(mask>>(n+i)&1)}
        characterization=len(A)<=2 and len(B)<=2 and len(A&B)<=1
        assert (mask in zero_set)==characterization, ('set criterion',n,mask)
    print('n=%d subsets=%d minimal_forts=%d zero_forcing_sets=%d coefficients=%s' %
          (n,1<<(2*n),len(observed),len(zero_set),
           [counts[2*n-k] for k in range(5)]))
print('PASS: all direct-definition checks completed.')
