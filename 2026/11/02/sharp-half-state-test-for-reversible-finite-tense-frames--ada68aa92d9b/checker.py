"""Finite exhaustive checks of mixed-adjoint tense identities (Python 3 stdlib).
Finite tests corroborate, but do not replace, the symbolic proofs.
"""
from itertools import product
from math import comb, factorial

def stirling(n):
    s = [[0]*(n+1) for _ in range(n+1)]
    s[0][0] = 1
    for a in range(1, n+1):
        for b in range(1, a+1):
            s[a][b] = s[a-1][b-1] + b*s[a-1][b]
    return s

def count_rank_formula(n,k):
    if k==n:
        return factorial(n)
    s = stirling(n)
    return comb(n,k)*factorial(k)*sum(s[k][b]*s[n-k][k-b]
                                          for b in range(1,k))

def power(f,k):
    n=len(f)
    q=tuple(range(n))
    for _ in range(k):
        q=tuple(f[q[i]] for i in range(n))
    return q

def good(g):
    a=set(g)
    return not ({g[x] for x in a} & {g[x] for x in range(len(g)) if x not in a})

def modal_commutes(g):
    n=len(g)
    A=sum(1<<v for v in set(g))
    fibers=[0]*n
    for u,y in enumerate(g): fibers[y] |= 1<<u
    def closure(X):
        ans=0
        for u in range(n):
            if X&(1<<u): ans |= fibers[g[u]]
        return ans
    for X in range(1<<n):
        if closure(X&A) != (closure(X)&A):
            return False
    return True

def height(f):
    h=0
    for x in range(len(f)):
        seen={}
        y=x
        while y not in seen:
            seen[y]=len(seen)
            y=f[y]
        h=max(h,seen[y])
    return h

def run():
    total=0
    for n in range(1,7):
        by_rank=[0]*(n+1)
        for f in product(range(n), repeat=n):
            a=len(set(f))
            if good(f): by_rank[a]+=1
            h=height(f)
            K=(n+1)//2
            if h==0:
                assert good(power(f,K))
            else:
                assert not good(power(f,K)), ('uniform cutoff',n,f,h)
                for k in range(h//2+1,n+1):
                    assert not good(power(f,k)), ('height cutoff',n,f,k)
            if n<=4:
                for k in range(n+1):
                    g=power(f,k)
                    assert good(g)==modal_commutes(g),('modal identity',n,f,k)
        for k in range(1,n+1):
            assert by_rank[k]==count_rank_formula(n,k),('Stirling formula',n,k)
        chain=tuple(min(i+1,n-1) for i in range(n))
        K=(n+1)//2
        if n>=2:
            assert all(good(power(chain,k)) for k in range(K))
            assert all(not good(power(chain,k)) for k in range(K,n+1))
        print(f'n={n} rank_counts={by_rank} total={sum(by_rank)} cutoff={K}')
        total+=n**n
    for n in range(7,31):
        chain=tuple(min(i+1,n-1) for i in range(n))
        K=(n+1)//2
        assert all(good(power(chain,k)) for k in range(K))
        assert all(not good(power(chain,k)) for k in range(K,n+1))
    for n in [7,8,9,10]:
        print(f'n={n} count_formula={sum(count_rank_formula(n,k) for k in range(1,n+1))}')
    print(f'ALL_CHECKS_OK: {total} endofunctions; all iterates n<=6; direct modal identities n<=4; sharp chains n<=30.')

if __name__=='__main__': run()
