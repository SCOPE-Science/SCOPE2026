#!/usr/bin/env python3
"""Exact chain, cycle-certificate and 336-automorphism checks for the Heawood two-point space.
Run with Python 3 using heawood_cycles.json in the same directory.
"""
import json
from collections import Counter, deque, defaultdict
from itertools import combinations, product
from pathlib import Path

def rank_mod(cols, p):
    piv = {}
    for col in cols:
        v = {i:(a % p) for i,a in col.items() if a % p}
        while v:
            i=min(v)
            if i not in piv:
                scalar=pow(v[i],-1,p)
                piv[i]={j:(scalar*a)%p for j,a in v.items() if scalar*a%p}
                break
            scalar=v[i]
            for j,a in piv[i].items():
                w=(v.get(j,0)-scalar*a)%p
                if w:v[j]=w
                else:v.pop(j,None)
    return len(piv)

def dot(a,b):return ((a & b).bit_count())%2

def image(A,x):
    y=0
    for j in range(3):
        if (x>>j)&1:y^=A[j]
    return y

def inverse(A):
    return tuple(next(x for x in range(8) if image(A,x)==(1<<j)) for j in range(3))

def transpose(A):
    return tuple(sum(((A[j]>>i)&1)<<j for j in range(3)) for i in range(3))

def permutation_order(g):
    q=list(range(len(g)))
    for k in range(1,100):
        q=[g[x] for x in q]
        if q==list(range(len(g))):return k
    raise AssertionError('not finite-order')

def build():
    vertices=range(14)
    E=[(i,7+j) for i in range(7) for j in range(7) if dot(i+1,j+1)==0]
    C0=list(combinations(vertices,2))
    C1=[(k,v) for k,e in enumerate(E) for v in vertices if v not in e]
    C2=[(i,j) for i,j in combinations(range(len(E)),2) if len(set(E[i]+E[j]))==4]
    assert len(E)==21 and (len(C0),len(C1),len(C2))==(91,252,168)
    zidx={frozenset(c):k for k,c in enumerate(C0)}
    oidx={c:k for k,c in enumerate(C1)}
    d1=[]
    for k,v in C1:
        a,b=E[k]
        d1.append({zidx[frozenset((a,v))]:-1,zidx[frozenset((b,v))]:1})
    d2=[]
    for i,j in C2:
        a,b=E[i]; c,d=E[j]
        col={oidx[(j,b)]:1,oidx[(j,a)]:-1,oidx[(i,c)]:1,oidx[(i,d)]:-1}
        test={}
        for row,coef in col.items():
            for target,coef2 in d1[row].items():test[target]=test.get(target,0)+coef*coef2
        assert all(t==0 for t in test.values())
        d2.append(col)
    return E,C0,C1,C2,d1,d2

def trace(g,E,C0,C1,C2):
    idx={frozenset(e):i for i,e in enumerate(E)}
    edges=[]
    for a,b in E:
        aa,bb=g[a],g[b]
        j=idx[frozenset((aa,bb))]
        edges.append((j,1 if E[j]==(aa,bb) else -1))
    z=sum(frozenset((g[a],g[b]))==frozenset((a,b)) for a,b in C0)
    o=sum(s for i,v in C1 for j,s in [edges[i]] if j==i and g[v]==v)
    t=0
    for i,j in C2:
        ii,si=edges[i]; jj,sj=edges[j]
        if {ii,jj}=={i,j}:t+=si*sj*(1 if ii<jj else -1)
    vg=sum(g[v]==v for v in range(14))
    eg=sum(s for i,(j,s) in enumerate(edges) if i==j)
    h1=eg-vg+1
    h2=z-o+t-1+h1
    return z,o,t,vg,eg,h1,h2

def check_graph_cycles(E):
    adj={i:[] for i in range(14)}
    for a,b in E:adj[a].append(b);adj[b].append(a)
    assert all(len(adj[v])==3 for v in range(14))
    depths={0:0};parent={0:-1};Q=deque([0])
    while Q:
        x=Q.popleft()
        for y in adj[x]:
            if y not in depths:depths[y]=depths[x]+1;parent[y]=x;Q.append(y)
    assert len(depths)==14 and max(depths.values())<=3
    tree={frozenset((v,p)) for v,p in parent.items() if p>=0}
    assert len(tree)==13 and len(E)-len(tree)==8
    # Every fundamental cycle lies entirely in <= 7 vertices, so a stationary particle exists.
    for a,b in E:
        if frozenset((a,b)) in tree:continue
        a_anc=set();x=a
        while x!=-1:a_anc.add(x);x=parent[x]
        x=b;bd=0
        while x not in a_anc:bd+=1;x=parent[x]
        meet=x;ad=0;x=a
        while x!=meet:ad+=1;x=parent[x]
        assert ad+bd+1<=7

E,C0,C1,C2,d1,d2=build()
check_graph_cycles(E)
assert rank_mod(d1,3)==90
assert rank_mod(d2,3)==154
# Fourteen independent rational cycles force rank(d2) <= 168-14 = 154;
# a nonzero 154-minor modulo 3 forces the opposite inequality over Q.
cert=json.loads((Path(__file__).parent/'heawood_cycles.json').read_text('utf-8'))
assert len(cert['cycles'])==14
cy=[{int(k):int(v) for k,v in c.items()} for c in cert['cycles']]
assert rank_mod(cy,3)==14
for col in cy:
    boundary={}
    for i,coef in col.items():
        for row,val in d2[i].items():boundary[row]=boundary.get(row,0)+coef*val
    assert all(x==0 for x in boundary.values())
assert len(C2)-154==14
assert len(C1)-90-154==8
assert rank_mod(d2,2)==153  # Detects the established extra mod-two first-homology class.

matrices=[A for A in product(range(1,8),repeat=3) if len({image(A,x) for x in range(8)})==8]
assert len(matrices)==168
expected={('col',1):(1,14),('col',2):(21,-2),('col',3):(56,-1),('col',4):(42,2),('col',7):(48,0),('dual',2):(28,-2),('dual',6):(56,1),('dual',8):(84,0)}
observed=Counter()
for A in matrices:
    I=transpose(inverse(A))
    for swap in (False,True):
        g=([7+image(I,x)-1 if swap else image(A,x)-1 for x in range(1,8)]
           +[image(A,x)-1 if swap else 7+image(I,x)-1 for x in range(1,8)])
        assert set(frozenset((g[a],g[b])) for a,b in E)==set(map(frozenset,E))
        o=permutation_order(g)
        val=trace(g,E,C0,C1,C2)
        observed[(('dual' if swap else 'col'),o,val[-1])]+=1
assert sum(observed.values())==336
for (kind,order),(size,t) in expected.items():
    assert observed[(kind,order,t)]==size,(kind,order,t,observed)
assert len(observed)==len(expected)
assert sum(size*t for size,t in expected.values())==0
assert (14**2+21*4+56+42*4+28*4+56)==672  # character self inner product = 2
print('HEAWOOD_VERIFY_OK')
print('cells C0=91 C1=252 C2=168; rankZ2=154 rankZ1=90; 14 integral independent top cycles')
for key,(size,val) in expected.items():print(f'{key[0]} order {key[1]}: elements={size}, H2 character={val}')
print('full symmetry order=336; H2 invariants=0; H2 character inner product=2')
