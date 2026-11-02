"""Exact independent checks for period-two chip-firing orbit masses on cycles."""
from collections import Counter
from itertools import product

def plus(A,B):
    C=Counter(A)
    for e,v in B.items():C[e]+=v
    return {e:v for e,v in C.items() if v}
def times(A,B):
    C=Counter()
    for a,va in A.items():
        for b,vb in B.items():C[a+b]+=va*vb
    return dict(C)
def scale(A,c):return {e:c*v for e,v in A.items() if c*v}

def closed_poly(n):
    # s_n = lambda_+^n + lambda_-^n obeys second-order recurrence.
    s0={0:2};s1={1:1,2:1}
    for j in range(2,n+1):
        s0,s1=s1,plus(times({1:1,2:1},s1),times({3:1},s0))
    correction={n:(-1)**n,2*n:(-1)**n}
    total=plus(s1,correction)
    assert all(x%2==0 for x in total.values())
    return {e:v//2 for e,v in total.items() if v}

def step(c):
    n=len(c); fire=[int(v>=2) for v in c]
    return tuple(c[i]-2*fire[i]+fire[(i-1)%n]+fire[(i+1)%n] for i in range(n))

def brute(n):
    count=Counter();two_states=0
    for c in product(range(4),repeat=n):
        nxt=step(c)
        if nxt!=c and step(nxt)==c:
            count[sum(c)]+=1
            two_states+=1
    assert all(v%2==0 for v in count.values())
    return {k:v//2 for k,v in count.items()},two_states

if __name__=='__main__':
    total=0
    for n in range(3,10):
        count,states=brute(n)
        expect=closed_poly(n)
        assert count==expect,(n,count,expect)
        assert sum(count.values())==sum(expect.values())
        assert all(n<=k<=2*n for k in count)
        assert all(count.get(k,0)==count.get(3*n-k,0) for k in count)
        total+=4**n
        print('n',n,'configs',4**n,'two_states',states,'orbits',sum(expect.values()),'energy_counts',sorted(expect.items()))
    print('EXACT_RING_CHIPFIRE_MASS_VERIFY_OK','configurations',total)
