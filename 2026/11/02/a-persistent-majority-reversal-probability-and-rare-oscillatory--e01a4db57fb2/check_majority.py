"""Checks finite state dynamics and exact weighted macro census for majority on K_{n,n,n}."""
from itertools import product
from math import comb, atan, sqrt, pi
from collections import Counter


def macro_step(q,n):
    return tuple(n if (sum(q)-q[i])>n else (0 if (sum(q)-q[i])<n else q[i]) for i in range(3))

def orbit_info(q,n):
    seen={};z=q
    while z not in seen:
        seen[z]=len(seen);z=macro_step(z,n)
        assert len(seen)<20
    return seen[z],len(seen)-seen[z],z

def basin_formula(n):
    ans=0
    for a in range(n+1):
        lo=min(a,n-a);hi=max(a,n-a)
        ans+=comb(n,a)**2*sum(comb(n,b) for b in range(lo+1,hi))
    return 3*ans

def weighted_macro_check(n):
    counts=Counter()
    for q in product(range(n+1),repeat=3):
        w=comb(n,q[0])*comb(n,q[1])*comb(n,q[2]); t,p,_=orbit_info(q,n)
        assert t<=2 and p<=2
        counts[t,p]+=w
    assert sum(counts.values())==2**(3*n)
    period2=sum(v for (t,p),v in counts.items() if p==2)
    period2_initial=counts[(0,2)]
    fixed=counts[(0,1)]
    assert period2==basin_formula(n),(n,period2,basin_formula(n))
    assert period2_initial==6*(2**n-2)
    assert fixed==2+(comb(n,n//2)**3 if n%2==0 else 0)
    return counts

def microscopic_check(n):
    nn=3*n; neighbors=[tuple(range(n,3*n)) if i<n else (tuple(range(n))+tuple(range(2*n,3*n)) if i<2*n else tuple(range(2*n))) for i in range(nn)]
    # First part has two other parts, not only the last part.
    neighbors=[tuple(j for j in range(nn) if j//n != i//n) for i in range(nn)]
    result=Counter()
    for mask in range(1<<nn):
        def step(x):
            y=0
            for i in range(nn):
                ones=sum((x>>j)&1 for j in neighbors[i]);bit=(x>>i)&1
                val=1 if ones>n else (0 if ones<n else bit)
                y|=val<<i
            return y
        seen={};x=mask
        while x not in seen:
            seen[x]=len(seen);x=step(x)
            assert len(seen)<10
        t=seen[x];p=len(seen)-t
        result[t,p]+=1
    assert result==weighted_macro_check(n),(n,result,weighted_macro_check(n))
    return result

for n in range(1,31):
    c=weighted_macro_check(n)
    if n <= 5:
        assert c==microscopic_check(n)
    print(n, 'two_cycle',sum(v for (t,p),v in c.items() if p==2), 'P',round(basin_formula(n)/2**(3*n),10),'transient_max',max(t for t,p in c))
print('reversal_constant',1-3*atan(sqrt(2))/pi)
print('oscillation_sqrt_n_constant',6*atan(1/sqrt(2))/pi**1.5)
print('BALANCED_TRIPARTITE_MAJORITY_CHECK_OK')
