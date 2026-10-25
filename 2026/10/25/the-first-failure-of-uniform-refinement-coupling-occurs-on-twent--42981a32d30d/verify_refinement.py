"""Exact, dependency-free certificate for uniform partition-refinement coupling cutoff.

For each n<=19 and adjacent block counts k,k+1, an integer max-flow on
block-size profiles proves the existence of a uniform refinement coupling.
For n=20,k=2, a rational Hall inequality forbids such a coupling.
"""
from functools import lru_cache
from collections import Counter, deque
from math import factorial, lcm, comb

@lru_cache(maxsize=None)
def integer_partitions(n, top=None):
    if top is None: top=n
    if n==0:return ((),)
    return tuple((j,)+tail for j in range(min(n,top),0,-1)
                 for tail in integer_partitions(n-j,j))

@lru_cache(maxsize=None)
def orbit_size(shape):
    denom=1
    for size,multiplicity in Counter(shape).items():
        denom*=factorial(size)**multiplicity*factorial(multiplicity)
    return factorial(sum(shape))//denom

def one_splits(shape):
    answers=set()
    for size in set(shape):
        rest=list(shape)
        rest.remove(size)
        for x in range(1,size//2+1):
            answers.add(tuple(sorted(rest+[x,size-x],reverse=True)))
    return answers

class Dinic:
    def __init__(self,n):
        self.g=[[] for _ in range(n)]
    def add(self,u,v,capacity):
        a=[v,int(capacity),len(self.g[v])]
        b=[u,0,len(self.g[u])]
        self.g[u].append(a);self.g[v].append(b)
    def run(self,s,t):
        n=len(self.g);ans=0
        while True:
            lvl=[-1]*n;lvl[s]=0;q=deque([s])
            while q:
                u=q.popleft()
                for v,c,_ in self.g[u]:
                    if c and lvl[v]<0:lvl[v]=lvl[u]+1;q.append(v)
            if lvl[t]<0:return ans
            ptr=[0]*n
            def dfs(u,f):
                if u==t:return f
                while ptr[u]<len(self.g[u]):
                    e=self.g[u][ptr[u]];v,c,rev=e
                    if c and lvl[v]==lvl[u]+1:
                        send=dfs(v,min(f,c))
                        if send:
                            e[1]-=send;self.g[v][rev][1]+=send;return send
                    ptr[u]+=1
                return 0
            while True:
                pushed=dfs(s,10**200)
                if not pushed:break
                ans+=pushed

def check(n,k):
    partitions=integer_partitions(n)
    left=[p for p in partitions if len(p)==k]
    right=[p for p in partitions if len(p)==k+1]
    sz_left=sum(map(orbit_size,left));sz_right=sum(map(orbit_size,right))
    cap=lcm(sz_left,sz_right)
    A=len(left);B=len(right);source=A+B;sink=source+1
    network=Dinic(sink+1)
    for i,p in enumerate(left):network.add(source,i,orbit_size(p)*(cap//sz_left))
    index={p:i for i,p in enumerate(right)}
    for j,p in enumerate(right):network.add(A+j,sink,orbit_size(p)*(cap//sz_right))
    for i,p in enumerate(left):
        for q in one_splits(p):network.add(i,A+index[q],cap)
    return network.run(source,sink)==cap

def run():
    assert orbit_size((10,10))==92378
    assert sum(orbit_size(p) for p in integer_partitions(20) if len(p)==2)==524287
    assert sum(orbit_size(p) for p in integer_partitions(20) if len(p)==3)==580606446
    neighbors=one_splits((10,10))
    assert neighbors=={(10,9,1),(10,8,2),(10,7,3),(10,6,4),(10,5,5)}
    assert sum(orbit_size(p) for p in neighbors)==94410316
    assert 92378*580606446>94410316*524287
    checked=0
    for n in range(2,20):
        for k in range(1,n):
            assert check(n,k),(n,k)
            checked+=1
    assert not check(20,2)
    print('PASS',checked,'exact feasible adjacent couplings for n<=19; exact obstruction for n=20,k=2')

if __name__=='__main__':run()
