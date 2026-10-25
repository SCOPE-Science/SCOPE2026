#!/usr/bin/env python3
"""Reproducibility checks for a density obstruction to three-state excitation.

All arithmetic is integer or Fraction arithmetic. This program is not part
of the proof of the all-graph theorem, which follows from event matching.
"""
from fractions import Fraction
from itertools import product


def graph(n, edges):
    ee = sorted(set(tuple(sorted(edge)) for edge in edges))
    assert all(0 <= a < b < n for a, b in ee)
    adj = [set() for _ in range(n)]
    for a,b in ee:
        adj[a].add(b)
        adj[b].add(a)
    return n, ee, tuple(tuple(sorted(a)) for a in adj)


def path(n):
    return graph(n, ((i,i+1) for i in range(n-1)))


def cycle(n):
    return graph(n, ((i,(i+1)%n) for i in range(n)))


def wheel(n):
    return graph(n+1, list((i,(i+1)%n) for i in range(n)) + [(n,i) for i in range(n)])


def prism(n):
    return graph(2*n, [(i,(i+1)%n) for i in range(n)] +
                 [(n+i,n+(i+1)%n) for i in range(n)] +
                 [(i,n+i) for i in range(n)])


def clique(n):
    return graph(n, ((i,j) for i in range(n) for j in range(i+1,n)))


def biclique(a,b):
    return graph(a+b, ((i,a+j) for i in range(a) for j in range(b)))


def alpha(g):
    n, edges, _ = g
    ans = Fraction(0)
    for mask in range(1,1<<n):
        e = sum(bool(mask & (1<<a)) and bool(mask & (1<<b)) for a,b in edges)
        ans = max(ans, Fraction(e,mask.bit_count()))
    return ans


def step(g, s, q):
    n,_, adj = g
    return tuple(2 if s[i]==1 else 0 if s[i]==2 else
                 int(sum(s[j]==1 for j in adj[i])>=q) for i in range(n))


def trajectory(g, s, q):
    states=[s]; seen={s}
    while states[-1] != (0,)*len(s):
        nxt=step(g,states[-1],q)
        assert nxt not in seen, 'unexpected nonzero period'
        states.append(nxt);seen.add(nxt)
    return states


def check_events(g, states, q):
    n,edges,_=g
    T=len(states)-1
    times=[[t for t,s in enumerate(states) if s[v]==1] for v in range(n)]
    N=sum(len(ts) for ts in times)
    m=sum(v==1 for v in states[0])
    assert all(b-a>=3 for ts in times for a,b in zip(ts,ts[1:]))
    transmissions=0
    for u,v in edges:
        e_trans=[]
        for t in range(1,T+1):
            if states[t-1][u]==1 and states[t][v]==1: e_trans.append(((u,t-1),(v,t)))
            if states[t-1][v]==1 and states[t][u]==1: e_trans.append(((v,t-1),(u,t)))
        endpoints=[x for pair in e_trans for x in pair]
        assert len(endpoints)==len(set(endpoints))
        assert len(e_trans)<=min(len(times[u]),len(times[v]))
        transmissions+=len(e_trans)
    assert q*(N-m) <= transmissions
    return N,m


def check_family(name, g, q):
    a=alpha(g)
    assert a<q,(name,q,a)
    limit=Fraction(q,q-a)
    mx_ratio=Fraction(0)
    mx_depth=0
    count=0
    for s in product(range(3),repeat=g[0]):
        hist=trajectory(g,s,q)
        N,m=check_events(g,hist,q)
        assert N<=limit*m,(name,s,N,m,limit)
        assert len(hist)-1 <= (limit*m).__floor__()+1
        if m:mx_ratio=max(mx_ratio,Fraction(N,m))
        mx_depth=max(mx_depth,len(hist)-1)
        count+=1
    print(f'{name}, q={q}, n={g[0]}, alpha={a}, states={count}, max_events_per_seed={mx_ratio}, max_extinction_step={mx_depth}')
    return count


def critical(q):
    g=biclique(2*q,2*q)
    assert alpha(g)==q
    # Left classes A0,A1 of size q, right classes B0,B1 of size q.
    x=tuple([1]*q+[0]*q+[0]*q+[2]*q)
    v=x
    for t in range(4):
        v=step(g,v,q)
        assert v != x if t<3 else v==x
    print(f'critical q={q}, graph=K_{2*q},{2*q}, density={alpha(g)}, nonzero_period=4')


def main():
    total=0
    for name,g,q in [
        ('path5',path(5),2),('cycle5',cycle(5),2),
        ('wheel4',wheel(4),2),('wheel6',wheel(6),2),
        ('prism3',prism(3),2),('star7',biclique(1,7),2),
        ('clique4',clique(4),2),('clique6',clique(6),3),
        ('path5_threshold1',path(5),1),
    ]:
        total+=check_family(name,g,q)
    for q in (1,2,3): critical(q)
    print('EXHAUSTIVE_CONFIGURATIONS',total)
    print('VERIFICATION_OK')

if __name__=='__main__': main()
