"""Independent direct enumeration of Hamming-ball intersection maxima."""
from itertools import permutations
from collections import Counter
from math import factorial

def derangements(n):
    a,b=1,0
    if n==0:return a
    for k in range(2,n+1):a,b=b,(k-1)*(a+b)
    return b

def conjugacy_types(n):
    for p in permutations(range(n)):
        seen=set(); lengths=[]
        for j in range(n):
            if j not in seen:
                k=j; L=0
                while k not in seen:
                    seen.add(k); L+=1; k=p[k]
                if L>1:lengths.append(L)
        yield tuple(sorted(lengths)),p

for n in range(3,9):
    allp=list(permutations(range(n)))
    der=[p for p in allp if all(p[i]!=i for i in range(n))]
    Dn=len(der)
    accum={}
    for typ,p in conjugacy_types(n):
        if not typ or typ in accum:continue
        q=sum(all(w[i]!=p[i] for i in range(n)) for w in der)
        accum[typ]=factorial(n)-2*Dn+q
    best=max(accum.values()); winners=[typ for typ,count in accum.items() if count==best]
    formula=factorial(n)-derangements(n)-2*derangements(n-1)-derangements(n-2)
    assert accum[(2,)]==formula, (n,accum[(2,)],formula)
    if n>=5:assert winners==[(2,)],(n,winners)
    print('n=',n,'types=',len(accum),'max=',best,'winners=',winners,'formula=',formula,'min_gap=',best-max(v for t,v in accum.items() if t!=(2,)) if winners==[(2,)] else 'tie/nonmax')
print('DIRECT_OK')
