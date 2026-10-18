"""Exact tests of run-limited cyclic coverage; Python 3, standard library only.
Run: python3 CHECK.py
"""
from itertools import product
from collections import Counter, defaultdict
from math import prod


def admissible(w, r):
    return (0,) * r not in tuple(w[i:i+r] for i in range(len(w)-r+1))


def D_coeff(q, m, N):
    return [1]+[-(q-1) if i <= m else 0 for i in range(1,N+1)]


def series_inv(d,N):
    a=[0]*(N+1); a[0]=1
    for k in range(1,N+1): a[k]=-sum(d[j]*a[k-j] for j in range(1,min(k,len(d)-1)+1))
    return a


def overhead_from_gf(q,r,n):
    N=n-r
    a=series_inv(D_coeff(q,r-1,N),N)
    b=series_inv(D_coeff(q,r,N),N)
    c=[sum(a[j]*b[k-j] for j in range(k+1)) for k in range(N+1)]
    return (q-1)*sum(j*c[N-j] for j in range(1,min(r-1,N)+1))


def graph_and_cycle(q,r,n):
    m=r-1; L=n-1
    V=[w for w in product(range(q),repeat=L) if admissible(w,r)]
    E=[w for w in product(range(q),repeat=n) if admissible(w,r)]
    count=Counter((w[:-1],w[1:]) for w in E)
    sources=[]; sinks=[]; extra=0
    inf=L-m+1
    def phi(w):
        for j in range(L-m+1):
            if w[j:j+m]==(0,)*m: return j
        return inf
    for v in V:
        source=(v[-m:]==(0,)*m and v[:m]!=(0,)*m)
        sink=(v[:m]==(0,)*m and v[-m:]!=(0,)*m)
        if source:sources.append(v)
        if sink:sinks.append(v)
    pairs=[]
    for s in sources:
        j=phi(s); assert j>0
        P=s[:j]; Q=s[j:]
        target=Q+P[::-1]
        assert target in sinks and phi(target)==0
        cur=s
        for letter in P[::-1]:
            nxt=cur[1:]+(letter,)
            assert admissible(cur+(letter,),r)
            assert phi(cur)-phi(nxt)==1
            count[(cur,nxt)]+=1
            cur=nxt; extra+=1
        assert cur==target
        pairs.append(target)
    assert len(sources)==len(sinks)==len(set(pairs))
    # Confirm all directed arcs have dual cost >= their potential difference.
    for w in E:assert phi(w[:-1])-phi(w[1:])<=1
    lower=sum(phi(v) for v in sources)
    assert extra==lower==overhead_from_gf(q,r,n)
    assert sum(count.values())==len(E)+extra
    indeg=Counter(); outdeg=Counter()
    for (u,v),num in count.items(): outdeg[u]+=num; indeg[v]+=num
    assert all(indeg[v]==outdeg[v] for v in V)
    # Hierholzer's algorithm on the augmented Eulerian directed multigraph.
    adj=defaultdict(list)
    for (u,v),num in sorted(count.items()):adj[u].extend([v]*num)
    first=V[0]; stack=[first]; tour=[]
    while stack:
        v=stack[-1]
        if adj[v]:stack.append(adj[v].pop())
        else:tour.append(stack.pop())
    tour=tour[::-1]
    assert len(tour)==len(E)+extra+1 and tour[0]==tour[-1]
    cyclic=tuple(v[-1] for v in tour[1:])
    assert len(cyclic)==len(E)+extra
    got=Counter(tuple(cyclic[(i+k)%len(cyclic)] for k in range(n)) for i in range(len(cyclic)))
    assert set(got)==set(E)
    assert all(admissible(w,r) for w in got)
    # lower bound tested against independently reconstructed imbalance
    return extra,len(E),len(sources)


if __name__=='__main__':
    cases=[(2,2,range(2,10)),(2,3,range(3,11)),(2,4,range(4,10)),
           (3,2,range(2,8)),(3,3,range(3,9)),(3,4,range(4,8)),
           (4,2,range(2,7)),(4,3,range(3,7))]
    count=0
    for q,r,ns in cases:
        outputs=[]
        for n in ns:
            x,edges,sources=graph_and_cycle(q,r,n)
            outputs.append(x)
            count+=1
        print(f'q={q}, r={r}: n={ns.start}..{ns.stop-1}, overhead={outputs}')
    # Exhaustive comparison against cycles shorter than formula at small lengths.
    for q,r,n in [(2,2,2),(2,2,3),(2,3,3),(2,3,4),(2,4,4),(3,2,2)]:
        target={w for w in product(range(q),repeat=n) if admissible(w,r)}
        opt=len(target)+overhead_from_gf(q,r,n)
        for N in range(n,opt):
            for w in product(range(q),repeat=N):
                if any(tuple(w[(i+j)%N] for j in range(r))==(0,)*r for i in range(N)):continue
                windows={tuple(w[(i+j)%N] for j in range(n)) for i in range(N)}
                assert windows!=target
        print(f'exhaustive q={q},r={r},n={n}: no covering cycle shorter than {opt}')
    print(f'CHECK_OK: {count} parameter instances; Euler tours, all windows, bijection, dual bounds, exact generating functions and short exhaustive optima')
