#!/usr/bin/env python3
"""Verify a Lucas-number cyclic covering formula for no-triple-run binary words."""
from collections import Counter, defaultdict


def fib(j):
    a,b=0,1
    for _ in range(j):a,b=b,a+b
    return a


def admissible_words(n):
    a=['']
    for i in range(n):
        a=[s+c for s in a for c in '01' if len(s)<2 or s[-2:]!=c+c]
    return a


def shortest_overlap_distance(a,b):
    n=len(a)
    return next(t for t in range(n+1) if a[t:]==b[:n-t])


def hungarian(cost):
    # Exact rectangular assignment by primal-dual potentials (square use here).
    n=len(cost)
    if not n:return 0
    u=[0]*(n+1);v=[0]*(n+1);p=[0]*(n+1);way=[0]*(n+1)
    for i in range(1,n+1):
        p[0]=i;j0=0;minv=[10**8]*(n+1);used=[False]*(n+1)
        while True:
            used[j0]=True;i0=p[j0];delta=10**8;j1=0
            for j in range(1,n+1):
                if used[j]:continue
                cur=cost[i0-1][j-1]-u[i0]-v[j]
                if cur<minv[j]:minv[j]=cur;way[j]=j0
                if minv[j]<delta:delta=minv[j];j1=j
            for j in range(n+1):
                if used[j]:u[p[j]]+=delta;v[j]-=delta
                else:minv[j]-=delta
            j0=j1
            if p[j0]==0:break
        while True:
            j1=way[j0];p[j0]=p[j1];j0=j1
            if j0==0:break
    return -v[0]


def run(k):
    n=k-1; V=admissible_words(n); W=admissible_words(k)
    incoming=Counter(e[1:] for e in W);outgoing=Counter(e[:-1] for e in W)
    deficit=[v for v in V if outgoing[v]<incoming[v]]
    surplus=[v for v in V if outgoing[v]>incoming[v]]
    assert all(abs(outgoing[v]-incoming[v])<=1 for v in V)
    assert len(deficit)==len(surplus)
    mult=Counter(W)
    seen_targets=set(); added=0
    for v in deficit:
        t=next(j for j in range(1,n-1) if v[j]==v[j+1]);s=v[t:]
        assert v[:2] in ('01','10') and v[-2:] in ('00','11')
        assert s[:2] in ('00','11')
        y='';last=s[-1]
        for i in range(t):
            last='1' if last=='0' else '0';y+=last
        w=s+y
        assert w in surplus and w not in seen_targets
        seen_targets.add(w)
        assert shortest_overlap_distance(v,w)==t
        assert min(shortest_overlap_distance(v,z) for z in surplus)==t if k<=12 else True
        added+=t; temp=v
        for letter in y:
            e=temp+letter
            assert '000' not in e and '111' not in e
            mult[e]+=1;temp=e[1:]
        assert temp==w
    assert seen_targets==set(surplus)
    assert added==2*(fib(k-1)-1)
    assert len(W)==2*fib(k+1)
    assert sum(mult.values())==2*(fib(k-1)+fib(k+1))-2
    out=defaultdict(list);ind=Counter();oud=Counter()
    for e,m in mult.items():
        for _ in range(m):out[e[:-1]].append(e[-1]);oud[e[:-1]]+=1;ind[e[1:]]+=1
    assert all(oud[v]==ind[v] for v in V)
    st=[next(v for v in V if oud[v]>0)];letters=[]
    # Hierholzer in edge-list form: vertex stack; collect final vertex order.
    ordered=[]
    while st:
        v=st[-1]
        if out[v]:
            b=out[v].pop();st.append(v[1:]+b)
        else:ordered.append(st.pop())
    ordered=ordered[::-1]
    assert len(ordered)==sum(mult.values())+1 and ordered[0]==ordered[-1]
    host=''.join(v[-1] for v in ordered[1:]);L=len(host)
    assert '000' not in host+host[:2] and '111' not in host+host[:2]
    windows=Counter((host+host[:k-1])[j:j+k] for j in range(L))
    assert all(windows[e]>=1 for e in W)
    assert windows==mult
    if k<=11:
        C=[[shortest_overlap_distance(a,b) for b in surplus] for a in deficit]
        assert hungarian(C)==added
    if k<=5:
        for length in range(len(W),L):
            for i in range(1<<length):
                z=format(i,f'0{length}b')
                wz={((z+z[:k-1])[j:j+k]) for j in range(length)}
                assert not set(W).issubset(wz)
    return len(W),len(deficit),added,L,host[:min(L,64)]

if __name__=='__main__':
    for k in range(3,19):
        a,b,c,d,host=run(k)
        print('k',k,'required',a,'imbalance_pairs',b,'overhead',c,'cycle',d,'prefix',host)
    print('VERIFY_OK exact_Lucas_cycles_k=3..18 independent_assignment_k=3..11 exhaustive_hosts_k=3..5')
