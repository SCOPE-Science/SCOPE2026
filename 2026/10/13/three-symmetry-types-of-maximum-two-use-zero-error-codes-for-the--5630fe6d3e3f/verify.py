#!/usr/bin/env python3
from itertools import product, permutations
from collections import Counter, defaultdict
from hashlib import sha256

M=7
V=list(product(range(M), repeat=2))
IDX={v:i for i,v in enumerate(V)}
N=len(V)

def cd(a,b):
    d=(a-b)%M
    return min(d, M-d)

def compatible(a,b):
    # Nonconfusable in C7 \boxtimes C7: at least one coordinate is nonadjacent in C7.
    return any(cd(x,y)>=2 for x,y in zip(a,b))

ADJ=[]
for i,a in enumerate(V):
    mask=0
    for j,b in enumerate(V):
        if i!=j and compatible(a,b):
            mask |= 1<<j
    ADJ.append(mask)

# --- Independent transfer-matrix verification of alpha and leading coefficient. ---
# A layer is an independent subset of a single C7, hence no two chosen residues are adjacent.
layer_states=[]
for mask in range(1<<M):
    ok=True
    for i in range(M):
        if (mask>>i)&1 and ((mask>>((i+1)%M))&1):
            ok=False; break
    if ok:
        layer_states.append(mask)
assert len(layer_states)==29
weights=[m.bit_count() for m in layer_states]

def layer_compatible(a,b):
    # Adjacent first-coordinate layers: selected second-coordinate positions may not be equal or adjacent.
    for i in range(M):
        if (a>>i)&1:
            for j in ((i-1)%M,i,(i+1)%M):
                if (b>>j)&1:
                    return False
    return True
LC=[[layer_compatible(a,b) for b in layer_states] for a in layer_states]

# Polynomial DP around the 7-cycle of first coordinates.
poly=[0]*50
for s0,a0 in enumerate(layer_states):
    # dp[state] -> polynomial counts by total size, after current layer
    dp={s0:{weights[s0]:1}}
    for _ in range(1,M):
        nd=defaultdict(lambda: defaultdict(int))
        for prev,pc in dp.items():
            for nxt in range(len(layer_states)):
                if not LC[prev][nxt]: continue
                w=weights[nxt]
                for deg,c in pc.items():
                    nd[nxt][deg+w]+=c
        dp={k:dict(v) for k,v in nd.items()}
    for last,pc in dp.items():
        if LC[last][s0]:
            for deg,c in pc.items():
                poly[deg]+=c
alpha=max(i for i,c in enumerate(poly) if c)
lead=poly[alpha]
assert alpha==10 and lead==980

# --- Independent maximum-set enumeration normalized to contain (0,0). ---
def color_sort(P):
    order=[]; bounds=[]; U=P; color=0
    while U:
        color+=1
        Q=U
        while Q:
            lsb=Q & -Q
            v=lsb.bit_length()-1
            order.append(v); bounds.append(color)
            U &= ~lsb
            Q &= ~lsb
            Q &= ~ADJ[v]
    return order,bounds

target=10
norm=[]

def enum_target(R,P):
    need=target-len(R)
    if need==0:
        norm.append(tuple(sorted(R))); return
    if P.bit_count()<need:
        return
    order,bounds=color_sort(P)
    if not bounds or bounds[-1]<need:
        return
    for k in range(len(order)-1,-1,-1):
        v=order[k]
        if bounds[k]<need:
            return
        if (P>>v)&1:
            enum_target(R+[v], P & ADJ[v])
            P &= ~(1<<v)
            if P.bit_count()<need:
                return

enum_target([IDX[(0,0)]], ADJ[IDX[(0,0)]])
norm=sorted(set(norm))
assert len(norm)==200

# Expand by all coordinatewise translations; any nonempty maximum can be translated to contain (0,0).
allmax=set()
for C in norm:
    pts=[V[i] for i in C]
    for a in range(M):
        for b in range(M):
            T=tuple(sorted(IDX[((x+a)%M,(y+b)%M)] for x,y in pts))
            allmax.add(T)
assert len(allmax)==980
# Direct compatibility and size check of every enumerated maximum.
for C in allmax:
    assert len(C)==10
    for ii in range(10):
        for jj in range(ii):
            assert compatible(V[C[ii]],V[C[jj]])
# incidence check: maxima containing origin
assert sum(IDX[(0,0)] in C for C in allmax)==200
assert len(allmax)*10 == 200*49

# Natural symmetry group: independent dihedral actions on coordinates and coordinate swap.
GROUP=[]
for swap in (False,True):
    for sx in (1,-1):
        for sy in (1,-1):
            for ax in range(M):
                for ay in range(M):
                    mp=[]
                    for x,y in V:
                        if swap:
                            x,y=y,x
                        mp.append(IDX[((sx*x+ax)%M,(sy*y+ay)%M)])
                    GROUP.append(mp)
assert len(GROUP)==392
assert len({tuple(g) for g in GROUP})==392

def canon(C):
    return min(tuple(sorted(g[i] for i in C)) for g in GROUP)

orbits=defaultdict(list)
for C in allmax:
    orbits[canon(C)].append(C)
assert len(orbits)==3
orbit_sizes=sorted(len(v) for v in orbits.values())
assert orbit_sizes==[196,392,392]

def inv_uv(C):
    u=v=0
    P=[V[i] for i in C]
    for i in range(len(P)):
        for j in range(i):
            ds=tuple(sorted((cd(P[i][0],P[j][0]), cd(P[i][1],P[j][1]))))
            if ds==(0,3): u+=1
            if ds==(2,2): v+=1
    return (u,v)

orbit_rows=[]
for rep,members in orbits.items():
    uv=inv_uv(rep)
    assert all(inv_uv(C)==uv for C in members)
    stab=392//len(members)
    pts=tuple(V[i] for i in rep)
    orbit_rows.append((uv,len(members),stab,pts))
orbit_rows.sort()
assert [(r[0],r[1],r[2]) for r in orbit_rows]==[((0,2),392,1),((1,1),392,1),((1,2),196,2)]

# Every maximum has row and column multiplicities 2,2,2,1,1,1,1.
for C in allmax:
    P=[V[i] for i in C]
    rm=sorted(Counter(x for x,y in P).values(), reverse=True)
    cm=sorted(Counter(y for x,y in P).values(), reverse=True)
    assert rm==[2,2,2,1,1,1,1] and cm==[2,2,2,1,1,1,1]

# Stable hashes of normalized and full maximum lists.
def enc(C):
    return ';'.join(f'{V[i][0]}{V[i][1]}' for i in C)
norm_blob=('\n'.join(enc(C) for C in norm)+'\n').encode()
all_blob=('\n'.join(enc(C) for C in sorted(allmax))+'\n').encode()
norm_sha=sha256(norm_blob).hexdigest()
all_sha=sha256(all_blob).hexdigest()

print('VERIFY_OK '
      f'vertices=49 layer_states=29 maximum={alpha} maxima={len(allmax)} normalized_origin={len(norm)} '
      f'natural_group=392 orbits=3 orbit_sizes=196,392,392 stabilizers=2,1,1 '
      'orbit_fingerprints=(0,2):392;(1,1):392;(1,2):196 '
      'row_col_profile=2,2,2,1,1,1,1 '
      f'normalized_sha256={norm_sha} maxima_sha256={all_sha}')
for uv,size,stab,pts in orbit_rows:
    print('ORBIT',f'uv={uv[0]},{uv[1]}',f'size={size}',f'stabilizer={stab}',
          'rep='+','.join(f'{x}{y}' for x,y in pts))
