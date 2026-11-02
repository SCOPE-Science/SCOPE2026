"""Standalone finite sanity tests for alternating bi-Heyting negation."""
from itertools import combinations

def upclosures(n, edge_mask):
    edges = [(i,j) for i in range(n) for j in range(i+1,n)]
    up = [1 << i for i in range(n)]
    for t, (i,j) in enumerate(edges):
        if edge_mask & (1 << t):
            up[i] |= 1 << j
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if up[i] & (1 << j):
                up[i] |= up[j]
    return up

def algebraic_step(up, U):
    n=len(up); whole=(1<<n)-1
    down_U=0
    for i in range(n):
        if U & (1<<i):
            for j in range(n):
                if up[j] & (1<<i): down_U |= 1<<j
    heyting_neg=whole & ~down_U
    co_neg=whole & ~heyting_neg
    answer=0
    for j in range(n):
        if co_neg & (1<<j):answer |= up[j]
    return answer

def is_upset(up, U):
    return all(not(U&(1<<i)) or (U & up[i]) == up[i] for i in range(len(up)))

def graph_step(up, U):
    n=len(up); answer=U
    for x in range(n):
        if U & (1<<x):
            for y in range(n):
                if any((up[z]&(1<<x)) and (up[z]&(1<<y)) for z in range(n)):
                    answer |= 1<<y
    return answer

def steps(up,U):
    v=U; k=0
    while True:
        w=algebraic_step(up,v)
        if w==v:return k
        assert (w|v)==w
        k+=1
        assert k <= len(up)
        v=w

def fence(k, odd=False):
    n=2*k+int(odd)
    # 0,...,k-1 are minima; k,...,2k-1 are maxima.
    up=[1<<i for i in range(n)]
    for i in range(k):
        up[i]|=1<<(k+i)
        if i<k-1: up[i]|=1<<(k+i+1)
    return up, 1<<k

def run():
    counts={}
    for n in range(1,7):
        mx=0; checked=0; checked_upsets=0
        for em in range(1<<(n*(n-1)//2)):
            up=upclosures(n,em)
            for U in range(1<<n):
                if not is_upset(up,U):continue
                checked_upsets+=1
                f=algebraic_step(up,U)
                g=graph_step(up,U)
                assert f==g, ('algebra/graph mismatch',n,em,U)
                k=steps(up,U)
                assert k <= n//2, ('bound failure',n,em,U,k)
                mx=max(mx,k)
            checked+=1
        assert mx==n//2, ('sharp max failure',n,mx)
        counts[n]=(checked,checked_upsets,mx)
    for k in range(1,51):
        for odd in (False, True):
            up,U=fence(k,odd)
            assert is_upset(up,U)
            assert steps(up,U)==k, ('fence failure',k,odd)
    print('EXHAUSTIVE',counts)
    print('FENCES',100,'ALL_CHECKS_OK')
if __name__=='__main__':run()
