"""Exact symbolic and independent finite checks for dominating matchings of prisms.

Requires Python 3.10+ and SymPy 1.12+; run: python verify.py.
"""
from collections import Counter
from itertools import product
from math import ceil
import sympy as S

LETTERS = (0, 1, 2, 4, 6)  # empty, rung, upper edge, lower edge, both horizontals

def compatible(a, b):
    return not ((a & b & 2) or (a & b & 4) or ((a & 6) and (b & 1)))

def top(a, b):
    return bool((b & 1) or (a & 2) or (b & 2))

def bottom(a, b):
    return bool((b & 1) or (a & 4) or (b & 4))

def dominates_middle(a, b, c, d):
    return ((top(a,b) or top(b,c) or top(c,d) or bottom(b,c))
            and (bottom(a,b) or bottom(b,c) or bottom(c,d) or top(b,c)))

states = [(a,b,c) for a,b,c in product(LETTERS, repeat=3)
          if compatible(a,b) and compatible(b,c)]
index = {s:i for i,s in enumerate(states)}
arcs = []
for a,b,c in states:
    for d in LETTERS:
        if compatible(c,d) and dominates_middle(a,b,c,d):
            arcs.append((index[(a,b,c)], index[(b,c,d)], d.bit_count()))
assert len(states)==49 and len(arcs)==147

# Bellman--Ford provides a potential for the integer reduced cost
# 3(number of selected edges) - (number of columns).
potential = [0]*len(states)
for _ in range(len(states)):
    changed = False
    for i,j,c in arcs:
        if potential[j] > potential[i] + 3*c - 1:
            potential[j] = potential[i] + 3*c - 1
            changed = True
    if not changed:
        break
assert not changed, 'Unexpected negative-cost cycle'
reduced = [(i,j,3*c-1+potential[i]-potential[j]) for i,j,c in arcs]
assert min(c for _,_,c in reduced) >= 0
A = [S.zeros(len(states)) for _ in range(3)]
for i,j,c in reduced:
    if c < 3: A[c][i,j] += 1
z = S.symbols('z')
R = (S.eye(len(states))-z*A[0]).inv()
T1 = S.factor(S.trace(R*A[1]))
T2 = S.factor(S.trace(R*A[2]))
T11 = S.factor(S.trace(R*A[1]*R*A[1]))
assert S.cancel(T1-z*(3-z**3)/(1-z**3)**2)==0
assert S.cancel(T2-(1+3*z**3)/(1-z**6))==0
assert S.cancel(T11-z**2*(3-z**3)*(2*z**6-5*z**3+5)/(1-z**3)**4)==0
assert S.factor((S.eye(len(states))-z*A[0]).det()-(1-z**3)*(1-z**6))==0

# The closed-walk theorem gives sum_n tr(A(z)^n)t^n.
# For reduced cost delta=0,1,2, its coefficients come from
# F0=-z(d/dz)log det(I-z*A0),
# F1=z(d/dz)(z tr(R A1)),
# F2=z(d/dz)(z tr(R A2) + (z^2/2) tr(R A1 R A1)).
# The three exact identities above are symbolic finite certificates.

def expected_min_count(n):
    k, r = divmod(n, 3)
    if r==0: return 9 if k%2==0 else 3
    if r==2: return n*(2*k+3)
    assert r==1
    return n*(S.Rational(2*k**3+12*k**2+25*k+6, 6)
              +2-(-1)**k)

def transfer_histogram(n):
    total = Counter()
    for start in range(len(states)):
        dp = {(start,0):1}
        for _ in range(n):
            nd = Counter()
            for (j,cost),v in dp.items():
                for i,k,w in arcs:
                    if i == j: nd[k,cost+w]+=v
            dp = nd
        for (j,cost),v in dp.items():
            if j==start:total[cost]+=v
    return total

def direct_histogram(n):
    edges = ([(i,(i+1)%n) for i in range(n)]
             + [(n+i,n+(i+1)%n) for i in range(n)]
             + [(i,n+i) for i in range(n)])
    closed = [1 << i for i in range(2*n)]
    for a,b in edges:
        closed[a] |= 1<<b
        closed[b] |= 1<<a
    endpoints = [(1<<a)|(1<<b) for a,b in edges]
    neighborhoods = [closed[a]|closed[b] for a,b in edges]
    complete = (1 << (2*n))-1
    out = Counter()
    def dfs(i, used, dominated, count):
        if i == len(edges):
            if dominated == complete:out[count]+=1
            return
        dfs(i+1,used,dominated,count)
        if used & endpoints[i] == 0:
            dfs(i+1,used|endpoints[i],dominated|neighborhoods[i],count+1)
    dfs(0,0,0,0)
    return out

checks = 0
for n in range(3,10):
    direct = direct_histogram(n)
    derived = transfer_histogram(n)
    assert direct == derived,(n,direct,derived)
    minimum = ceil(n/3)
    assert min(derived)==minimum
    assert derived[minimum]==expected_min_count(n)
    checks += sum(direct.values())
for n in range(10,31):
    derived = transfer_histogram(n)
    minimum = ceil(n/3)
    assert min(derived)==minimum
    assert derived[minimum]==expected_min_count(n)
print('VERIFY_OK states=49 arcs=147 symbolic_trace_identites=4 direct_prism_orders=3..9 checked_dominating_matchings=',checks,'transfer_orders=3..30')
