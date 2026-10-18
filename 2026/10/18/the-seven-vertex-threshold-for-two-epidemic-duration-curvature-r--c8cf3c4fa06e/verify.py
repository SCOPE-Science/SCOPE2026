"""Exact rooted-tree Reed--Frost duration-curvature census, through seven vertices.

Dependencies: Python >=3.9 and SymPy >=1.10. Standard-library Prüfer enumeration
and independent mask enumeration supply an exhaustive certificate.
Run: python verify.py [optional_output_csv_path]
"""
from __future__ import annotations
import itertools
import collections
import math
import sys
import csv
from sympy import Poly, symbols, Integer

p = symbols('p')

def decode_prufer(seq):
    """Independent construction of every labeled tree on 2..7 vertices."""
    n=len(seq)+2
    d=[1]*n
    for a in seq: d[a]+=1
    edges=[]
    for a in seq:
        v=next(i for i in range(n) if d[i]==1)
        edges.append((v,a));d[v]-=1;d[a]-=1
    u,v=[i for i in range(n) if d[i]==1]
    edges.append((u,v))
    return edges

def adjacency(n,edges):
    a=[[] for _ in range(n)]
    for u,v in edges:
        a[u].append(v);a[v].append(u)
    return a

def canonical(a,r,parent=-1):
    """A rooted tree isomorphism invariant, complete by induction on height."""
    return '('+''.join(sorted(canonical(a,u,r) for u in a[r] if u!=parent))+')'

def duration_poly(a,r):
    """Exact tail recursion, with polynomial arithmetic implemented by SymPy."""
    def tails(v,parent):
        children=[tails(u,v) for u in a[v] if u!=parent]
        if not children:return [Integer(1)]
        h=max(map(len,children))
        out=[Integer(1)]
        for k in range(1,h+1):
            prod=Integer(1)
            for child in children:
                prod *= 1-p*(child[k-1] if k-1<len(child) else 0)
            out.append((1-prod).expand())
        return out
    return Poly(sum(tails(r,-1)[1:]),p)

def duration_mask(a,r):
    """Independent direct summation over all open-edge subsets: no tail recursion."""
    edges=sorted({tuple(sorted((u,v))) for u,row in enumerate(a) for v in row})
    n=len(a);m=len(edges)
    b=[0]*(m+1)
    for mask in range(1<<m):
        opened=[[] for _ in range(n)]
        for i,(u,v) in enumerate(edges):
            if mask>>i&1:opened[u].append(v);opened[v].append(u)
        seen={r};stack=[(r,-1,0)];longest=0
        while stack:
            u,prev,depth=stack.pop()
            if depth>longest:longest=depth
            for v in opened[u]:
                if v not in seen:
                    seen.add(v);stack.append((v,u,depth+1))
        b[mask.bit_count()]+=longest
    return Poly(sum(b[k]*p**k*(1-p)**(m-k) for k in range(m+1)),p)

def interior_roots(poly):
    """Distinct real roots strictly inside (0,1) via exact Sturm arithmetic."""
    if poly.is_zero or poly.degree()<1:return 0
    # SymPy count_roots uses closed endpoints. Remove each endpoint if a root.
    return int(poly.count_roots(0,1)) - int(poly.eval(0)==0) - int(poly.eval(1)==0)

def run(csv_path=None):
    rows=[];complete=[]
    for n in range(2,8):
        types={}
        for seq in itertools.product(range(n),repeat=n-2):
            adj=adjacency(n,decode_prufer(seq))
            for root in range(n):
                key=canonical(adj,root)
                if key not in types:types[key]=(adj,root)
        counts=collections.Counter()
        for key,(adj,root) in sorted(types.items()):
            dynamic=duration_poly(adj,root)
            direct=duration_mask(adj,root)
            assert dynamic==direct, (n,key,dynamic,direct)
            curvature=dynamic.diff().diff()
            c=interior_roots(curvature)
            assert c in (0,1,2), (n,key,c)
            counts[c]+=1
            rows.append((n,key,str(dynamic.as_expr()),str(curvature.as_expr()),c))
            if c>=2:
                complete.append((n,key,str(dynamic.as_expr()),str(curvature.as_expr())))
        print(f'n={n}: rooted types={len(types)}; interior curvature roots 0={counts[0]}, 1={counts[1]}, 2={counts[2]}')
        assert len(types)=={2:1,3:2,4:4,5:9,6:20,7:48}[n]
        assert counts[2] == (1 if n==7 else 0)
    assert len(complete)==1
    n,k,ex,second=complete[0]
    expected_key='(((()))(())())'
    assert (n,k,ex,second)==(7,expected_key,'-p**4 + 2*p**3 - p**2 + 3*p','-12*p**2 + 12*p - 2')
    print('UNIQUE ROOTED WITNESS',complete[0])
    if csv_path:
        with open(csv_path,'w',newline='',encoding='utf-8') as f:
            w=csv.writer(f);w.writerow(['vertices','rooted_canonical','expected_duration','second_derivative','interior_inflections']);w.writerows(rows)
        print('CSV records',len(rows),'path',csv_path)
    print('PASS: two independent exact probability calculations, complete labeled-Prüfer rooted-tree census and exact root counts')

if __name__=='__main__': run(sys.argv[1] if len(sys.argv)>1 else None)
