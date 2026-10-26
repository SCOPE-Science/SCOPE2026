#!/usr/bin/env python3
"""Independent open-neighborhood verification for minimal total domination in T(n)."""
from collections import Counter
from itertools import combinations

def direct(n):
    vertices=list(combinations(range(n),2)); m=len(vertices)
    adj=[]
    for i,e in enumerate(vertices):
        adj.append(sum(1<<j for j,f in enumerate(vertices) if i!=j and set(e)&set(f)))
    poly=Counter(); representatives=[]
    for selected in range(1<<m):
        neighborhoods=[selected & a for a in adj]
        if not all(neighborhoods): continue
        # Each selected vertex must have an exclusive witness among open neighborhoods.
        if not all(any(nb == (1<<i) for nb in neighborhoods)
                   for i in range(m) if selected>>i & 1): continue
        poly[selected.bit_count()]+=1
        if len(representatives)<3:
            representatives.append([vertices[j] for j in range(m) if selected>>j&1])
    return dict(sorted(poly.items())),representatives

if __name__=='__main__':
    for n in range(3,8):
        poly,reps=direct(n)
        print(f'n={n} minimal_total_domination={poly} total={sum(poly.values())}')
