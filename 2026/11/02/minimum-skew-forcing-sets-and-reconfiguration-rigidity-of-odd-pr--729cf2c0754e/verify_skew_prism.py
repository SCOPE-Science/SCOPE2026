#!/usr/bin/env python3
"""Independent exhaustive skew-forcing and reconfiguration checks for odd prisms."""
from itertools import combinations
from collections import deque,Counter

def check(n):
    assert n >= 5 and n%2==1
    N=2*n
    def v(i,r): return 2*(i%n)+r
    adj=[set() for _ in range(N)]
    for i in range(n):
        for r in (0,1):
            s=v(i,r)
            adj[s]={v(i-1,r),v(i+1,r),v(i,1-r)}
    assert all(len(x)==3 for x in adj)
    def forcing(S):
        white=set(range(N))-set(S)
        while white:
            forced={next(iter(nb&white)) for nb in adj if len(nb&white)==1}
            if not forced: return False
            white.difference_update(forced)
        return True
    assert not forcing(())
    assert all(not forcing((u,)) for u in range(N))
    allowed={frozenset((u,w)) for u,w in combinations(range(N),2) if len(adj[u]&adj[w])>0}
    actual={frozenset((u,w)) for u,w in combinations(range(N),2) if forcing((u,w))}
    assert allowed==actual,(n,len(allowed),len(actual),allowed^actual)
    assert len(actual)==4*n
    def gdist(a,b):
        front={a}; seen={a}; d=0
        while front:
            if b in front:return d
            seen|=front
            front=set().union(*(adj[z] for z in front))-seen;d+=1
        raise ValueError('disconnected')
    assert all(gdist(*pair)==2 for pair in actual)
    Hdeg=Counter(u for pair in actual for u in pair)
    assert set(Hdeg)==set(range(N)) and set(Hdeg.values())=={4}
    nodes=list(actual); te=[set() for _ in nodes]; ts=[set() for _ in nodes]
    for i in range(len(nodes)):
        for j in range(i+1,len(nodes)):
            inter=nodes[i]&nodes[j]
            if len(inter)!=1:continue
            te[i].add(j);te[j].add(i)
            u=next(iter(nodes[i]-inter));w=next(iter(nodes[j]-inter))
            if w in adj[u]:ts[i].add(j);ts[j].add(i)
    assert all(len(x)==6 for x in te)
    def comps(A):
        seen=set(); sizes=[]
        for a in range(len(A)):
            if a in seen:continue
            todo=[a];seen.add(a);cnt=0
            while todo:
                q=todo.pop();cnt+=1
                for x in A[q]:
                    if x not in seen:seen.add(x);todo.append(x)
            sizes.append(cnt)
        return sorted(sizes)
    assert comps(te)==[4*n]
    if n==5:
        assert len([x for x in ts if len(x)==2])==10
        assert comps(ts)==[1]*10+[5,5],comps(ts)
    else:
        assert comps(ts)==[1]*(4*n)
    return (n,len(actual),sum(len(x) for x in te)//2,sum(len(x) for x in ts)//2,Counter(comps(ts)))

if __name__=='__main__':
    for n in range(5,20,2):print(check(n))
    print('VERIFY_OK')

def constructive_certificate(n):
    assert n>=5 and n%2
    def V(i,r):return (i%n,r)
    S={V(0,0),V(2,0)}
    def force(src,target):
        i,r=src
        nb={V(i-1,r),V(i+1,r),V(i,1-r)}
        assert target in nb and target not in S
        assert nb-S == {target},(n,src,target,nb-S)
        S.add(target)
    force(V(1,0),V(1,1))
    for j in range(1,n-1):
        parity=j%2
        force(V(j+1,parity),V(j+2,parity))
        force(V(1-j,parity),V(-j,parity))
    force(V(0,0),V(1,0))
    assert len(S)==2*n
if __name__=='__main__':
    for n in range(5,300,2):constructive_certificate(n)
    print('CONSTRUCTIVE_CERTIFICATES_OK')
