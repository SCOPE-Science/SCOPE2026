"""Exhaustively check cyclic homopolymer-free three-gram fibers against the theorem."""
from itertools import product
from collections import Counter
from math import comb,ceil
LABELS=['001','010','011','100','101','110']
def fiber_formula(n):
    counts={}
    for s in range((n+3)//4,n//2+1):
        for a in range(s+1):
            b=n-2*s-a
            if 0<=b<=s:
                p=(a,s-b,b,a,s-a,b)
                k=n*comb(s,a)*comb(s,b)
                assert k%s==0
                counts[p]=k//s
    return counts
for n in range(2,19):
    direct=Counter()
    for seq in product('01',repeat=n):
        if any(seq[i]==seq[(i+1)%n]==seq[(i+2)%n] for i in range(n)):
            continue
        p=[0]*6
        for i in range(n):
            gram=seq[i]+seq[(i+1)%n]+seq[(i+2)%n]
            p[LABELS.index(gram)]+=1
        direct[tuple(p)]+=1
    assert dict(direct)==fiber_formula(n),(n, direct, fiber_formula(n))
    best=max(direct.values())
    reduced=max(n*comb(s,(n-2*s)//2)*comb(s,(n-2*s+1)//2)//s
                for s in range((n+3)//4,n//2+1))
    assert best==reduced
    print(n,len(direct),best)
print('EXHAUSTIVE_OK n=2..18')
