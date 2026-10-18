#!/usr/bin/env python3
"""Independent gap-word reconstruction and explicit clockwise-cycle checker.
Computes configurations without testing all vertex subsets or using brute_cycle.py.
"""
from collections import Counter, deque
from itertools import combinations
from math import comb,gcd


def configurations(n,k):
    t=n-2*k
    result=set()
    for choices in combinations(range(k),t):
        gap=[2+(int(i in choices)) for i in range(k)]
        for anchor in range(n):
            pos=anchor; state=[]
            for g in gap:
                state.append(pos%n);pos+=g
            assert pos==anchor+n
            result.add(tuple(sorted(state)))
    return result


def gap_of_state(s,n):
    return [((s[(i+1)%len(s)]-s[i])%n) for i in range(len(s))]


def graph(n,k):
    states=sorted(configurations(n,k))
    lut={s:i for i,s in enumerate(states)}
    A=[set() for s in states]
    for idx,s in enumerate(states):
        g=gap_of_state(s,n)
        for j in range(k):
            if g[(j-1)%k]==2 and g[j]==3:
                u=s[j];a=tuple(sorted((set(s)-{u})|{(u+1)%n}))
                A[idx].add(lut[a])
            if g[(j-1)%k]==3 and g[j]==2:
                u=s[j];a=tuple(sorted((set(s)-{u})|{(u-1)%n}))
                A[idx].add(lut[a])
    return states,A


def beatty_cycle(n,k,lookup):
    # For each s, the positions floor((i*n+s)/k) are spaced by 2 or 3.
    # At a step s->s+1, moved indices are non-adjacent in the token ring.
    current=tuple(sorted(((i*n)//k)%n for i in range(k)))
    start=current
    seen={current}
    moves=0
    for s in range(n):
        before=[((i*n+s)//k)%n for i in range(k)]
        after=[((i*n+s+1)//k)%n for i in range(k)]
        assert set(before)==set(current)
        change=[i for i in range(k) if before[i]!=after[i]]
        assert all((i+1)%k not in change and (i-1)%k not in change for i in change)
        for i in change:
            u=before[i];v=after[i]
            assert v==(u+1)%n
            current=tuple(sorted((set(current)-{u})|{v}))
            assert current in lookup
            moves+=1
            if moves<n:
                assert current not in seen
                seen.add(current)
    assert current==start and moves==n and len(seen)==n
    return moves


def verify(n,k):
    states,A=graph(n,k)
    t=n-2*k
    N=len(states);E=sum(len(z) for z in A)//2
    assert all(i in A[j] for i,ns in enumerate(A) for j in ns)
    expected_N=n*comb(k,t)//k
    expected_E=0 if t==0 else n*comb(k-2,t-1)
    assert (N,E)==(expected_N,expected_E)
    if 0<t<k:
        assert beatty_cycle(n,k,set(states))==n
        seen={0};queue=deque([0])
        while queue:
            u=queue.popleft()
            for v in A[u]:
                if v not in seen:seen.add(v);queue.append(v)
        assert len(seen)==N
        deg=Counter(len(z) for z in A)
        expect=Counter({2*r:n*comb(t-1,r-1)*comb(k-t-1,r-1)//r
                        for r in range(1,min(t,k-t)+1)})
        assert deg==expect
    else:
        assert t==0 and N==2 and E==0
    return f'n={n} k={k} t={t} N={N} E={E} beatty_cycle={n if t else None}'

if __name__=='__main__':
    count=0
    for n in range(8,30):
        for k in range((n+2)//3+1,n//2+1):
            if n*comb(k,n-2*k)//k>100000:continue
            print(verify(n,k));count+=1
    print(f'REPLAY_OK gap pairs={count}')
