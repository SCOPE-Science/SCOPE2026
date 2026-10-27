"""Reproduce finite tests for the three-state threshold excitation rule on complete bipartite graphs."""
from itertools import product
from math import comb, factorial

def step(z, a, k):
    left, right = z[:a], z[a:]
    l, r = left.count(1), right.count(1)
    return (tuple(2 if v == 1 else 0 if v == 2 else (1 if r >= k else 0) for v in left)
            + tuple(2 if v == 1 else 0 if v == 2 else (1 if l >= k else 0) for v in right))

def two(n,k):
    return sum(comb(n,i) for i in range(k,n-k+1))

def three(n,k):
    return sum(factorial(n)//(factorial(i)*factorial(j)*factorial(n-i-j))
               for i in range(k,n+1) for j in range(k,n-i+1) if n-i-j>=k)

def check(a,b,k):
    observed = {1:0,3:0,4:0}
    latest = 0
    for z in product(range(3),repeat=a+b):
        t=z
        states=[z]
        for i in range(17):
            t=step(t,a,k)
            states.append(t)
        assert states[17] == states[5], ('bound',a,b,k,z)
        period = None
        for p in (1,3,4):
            if states[p] == z:
                period = p
                observed[p]+=1
                break
        for t in range(6):
            if any(states[t] == states[t+p]
                   for p in (1,3,4)):
                latest=max(latest,t)
                break
        else:
            raise AssertionError(('transient',a,b,k,z))
    expected={1:1,3:three(a,k)*three(b,k),4:2*two(a,k)*two(b,k)}
    assert observed==expected, (a,b,k,observed,expected)
    print('a=%d b=%d threshold=%d states=%d fixed=%d period3=%d period4=%d max_preperiod=%d PASS' %
          (a,b,k,3**(a+b),observed[1],observed[3],observed[4],latest))

if __name__=='__main__':
    pairs=[(2,2,1),(3,3,1),(4,4,2),(3,4,2),(4,5,2),(5,5,2),
           (4,6,2),(3,3,3),(3,5,2),(5,4,3)]
    for a,b,k in pairs:
        check(a,b,k)
