#!/usr/bin/env python3
"""Exact integral and mod-three computations for an icosahedral matching complex.

Usage: python3 verify_icosahedral_torsion.py
Requires Python 3.9+ standard library only; no network or external data.
"""
from collections import Counter, defaultdict
from functools import reduce
from math import gcd
from heapq import heappush, heappop

N = 12
S = set()
def edge(a,b):
    S.add(tuple(sorted((a,b))))
for i in range(5):
    u, v = 1+i, 6+i
    for a,b in ((0,u),(11,v),(u,1+(i+1)%5),(v,6+(i+1)%5),
                (u,v),(u,6+(i-1)%5)):
        edge(a,b)
E = sorted(S)
assert len(E)==30
adj = [set() for _ in range(N)]
for u,v in E:
    adj[u].add(v);adj[v].add(u)
assert all(len(a)==5 for a in adj)
triangles = [t for t in __import__('itertools').combinations(range(N),3)
             if all(v in adj[u] for u,v in __import__('itertools').combinations(t,2))]
assert len(triangles)==20

# Unique antipode of every vertex, found intrinsically by graph distance.
def distances(i):
    dist={i:0};todo=[i]
    for v in todo:
        for w in adj[v]:
            if w not in dist:
                dist[w]=dist[v]+1;todo.append(w)
    return dist
opp=tuple(next(j for j,d in distances(i).items() if d==3) for i in range(N))
assert all(opp[opp[i]]==i for i in range(N))
assert all(opp[v] in adj[opp[u]] for u,v in E)
edge_index={e:i for i,e in enumerate(E)}
edge_opp=tuple(edge_index[tuple(sorted((opp[u],opp[v])))] for u,v in E)
assert all(edge_opp[edge_opp[i]]==i for i in range(30))

# Every matching, including the empty matching as the augmented -1-cell.
meet=[sum((1<<j) for j,f in enumerate(E) if set(e)&set(f)) for e in E]
faces={-1:[()]}
for d in range(6):
    faces[d]=[a+(j,) for a in faces[d-1]
              for j in range((a[-1]+1) if a else 0,30)
              if all(not(meet[j]&(1<<i)) for i in a)]
assert [len(faces[d]) for d in range(6)]==[30,315,1400,2535,1482,125]

def boundary(a):
    return {a[:k]+a[k+1:]:(-1)**k for k in range(len(a))}

def check_original_chain():
    for d in range(1,6):
        for a in faces[d]:
            comp=defaultdict(int)
            for b,c in boundary(a).items():
                for z,w in boundary(b).items():comp[z]+=c*w
            assert not any(comp.values())
check_original_chain()

# Compute a full group order certificate from exact graph-isomorphism backtracking.
def automorphisms():
    order=[];unassigned=set(range(N))
    while unassigned:
        x=max(unassigned,key=lambda v:(len(adj[v].intersection(order)),
                                          -(min([order.index(u) for u in adj[v].intersection(order)] or [99])),
                                          -v))
        order.append(x);unassigned.remove(x)
    mp={};out=[];used=set()
    def rec(k):
        if k==N:
            out.append(tuple(mp[i] for i in range(N)));return
        v=order[k]
        for w in range(N):
            if w in used:continue
            if all((u in adj[v])==(mp[u] in adj[w]) for u in order[:k]):
                mp[v]=w;used.add(w);rec(k+1);used.remove(w);del mp[v]
    rec(0)
    return out
A=automorphisms()
assert len(A)==120 and len(set(A))==120 and opp in A
idperm=tuple(range(N))
def product(p,q):return tuple(p[q[i]] for i in range(N))
def inverse(p):
    q=[0]*N
    for i,w in enumerate(p):q[w]=i
    return tuple(q)
inv={p:inverse(p) for p in A}
comm={product(product(product(p,q),inv[p]),inv[q]) for p in A for q in A}
assert len(comm)==60 and opp not in comm
assert all(product(p,q) in comm for p in comm for q in comm)
assert all(product(p,opp)==product(opp,p) for p in A)

# Integral algebraic-Morse unit cancellation, preserving the integral chain
# homotopy type at each step. All coefficients are Python arbitrary integers.
B={a:({} if not a else boundary(a)) for F in faces.values() for a in F}
upper={a:set() for a in B}
for b,bd in B.items():
    for a in bd:upper[a].add(b)

def cost(a,b):return (len(upper[a])-1)*(len(B[b])-1)
heap=[]
for b,bd in B.items():
    for a,v in bd.items():
        if abs(v)==1:heappush(heap,(cost(a,b),len(b),a,b))
removed=0
while heap:
    old,d,a,b=heappop(heap)
    if a not in B or b not in B or abs(B[b].get(a,0))!=1:continue
    cst=cost(a,b)
    if cst>old:
        heappush(heap,(cst,d,a,b));continue
    unit=B[b][a]
    for c in tuple(upper[a]):
        if c==b:continue
        factor=B[c][a]//unit
        for z,w in B[b].items():
            if z==a:continue
            prior=B[c].get(z,0);new=prior-factor*w
            if prior and not new:
                del B[c][z];upper[z].discard(c)
            elif new:
                B[c][z]=new;upper[z].add(c)
                if abs(new)==1:heappush(heap,(cost(z,c),len(c),z,c))
        del B[c][a];upper[a].discard(c)
    for c in tuple(upper[b]):
        del B[c][b];upper[b].discard(c)
    for z in B[b]:upper[z].discard(b)
    for z in B[a]:upper[z].discard(a)
    del B[b],B[a],upper[a],upper[b]
    removed+=1
assert removed==2911
assert Counter(len(a)-1 for a in B)=={3:65,4:1}
fourcell=next(a for a in B if len(a)==5)
entries=list(B[fourcell].values())
print("top boundary nnz",len(entries),"gcd",reduce(gcd,map(abs,entries),0))
assert len(entries)>0
assert reduce(gcd,map(abs,entries),0)==3
assert all(B[a]=={} for a in B if len(a)==4)
# A complex with exactly 65 cells in degree 3 and one degree-4 cell,
# whose sole boundary column has entries with gcd exactly 3, has
# H_3 = Z^64 + Z/3 and all other reduced integral homology zero.

# Antipodal eigenspace chain complexes over F_3.
def transform(a):
    v=[edge_opp[i] for i in a]
    parity=sum(v[i]>v[j] for i in range(len(v)) for j in range(i+1,len(v)))
    return tuple(sorted(v)),(-1 if parity%2 else 1)

def eigenspace(e):
    data={}
    for d,F in faces.items():
        seen=set();basis=[];where={}
        for a in F:
            if a in seen:continue
            b,s=transform(a);seen.add(a);seen.add(b)
            if a==b:
                if s==e:
                    where[a]=(len(basis),1);basis.append(((a,1),))
            else:
                at=len(basis)
                basis.append(((a,1),(b,e*s)))
                where[a]=(at,1);where[b]=(at,e*s)
        data[d]=(basis,where)
    return data

def rankp(columns,prime):
    piv={}
    for col in columns:
        v={r:c%prime for r,c in col.items() if c%prime}
        while v:
            r=min(v);c=v[r]
            if r not in piv:
                if c!=1:
                    mult=pow(c,-1,prime);v={x:(mult*y)%prime for x,y in v.items()}
                piv[r]=v;break
            for x,y in piv[r].items():
                z=(v.get(x,0)-c*y)%prime
                if z:v[x]=z
                elif x in v:del v[x]
    return len(piv)

def ranks(e,prime=3):
    D=eigenspace(e); out={}
    for d in range(1,6):
        columns=[]
        for generator in D[d][0]:
            col=defaultdict(int)
            for a,k in generator:
                for b,s in boundary(a).items():
                    if b in D[d-1][1]:
                        index,coef=D[d-1][1][b]
                        # Keep coefficient of the chosen orbit representative.
                        if coef==1:col[index]+=k*s
            columns.append(col)
        out[d]=rankp(columns,prime)
    dim4=len(D[4][0]);h4=dim4-out[4]-out[5]
    h3=len(D[3][0])-out[3]-out[4]
    return dim4,out[4],out[5],h4,h3,out
plus=ranks(1);minus=ranks(-1)
assert plus[:4]==(741,686,55,0)
assert minus[:4]==(741,670,70,1)
assert plus[4]==40 and minus[4]==25
assert [plus[5][i]+minus[5][i] for i in range(1,6)]==[29,286,1114,1356,125]
plus5=ranks(1,5);minus5=ranks(-1,5)
assert plus5[3:5]==(0,40) and minus5[3:5]==(0,24)

# The equivariant coefficient exact sequence yields
# H_4(X; F_3) = Tor(H_3(X; Z), F_3), as H_4(X;Z)=0.
# Thus inversion acts as -1 on the order-three torsion of integral H_3.
# The commutator subgroup has index two and does not contain inversion,
# proving the action of EVERY graph symmetry is its quotient C_2 character.
print('ICOSAHEDRAL_TORSION_ACTION_PASS')
print('face_vector',*[len(faces[d]) for d in range(6)])
print('integral_unit_cancellations',removed,'remaining_dimension_counts',dict(Counter(len(a)-1 for a in B)))
print('remaining_top_boundary_nonzero',len(entries),'gcd',reduce(gcd,map(abs,entries),0))
print('full_group_order',len(A),'commutator_subgroup_order',len(comm))
print('antipodal_plus_dim_rank4_rank5_H4mod3_H3mod3',plus[:5])
print('antipodal_minus_dim_rank4_rank5_H4mod3_H3mod3',minus[:5])
print('antipodal_plus_H3mod5',plus5[4],'antipodal_minus_H3mod5',minus5[4])
print('ranks_mod5_plus',plus5[5], 'ranks_mod5_minus',minus5[5])
