#!/usr/bin/env python3
"""Independent exact checks for choice-controlled walks on rooted regular trees.

Runs with Python 3 standard library; no external data or packages.
"""
from fractions import Fraction as F
from itertools import product
from decimal import Decimal, localcontext

CHECKS = 0

def require(condition, context):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(context)

def exact_values(b, k, height):
    p = F(1) - F(b, b + 1)**k
    q = F(1) - p
    increments = [F(0)] * (height + 1)
    increments[height] = F(1)
    for j in range(height - 1, 0, -1):
        increments[j] = (1 + q * increments[j + 1]) / p
    values = [F(0)]
    for j in range(1, height + 1):
        values.append(values[-1] + increments[j])
    return p, q, values

def closed_mean(b, k, height):
    p = F(1) - F(b, b + 1)**k
    q = 1 - p
    if p == q:
        return F(height * height)
    gap = p - q
    return F(height) / gap - 2 * p * q / (gap * gap) * (1 - (q / p)**height)

def exact_tree(b, height):
    adj, levels = [[]], [0]
    frontier = [0]
    for depth in range(1, height + 1):
        new = []
        for parent in frontier:
            for _ in range(b):
                child = len(adj)
                adj.append([parent]); adj[parent].append(child)
                levels.append(depth); new.append(child)
        frontier = new
    return adj, levels

# Full finite graph Bellman inequalities with all offered multisets (ordered tuples).
for b in (2, 3, 4):
    for height in (1, 2, 3):
        adj, levels = exact_tree(b, height)
        for k in (1, 2, 3, 4):
            p, q, vals = exact_values(b, k, height)
            require(vals[-1] == closed_mean(b, k, height), ('closed mean', b,k,height))
            require(all(vals[i] > vals[i-1] for i in range(1, len(vals))), ('monotonicity',b,k,height))
            for v, neighbors in enumerate(adj):
                if v == 0:
                    continue
                d = len(neighbors)
                bellman = F(1) + sum((min(vals[levels[u]] for u in offer) for offer in product(neighbors, repeat=k)), F(0)) / d**k
                require(bellman == vals[levels[v]], ('Bellman', b,k,height,v))

# Exact second moments from the full first-step equations, not a simulation.
def exact_moments(b, k, height):
    p,q,ev = exact_values(b,k,height)
    dif=[F(0)]*(height+1)
    dif[height] = 1+2*ev[height-1]
    for i in range(height-1,0,-1):
        dif[i]=(2*ev[i]-1+q*dif[i+1])/p
    ev2=sum(dif)
    return ev[-1], ev2-ev[-1]**2
for b,k in ((2,1),(2,2),(3,2),(3,3),(4,4)):
    for h in range(1,11):
        m,v=exact_moments(b,k,h)
        require(m==closed_mean(b,k,h), ('moments mean',b,k,h))
        require(v>=0, ('negative variance',b,k,h))
        if h==1: require(v==0, ('one step variance',b,k))

# Exact first-excursion success probabilities by gambler's-ruin recurrence.
for b,k in ((2,1),(2,2),(3,2),(3,3),(4,3)):
    p,q,_=exact_values(b,k,2)
    ratio=q/p
    for h in range(2,15):
        u=[F(0)]*(h+1)
        # u_i = P_i(hit root before leaf), u_0=1 and u_h=0
        # solve by increments from boundary and check all equations
        if ratio==1:
            u=[F(h-i,h) for i in range(h+1)]
        else:
            u=[((ratio**(h-i)-1)/(ratio**h-1)) for i in range(h+1)]
        require(u[0]==1 and u[h]==0, ('ruin boundary',b,k,h))
        for i in range(1,h):
            require(u[i]==p*u[i-1]+q*u[i+1], ('ruin equation',b,k,h,i))
        # A cycle begins by stepping from the leaf h to level h-1.
        require(u[h-1]==(ratio-1)/(ratio**h-1) if ratio!=1 else u[h-1]==F(1,h), ('cycle success',b,k,h))

# The putative critical case is impossible for integers b>=2, k>=1.
for b in range(2,101):
    for k in range(1,21):
        require(2*b**k != (b+1)**k, ('unexpected tie',b,k))

# Numeric illustration of the two phases with exact rational mean.
for b,k in ((2,2),(3,2),(3,3)):
    p,q,_=exact_values(b,k,2)
    h=120
    m=closed_mean(b,k,h)
    if p>q:
        require(abs(float(m)/h-1/float(p-q))<1.5, ('linear scaling',b,k))
    else:
        r=q/p
        lead=2*p*q/(p-q)**2
        require(abs(float(m/(lead*r**h))-1)<1e-8, ('exponential scaling',b,k))

print('PASS', CHECKS, 'exact and analytic consistency assertions')
print('b=2,k=2: E T_h = 9h - 40(1-(4/5)^h)')
print('b=3,k=2: E T_h = -8h + (63/2)((9/7)^h-1)')
