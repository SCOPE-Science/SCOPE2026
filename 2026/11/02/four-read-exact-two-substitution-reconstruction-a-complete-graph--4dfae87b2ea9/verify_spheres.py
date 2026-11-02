"""Exact-radius two binary four-read enumeration, independent bitset test."""
from itertools import combinations
from math import comb

def expected(n):
    return (10*comb(n,5)+180*comb(n,6)+315*comb(n,7)+105*comb(n,8)
            +(5 if n==5 else 0))

def full_reconstruction(n):
    outputs=[(1<<i)|(1<<j) for i,j in combinations(range(n),2)]
    centers={y:sum(1<<x for x in range(1<<n) if (x^y).bit_count()==2) for y in outputs}
    success=0; exceptional=0
    for a,b,c,d in combinations(outputs,4):
        shared=centers[a]&centers[b]&centers[c]&centers[d]
        if shared==1:
            success+=1
            if n==5 and (a|b|c|d).bit_count()==5 and any(sum((x>>i)&1 for x in (a,b,c,d))==4 for i in range(n)):
                exceptional+=1
    return success,exceptional

for n in range(5,10):
    count,ex=full_reconstruction(n)
    print(f'n={n}; exact_uniques={count}; formula={expected(n)}; exceptional_stars={ex}')
    assert count==expected(n)
    assert ex==(5 if n==5 else 0)
print('VERIFY_EXACT_SPHERES_OK')
