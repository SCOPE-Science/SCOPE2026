from itertools import combinations_with_replacement
from math import comb
from collections import Counter
from sympy import totient, divisors

def calc(p):
    unvisited=set(combinations_with_replacement(range(p),5))
    cnt=0
    while unvisited:
        a=next(iter(unvisited)); cnt+=1
        for sc in range(1,p):
            for sh in range(p):
                b=tuple(sorted(((sc*x+sh)%p for x in a)))
                unvisited.discard(b)
    A=comb(p+4,5)
    B=0
    for d in divisors(p-1):
        if d==1:continue
        m=(p-1)//d
        F=sum(comb(m+j-1,j) for j in range(5//d+1))
        B+=int(totient(d))*F
    if p==5:A+=p-1
    formula=(A+p*B)//(p*(p-1))
    assert formula==cnt,(p,formula,cnt)
    return p, cnt-2
for p in (3,5,7,11,13):
    if p<=11: print('CHECK',calc(p),flush=True)
    else:
        # formula-only at p13
        print('CHECK',calc(p),flush=True)
print('RANK3_ORBIT_OK')
