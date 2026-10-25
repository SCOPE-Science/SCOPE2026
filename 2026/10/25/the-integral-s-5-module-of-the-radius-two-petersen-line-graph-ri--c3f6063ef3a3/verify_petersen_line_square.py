#!/usr/bin/env python3
"""Exact graph, join, full S5 character and Specht decomposition checks.
Uses only the Python standard library. Vertices are two-element subsets of range(5).
"""
from collections import Counter, deque
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial

V = list(combinations(range(5), 2))
vi = {x:i for i,x in enumerate(V)}
P = [(i,j) for i,j in combinations(range(10),2) if set(V[i]).isdisjoint(V[j])]
assert len(P)==15
pi={x:i for i,x in enumerate(P)}
L=[set() for _ in range(15)]
for i,j in combinations(range(15),2):
    if set(P[i]) & set(P[j]): L[i].add(j);L[j].add(i)
assert sum(map(len,L))==60
D=[]
for x in range(15):
    dist=[None]*15;dist[x]=0;queue=deque([x])
    while queue:
        a=queue.popleft()
        for b in L[a]:
            if dist[b] is None:
                dist[b]=dist[a]+1;queue.append(b)
    D.append(dist)
assert Counter(D[a][b] for a,b in combinations(range(15),2))=={1:30,2:60,3:15}
color=[]
for a,b in P:
    missing=next(iter(set(range(5))-set(V[a])-set(V[b])))
    color.append(missing)
blocks=[[i for i in range(15) if color[i]==c] for c in range(5)]
assert all(len(b)==3 for b in blocks)
assert all((D[i][j]==3)==(color[i]==color[j]) for i,j in combinations(range(15),2))
assert all(D[i][j]<=3 for i,j in combinations(range(15),2))

faces=[]
for mask in range(1,1<<15):
    face=[v for v in range(15) if mask>>v & 1]
    if all(D[a][b]<=2 for a,b in combinations(face,2)):faces.append(tuple(face))
assert Counter(len(f) for f in faces)=={1:15,2:90,3:270,4:405,5:243}
# Five-way join is an *isomorphism of simplicial complexes*, not only a homology fit.
assert all(len([j for j in f if color[j]==c])<=1 for f in faces for c in range(5))
assert len(faces)==4**5-1

# Evaluate the trace on top H_4 independently in two exact ways.
def sign_of_order(seq):
    return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1

def group_action(g):
    pv=[vi[tuple(sorted(g[t] for t in v))] for v in V]
    return [pi[tuple(sorted((pv[a],pv[b])))] for a,b in P]

def lefschetz(g):
    m=group_action(g); tot=0
    for f in faces:
        im=[m[x] for x in f]
        if set(im)==set(f):tot+=(-1)**(len(f)-1)*sign_of_order(im)
    return tot-1   # subtract the H_0 trace; the remaining homology is in degree 4

def tensor_trace(g):
    m=group_action(g);used=set();ans=1
    for seed in range(5):
        if seed in used:continue
        c=seed;ell=0
        while c not in used:
            used.add(c);c=g[c];ell+=1
        assert c==seed
        fixed=0
        for start in blocks[seed]:
            x=start
            for _ in range(ell):x=m[x]
            if x==start:fixed+=1
        ans*=fixed-1
    return ans*sign_of_order(list(g)) # permutation of the five join factors

perms=list(permutations(range(5)))
assert len(perms)==120
for g in perms:assert lefschetz(g)==tensor_trace(g)

def part(n,maxpart=None):
    if n==0:
        yield ();return
    if maxpart is None:maxpart=n
    for j in range(min(n,maxpart),0,-1):
        for rest in part(n-j,j):yield (j,)+rest

def z(mu):
    return __import__('math').prod(k**r*factorial(r) for k,r in Counter(mu).items())

def cycletype(g):
    seen=set();result=[]
    for a in range(5):
        if a in seen:continue
        t=0;b=a
        while b not in seen:
            seen.add(b);t+=1;b=g[b]
        result.append(t)
    return tuple(sorted(result,reverse=True))

conjs=list(part(5));char={mu:None for mu in conjs}
for g in perms:
    mu=cycletype(g);x=lefschetz(g)
    if char[mu] is not None:assert char[mu]==x
    char[mu]=x
assert char=={(5,):2,(4,1):0,(3,2):0,(3,1,1):2,(2,2,1):8,(2,1,1,1):0,(1,1,1,1,1):32}

# Reconstruct the S_5 irreducible character table by the Frobenius/Jacobi--Trudi identity.
ZERO=(0,0,0,0,0)
def mul(a,b):
    o={}
    for k,v in a.items():
        for j,w in b.items():
            t=tuple(x+y for x,y in zip(k,j));o[t]=o.get(t,0)+v*w
    return o
h={0:{ZERO:Fraction(1)}}
for k in range(1,6):
    h[k]={}
    for mu in part(k):
        ex=tuple(Counter(mu).get(j,0) for j in range(1,6))
        h[k][ex]=Fraction(1,z(mu))
chars={}
for la in conjs:
    m=len(la);poly={}
    for order in permutations(range(m)):
        s=sign_of_order(order);a={ZERO:Fraction(s)}
        for i in range(m):
            k=la[i]-i+order[i]
            a=mul(a,h.get(k,{}))
        for ex,c in a.items():poly[ex]=poly.get(ex,0)+c
    chars[la]={}
    for mu in conjs:
        ex=tuple(Counter(mu).get(j,0) for j in range(1,6))
        coeff=poly.get(ex,0)*z(mu)
        assert coeff.denominator==1
        chars[la][mu]=int(coeff)
for la in conjs:
    for lb in conjs:
        scalar=sum(Fraction(chars[la][mu]*chars[lb][mu],z(mu)) for mu in conjs)
        assert scalar==int(la==lb)
mult={la:sum(Fraction(char[mu]*chars[la][mu],z(mu)) for mu in conjs) for la in conjs}
assert all(v.denominator==1 and v>=0 for v in mult.values())
assert mult=={(5,):2,(4,1):1,(3,2):2,(3,1,1):0,(2,2,1):2,(2,1,1,1):1,(1,1,1,1,1):2}
assert sum(mult[la]*chars[la][(1,1,1,1,1)] for la in conjs)==32
print('PETERSEN_EDGES',len(P),'LINE_GRAPH_DISTANCES',dict(Counter(D[a][b] for a,b in combinations(range(15),2))))
print('FIVE_CANONICAL_THREE_EDGE_CLASSES',blocks)
print('VR_RADIUS_TWO_FACE_VECTOR',dict(sorted(Counter(len(f) for f in faces).items())))
print('VR_RADIUS_TWO_INTEGRAL_H4_RANK',2**5)
print('S5_CLASS_CHARACTER',[(mu,char[mu]) for mu in conjs])
print('S5_SPECHT_MULTIPLICITIES',[(la,int(mult[la])) for la in conjs])
print('FULL_S5_INVARIANT_RATIONAL_H4_DIMENSION',mult[(5,)])
print('GROUP_ELEMENTS_CHECKED',len(perms),'TWO_TRACE_METHODS_AGREE',True)
print('VERIFY_OK_PETERSEN_LINE_GRAPH_EQUIVARIANT_RIPS_FILTRATION')
