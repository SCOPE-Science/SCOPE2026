#!/usr/bin/env python3
"""Independent finite checks for the binary edge-granulation spectrum theorem.
No external dependencies. Run: python verify_edge_observation.py
"""
from collections import Counter
from itertools import combinations
import random


def components(n, edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    seen=set(); blocks=[]
    for v in range(n):
        if v in seen: continue
        todo=[v]; seen.add(v); comp=[]; color={v:0}; bip=True
        while todo:
            x=todo.pop(); comp.append(x)
            for y in adj[x]:
                if y not in color: color[y]=1-color[x]
                elif color[y]==color[x]: bip=False
                if y not in seen:
                    seen.add(y); todo.append(y)
        blocks.append((len(comp),bip))
    return blocks


def observation_fibers(n, edges):
    f=Counter()
    for mask in range(1<<n):
        key=tuple(((mask>>a)&1)+((mask>>b)&1) for a,b in edges)
        # 0=both endpoints absent, 1=one present, 2=both present
        f[key]+=1
    return f


def poly_mul(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q): out[i+j]+=x*y
    return out


def formula_poly(n, edges):
    blocks=components(n,edges)
    s=sum(v==1 for v,_ in blocks)
    u=sum(v for v,b in blocks if v>=2 and not b)
    bip_sizes=sorted(v for v,b in blocks if v>=2 and b)
    p=[1]
    for v in bip_sizes: p=poly_mul(p,[2**v-2,1])
    return [0]*s + [2**u*x for x in p], (s,u,tuple(bip_sizes))


def observed_poly(n,edges):
    fibers=observation_fibers(n,edges)
    counts=Counter(fibers.values())
    assert all(k>0 and k&(k-1)==0 for k in counts)
    degrees={k.bit_length()-1:v for k,v in counts.items()}
    return [degrees.get(k,0) for k in range(max(degrees)+1)]


def recover(poly):
    s=next(i for i,v in enumerate(poly) if v)
    c=poly[s:]; k=c[-1]
    assert k&(k-1)==0
    u=k.bit_length()-1
    assert all(v%k==0 for v in c)
    c=[v//k for v in c]
    total=sum(v*(2**i) for i,v in enumerate(poly))
    assert total>0 and total&(total-1)==0
    n=total.bit_length()-1
    found=[]
    while len(c)>1:
        for v in range(2,n+1):
            a=2**v-2
            d=len(c)-1
            q=[0]*d
            q[d-1]=c[d]
            for j in range(d-1,0,-1): q[j-1]=c[j]-a*q[j]
            if c[0]==a*q[0]:
                found.append(v); c=q; break
        else: raise AssertionError('linear factor not found')
    assert c==[1] and n==s+u+sum(found)
    return (s,u,tuple(sorted(found)))


def check(n,edges):
    predicted,sig=formula_poly(n,edges)
    actual=observed_poly(n,edges)
    assert actual==predicted,(n,edges,actual,predicted)
    assert recover(actual)==sig,(n,edges,recover(actual),sig)
    fibers=observation_fibers(n,edges)
    assert sum(fibers.values())==2**n
    assert len(fibers)==sum(actual)
    assert max(fibers.values())==2**(sig[0]+len(sig[2]))
    assert sum(v==max(fibers.values()) for v in fibers.values())==2**sig[1]


def main():
    tested=0
    for n in range(1,7):
        all_edges=list(combinations(range(n),2))
        for bits in range(1<<len(all_edges)):
            ed=[e for i,e in enumerate(all_edges) if bits>>i&1]
            check(n,ed); tested+=1
        print('ALL_GRAPHS',n,1<<len(all_edges),'PASS')
    rng=random.Random(20261017)
    for n in (7,8,9):
        all_edges=list(combinations(range(n),2))
        for _ in range(250):
            ed=[e for e in all_edges if rng.randrange(2)]
            check(n,ed); tested+=1
        print('SAMPLED_GRAPHS',n,250,'PASS')
    # Sharp rank-two boundary: one size-three hyperedge has 1,6,1 fibers.
    ternary=Counter()
    for mask in range(8):
        count=mask.bit_count()
        ternary[0 if count==0 else 2 if count==3 else 1]+=1
    assert sorted(ternary.values())==[1,1,6]
    print('VERIFY_OK graphs',tested,'fiber_enumerator=PASS','inverse_recovery=PASS','rank3_boundary=PASS')

if __name__=='__main__': main()
