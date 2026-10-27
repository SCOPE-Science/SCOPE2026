"""Exact checks for synchronous majority dynamics on circular prism graphs.

Python 3.10+ and SymPy. Usage: python verify_prism_majority.py
The finite symbolic transfer computation proves all-size trace identities.
The direct state-space enumeration is a separate finite cross-check only.
"""
from collections import Counter
from math import comb
from sympy import Matrix, Symbol, factor, trace


def triple_good(a, b, c):
    # Each of a,b,c holds (top at t, bottom at t, top at t+1, bottom at t+1).
    def bit(s, i): return (s >> i) & 1
    for row in (0, 1):
        forward = bit(a, row) + bit(c, row) + bit(b, 1-row)
        reverse = bit(a, 2+row) + bit(c, 2+row) + bit(b, 3-row)
        if (forward >= 2) != bool(bit(b, 2+row)):
            return False
        if (reverse >= 2) != bool(bit(b, row)):
            return False
    return True


def transfer_graph():
    edges = [[] for _ in range(256)]
    for a in range(16):
        for b in range(16):
            for c in range(16):
                if triple_good(a,b,c):
                    edges[16*a+b].append(16*b+c)
    return edges


def sccs(edges):
    # Standard Tarjan SCC algorithm.
    seq = 0
    stack = []
    on = set()
    idx = [-1]*len(edges)
    low = [-1]*len(edges)
    comps = []
    def visit(v):
        nonlocal seq
        idx[v] = low[v] = seq
        seq += 1
        stack.append(v)
        on.add(v)
        for w in edges[v]:
            if idx[w] < 0:
                visit(w)
                low[v] = min(low[v],low[w])
            elif w in on:
                low[v] = min(low[v],idx[w])
        if low[v] == idx[v]:
            component=[]
            while True:
                w=stack.pop(); on.remove(w);component.append(w)
                if w == v: break
            comps.append(sorted(component))
    for v in range(len(edges)):
        if idx[v] < 0: visit(v)
    return comps


def component_matrix(nodes,edges):
    look=set(nodes)
    return Matrix([[int(v in edges[u]) for v in nodes] for u in nodes])


def lucas(n):
    a,b=2,1
    for _ in range(n): a,b=b,a+b
    return a


def fixed_formula(n):
    # 2+2cos(n*pi/3) is the integer period-6 sequence 4,3,1,0,1,3.
    q=(4,3,1,0,1,3)[n%6]
    return lucas(n)+q


def twice_periodic_formula(n):
    a=n%6
    if a==0: return lucas(2*n)+8*lucas(n)+18
    if a in (2,4): return lucas(2*n)+2*lucas(n)+3
    if a==3: return lucas(2*n)+4
    return lucas(2*n)+1


def majority(x,n):
    output=0
    for row in (0,1):
        for i in range(n):
            sum_nei=sum((x>>j)&1 for j in (
                row*n+(i-1)%n,row*n+(i+1)%n,(1-row)*n+i))
            if sum_nei >= 2: output |= 1 << (row*n+i)
    return output


def main():
    edges=transfer_graph()
    assert sum(map(len,edges))==400
    comps=sccs(edges)
    assert sum(map(len,comps)) ==256
    live=[c for c in comps if len(c)>1 or c[0] in edges[c[0]]]
    polys=Counter()
    poly_symbol=Symbol('T')
    for nodes in live:
        pol=factor(component_matrix(nodes,edges).charpoly(poly_symbol).as_expr())
        polys[(len(nodes),str(pol))] += 1
    expected={
      (16,'(T - 1)**2*(T + 1)**2*(T**2 - 3*T + 1)*(T**2 + T + 1)*(T**4 - T**3 + 2*T**2 + T + 1)*(T**4 + T**3 + 2*T**2 - T + 1)'):1,
      (8,'(T**2 - T - 1)*(T**2 - T + 1)*(T**2 + T - 1)*(T**2 + T + 1)'):2,
      (2,'(T - 1)*(T + 1)'):1,
      (1,'T - 1'):2,
    }
    assert dict(polys)==expected,polys
    print('TRANSFER: 256 states, 400 edges, live SCC sizes [16,8,8,2,1,1]')
    print('EXACT COMPONENT CHARACTERISTIC POLYNOMIALS:')
    for key,cnt in sorted(polys.items(),reverse=True):print(cnt,key)
    for n in range(3,11):
        t=sum(int(trace(component_matrix(c,edges)**n)) for c in live)
        assert t == twice_periodic_formula(n),(n,t,twice_periodic_formula(n))
    print('Symbolic transfer checks: n = 3..10 matched six-residue Lucas formula')
    for n in range(3,11):
        f=0;p=0
        for x in range(1<<(2*n)):
            y=majority(x,n)
            f += (x == y)
            p += (majority(y,n) == x)
        assert f == fixed_formula(n),(n,f,fixed_formula(n))
        assert p == twice_periodic_formula(n),(n,p,twice_periodic_formula(n))
        print('n',n,'fixed',f,'F2fixed',p,'primitive_two_cycles',(p-f)//2)
    print('PASS: exact transfer factorization, Lucas formulas and direct finite enumeration')


if __name__=='__main__': main()
