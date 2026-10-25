from functools import lru_cache
from itertools import permutations
from math import gcd

def graph(n,l):
    # index t*(2*n)+s*n+i
    N=(l+1)*2*n+1
    edges=set()
    def ix(t,s,i):return t*2*n+s*n+i
    def add(a,b):
        if a!=b:edges.add((min(a,b),max(a,b)))
    for t in range(l):
        for i in range(n):
            for j in range(n):
                if i!=j:
                    add(ix(t,0,i),ix(t+1,1,j));add(ix(t,1,i),ix(t+1,0,j))
    for i in range(n):
        for j in range(n):
            if i!=j: add(ix(l,0,i),ix(l,1,j))
    for s in range(2):
        for i in range(n):add(N-1,ix(0,s,i))
    return N,edges

def inv_orbits(n,l,p,tau):
    N, edges=graph(n,l)
    def g(a):
        if a==N-1:return a
        t,si=divmod(a,2*n);s,i=divmod(si,n)
        return t*(2*n)+(s^tau)*n+p[i]
    unseen=set(range(N));groups=[]; orbitid={}
    while unseen:
        x=min(unseen);v=x;group=[]
        while v in unseen:
            unseen.remove(v);group.append(v);v=g(v)
        assert v==x
        for a in group:orbitid[a]=len(groups)
        groups.append(group)
    M=len(groups);forbidden=set();adj=[0]*M
    for a,b in edges:
        u,v=orbitid[a],orbitid[b]
        if u==v: forbidden.add(u)
        else:adj[u]|=1<<v;adj[v]|=1<<u
    mask=sum(1<<i for i in range(M) if i not in forbidden)
    @lru_cache(maxsize=None)
    def poly(mask):
        if mask==0:return 1
        # choose max degree vertex
        x=max((i for i in range(M) if mask>>i&1),key=lambda i:(adj[i]&mask).bit_count())
        return poly(mask&~(1<<x))-poly(mask&~(1<<x)&~adj[x])
    return poly(mask),M,poly.cache_info()

def expect(n,l,p,tau):
    f=sum(x==p[x] for x in range(n));f2=sum(x==p[p[x]] for x in range(n));u=f-1;v=f2-1
    k,r=divmod(l,3)
    if not tau:
        if r==0:return u**(2*k+1)-u**(2*k)
        if r==1:return -u**(2*k+1)
        return u**(2*k+2)
    if r==0:return -f*v**k
    if r==1:return u*v**k
    return v**(k+1)

from collections import defaultdict
from itertools import combinations

def faces(n,l):
    N,edges=graph(n,l)
    forb=[0]*N
    for a,b in edges:forb[a]|=1<<b;forb[b]|=1<<a
    result=defaultdict(list)
    def rec(face,possible):
        if face:result[len(face)-1].append(face)
        while possible:
            lb=possible&-possible;x=lb.bit_length()-1;possible-=lb
            rec(face+(x,),possible&~forb[x])
    rec((),(1<<N)-1)
    return result

def homology(n,l):
    dd=faces(n,l)
    print('n',n,'l',l,'fvector',[(d,len(dd[d])) for d in sorted(dd)],flush=True)
    ranks={}
    for d in sorted(dd):
        if d==0:ranks[d]=0;continue
        idx={s:i for i,s in enumerate(dd[d-1])}
        pivot={}
        for f in dd[d]:
            col=0
            for k in range(len(f)):
                col^=1<<idx[f[:k]+f[k+1:]]
            while col:
                i=col.bit_length()-1
                if i not in pivot:pivot[i]=col;break
                col^=pivot[i]
        ranks[d]=len(pivot)
    betti={d:len(dd[d])-ranks[d]-ranks.get(d+1,0) for d in sorted(dd)}
    betti[0]-=1
    print('reduced F2 betti',betti,flush=True)
    return betti


def integer_partitions(total, low=1):
    if total==0:
        yield []
    else:
        for first in range(low,total+1):
            for tail in integer_partitions(total-first,first):
                yield [first]+tail

def cycle_representative(parts):
    out=[]; start=0
    for size in parts:
        out.extend([start+i+1 for i in range(size-1)]+[start]); start+=size
    return tuple(out)

def run_all():
    checks=0
    for n in (3,4,5):
        for ell in range(6):
            for part in integer_partitions(n):
                perm=cycle_representative(part)
                for exchange in (0,1):
                    got,_,_=inv_orbits(n,ell,perm,exchange)
                    target=expect(n,ell,perm,exchange)
                    assert got==target, (n,ell,part,exchange,got,target)
                    checks+=1
    assert checks==180
    print('PASS 180 orbit-independence/equivariant-Euler checks')
    expected={(3,0):{0:1,1:2},(3,1):{2:2},(3,2):{3:4},
             (3,3):{4:4,5:8},(4,0):{0:1,1:3},(4,1):{2:3}}
    for (n,ell),nonzero in expected.items():
        result=homology(n,ell)
        assert {degree:rank for degree,rank in result.items() if rank}==nonzero
    print('PASS 6 mod-two homology vectors')

if __name__=='__main__':
    run_all()
