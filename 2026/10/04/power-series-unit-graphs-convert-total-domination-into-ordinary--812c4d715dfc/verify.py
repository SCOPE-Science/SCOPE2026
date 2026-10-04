#!/usr/bin/env python3
from itertools import combinations, product


def domination_number(vertices, adj):
    n=len(vertices)
    for k in range(1,n+1):
        for comb in combinations(range(n),k):
            S=set(comb)
            ok=True
            for v in range(n):
                if v in S:
                    continue
                if not (adj[v] & S):
                    ok=False
                    break
            if ok:
                return k
    raise RuntimeError


def total_domination_number(vertices, adj):
    n=len(vertices)
    for k in range(1,n+1):
        for comb in combinations(range(n),k):
            S=set(comb)
            if all(adj[v] & S for v in range(n)):
                return k
    raise RuntimeError


def graph_from_ring(elements, add, is_unit):
    n=len(elements)
    adj=[set() for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if is_unit(add(elements[i],elements[j])):
                adj[i].add(j); adj[j].add(i)
    return adj


def truncated_power_series_graph(elements, add, is_unit, length=2):
    verts=list(product(elements, repeat=length))
    n=len(verts)
    adj=[set() for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            # A truncated formal power series is a unit iff its constant term is a unit.
            if is_unit(add(verts[i][0], verts[j][0])):
                adj[i].add(j); adj[j].add(i)
    return verts,adj

# Z/4Z
Z4=list(range(4))
add4=lambda a,b:(a+b)%4
unit4=lambda a:a in (1,3)
adj4=graph_from_ring(Z4,add4,unit4)
gt4=total_domination_number(Z4,adj4)
v4t,a4t=truncated_power_series_graph(Z4,add4,unit4,2)
g4t=domination_number(v4t,a4t)
assert gt4==2 and g4t==2

# F_2 x F_2: its unit graph is a disjoint union of two edges, so total domination is 4.
F22=list(product((0,1), repeat=2))
add22=lambda a,b:((a[0]^b[0]),(a[1]^b[1]))
unit22=lambda a:a==(1,1)
adj22=graph_from_ring(F22,add22,unit22)
gt22=total_domination_number(F22,adj22)
v22t,a22t=truncated_power_series_graph(F22,add22,unit22,2)
g22t=domination_number(v22t,a22t)
assert gt22==4 and g22t==4

print('VERIFY_OK')
print('Z4: gamma_t(G(R))=2, gamma(G(R[x]/(x^2)))=2')
print('F2xF2: gamma_t(G(R))=4, gamma(G(R[x]/(x^2)))=4')
print('finite_truncation_check=constant-term blow-up agrees with theorem')
