"""Independent finite checks for minimum robust dominating-set reconfiguration on crown graphs."""
from itertools import combinations
from collections import deque
from math import comb
from crown_conn_check import kappa, direct_dom

def checked(n,k):
    adj=[0]*(2*n)
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i] |= 1<<(n+j)
                adj[n+j] |= 1<<i
    feasible=[]
    for a in range(1<<n):
        for b in range(1<<n):
            mask=a|(b<<n)
            if direct_dom(n,a,b) and kappa(mask,adj)>=k:
                feasible.append((a,b))
    minim=min((a.bit_count()+b.bit_count()) for a,b in feasible)
    vertices={p for p in feasible if p[0].bit_count()+p[1].bit_count()==minim}
    if n>=2*k:
        exp_min=2*k; exp_n=comb(n,k)*comb(n-k,k)
    else:
        exp_min=2*k+2; exp_n=comb(n,k+1)**2
    assert minim==exp_min and len(vertices)==exp_n, ('min-count',n,k,minim,exp_min,len(vertices),exp_n)
    neighbors={p:set() for p in vertices}
    for a,b in vertices:
        for d in range(2):
            old=a if d==0 else b
            other=b if d==0 else a
            for i in range(n):
                if not old>>i&1: continue
                for j in range(n):
                    if old>>j&1: continue
                    new=old^(1<<i)^(1<<j)
                    q=(new,other) if d==0 else (other,new)
                    if q in vertices:neighbors[a,b].add(q)
        # All potential cross-side token jumps are checked separately for absence of missing legal adjacencies.
        for d in range(2):
            old=a if d==0 else b
            other=b if d==0 else a
            for i in range(n):
                if not old>>i&1: continue
                for j in range(n):
                    if other>>j&1:continue
                    q=(old^(1<<i), other|(1<<j)) if d==0 else (other|(1<<j),old^(1<<i))
                    assert q not in vertices,('cross-side legal',n,k,(a,b),q)
    assert all(p in neighbors[q] for q,ss in neighbors.items() for p in ss)
    seen=set(); components=0
    for p in vertices:
        if p in seen: continue
        components+=1;queue=deque([p]);seen.add(p)
        while queue:
            for q in neighbors[queue.popleft()]:
                if q not in seen:seen.add(q);queue.append(q)
    exp_components=comb(n,k) if n==2*k else 1
    exp_degree= 2*k*(n-2*k) if n>=2*k else 2*(k+1)*(n-k-1)
    assert components==exp_components, ('components',n,k,components,exp_components)
    assert all(len(x)==exp_degree for x in neighbors.values()),('degrees',n,k,exp_degree,sorted(set(map(len,neighbors.values()))))
    return len(feasible),len(vertices),components,exp_degree

if __name__=='__main__':
    rows=[]
    for n in range(3,7):
        for k in range(2,n):
            rows.append((n,k,*checked(n,k)))
    print('VERIFICATION_OK profiles='+str(len(rows))+' minimum_configs='+str(sum(r[3] for r in rows)))
    for r in rows:print('n=%d k=%d feasible=%d minima=%d components=%d degree=%d'%r)
