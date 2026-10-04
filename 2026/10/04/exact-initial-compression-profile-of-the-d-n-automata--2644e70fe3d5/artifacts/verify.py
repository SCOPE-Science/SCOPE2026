from collections import deque

def h(n):
    return 2*n//3 if n%3==0 else n//3+1

def step(n,S,c):
    if c=='b':
        return frozenset((x+1 if x<n else 1) for x in S)
    out=set()
    for x in S:
        if x<=n-2: out.add(x+1)
        elif x==n-1: out.add(1)
        else: out.add(2)
    return frozenset(out)

def apply(n,w):
    S=frozenset(range(1,n+1))
    for c in w: S=step(n,S,c)
    return S

def bfs(n):
    Q=frozenset(range(1,n+1)); d={Q:0}; cnt={Q:1}; q=deque([Q])
    while q:
        S=q.popleft(); ds=d[S]
        for c in 'ab':
            T=step(n,S,c)
            if T not in d:
                d[T]=ds+1; cnt[T]=cnt[S]; q.append(T)
            elif d[T]==ds+1:
                cnt[T]+=cnt[S]
    return d,cnt

# exhaustive shortest-length and uniqueness checks through the claimed interval and first boundary
for n in range(4,19):
    d,cnt=bfs(n)
    H=h(n)
    for s in range(1,H+1):
        md=min(ds for S,ds in d.items() if n-len(S)>=s)
        ways=sum(cnt[S] for S,ds in d.items() if ds==md and n-len(S)>=s)
        assert md==3*s-2, (n,s,md)
        assert ways==1, (n,s,ways)
        w='a'+'bba'*(s-1)
        assert len(w)==md and n-len(apply(n,w))==s
    s=H+1
    if s<n:
        md=min(ds for S,ds in d.items() if n-len(S)>=s)
        assert md>3*s-2, (n,s,md)

# symbolic witness/hole-orbit checks much farther out
for n in range(4,301):
    H=h(n)
    Q=set(range(1,n+1))
    for s in range(1,H+1):
        w='a'+'bba'*(s-1)
        S=set(apply(n,w))
        assert len(Q-S)==s
    if H+1<n:
        w='a'+'bba'*H
        assert len(Q-set(apply(n,w)))==H
print('VERIFY_OK')
