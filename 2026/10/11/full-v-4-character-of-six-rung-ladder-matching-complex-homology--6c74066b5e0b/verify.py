#!/usr/bin/env python3
from itertools import combinations
from collections import defaultdict, deque

N=6
V=[(r,c) for c in range(N) for r in (0,1)]
edges=[]
for c in range(N): edges.append(((0,c),(1,c)))
for r in (0,1):
    for c in range(N-1): edges.append(((r,c),(r,c+1)))
edges=[tuple(sorted(e)) for e in edges]
edge_index={e:i for i,e in enumerate(edges)}
assert len(edges)==16 and len(set(edges))==16
adj={v:set() for v in V}
for a,b in edges: adj[a].add(b); adj[b].add(a)

def is_matching(ids):
    used=set()
    for i in ids:
        a,b=edges[i]
        if a in used or b in used: return False
        used|={a,b}
    return True

faces=[]
for k in range(1,7):
    for s in combinations(range(len(edges)),k):
        if is_matching(s): faces.append(s)
F=set(faces)
bydim=defaultdict(list)
for f in faces: bydim[len(f)-1].append(f)
fvec=[len(bydim[d]) for d in range(max(bydim)+1)]
assert fvec==[16,92,234,263,114,13], fvec
covers=sum(len(f) for f in faces if len(f)>1)
assert covers==2586, covers

# Staged element matching: for edge-index v, pair an unmatched face s not containing v
# with s U {v} whenever both are currently unmatched faces.
unmatched=set(F); pairs=[]
for v in range(len(edges)):
    for s in sorted(list(unmatched), key=lambda x:(len(x),x)):
        if s not in unmatched or v in s: continue
        t=tuple(sorted(s+(v,)))
        if t in unmatched:
            unmatched.remove(s); unmatched.remove(t); pairs.append((s,t))
assert len(pairs)==363
crit=sorted(unmatched,key=lambda x:(len(x),x))
expected_crit=[(0,), (6,8,10,14), (6,9,12,15), (6,9,13,15), (7,9,11,15), (7,10,11,14)]
assert crit==expected_crit, crit

# Complete directed Hasse graph: unmatched cover arrows point downward; matched arrows reversed.
pairset={(a,b) for a,b in pairs}
out=defaultdict(list); indeg={f:0 for f in faces}
for t in faces:
    if len(t)<=1: continue
    for j in range(len(t)):
        s=t[:j]+t[j+1:]
        if (s,t) in pairset:
            out[s].append(t); indeg[t]+=1
        else:
            out[t].append(s); indeg[s]+=1
q=deque([f for f in faces if indeg[f]==0]); seen=0
while q:
    x=q.popleft(); seen+=1
    for y in out[x]:
        indeg[y]-=1
        if indeg[y]==0:q.append(y)
assert seen==len(faces), (seen,len(faces))

# Graph automorphisms via exact backtracking with adjacency constraints.
verts=V
sig={v:(len(adj[v]), tuple(sorted(len(adj[w]) for w in adj[v]))) for v in verts}
classes=defaultdict(list)
for v in verts: classes[sig[v]].append(v)
order=sorted(verts,key=lambda v:(len(classes[sig[v]]),-len(adj[v]),v))
autos=[]

def backtrack(i,m,used):
    if i==len(order):
        autos.append(dict(m)); return
    v=order[i]
    for w in classes[sig[v]]:
        if w in used: continue
        ok=True
        for u,mu in m.items():
            if ((u in adj[v]) != (mu in adj[w])):
                ok=False; break
        if ok:
            m[v]=w; used.add(w); backtrack(i+1,m,used); used.remove(w); del m[v]
backtrack(0,{},set())
assert len(autos)==4, len(autos)

def h(v): r,c=v; return (1-r,c)
def vflip(v): r,c=v; return (r,N-1-c)
def hv(v): return h(vflip(v))
gens={'1':lambda x:x,'h':h,'v':vflip,'hv':hv}
canon=lambda m: tuple(m[x] for x in sorted(verts))
autoset={canon(m) for m in autos}
for fn in gens.values(): assert tuple(fn(x) for x in sorted(verts)) in autoset

# Induced edge permutations.
def edge_perm(fn):
    p=[]
    for e in edges:
        im=tuple(sorted((fn(e[0]),fn(e[1]))))
        assert im in edge_index
        p.append(edge_index[im])
    return p
perms={name:edge_perm(fn) for name,fn in gens.items()}

# sign of permutation induced on sorted vertices of a setwise-fixed oriented simplex.
def perm_sign(seq):
    inv=0
    for i in range(len(seq)):
        for j in range(i+1,len(seq)):
            inv += seq[i]>seq[j]
    return -1 if inv%2 else 1

def chain_trace(p,d):
    tr=0
    for f in bydim[d]:
        img=tuple(sorted(p[i] for i in f))
        if img!=f: continue
        pos={x:j for j,x in enumerate(f)}
        seq=[pos[p[i]] for i in f]
        tr += perm_sign(seq)
    return tr

traces={name:[chain_trace(p,d) for d in range(6)] for name,p in perms.items()}
expected_traces={
    '1':[16,92,234,263,114,13],
    'h':[6,10,0,-9,-2,1],
    'v':[2,-6,-10,7,8,-1],
    'hv':[0,-8,0,15,0,-5],
}
assert traces==expected_traces, traces
lefs={name:sum(((-1)**d)*x for d,x in enumerate(ts)) for name,ts in traces.items()}
assert lefs=={'1':-4,'h':2,'v':0,'hv':-2},lefs
# With one critical 0-cell and five critical 3-cells, reduced homology is only H_3, rank 5.
# L(g)=tr(H_0)-tr(H_1)+...=1-tr(H_3), hence tr(H_3)=1-L(g).
char={name:1-lefs[name] for name in gens}
assert char=={'1':5,'h':-1,'v':1,'hv':3},char

# Decompose V4 character into one-dimensional rational characters chi_{a,b},
# where h acts by a and v by b.
mult={}
for a in (1,-1):
    for b in (1,-1):
        val=(char['1']+a*char['h']+b*char['v']+a*b*char['hv'])//4
        mult[(a,b)]=val
assert mult=={(1,1):2,(1,-1):0,(-1,1):1,(-1,-1):2},mult

# Independent mod-p homology check using all boundary matrices.
def rank_mod(mat,p):
    if not mat:return 0
    A=[row[:] for row in mat]
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]%p),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c]%p,-1,p)
        A[r]=[(x*inv)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%p:
                q=A[i][c]%p
                A[i]=[(A[i][j]-q*A[r][j])%p for j in range(n)]
        r+=1
        if r==m:break
    return r

def boundary_rank(d,p):
    if d<=0:return 0
    rows=bydim[d-1]; cols=bydim[d]
    ridx={f:i for i,f in enumerate(rows)}
    A=[[0]*len(cols) for _ in rows]
    for j,f in enumerate(cols):
        for k in range(len(f)):
            s=f[:k]+f[k+1:]
            A[ridx[s]][j]=(1 if k%2==0 else -1)%p
    return rank_mod(A,p)
for p in (2,3,5):
    ranks=[0]+[boundary_rank(d,p) for d in range(1,6)]+[0]
    betti=[]
    dims=fvec
    for d in range(6):
        betti.append(dims[d]-ranks[d]-ranks[d+1])
    assert betti==[1,0,0,5,0,0],(p,betti,ranks)

print('VERIFY_OK')
print('vertices=12 edges=16 faces=732 hasse_covers=2586 matched_pairs=363')
print('critical_cells=1_in_dim0,5_in_dim3')
print('aut_group_order=4 generators=h(row_swap),v(column_reversal)')
print('chain_traces=',traces)
print('H3_character=',char)
print('V4_multiplicities=',mult)
print('mod_p_betti=[1,0,0,5,0,0] for p=2,3,5')
