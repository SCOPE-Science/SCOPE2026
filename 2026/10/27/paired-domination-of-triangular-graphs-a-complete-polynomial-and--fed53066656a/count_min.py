"""Supplemental exhaustive minimum-weight checks via edge-component parity."""
from itertools import combinations
from math import factorial

def is_valid(n, edges):
    p = list(range(n))
    deg = [0]*n
    def root(u):
        while p[u] != u: u = p[u]
        return u
    for u,v in edges:
        p[root(u)] = root(v)
        deg[u] += 1; deg[v] += 1
    if deg.count(0)>1: return False
    parity=[0]*n
    for u,v in edges: parity[root(u)] += 1
    return all(k%2==0 for k in parity)

def predicted(n):
    b=(n+1)//3
    t=n//3
    d=factorial(n)
    if n%3==1:
        return d//(2**t*factorial(t))
    if n%3==0:
        a=d//(2**t*factorial(t))
        if t>=2:
            a+= d*125//(120*2**(t-2)*factorial(t-2))
        return a
    ans=d*125//(120*2**(t-1)*factorial(t-1))
    ans+=d*15//(24*2**(t-1)*factorial(t-1))
    if t>=2: ans+=d*16807//(5040*2**(t-2)*factorial(t-2))
    if t>=3: ans+=d*125*125//(120*120*2*2**(t-3)*factorial(t-3))
    return ans

if __name__=='__main__':
 for n in range(3,9):
    m=n*(n-1)//2
    k=2*((n+1)//3)
    E=list(combinations(range(n),2))
    count=sum(is_valid(n,edges) for edges in combinations(E,k))
    assert count==predicted(n),(n,count,predicted(n))
    print(f'n={n} min_size={k} exact_count={count} predicted={predicted(n)}')
 print('ALL MINIMUM-COUNT CHECKS PASSED')
