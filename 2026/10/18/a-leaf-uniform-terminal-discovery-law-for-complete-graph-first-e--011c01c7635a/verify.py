#!/usr/bin/env python3
"""Finite, independent, exact-rational checks for leaf-refined order mass."""
import itertools, math

def trees(n):
    # Cayley trees from Prufer words; fixed root=0.
    if n==2:
        yield [-1,0];return
    for code in itertools.product(range(n), repeat=n-2):
        deg=[1]*n
        for x in code:deg[x]+=1
        edges=[]
        for x in code:
            v=next(i for i,d in enumerate(deg) if d==1)
            edges.append((v,x));deg[v]-=1;deg[x]-=1
        a,b=[i for i,d in enumerate(deg) if d==1];edges.append((a,b))
        adj=[[] for _ in range(n)]
        for a,b in edges:adj[a].append(b);adj[b].append(a)
        p=[-2]*n;p[0]=-1;seen=[0]
        for x in seen:
            for y in adj[x]:
                if p[y]==-2:p[y]=x;seen.append(y)
        yield p

def expand(p,order):
    emitted={0};out=[]
    for x in order:
        chain=[];y=x
        while y not in emitted:
            chain.append(y);y=p[y]
        for y in reversed(chain):
            emitted.add(y);out.append(y)
    return tuple(out)

def test(p):
    n=len(p);k=n-1
    leaves=[v for v in range(1,n) if v not in p[1:]]
    image={};total={v:0 for v in leaves}
    for perm in itertools.permutations(range(1,n)):
        tau=expand(p,perm)
        image[tau]=image.get(tau,0)+1
        assert tau[-1] in leaves
        assert tau[-1]==next(v for v in reversed(perm) if v in leaves)
    for tau,fiber in image.items():
        w=math.prod(k-i for i in range(k-1) if p[tau[i+1]]==tau[i])
        assert fiber==w, (p,tau,fiber,w)
        total[tau[-1]]+=fiber
    assert set(total.values())=={math.factorial(k)//len(leaves)}
    assert sum(total.values())==math.factorial(k)

if __name__=='__main__':
    cases=0
    for n in range(2,7):
        for p in trees(n):test(p);cases+=1
    print('PASS:',cases,'rooted labeled trees, exact expansion fibers and uniform terminal leaves')
