"""Independent finite check of one-sided multiset deletion sphere moments."""
from itertools import combinations_with_replacement
from math import comb
from fractions import Fraction

def comps(n,q):
    if q==1:
        yield (n,)
    else:
        for j in range(n+1):
            for rest in comps(n-j,q-1):
                yield (j,)+rest

def choose(n,k):
    return comb(n,k) if n>=k>=0 else 0

def volume(x,t):
    return sum(all(d<=a for d,a in zip(y,x)) for y in comps(t,len(x)))

def c(q,m):
    return sum(comb(q-1,j)**2*choose(m-j+q-2,q-2) for j in range(min(m,q-1)+1))

count=0
for q in range(2,6):
    for t in range(1,5):
        for n in range(t,12):
            vals=[volume(x,t) for x in comps(n,q)]
            N=choose(n+q-1,q-1)
            mean=Fraction(sum(vals),N)
            m2=Fraction(sum(v*v for v in vals),N)
            predicted_mean=Fraction(choose(q+t-1,t)*choose(n-t+q-1,q-1),N)
            predicted_second=Fraction(sum(c(q,m)*choose(t-m+q-1,q-1)*choose(n-t-m+q-1,q-1) for m in range(t+1)),N)
            assert mean==predicted_mean,('mean',n,q,t,mean,predicted_mean)
            assert m2==predicted_second,('second',n,q,t,m2,predicted_second)
            count+=len(vals)
print('Exact rational moment checks passed for',count,'centers; all q=2..5, t=1..4, n=t..11.')
