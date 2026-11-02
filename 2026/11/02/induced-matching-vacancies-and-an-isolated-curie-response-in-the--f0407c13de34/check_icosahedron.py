#!/usr/bin/env python3
"""Exact finite check of the icosahedral spin-one Ising vacancy theorem.
Run: python3 check_icosahedron.py
No external modules required. All computations are integer exact.
"""
from collections import Counter, defaultdict
from itertools import combinations, product

N=12
EDGES=set()
def edge(i,j):
    EDGES.add(tuple(sorted((i,j))))
for i in range(5):
    edge(0,1+i)
    edge(11,6+i)
    edge(1+i,1+(i+1)%5)
    edge(6+i,6+(i+1)%5)
    edge(1+i,6+i)
    edge(1+i,6+(i-1)%5)
EDGES=tuple(sorted(EDGES))
assert len(EDGES)==30
assert all(sum(i in e for e in EDGES)==5 for i in range(N))
assert sum(all(tuple(sorted(p)) in EDGES for p in combinations(t,2))
           for t in combinations(range(N),3))==20

# Direct computation from the physical spin Hamiltonian.
micro={m:[10**9,0,Counter()] for m in range(N+1)}
critical_half=Counter()
critical_one=Counter()
for s in product((-1,0,1),repeat=N):
    m=sum(x*x for x in s)
    b=sum(s[i]*s[j] for i,j in EDGES)
    mag=sum(s)
    record=micro[m]
    if b<record[0]:micro[m]=[b,1,Counter([mag])]
    elif b==record[0]:record[1]+=1; record[2][mag]+=1
    if 2*b+m==-8:critical_half[m,mag]+=1
    if b+m==0:critical_one[m,mag]+=1
    assert 2*b+m>=-8 and b+m>=0

EXPECTED_MIN=[0,0,-1,-2,-3,-4,-6,-7,-8,-8,-9,-9,-10]
EXPECTED_COUNTS=[1,24,60,120,300,480,80,120,150,960,240,600,72]
assert [micro[m][0] for m in range(N+1)]==EXPECTED_MIN
assert [micro[m][1] for m in range(N+1)]==EXPECTED_COUNTS
assert dict(critical_half)=={(8,0):150,(10,0):240,(12,0):72}
assert dict(critical_one)=={(0,0):1,(6,0):80,(7,-1):60,(7,1):60,(8,0):150}

# INDEPENDENT combinatorial computation: write the occupied set as a disjoint
# union of positive and negative sets, and count same-sign and cross-sign edges.
# The edge contribution is 2[e(P)+e(N)]-e(A). This differs from the
# direct spin-product calculation, and enumerates by masks instead of tuples.
ALL=(1<<N)-1
adj=[0]*N
for i,j in EDGES:adj[i]|=1<<j; adj[j]|=1<<i
induced_edges=[0]*(ALL+1)
for mask in range(1,ALL+1):
    lowest=mask & -mask
    i=lowest.bit_length()-1
    prev=mask^lowest
    induced_edges[mask]=induced_edges[prev]+(adj[i]&prev).bit_count()
micro2={m:[10**9,0,Counter()] for m in range(N+1)}
mask8=defaultdict(int)
mask10=defaultdict(int)
for occupied in range(ALL+1):
    m=occupied.bit_count()
    p=occupied
    while True:
        n=occupied^p
        bond=2*(induced_edges[p]+induced_edges[n])-induced_edges[occupied]
        magnetization=p.bit_count()-n.bit_count()
        rec=micro2[m]
        if bond<rec[0]:micro2[m]=[bond,1,Counter([magnetization])]
        elif bond==rec[0]:rec[1]+=1;rec[2][magnetization]+=1
        if m==8 and bond==-8:mask8[ALL^occupied]+=1
        if m==10 and bond==-9:mask10[ALL^occupied]+=1
        if p==0:break
        p=(p-1)&occupied
assert micro==micro2
assert len(mask8)==75 and all(v==2 for v in mask8.values())
assert len(mask10)==30 and all(v==8 for v in mask10.values())
# Geometric characterization, both necessary and sufficient.
# Every vacancy quadruple with two disjoint induced edges must be included.
matchings=set()
for quartet in combinations(range(N),4):
    z=sum(1<<i for i in quartet)
    degrees=[(adj[i]&z).bit_count() for i in quartet]
    if degrees==[1,1,1,1]:matchings.add(z)
assert len(matchings)==75
assert set(mask8)==matchings
assert all(induced_edges[z]==1 for z in mask10)
assert set(mask10)=={(1<<i)|(1<<j) for i,j in EDGES}

# Exact zero-temperature equal-weight Curie coefficient at D=J.
curie_num=sum(c*mag*mag for (m,mag),c in critical_one.items())
curie_den=sum(critical_one.values())
assert (curie_num,curie_den)==(120,351)
assert sum(critical_half.values())==462
assert sum(critical_one.values())==351
assert curie_num*117==curie_den*40

print('PASS: 531441 ternary configurations; 531441 mask partitions; 30 edges, 20 faces.')
print('PASS: occupancy minima and multiplicities, sharp inequalities, critical sectors.')
print('PASS: intermediate vacancy sets are exactly 75 induced 2K2 patterns, each with 2 signs.')
print('PASS: first-boundary 462, second-boundary 351, Curie coefficient 40/117.')
