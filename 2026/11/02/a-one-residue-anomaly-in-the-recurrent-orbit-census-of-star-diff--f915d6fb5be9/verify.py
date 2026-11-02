"""Separate finite-state checks for the star integer-diffusion orbit census."""
from itertools import product
from collections import Counter
from math import comb

def step(xs):
    c, *leaf=xs
    out=[c, *leaf]
    for i,a in enumerate(leaf,1):
        if a>c:
            out[0]+=1;out[i]-=1
        elif a<c:
            out[0]-=1;out[i]+=1
    return tuple(out)

def periodic_model(xs):
    c,*leaf=xs
    d=[a-c for a in leaf]
    return ('fixed' if all(u==0 for u in d) else 'two' if (all(1<=u<=len(d) for u in d) or all(-len(d)<=u<=-1 for u in d)) else 'none')

checks=0
for r in range(1,6):
    arr=range(-r-2,r+3)
    for d in product(arr,repeat=r):
        xs=(0,*d)
        a=step(xs);b=step(a)
        cat=('fixed' if a==xs else 'two' if b==xs else 'none')
        expected=periodic_model(xs)
        assert cat==expected,(r,xs,cat,expected)
        checks+=1
print('exhaustive_fixed_two_periodic_classifications=',checks)

counts=0
for r in range(1,8):
    byres=Counter()
    for d in product(range(1,r+1),repeat=r):
        byres[sum(d)%(r+1)]+=1
    alpha=(r**r-(-1)**r)//(r+1)
    for s in range(r+1):
        predicted=alpha+((-1)**r if s==0 else 0)
        assert byres[s]==predicted,(r,s,byres[s],predicted)
        counts+=1
print('exact_residue_counts=',counts)

energies=0
for r in range(1,7):
    for target in range(0, r*r+9*(r+1)+1):
        got=0
        for d in product(range(1,r+1),repeat=r):
            rem=target-sum(d)
            if rem>=0 and rem%(r+1)==0:got+=1
        # Independent coefficient calculation via convolution and geometric series.
        dp=[0]*(target+1);dp[0]=1
        for i in range(r):
            new=[0]*(target+1)
            for s,a in enumerate(dp):
                if a:
                    for v in range(1,r+1):
                        if s+v<=target:new[s+v]+=a
            dp=new
        coeff=sum(dp[target-k*(r+1)] for k in range(target//(r+1)+1))
        assert got==coeff,(r,target,got,coeff)
        energies+=1
print('nonnegative_energy_generating_checks=',energies)
print('STAR_DIFFUSION_CENSUS_VERIFIED')
