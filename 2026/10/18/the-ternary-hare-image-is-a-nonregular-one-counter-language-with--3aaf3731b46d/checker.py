"""Independent finite checks for the ternary hare image and fiber theorem."""
from functools import lru_cache
from itertools import product
from collections import Counter
from math import comb

@lru_cache(None)
def hare(w):
    if not w:
        return ()
    biggest=max(w)
    parts=[]; current=[]; num=0
    for a in w:
        if a==biggest:
            parts.append(tuple(current)); current=[]; num+=1
        else: current.append(a)
    parts.append(tuple(current))
    return tuple(a for p in parts for a in hare(p)) + (biggest,)*num

def desc(v):
    return sum((v[i],v[i+1])==(1,0) for i in range(len(v)-1))

def predicted(w):
    k=0
    while k<len(w) and w[-k-1]==2:
        k+=1
    binary=w[:len(w)-k]
    return all(a<2 for a in binary) and desc(binary)<=k

def predicted_fiber(w):
    k=0
    while k<len(w) and w[-k-1]==2:k+=1
    v=w[:len(w)-k]
    if not predicted(w):return 0
    @lru_cache(None)
    def count(i,blocks):
        if blocks==0:return int(i==len(v))
        total=0
        for j in range(i,len(v)+1):
            part=v[i:j]
            if any(part[t]>part[t+1] for t in range(len(part)-1)):break
            total+=comb(len(part),part.count(0))*count(j,blocks-1)
        return total
    return count(0,k+1)

def pred_count(n):
    return sum(comb(n-k+1,2*d+1)
       for k in range(n+1)
       for d in range(min(k,(n-k)//2)+1))

all_counts=[]; checks=0
for n in range(11):
    freq=Counter(hare(w) for w in product(range(3),repeat=n))
    allwords=product(range(3),repeat=n)
    for w in allwords:
        assert (w in freq)==predicted(w),(n,w)
        assert freq.get(w,0)==predicted_fiber(w),(n,w,freq.get(w,0),predicted_fiber(w))
        checks+=1
    assert len(freq)==pred_count(n),(n,len(freq),pred_count(n))
    assert sum(freq.values())==3**n
    all_counts.append(len(freq))
print('lengths 0..10:',all_counts)
print('distinct outputs, all fibers, total inputs and recognition checked for', checks, 'ternary candidate words')
for n in range(4,11):
    assert all_counts[n]==3*all_counts[n-1]-3*all_counts[n-2]+2*all_counts[n-3]-all_counts[n-4]
print('rational generating-function recurrence: verified at lengths 4..10')
print('PASS')
