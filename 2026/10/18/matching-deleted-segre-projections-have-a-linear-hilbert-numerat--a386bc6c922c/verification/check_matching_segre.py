#!/usr/bin/env python3
"""Independent finite degree-by-degree monomial enumeration for coordinate-projected rank-one matrix varieties."""
from math import comb
from itertools import product

def monomial_exponents(a,b,k,t):
    edges=[(i,j) for i in range(a) for j in range(b) if not(i==j and i<k)]
    state={(0,)*(a+b)}
    for _ in range(t):
        nxt=set()
        for p in state:
            for i,j in edges:
                v=list(p);v[i]+=1;v[a+j]+=1
                nxt.add(tuple(v))
        state=nxt
    return len(state)

def predicted(a,b,k,t):
    return comb(t+a-1,a-1)*comb(t+b-1,b-1)-k*comb(t+a+b-3,a+b-2) if t else 1

def run():
    ncases=0
    for a,b,max_t in [(3,3,5),(3,4,4),(3,5,3),(4,4,3),(4,5,3),(5,5,2),(6,6,2)]:
        for k in range(min(a,b)+1):
            for t in range(max_t+1):
                observed=monomial_exponents(a,b,k,t)
                expected=predicted(a,b,k,t)
                if observed!=expected:
                    raise AssertionError(f'a={a}, b={b}, k={k}, t={t}: direct={observed}, predicted={expected}')
                ncases+=1
        print(f'PASS a={a}, b={b}, k=0..{min(a,b)}, t=0..{max_t}')
    print(f'PASS {ncases} cases: independent edge-sum enumeration equals polynomial formula')
if __name__=='__main__':run()
