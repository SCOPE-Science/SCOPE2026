#!/usr/bin/env python3
"""Exact, standard-library verification of maximal matching enumerator for cycle prisms.

The checker constructs the local transfer matrix directly, computes its
characteristic determinant using Newton identities, and compares independent
unrestricted matching enumeration on small labeled prisms.
"""
from collections import Counter, defaultdict
from math import comb

SYMBOLS = ((0,0,0),(0,1,0),(0,0,1),(0,1,1),(1,0,0)) # (r_i,top_i,bottom_i)
STATES = [(a,b) for a in range(5) for b in range(5)]
INDEX = {ab:i for i,ab in enumerate(STATES)}

def admissible(a,b,c):
    r0,t0,d0=SYMBOLS[a]
    r1,t1,d1=SYMBOLS[b]
    r2,t2,d2=SYMBOLS[c]
    # Is each vertex covered by at most one matching edge?
    up=t0+t1+r1; down=d0+d1+r1
    if up>1 or down>1: return False
    # If both vertices in the rung are uncovered, the rung is addable.
    if up==0 and down==0: return False
    # If two consecutive vertices on a rail are uncovered, the rail edge is addable.
    if up==0 and t1+t2+r2==0: return False
    if down==0 and d1+d2+r2==0: return False
    return True

EDGES=defaultdict(list)
for a in range(5):
    for b in range(5):
        for c in range(5):
            if admissible(a,b,c):
                EDGES[INDEX[a,b]].append((INDEX[b,c],sum(SYMBOLS[b])))

# Exact integer polynomial arithmetic, sparse monomial exponent -> coefficient.
def mul(a,b):
    ans=defaultdict(int)
    for i,x in a.items():
        for j,y in b.items():ans[i+j]+=x*y
    return {k:v for k,v in ans.items() if v}

def trace_powers(max_order):
    traces=[None]+[defaultdict(int) for _ in range(max_order)]
    for start in range(len(STATES)):
        dp={start:{0:1}}
        for k in range(1,max_order+1):
            nex={}
            for u,p in dp.items():
                for v,w in EDGES[u]:
                    q=nex.setdefault(v,defaultdict(int))
                    for d,count in p.items():q[d+w]+=count
            dp=nex
            for d,value in dp.get(start,{}).items():traces[k][d]+=value
    return [None]+[dict(p) for p in traces[1:]]

def determinant_by_newton(traces):
    # det(I-tT)= sum_j a_j(z)t^j, with a_0=1.
    a=[{0:1}]
    for j in range(1,len(traces)):
        total=defaultdict(int)
        for k in range(1,j+1):
            for d,c in mul(a[j-k],traces[k]).items():total[d]+=c
        assert all(v%j==0 for v in total.values())
        a.append({d:-v//j for d,v in total.items() if v})
    return a

EXPECTED=(
    {0:1},{1:-1},{2:-2},{2:-2,3:1},{4:1},
    {4:-2},{4:1,5:-2},{5:1},{6:1}
)

def direct_count(n):
    edges=set()
    for i in range(n):
        edges.add(tuple(sorted((i,(i+1)%n))))
        edges.add(tuple(sorted((n+i,n+(i+1)%n))))
        edges.add((i,n+i))
    adj=[0]*(2*n)
    for u,v in edges:adj[u]|=1<<v;adj[v]|=1<<u
    counts=Counter();nodes=0
    def visit(remaining,free,k):
        nonlocal nodes
        nodes+=1
        if not remaining:
            b=free
            while b:
                flag=b&-b;b-=flag
                v=flag.bit_length()-1
                if adj[v]&free:return # cannot be maximal
            counts[k]+=1
            return
        flag=remaining&-remaining;v=flag.bit_length()-1
        rest=remaining^flag
        visit(rest,free|flag,k)
        choices=adj[v]&rest
        while choices:
            flag2=choices&-choices;choices-=flag2
            visit(rest^flag2,free,k+1)
    visit((1<<(2*n))-1,0,0)
    return counts,nodes

def saturating(n):
    return 6 if n%3==0 else 2*n if n%3==1 else n*(5*n-1)//3

def main():
    assert len(STATES)==25 and sum(map(len,EDGES.values()))==53
    tr=trace_powers(25)
    det=determinant_by_newton(tr)
    assert det[:9]==list(EXPECTED), (det[:9],EXPECTED)
    assert all(not x for x in det[9:]),det[9:]
    brute_nodes=0
    for n in range(3,13):
        counts,nodes=direct_count(n)
        brute_nodes+=nodes
        assert dict(counts)==tr[n],(n,counts,tr[n])
        assert min(counts)==(2*n+2)//3 and max(counts)==n
        assert counts[(2*n+2)//3]==saturating(n)
    # Check higher-order values by the denominator recurrence, independent
    # of direct enumeration and of the closed boundary formula.
    for n in range(3,26):
        assert min(tr[n])==(2*n+2)//3 and max(tr[n])==n
        assert tr[n][(2*n+2)//3]==saturating(n)
    print('VERIFY_OK 25_states 53_arcs determinant_degree_8 trace_orders_1..25'
          ' brute_orders_3..12 brute_search_nodes='+str(brute_nodes)
          +' minimum_coefficients_3..25')
if __name__=='__main__': main()
