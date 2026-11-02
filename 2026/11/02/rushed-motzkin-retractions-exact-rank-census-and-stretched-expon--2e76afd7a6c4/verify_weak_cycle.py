"""Exhaustive small-case weak-cycle retraction enumeration against the transfer formula."""
from itertools import product
from collections import Counter

def transfer(n,weak):
    result=Counter({n:1})
    if not weak and n%2: return dict(result)
    for ell in range(0 if weak else 1, n//2+1):
        rank=ell+1
        d=[0]*(ell+1)
        d[0]=1
        for _ in range(n-ell):
            d=[(d[i] if weak else 0)+(d[i-1] if i>0 else 0)+(d[i+1] if i<ell else 0) for i in range(ell+1)]
        result[rank]+=n*d[ell]
    return dict(result)

def brute(n,weak):
    result=Counter()
    steps=(-1,0,1) if weak else (-1,1)
    nwalk=0
    for w in product(steps, repeat=n):
        if sum(w)%n:continue
        nwalk+=1
        path=[0]
        for step in w[:-1]:path.append((path[-1]+step)%n)
        for shift in range(n):
            f=[(z+shift)%n for z in path]
            if all(f[f[i]]==f[i] for i in range(n)):
                result[len(set(f))]+=1
    return dict(result),n*nwalk

def run():
    for n in range(3,10):
        for weak in (True,):
            census,total=brute(n,weak)
            formula=transfer(n,weak)
            assert census==formula,(n,weak,census,formula)
            print('PASS',n,'weak' if weak else 'strict','rank_counts',sorted(formula.items()),'monoid_size',total)
    print('VERIFY_OK')

if __name__=='__main__':run()
