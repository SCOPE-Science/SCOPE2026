"""Independent gap-composition construction, checking all adjacency and local faces."""
from itertools import combinations_with_replacement,combinations
from collections import defaultdict,Counter

def compositions_two(m):
    for i in range(m):
        for j in range(i,m):
            x=[0]*m;x[i]+=1;x[j]+=1
            yield x

def check(k,m):
    q=k+1;n=q*m+2
    states=set()
    for anchor in range(n):
        for s in compositions_two(m):
            a=[anchor]
            for i in range(m-1):a.append((a[-1]+q+s[i])%n)
            states.add(tuple(sorted(a)))
    states=sorted(states);idx={a:i for i,a in enumerate(states)}
    assert len(states)==n*(m+1)//2
    adj=[set() for _ in states]
    for r,a in enumerate(states):
        cyclic=list(a)
        gap=[(cyclic[(i+1)%m]-cyclic[i])%n-q for i in range(m)]
        assert sum(gap)==2 and all(v>=0 for v in gap)
        for i,x in enumerate(cyclic):
            for d in (1,2):
                if gap[i]>=d:
                    b=tuple(sorted((set(a)-{x})|{(x+d)%n}))
                    adj[r].add(idx[b])
                if gap[(i-1)%m]>=d:
                    b=tuple(sorted((set(a)-{x})|{(x-d)%n}))
                    adj[r].add(idx[b])
    assert all(len(s)==4 for s in adj)
    As={r for r,a in enumerate(states) if any((a[(i+1)%m]-a[i])%n==q+2 for i in range(m))}
    Ts=[(u,v,w) for u in range(len(states)) for v in adj[u] if v>u for w in adj[u]&adj[v] if w>v]
    squares=[]
    for u in range(len(states)):
        for w in range(u+1,len(states)):
            for v,z in combinations(sorted(adj[u]&adj[w]),2):
                if w not in adj[u] and z not in adj[v]:squares.append((u,v,w,z))
    squares=list({tuple(sorted(f)):f for f in squares}.values())
    TsByVertex=Counter(v for f in Ts for v in f)
    SqByVertex=Counter(v for f in squares for v in f)
    assert len(Ts)==n and len(squares)==n*(m-1)//2
    for r in range(len(states)):
        if r in As: assert (TsByVertex[r],SqByVertex[r])==(2,1)
        elif m==2:assert (TsByVertex[r],SqByVertex[r])==(2,2)
        elif TsByVertex[r]:assert (TsByVertex[r],SqByVertex[r])==(1,3)
        else:assert (TsByVertex[r],SqByVertex[r])==(0,4)
    # Special-gap configurations: the one-gap family is indexed by the token before the long gap.
    A_by_x={}
    for r in As:
        a=states[r]
        positions=[a[i] for i in range(m) if (a[(i+1)%m]-a[i])%n==q+2]
        assert len(positions)==1
        A_by_x[positions[0]]=r
    assert len(A_by_x)==n
    for x,r in A_by_x.items():
        assert {A_by_x[(x-q)%n],A_by_x[(x+q)%n]}==adj[r]&As
    print(f'GAPS_PASS k={k} m={m} states={len(states)} A={len(As)}')
for k in range(2,7):
    for m in range(2,7):
        if (k+1)*m+2<=35:check(k,m)
print('GAPS_ALL_PASS')
