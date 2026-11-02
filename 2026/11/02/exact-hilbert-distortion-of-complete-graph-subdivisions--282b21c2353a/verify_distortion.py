#!/usr/bin/env python3
"""Exact arithmetic checks for the Hilbert distortion of a complete-graph subdivision.

No third-party modules are required. This checks a finite set of orders and
identities; the all-orders lower bound is mathematical, not computational.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
from collections import deque

@dataclass(frozen=True)
class K:
    """Element a+b*sqrt(19) of Q(sqrt(19))."""
    a: F
    b: F = F(0)
    def __add__(self, other):
        other = as_k(other)
        return K(self.a+other.a, self.b+other.b)
    __radd__ = __add__
    def __neg__(self): return K(-self.a,-self.b)
    def __sub__(self, other): return self+(-as_k(other))
    def __rsub__(self, other): return as_k(other)-self
    def __mul__(self, other):
        other = as_k(other)
        return K(self.a*other.a+19*self.b*other.b, self.a*other.b+self.b*other.a)
    __rmul__ = __mul__
    def sign(self):
        a,b=self.a,self.b
        if a==0: return (b>0)-(b<0)
        if b==0 or (a>0)==(b>0): return (a>0)-(a<0)
        delta=a*a-19*b*b
        if delta==0: return 0
        return (1 if a>0 else -1)*(1 if delta>0 else -1)
    def __ge__(self, other): return (self-as_k(other)).sign()>=0
    def __le__(self, other): return (self-as_k(other)).sign()<=0
    def __eq__(self, other):
        other=as_k(other)
        return self.a==other.a and self.b==other.b

def as_k(x):
    if isinstance(x,K): return x
    return K(F(x))

def sqnorm(a): return sum((v*v for v in a), as_k(0))

def points(n):
    if n==3:
        # The common sqrt(27/8) factor is applied to squared distances.
        alpha=as_k(1); beta=as_k(1); factor=as_k(F(27,8)); bound=as_k(F(9,4))
    elif n==4:
        alpha=K(F(-4,3),F(2,3)); beta=as_k(2)
        factor=as_k(1); bound=K(F(43,3),F(-8,3))
    else:
        alpha=as_k(F(2*(n-2),n-1)); beta=as_k(2)
        factor=as_k(1); bound=as_k(F(4*(n-2),n-1))
    ans={}
    for i in range(n):
        ans[(i,)]=tuple(alpha*(F(1 if j==i else 0)-F(1,n)) for j in range(n))
    for i,j in combinations(range(n),2):
        ans[(i,j)]=tuple(beta*(F(int(k in (i,j)))-F(2,n)) for k in range(n))
    return ans,factor,bound

def shortest_paths(n):
    verts=[(i,) for i in range(n)]+list(combinations(range(n),2))
    adj={s:set() for s in verts}
    for i,j in combinations(range(n),2):
        adj[(i,)].add((i,j));adj[(j,)].add((i,j))
        adj[(i,j)].add((i,));adj[(i,j)].add((j,))
    for start in verts:
        d={start:0};todo=deque([start])
        while todo:
            u=todo.popleft()
            for v in adj[u]:
                if v not in d:
                    d[v]=d[u]+1;todo.append(v)
        assert len(d)==len(verts)
        for v in verts:
            assert d[v]==len(set(start)^set(v))

counts={}; tests=0
for n in range(3,12):
    coordinates,factor,bound=points(n)
    for i,(s,vec) in enumerate(coordinates.items()):
        for t,w in list(coordinates.items())[i+1:]:
            graphdist=len(set(s)^set(t))
            sq=factor*sqnorm([a-b for a,b in zip(vec,w)])
            assert sq>=graphdist*graphdist, (n,s,t,'lower',sq)
            assert sq<=bound*graphdist*graphdist, (n,s,t,'upper',sq)
            tests+=2
    if n<=10: shortest_paths(n)
    counts[n]=len(coordinates)
# Check the exceptional algebraic formula against the critical polynomial.
c=K(F(-8,3),F(4,3))
assert as_k(3)*c*c+as_k(16)*c-as_k(80)==as_k(0)
assert as_k(9)-as_k(2)*c==K(F(43,3),F(-8,3))
# Complete all-order normalized distance identities are in the written proof.
print('CHECK_OK orders=3..11 pairwise_exact_inequalities=',tests,
      'bfs_orders=3..10 algebraic_n4=Q(sqrt(19))')
