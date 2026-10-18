"""Exact certificates for protected-vertex residual connectivity on small habitat trees.

Only Python 3 and SymPy are needed. Run: python verify.py
"""
from itertools import product
from heapq import heappush, heappop
from collections import defaultdict
import sympy as sp

x=sp.symbols('x')

def from_prufer(code,n):
    deg=[1]*n
    for v in code: deg[v]+=1
    h=[]
    for v in range(n):
        if deg[v]==1: heappush(h,v)
    E=[]
    for v in code:
        u=heappop(h);E.append((min(u,v),max(u,v)))
        deg[u]-=1;deg[v]-=1
        if deg[v]==1: heappush(h,v)
    u=heappop(h);v=heappop(h);E.append((min(u,v),max(u,v)))
    return tuple(sorted(E))

def canonical(E,n):
    adj=[[] for _ in range(n)]
    for u,v in E:adj[u].append(v);adj[v].append(u)
    def rooted(u,par):
        return '('+''.join(sorted(rooted(v,u) for v in adj[u] if v!=par))+')'
    return min(rooted(u,-1) for u in range(n))

def tree_classes(n):
    d={}
    for seq in product(range(n),repeat=max(0,n-2)):
        E=from_prufer(seq,n)
        can=canonical(E,n)
        if can not in d:d[can]=E
    return d

def poly_root(E,n):
    adj=[0]*n
    for u,v in E:adj[u]|=1<<v;adj[v]|=1<<u
    counts=[[0]*(n+1) for v in range(n)]
    for subset in range(1,1<<n):
        reached=subset&-subset;todo=reached
        while todo:
            u=(todo&-todo).bit_length()-1;todo&=todo-1
            fresh=adj[u]&subset&~reached
            reached|=fresh;todo|=fresh
        if reached==subset:
            k=subset.bit_count()
            for v in range(n):
                if subset>>v &1:counts[v][k]+=1
    return [sp.Poly(sum(z*x**(k-1)*(1-x)**(n-k) for k,z in enumerate(row) if k),x) for row in counts]

def strict_sign(poly,a=0,b=1):
    if poly.is_zero:return 0
    # Delete only zeroes at the OPEN interval's endpoints; then Sturm counts interior roots.
    q=poly
    for endpoint in (a,b):
        while q.eval(endpoint)==0:
            q=q.exquo(sp.Poly(x-endpoint,x))
    if q.count_roots(a,b):return None
    z=poly.eval((a+b)/2)
    return 1 if z>0 else -1 if z<0 else None

def universal_sites(P):
    n=len(P)
    return [v for v in range(n) if all(strict_sign(P[v]-P[u]) in (0,1) for u in range(n))]

expected_counts={2:1,3:1,4:2,5:3,6:6,7:11}
exceptions=[]
for n in range(2,8):
    d=tree_classes(n)
    assert len(d)==expected_counts[n],(n,len(d))
    for can,E in d.items():
        P=poly_root(E,n)
        winners=universal_sites(P)
        if not winners:exceptions.append((n,can,E))
    print('n=',n,'unlabelled=',len(d),'nonuniform_so_far=',len(exceptions))
assert len(exceptions)==2 and {n for n,c,E in exceptions}=={7},exceptions

A=((0,1),(0,4),(1,2),(2,3),(4,5),(4,6))
B=((0,1),(0,4),(1,2),(1,3),(4,5),(4,6))
assert {c for n,c,E in exceptions}=={canonical(A,7),canonical(B,7)}

# Exact analytic envelope certificates in 7-node exceptions:
PA=poly_root(A,7)
assert sp.factor((PA[0]-PA[4]).as_expr())== -x*(x-1)**3*(2*x-1)
for v in (1,2,3,5,6):assert strict_sign(PA[0]-PA[v])==1
# Subdivide at x=1/2 to certify winner 4 at low and winner 0 at high.
for v in range(7):
    assert strict_sign(PA[4]-PA[v],sp.Rational(0),sp.Rational(1,2)) in (0,1)
    assert strict_sign(PA[0]-PA[v],sp.Rational(1,2),sp.Rational(1)) in (0,1)

PB=poly_root(B,7)
assert PB[1]==PB[4]
assert sp.factor((PB[0]-PB[1]).as_expr())==x*(x-1)**3*(x*x-3*x+1)
for v in (2,3,5,6):
    assert strict_sign(PB[0]-PB[v])==1
    assert strict_sign(PB[1]-PB[v])==1
r=(sp.Integer(3)-sp.sqrt(5))/2
for v in range(7):
    # Endpoint r is algebraic; use the exact sign decomposition of 0 versus 1.
    if v not in (0,1,4):
        assert strict_sign(PB[0]-PB[v])==1
        assert strict_sign(PB[1]-PB[v])==1
assert r>0 and r<1
print('Seven-site exceptions: (A) threshold 1/2; (B) threshold (3-sqrt(5))/2.')
print('A difference',sp.factor((PA[0]-PA[4]).as_expr()))
print('B difference',sp.factor((PB[0]-PB[1]).as_expr()))
print('PROTECTED_TREE_RELIABILITY_VERIFY_OK')
