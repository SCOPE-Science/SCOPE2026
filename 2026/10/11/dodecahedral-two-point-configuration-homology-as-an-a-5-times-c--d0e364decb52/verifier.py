#!/usr/bin/env python3
import itertools, json, math, os
from collections import Counter, defaultdict

HERE=os.path.dirname(os.path.abspath(__file__))
CERT=json.load(open(os.path.join(HERE,'kernel_certificate.json'),encoding='utf-8'))

# Generalized Petersen graph G(10,2), the dodecahedral graph.
V=tuple(range(20))
Eset=set()
for i in range(10):
    Eset.add(tuple(sorted((i,(i+1)%10))))
    Eset.add(tuple(sorted((i,10+i))))
    Eset.add(tuple(sorted((10+i,10+((i+2)%10)))))
E=tuple(sorted(Eset)); Eidx={e:i for i,e in enumerate(E)}
adj={v:set() for v in V}
for a,b in E:
    adj[a].add(b); adj[b].add(a)
assert len(E)==30 and all(len(adj[v])==3 for v in V)

C0=tuple(itertools.combinations(V,2)); I0={c:i for i,c in enumerate(C0)}
C1=tuple((e,v) for e in E for v in V if v not in e); I1={c:i for i,c in enumerate(C1)}
C2=tuple((e,f) for e,f in itertools.combinations(E,2) if set(e).isdisjoint(f)); I2={c:i for i,c in enumerate(C2)}
assert (len(C0),len(C1),len(C2))==(190,540,375)

# Degree-2 boundary columns, using product orientation on the ordered pair e<f.
d2cols=[]
for e,f in C2:
    a,b=e; c,d=f
    d2cols.append(((I1[(f,b)],1),(I1[(f,a)],-1),(I1[(e,d)],-1),(I1[(e,c)],1)))

# The 1-skeleton is the graph on C0 whose edges are C1. Connectedness implies rank(d1)=189 over Q.
conf_adj=[set() for _ in C0]
for e,v in C1:
    a,b=e
    x=I0[tuple(sorted((a,v)))]; y=I0[tuple(sorted((b,v)))]
    conf_adj[x].add(y); conf_adj[y].add(x)
seen={0}; stack=[0]
while stack:
    x=stack.pop()
    for y in conf_adj[x]:
        if y not in seen: seen.add(y); stack.append(y)
assert len(seen)==len(C0)
rank_d1=len(C0)-1

# Upper bound rank(d2)<=339: verify 36 linearly independent integral kernel vectors.
free=CERT['free_rows']; sparse=CERT['kernel_basis_sparse']
assert CERT['cell2_count']==len(C2) and CERT['cell1_count']==len(C1)
assert len(free)==len(sparse)==36 and len(set(free))==36
for j,vec in enumerate(sparse):
    vd=dict(vec)
    # identity coordinates make the 36 cycles visibly independent over every field
    for k,r in enumerate(free):
        assert vd.get(r,0)==(1 if j==k else 0)
    out=[0]*len(C1)
    for col,coef in vec:
        for row,s in d2cols[col]: out[row]+=coef*s
    assert not any(out)

# Lower bound rank(d2)>=339: exact GF(2) row rank using Python integer bitsets.
rows=[0]*len(C1)
for j,col in enumerate(d2cols):
    bit=1<<j
    for r,s in col:
        rows[r]^=bit  # signs disappear mod 2
basis={}
for x in rows:
    while x:
        p=x.bit_length()-1
        if p in basis: x^=basis[p]
        else:
            basis[p]=x
            break
rank_d2_mod2=len(basis)
assert rank_d2_mod2==339
rank_d2=339
b0=1; b1=len(C1)-rank_d1-rank_d2; b2=len(C2)-rank_d2
assert (b0,b1,b2)==(1,12,36)

# Enumerate all graph automorphisms. Fixing a vertex and a permutation of its three neighbors
# determines at most one automorphism; a small constraint search completes the map.
def complete_seed(seed):
    mp=dict(seed); used=set(mp.values()); sols=[]
    def rec():
        if len(mp)==len(V):
            sols.append(tuple(mp[v] for v in V)); return
        un=[u for u in V if u not in mp]
        # Most constrained first: maximize number of already mapped neighbors/nonneighbors.
        u=max(un,key=lambda x:sum(1 for y in adj[x] if y in mp))
        cands=[]
        for y in V:
            if y in used: continue
            ok=True
            for x,yx in mp.items():
                if ((x in adj[u]) != (yx in adj[y])):
                    ok=False; break
            if ok: cands.append(y)
        for y in cands:
            mp[u]=y; used.add(y); rec(); used.remove(y); del mp[u]
            if len(sols)>1: return
    rec();
    return sols

autset=set(); n0=sorted(adj[0])
for a in V:
    na=sorted(adj[a])
    for perm in itertools.permutations(na):
        seed={0:a, n0[0]:perm[0], n0[1]:perm[1], n0[2]:perm[2]}
        for sol in complete_seed(seed): autset.add(sol)
auts=sorted(autset)
assert len(auts)==120

def compose(g,h): return tuple(g[h[v]] for v in V)
def order(g):
    seen=set(); out=1
    for v in V:
        if v in seen: continue
        w=v; n=0
        while w not in seen:
            seen.add(w); w=g[w]; n+=1
        out=math.lcm(out,n)
    return out

def parity(perm):
    seen=set(); cycles=0
    for i in range(len(perm)):
        if i in seen: continue
        cycles+=1; j=i
        while j not in seen:
            seen.add(j); j=perm[j]
    return -1 if (len(perm)-cycles)%2 else 1

def edge_sign(g):
    ep=[]
    for a,b in E: ep.append(Eidx[tuple(sorted((g[a],g[b])))])
    return parity(ep)

def commutes(g,h): return compose(g,h)==compose(h,g)
center=[g for g in auts if all(commutes(g,h) for h in auts)]
assert len(center)==2
idg=tuple(V); z=next(g for g in center if g!=idg)
assert order(z)==2 and edge_sign(z)==-1
assert Counter(edge_sign(g) for g in auts)==Counter({1:60,-1:60})

# Precompute signed cell actions on C1 and C2.
def oriented_edge_image(g,e):
    a,b=e; ga,gb=g[a],g[b]
    return tuple(sorted((ga,gb))), (1 if ga<gb else -1)

def action_c2(g,j):
    e,f=C2[j]
    ee,se=oriented_edge_image(g,e); ff,sf=oriented_edge_image(g,f)
    sw=1
    if ee>ff: ee,ff=ff,ee; sw=-1
    return I2[(ee,ff)],se*sf*sw

def h2_trace(g):
    # The basis has identity coordinates at free[j], so the j-th diagonal entry is
    # exactly the coefficient of free[j] in g(kernel_basis[j]).
    total=0
    for j,vec in enumerate(sparse):
        target=free[j]
        coeff=0
        for src,a in vec:
            dest,s=action_c2(g,src)
            if dest==target: coeff += a*s
        total+=coeff
    return total

def chain_traces(g):
    t0=t1=t2=0
    for a,b in C0:
        if tuple(sorted((g[a],g[b])))==(a,b): t0+=1
    for e,v in C1:
        ee,s=oriented_edge_image(g,e)
        if ee==e and g[v]==v: t1+=s
    for j in range(len(C2)):
        d,s=action_c2(g,j)
        if d==j: t2+=s
    return t0,t1,t2

records=[]
for g in auts:
    eps=edge_sign(g)
    r=g if eps==1 else compose(z,g)
    ro=order(r)
    assert ro in (1,2,3,5)
    tr2=h2_trace(g)
    c0,c1,c2=chain_traces(g)
    lefs=c0-c1+c2
    tr1=1+tr2-lefs
    records.append((eps,ro,tr1,tr2))
classes=Counter(records)
expected={
 (1,1,12,36):1,(1,2,0,-4):15,(1,3,0,0):20,(1,5,2,1):24,
 (-1,1,0,-6):1,(-1,2,-4,2):15,(-1,3,0,0):20,(-1,5,0,-1):24,
}
assert classes==Counter(expected)

# Rational A5 irreducible characters on the merged classes 1,2,3,5.
chi1=(1,1,1,1); chi4=(4,0,1,-1); chi5=(5,1,-1,0); chi6=(6,-2,0,1)
def add(*vs): return tuple(sum(x) for x in zip(*vs))
# central + and - eigenspace characters recovered from chi(g) and chi(zg)
h1plus=(6,-2,0,1); h1minus=(6,2,0,1)
h2plus=(15,-1,0,0); h2minus=(21,-3,0,1)
assert h1plus==chi6
assert h1minus==add(chi1,chi5)
assert h2plus==add(chi4,chi5,chi6)
assert h2minus==add(chi4,chi5,chi6,chi6)

print('VERIFY_OK')
print('graph: |V|=20 |E|=30, discrete UConf_2 cells=(190,540,375)')
print('boundary ranks over Q: rank d1=189, rank d2=339; Betti=(1,12,36)')
print('Aut(D): 120 elements; center C2; edge-sign kernel has class counts 1,15,20,24 for orders 1,2,3,5')
print('H1 character, rotations orders 1/2/3/5:', (12,0,0,2))
print('H1 character after central inversion:', (0,-4,0,0))
print('H2 character, rotations orders 1/2/3/5:', (36,-4,0,1))
print('H2 character after central inversion:', (-6,2,0,-1))
print('decomposition H1: V6^+ + (1+V5)^-')
print('decomposition H2: (V4+V5+V6)^+ + (V4+V5+2V6)^-')
