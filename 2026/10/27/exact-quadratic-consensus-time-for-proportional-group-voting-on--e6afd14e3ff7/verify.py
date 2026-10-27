"""Exact independent checks for the hyperpath block-voter consensus theorem.
Requires only Python standard library. Run: python verify.py
"""
from fractions import Fraction as F
from collections import deque


def hyperpath(L, k, s):
    assert L >= 2 and 1 <= s and 2*s <= k
    edges = [tuple(range(k))]
    nxt = k
    for _ in range(1, L):
        fresh = tuple(range(nxt, nxt + k - s))
        nxt += k - s
        edges.append(tuple(edges[-1][-s:]) + fresh)
    assert nxt == L*k - (L-1)*s
    return edges, nxt


def transitions(x, edges):
    active = []
    for e in edges:
        full = sum(1<<v for v in e)
        nA = (x & full).bit_count()
        if 0 < nA < len(e):
            active.append((x | full, F(nA,len(e))))
            active.append((x & ~full, F(len(e)-nA,len(e))))
    return active


def reachable(edges, seed):
    seen = {seed}
    q = deque([seed])
    while q:
        x=q.popleft()
        for y,prob in transitions(x,edges):
            assert prob > 0
            if y not in seen:
                seen.add(y);q.append(y)
    return sorted(seen)


def solve(A, b):
    n=len(A)
    m=[A[i][:]+[b[i]] for i in range(n)]
    for i in range(n):
        pivot = next(h for h in range(i,n) if m[h][i])
        m[i],m[pivot]=m[pivot],m[i]
        t=m[i][i]
        m[i]=[v/t for v in m[i]]
        for h in range(n):
            if h != i:
                t=m[h][i]
                if t:m[h]=[v-t*w for v,w in zip(m[h],m[i])]
    return [m[i][-1] for i in range(n)]


def trial(L,k,s,j):
    edges,N=hyperpath(L,k,s)
    seed = 0
    for e in edges[:j]:
        for v in e:seed |=1<<v
    assert seed.bit_count() == j*(k-s)+s
    states=reachable(edges,seed)
    # Exactly one mixed edge before consensus; no additional absorbing state.
    full=(1<<N)-1
    assert len(states)==(2*L if k>2*s else L+2),(L,k,s,j,len(states))
    assert 0 in states and full in states
    transient=[x for x in states if x not in (0,full)]
    assert all(len(transitions(x,edges))==2 for x in transient)
    m=len(transient); index={x:i for i,x in enumerate(transient)}
    A=[[F(int(i==h)) for h in range(m)] for i in range(m)]
    t=[F(1) for _ in range(m)]; c=[F(0) for _ in range(m)]
    for x,i in index.items():
        for y,p in transitions(x,edges):
            if y in index: A[i][index[y]]-=p
            elif y==full:c[i]+=p
            else:assert y==0
    T=solve(A,t)[index[seed]]
    P=solve(A,c)[index[seed]]
    p=F(s,k)
    assert T == F(L-j) + (1-p)/p*F(j*(L-j)),(L,k,s,j,T)
    assert P == F(j*(k-s)+s,N),(L,k,s,j,P)
    return T,P

if __name__=='__main__':
    runs=0
    for L in range(2,8):
        for k in range(2,9):
            for s in range(1,k//2+1):
                for j in range(1,L):
                    trial(L,k,s,j)
                    runs+=1
    print('PASS exact labeled CTMC:',runs,'hyperpath/seed instances')
    print('PASS unique active hyperedge, exact state count, fixation and hitting-time formulas')
