"""Independent unsaturated vertex-level checks of excitable crown dynamics."""
from itertools import product
from collections import Counter
from math import factorial

def step(s):
    n=len(s)//2
    a,b=s[:n],s[n:]
    out=[]
    for shore,opposite in ((a,b),(b,a)):
        for i,x in enumerate(shore):
            if x:out.append((x+1)%3)
            else:out.append(int(sum(v==1 for j,v in enumerate(opposite) if j!=i)>=2))
    return tuple(out)

def classify(x):
    seen={};t=0
    while x not in seen:
        if t>100:raise AssertionError('unbounded')
        seen[x]=t;x=step(x);t+=1
    T=seen[x];return T,t-T

for n in range(1,6):
    counts=Counter(classify(x) for x in product(range(3),repeat=2*n))
    assert sum(counts.values())==3**(2*n)
    assert max(t for t,p in counts)<=9
    assert all(60%p==0 for t,p in counts)
    print(n, 'full labelled states',3**(2*n),'periods',sorted(set(p for t,p in counts)), 'maxT',max(t for t,p in counts))

TYPES=tuple(product(range(3),repeat=2))
def witness(code):
    cnt=[(code>>(2*i))&3 for i in range(9)]
    pair_states=tuple(st for i,c in enumerate(cnt) for st in [TYPES[i]]*c)
    n=len(pair_states)
    return tuple(x for a,b in pair_states for x in [a])+tuple(x for a,b in pair_states for x in [b])
assert classify(witness(70997))==(0,30)
assert classify(witness(86357))==(0,30)
assert classify(witness(83112))==(9,4)
print('direct-period-30-and-sharp-transient-witnesses-ok')
