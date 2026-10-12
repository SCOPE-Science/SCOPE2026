"""Exact finite replay for bounded positive-translation reset thresholds."""
from collections import deque


def capacity(m, k):
    s = 0
    denominations = []
    for _ in range(k):
        v = min(m, s+1)
        denominations.append(v)
        s += v
    return s, denominations


def predicted(n, m):
    k=0
    while capacity(m,k)[0]<n-1:
        k+=1
    return k


def shortest_bfs(n, m):
    start=(1<<n)-1
    q=deque([(start,0)])
    seen={start}
    while q:
        mask, depth = q.popleft()
        if mask.bit_count()==1:
            return depth
        for step in range(1,m+1):
            after=0
            for i in range(n):
                if mask & (1<<i):
                    j=i+step if i+step<n else i
                    after|=1<<j
            if after not in seen:
                seen.add(after)
                q.append((after,depth+1))
    raise AssertionError('No reset word')


def replay(n, m, k):
    bound, denoms = capacity(m,k)
    assert bound>=n-1
    assert k==0 or capacity(m,k-1)[0]<n-1
    assert all(1<=v<=min(m,n-1) for v in denoms)
    images=set(range(n))
    for v in reversed(denoms):
        images={min(x+v,n-1) if x+v<n else x for x in images}
    assert images=={n-1},(n,m,denoms,images)


def main():
    tests=0
    for n in range(2,17):
        for m in range(1,8):
            k=predicted(n,m)
            assert shortest_bfs(n,m)==k,(n,m,k)
            replay(n,m,k)
            tests+=1
    print(f'VERIFY_OK {tests} exact independent subset-automaton BFS instances, n=2..16 m=1..7; constructed reset words replayed')


if __name__=='__main__':
    main()
