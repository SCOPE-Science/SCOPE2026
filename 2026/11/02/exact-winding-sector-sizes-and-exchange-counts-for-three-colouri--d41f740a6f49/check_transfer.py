#!/usr/bin/env python3
"""Laurent-transfer verification for cyclic-prism three-colouring sectors.
Builds transfer matrices from allowed colour steps and independently counts
recolourable sites by inserting a marked two-step transition.
"""
from collections import defaultdict
from math import comb


def plus(*polys):
    out=defaultdict(int)
    for p in polys:
        for k,v in p.items():out[k]+=v
    return {k:v for k,v in out.items() if v}


def prod(p,q):
    d=defaultdict(int)
    for a,x in p.items():
        for b,y in q.items():d[a+b]+=x*y
    return {k:v for k,v in d.items() if v}


def matmul(a,b):
    m=len(a);r=len(b); n=len(b[0]); out=[[{} for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):out[i][j]=plus(*(prod(a[i][k],b[k][j]) for k in range(r)))
    return out


def power(a,n):
    size=len(a)
    v=[[{0:1} if i==j else {} for j in range(size)] for i in range(size)]
    while n:
        if n&1:v=matmul(v,a)
        a=matmul(a,a);n//=2
    return v


def trace(a):return plus(*(a[i][i] for i in range(len(a))))


def trinomial(n):
    v={0:1}
    for i in range(n):v=prod(v,{-1:1,0:1,1:1})
    return v

# State order +,-. A horizontal move has weight +/-1, according to the
# movement of the top colour in Z/3. A vertical orientation flip forces
# the horizontal increment to equal the departing orientation.
B=[[{-1:1,1:1},{1:1}],[{-1:1},{-1:1,1:1}]]
# A top recolouring at rung zero forces the preceding and following top
# colours to equal the bottom colour at that rung. The two horizontal
# moves are +/-epsilon; summed over epsilon, every boundary entry is 2.
M=[[{0:2},{0:2}],[{0:2},{0:2}]]


def check(n):
    total=trace(power(B,n))
    marked=trace(matmul(M,power(B,n-2)))
    tri_n=trinomial(n)
    tri_a=trinomial(n-1); tri_b=trinomial(n-2)
    for s in range(-n,n+1):
        if s%3==0:
            w=s//3
            actual_vertices=3*total.get(s,0)
            actual_top_sites=3*marked.get(s,0)
            if (n-w)%2==0:
                expected_vertices=6*tri_n.get(s,0)
                expected_top_sites=6*(tri_a.get(s,0)+tri_b.get(s,0))
            else:expected_vertices=expected_top_sites=0
            assert actual_vertices==expected_vertices,(n,s,actual_vertices,expected_vertices)
            assert actual_top_sites==expected_top_sites,(n,s,actual_top_sites,expected_top_sites)
    assert 3*sum(v for s,v in total.items() if s%3==0)==3**n+1+2*(-2)**n
    # Directly count colourings in each winding sector by another transfer
    # model: all 6 oriented coloured rung states, with a weighted edge.
    if n<=9:
        states=[(a,b) for a in range(3) for b in range(3) if b!=a]
        T=[]
        for a,b in states:
            row=[]
            for c,d in states:
                if c==a or d==b:row.append({});continue
                ds=(c-a)%3
                row.append({1 if ds==1 else -1:1})
            T.append(row)
        six=trace(power(T,n))
        for s in range(-n,n+1):
            if s%3==0:assert six.get(s,0)==3*total.get(s,0)
    print('n=%d vertices=%d marked_top=%d' %(n,
        3*sum(v for s,v in total.items() if s%3==0),
        3*sum(v for s,v in marked.items() if s%3==0)))

if __name__=='__main__':
    for n in range(3,31):check(n)
    print('PRISM_LAURENT_TRANSFER_PASS')
