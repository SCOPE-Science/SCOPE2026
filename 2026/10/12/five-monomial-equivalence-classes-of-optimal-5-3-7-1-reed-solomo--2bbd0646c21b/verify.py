"""Exact classification of coordinate-equivalence classes of optimal RS sunflowers over F7.
Python >=3.9, standard library only. The computation enumerates all finite objects.
"""
from itertools import permutations
from collections import Counter

P = 7

def rank(rows):
    a = [[int(x) % P for x in row] for row in rows]
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None: continue
        a[r], a[pivot] = a[pivot], a[r]
        u = pow(a[r][j], -1, P)
        a[r] = [x * u % P for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][j]:
                u = a[i][j]
                a[i] = [(x - u*y)%P for x,y in zip(a[i],a[r])]
        r += 1
        if r == len(a):break
    return r

V = [(0,1)+t for t in permutations(range(2,7),3)]
VI = {x:i for i,x in enumerate(V)}
assert len(V)==60
A = [0]*len(V)
for i,x in enumerate(V):
    for j in range(i):
        y = V[j]
        # Nonconstant intersection iff these five columns have rank less than 5.
        if rank([[1,u,u*u,v,v*v] for u,v in zip(x,y)]) == 5:
            A[i] |= 1<<j
            A[j] |= 1<<i
assert sum(s.bit_count() for s in A)//2==1200
assert {s.bit_count() for s in A}=={40}

# Bron-Kerbosch full enumeration with exact pivoting of 60-vertex compatibility graph.
maximal = []
def bron(r,p,x):
    if not (p or x):
        maximal.append(tuple(sorted(r)))
        return
    union=p|x
    pivot=max((u for u in range(len(V)) if (union>>u)&1),
              key=lambda u:(p&A[u]).bit_count()) if union else None
    candidates=p & (~A[pivot] if pivot is not None else -1)
    while candidates:
        bit = candidates & -candidates
        v = bit.bit_length()-1
        bron(r+(v,),p&A[v],x&A[v])
        p &= ~bit
        x |= bit
        candidates &= ~bit
bron((),(1<<len(V))-1,0)
H=Counter(map(len,maximal))
assert H==Counter({6:30,7:1920,8:5070,9:1800,10:138}), H
M={c for c in maximal if len(c)==10}
assert len(M)==138

# Independent, direct enumeration of every 10-clique using increasing labels.
direct=[]
def extension(clique,candidates):
    if len(clique)==10:
        direct.append(clique)
        return
    if len(clique)+candidates.bit_count()<10:
        return
    while candidates:
        bit=candidates & -candidates
        v=bit.bit_length()-1
        candidates &= ~bit
        extension(clique+(v,), candidates&A[v])
extension((),(1<<60)-1)
assert set(direct)==M and len(direct)==138

# S5 actions on normalized affine classes, induced by coordinate permutations.
permmaps=[]
for sigma in permutations(range(5)):
    pmap=[]
    for alpha in V:
        b=[alpha[h] for h in sigma]
        d=pow((b[1]-b[0])%P,-1,P)
        norm=tuple(((t-b[0])*d)%P for t in b)
        pmap.append(VI[norm])
    assert len(set(pmap))==60
    permmaps.append(tuple(pmap))
assert len(set(permmaps))==120

remain=set(M)
orbits=[]
while remain:
    c=min(remain)
    orb={tuple(sorted(phi[v] for v in c)) for phi in permmaps}
    assert orb<=M
    stabilizers=sum(tuple(sorted(phi[v] for v in c))==c for phi in permmaps)
    assert len(orb)*stabilizers==120
    orbits.append((len(orb),stabilizers,c))
    remain.difference_update(orb)
assert not remain
orbits.sort()
assert [(s,t) for s,t,_ in orbits]==[(6,20),(12,10),(30,4),(30,4),(60,2)]
assert sum(s for s,t,_ in orbits)==len(M)

# Element-order fingerprints identify the stabilizers, including two distinct C4 orbits.
perms = list(permutations(range(5)))
def compose(a,b):
    return tuple(a[b[i]] for i in range(5))
def group_order(a):
    v=tuple(range(5))
    for n in range(1,121):
        v=compose(v,a)
        if v==tuple(range(5)):
            return n
    raise AssertionError('not finite order dividing 120')
orders=[]
for sz,stab,c in orbits:
    fixed=[p for p,phi in zip(perms,permmaps) if tuple(sorted(phi[v] for v in c))==c]
    assert len(fixed)==stab
    orders.append(dict(sorted(Counter(map(group_order,fixed)).items())))
assert orders==[{1:1,2:5,4:10,5:4},{1:1,2:5,5:4},
                {1:1,2:1,4:2},{1:1,2:1,4:2},{1:1,2:1}]
print('DISTINCT_RS_CODES',len(V))
print('COMPATIBILITY_EDGES',sum(a.bit_count() for a in A)//2)
print('MAXIMAL_CLIQUE_HISTOGRAM',dict(sorted(H.items())))
print('MAXIMUM_FAMILIES',len(M))
print('COORDINATE_EQUIVALENCE_ORBITS',len(orbits))
print('ORBIT_SIZE_STABILIZER',[(s,t) for s,t,_ in orbits])
print('STABILIZER_ELEMENT_ORDERS',orders)
for k,(s,t,c) in enumerate(orbits,1):
    print('REP',k,'size',s,'stab',t,':',','.join(''.join(map(str,V[v])) for v in c))
print('VERIFY_OK')
