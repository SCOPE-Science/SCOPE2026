#!/usr/bin/env python3
"""Standard-library validation of forbidden-four-factor cyclic-cover certificates.
Run: python3 verify.py certificates.json
Verifies every primal/dual integer inequality and explicitly constructs a cyclic cover.
"""
import json, sys
from collections import defaultdict

PATTERNS=('0000','0001','0010','0011','0101','0110')
ORDERS=range(4,16)

def reachable(start, adjacency):
    seen={start};stack=[start]
    while stack:
        for v in adjacency.get(stack.pop(), ()):
            if v not in seen:
                seen.add(v);stack.append(v)
    return seen

def check(c):
    n=c['n'];pat=c['pattern'];N=1<<(n-1);mask=N-1
    assert type(n)==int and n in ORDERS and pat in PATTERNS
    assert len(c['potential'])==N and all(type(z)==int for z in c['potential'])
    p=c['potential'];b=[0]*N;count={};A={};adj=defaultdict(set);rev=defaultdict(set)
    banned=int(pat,2);required=0
    # Enumerate all binary n-words from the definition (including transient words).
    for w in range(1<<n):
        ww=w;has_forbidden=False
        for _ in range(n-3):
            if (ww & 15)==banned:
                has_forbidden=True;break
            ww>>=1
        if not has_forbidden:
            u=w>>1;v=w&mask;bit=w&1
            assert v==(((u<<1)|bit)&mask)
            count[(u,bit)]=1
            b[u]+=1;b[v]-=1;required+=1
            adj[u].add(v);rev[v].add(u)
    assert required==c['required']
    cost=0
    for row in c['added_edges']:
        assert type(row)==list and len(row)==3
        u,bit,m=row
        assert all(type(t)==int for t in row) and 0<=u<N and bit in (0,1) and m>0
        assert (u,bit) not in A
        A[(u,bit)]=m;cost+=m
        v=((u<<1)|bit)&mask
        count[(u,bit)]=count.get((u,bit),0)+m
        b[u]+=m;b[v]-=m
        adj[u].add(v);rev[v].add(u)
    assert cost==c['additional']
    assert all(t==0 for t in b), (n,pat,'unbalanced')
    # All nonisolated vertices lie in a single strongly connected component.
    active=set(adj)|set(rev)
    start=next(iter(active))
    assert reachable(start,adj)==active and reachable(start,rev)==active
    # Rebuild mandatory imbalance and certify the dual bound from scratch.
    b0=[0]*N
    for (u,bit),mult in count.items():
        v=((u<<1)|bit)&mask
        if (u,bit) in A:mult-=A[(u,bit)]
        b0[u]+=mult;b0[v]-=mult
    for u in range(N):
        for bit in (0,1):
            v=((u<<1)|bit)&mask
            assert p[v]-p[u]<=1, (n,pat,u,bit,'dual infeasible')
    assert sum(x*y for x,y in zip(b0,p))==cost, (n,pat,'dual mismatch')
    # Deterministic Eulerian traversal; emitted bits themselves form a witness.
    edges={u:[[bit,count[(u,bit)]] for bit in (0,1) if count.get((u,bit),0)] for u in active}
    choices={u:0 for u in active};stack=[(start,None)];labels=[]
    while stack:
        u=stack[-1][0];opts=edges[u];j=choices[u]
        while j<len(opts) and opts[j][1]==0:j+=1
        choices[u]=j
        if j==len(opts):
            _,incoming=stack.pop()
            if incoming is not None:labels.append(incoming)
        else:
            bit=opts[j][0];opts[j][1]-=1
            stack.append(((((u<<1)|bit)&mask),bit))
    labels.reverse();assert len(labels)==required+cost
    assert all(v[1]==0 for pairs in edges.values() for v in pairs)
    # The labels of consecutive Euler edges give all prescribed n-windows.
    bits=''.join(map(str,labels));L=len(bits)
    observed={int(''.join(bits[(i+j)%L] for j in range(n)),2) for i in range(L)}
    for w in range(1<<n):
        ww=w;bad=False
        for _ in range(n-3):
            if (ww&15)==banned:bad=True;break
            ww>>=1
        if not bad:assert w in observed,(n,pat,'missing window',w)
    return required,required+cost

def main(path):
    with open(path,encoding='utf-8') as f:data=json.load(f)
    assert set(data['forbidden_patterns'])==set(PATTERNS)
    assert data['window_orders']==list(ORDERS)
    assert len(data['cases'])==len(PATTERNS)*len(ORDERS)
    seen=set()
    for c in data['cases']:
        key=(c['n'],c['pattern']);assert key not in seen;seen.add(key)
        r,L=check(c)
        print(c['n'],c['pattern'],r,L)
    assert seen=={(n,p) for n in ORDERS for p in PATTERNS}
    print('VERIFY_OK',len(seen),'exact optima')

if __name__=='__main__':
    assert len(sys.argv)==2
    main(sys.argv[1])
