#!/usr/bin/env python3
"""Independent exact checks for strong odd colorings under partial matching deletion."""
from collections import Counter
from functools import lru_cache
from math import comb, factorial

@lru_cache(None)
def odd_stirling(n,k):
    if n == 0:
        return int(k == 0)
    if k == 0:
        return 0
    return sum(comb(n-1,j-1)*odd_stirling(n-j,k-1) for j in range(1,n+1,2))

def predicted_hist(p,q,t):
    m,r=p-t,q-t
    hist=Counter()
    for k in range(m+1):
        for l in range(r+1):
            x=odd_stirling(m,k)*odd_stirling(r,l)
            if x:
                for j in range(t+1):
                    hist[2*t+k+l-j]+=x*comb(t,j)
    return {d:c for d,c in sorted(hist.items()) if c}

def is_strong_odd(p,q,t,lab):
    n=p+q
    for a in range(p):
        neighbors=[p+b for b in range(q) if not (a<t and b==a)]
        if any(lab[a]==lab[v] for v in neighbors):
            return False
        if any(cnt%2==0 for cnt in Counter(lab[v] for v in neighbors).values()):
            return False
    for b in range(q):
        neighbors=[a for a in range(p) if not (b<t and a==b)]
        if any(lab[p+b]==lab[v] for v in neighbors):
            return False
        if any(cnt%2==0 for cnt in Counter(lab[v] for v in neighbors).values()):
            return False
    return True

def all_partitions(n):
    """Independently enumerate set partitions via restricted-growth words."""
    a=[0]*n
    def walk(i,high):
        if i==n:
            yield tuple(a)
            return
        for nxt in range(high+2):
            a[i]=nxt
            yield from walk(i+1,max(high,nxt))
    yield from walk(1,0)

def brute_hist(p,q,t):
    out=Counter()
    for colors in all_partitions(p+q):
        if is_strong_odd(p,q,t,colors):
            out[max(colors)+1]+=1
    return dict(sorted(out.items()))

def named_direct_count(p,q,t,Q):
    from itertools import product
    return sum(is_strong_odd(p,q,t,colors) for colors in product(range(Q),repeat=p+q))

def falling(Q,k):
    if Q<k:return 0
    ans=1
    for x in range(k):ans*=Q-x
    return ans

def main():
    checked=[]
    for p in range(2,6):
        for q in range(p,7):
            if p+q>10:
                continue
            for t in range(1,min(p,q)):
                want=predicted_hist(p,q,t)
                actual=brute_hist(p,q,t)
                assert actual==want,(p,q,t,actual,want)
                m,r=p-t,q-t
                eps=lambda n: 1 if n%2 else 2
                opt=t+eps(m)+eps(r)
                optimum=(1 if m%2 else 2**(m-2))*(1 if r%2 else 2**(r-2))
                assert min(actual)==opt,(p,q,t,opt,actual)
                assert actual[opt]==optimum,(p,q,t,optimum,actual)
                checked.append((p,q,t,sum(actual.values()),opt,optimum))
    direct=[]
    for p,q,t in [(2,2,1),(2,3,1),(3,3,1),(3,3,2),(3,4,2),(4,4,1)]:
        hist=predicted_hist(p,q,t)
        for Q in range(1,5):
            expected=sum(c*falling(Q,d) for d,c in hist.items())
            actual=named_direct_count(p,q,t,Q)
            assert actual==expected,(p,q,t,Q,actual,expected)
            direct.append((p,q,t,Q,actual))
    print('PASS: independent unlabeled set-partition enumeration versus odd-block formula')
    print('Tested (p,q,t) triples:',len(checked))
    print('Total set partitions examined:',sum(sum(1 for _ in all_partitions(p+q)) for p,q,t,*_ in checked))
    print('Named-color brute force tests:',len(direct))
    for triple in [(2,2,1),(3,3,1),(3,3,2),(4,4,1),(5,5,1),(4,6,2)]:
        p,q,t=triple
        hist=predicted_hist(p,q,t)
        print(f'{triple}: partitions-by-colors = {hist}; optimum = {min(hist)}; bases = {hist[min(hist)]}')
    print('PASS: all checks')
if __name__=='__main__':main()
