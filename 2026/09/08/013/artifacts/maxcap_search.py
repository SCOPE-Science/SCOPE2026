"""CORRECT exhaustive max-search for conic-plus (n,3)-arcs in PG(2,9).
Constraint model (exact): S subset of off-conic points valid iff for every line L
with c=|L cap C|, s=|L cap S|: c+s<=3, i.e.
 - c=2 -> s<=1 (pairwise: pairs whose line is bisecant forbidden),
 - c=1 -> s<=2 (triples on unisecant lines forbidden; 840),
 - c=0 -> s<=3 (quadruples on exterior lines forbidden),
 - c=0 triples allowed; c=1 pairs allowed.
B&B with bitmasks; quadruple pruning via per-line counters.
"""
import itertools, json, time, sys

def add(x,y): return ((x%3)+(y%3))%3 + 3*(((x//3)+(y//3))%3)
def neg(x): return ((-x)%3)+3*((-(x//3))%3)
def mul(x,y):
    u1,v1=x%3,x//3; u2,v2=y%3,y//3
    return (u1*u2-v1*v2)%3+3*((u1*v2+u2*v1)%3)
def inv(x):
    assert x!=0
    for z in range(1,9):
        if mul(x,z)==1: return z

pts=[]; seen=set()
for x in range(9):
    for y in range(9):
        for z in range(9):
            if x==y==z==0: continue
            v=(x,y,z)
            for c in v:
                if c: s=inv(c); break
            key=(mul(x,s),mul(y,s),mul(z,s))
            if key not in seen: seen.add(key); pts.append(key)
N=len(pts); assert N==91
index={p:i for i,p in enumerate(pts)}
def on_line(p,L): return add(add(mul(L[0],p[0]),mul(L[1],p[1])),mul(L[2],p[2]))==0
lines=set()
for i in range(N):
    for j in range(i+1,N):
        x1,y1,z1=pts[i]; x2,y2,z2=pts[j]
        a=add(mul(y1,z2),neg(mul(z1,y2))); b=add(mul(z1,x2),neg(mul(x1,z2))); c=add(mul(x1,y2),neg(mul(y1,x2)))
        for v in (a,b,c):
            if v: s=inv(v); break
        lines.add((mul(a,s),mul(b,s),mul(c,s)))
lines=list(lines); assert len(lines)==91
line_pts=[[i for i,p in enumerate(pts) if on_line(p,L)] for L in lines]
C=set()
for t in range(9): C.add(index[(1,t,mul(t,t))])
C.add(index[(0,0,1)]); assert len(C)==10
off=[i for i in range(N) if i not in C]; n=len(off); pos={v:k for k,v in enumerate(off)}
pair_line={}
for li,S in enumerate(line_pts):
    for a,b in itertools.combinations(S,2): pair_line[(min(a,b),max(a,b))]=li
c_occ=[len(set(S)&C) for S in line_pts]
# pairwise forbidden: line through pair is bisecant
fmask=[0]*n
for k1 in range(n):
    m=0
    for k2 in range(n):
        if k1==k2: continue
        li=pair_line[(min(off[k1],off[k2]),max(off[k1],off[k2]))]
        if c_occ[li]>=2: m|=1<<k2
    fmask[k1]=m
# triples forbidden: on unisecant lines
T1=set()
for li,S in enumerate(line_pts):
    if c_occ[li]==1:
        so=sorted(pos[x] for x in S if x not in C)
        for a,b,c in itertools.combinations(so,3): T1.add((a,b,c))
print("forbidden pairs:",sum(bin(m).count("1") for m in fmask)//2,"unisecant triples:",len(T1),flush=True)
# exterior lines' off-point lists (capacity 3 -> quads forbidden)
ext=[sorted(pos[x] for x in S if x not in C) for li,S in enumerate(line_pts) if c_occ[li]==0]
print("exterior lines:",len(ext),flush=True)
sys.setrecursionlimit(100000)
# order: fewest compatible first to prune
deg=[n-bin(fmask[k]).count("1") for k in range(n)]
order=sorted(range(n),key=lambda k:deg[k])
mp={o:k for k,o in enumerate(order)}
F=[0]*n
for k in range(n):
    m=0
    f=fmask[order[k]]
    kk=0
    while f:  # map bits
        if f&1: m|=1<<mp[kk]
        kk+=1; f>>=1
    F[k]=m
T2=set(tuple(sorted((mp[a],mp[b],mp[c]))) for a,b,c in T1)
EXT=[[mp[k] for k in E] for E in ext]
# greedy incumbent (lex-ish in new order)
cur=set()
for k in range(n):
    if any(((F[k]>>j)&1) for j in cur): continue
    if any(tuple(sorted((k,j1,j2))) in T2 for j1,j2 in itertools.combinations(cur,2)): continue
    bad=False
    for E in EXT:
        if k in E and len(cur & set(E))>=3:
            # would make 4 on exterior line? need all 4 collinear: count cur-on-E +k
            if sum(1 for j in cur if j in set(E))>=3: bad=True; break
    if bad: continue
    cur.add(k)
print("greedy:",len(cur),flush=True)
best=[set(cur)]; nodes=[0]; t0=time.time()
ESET=[set(E) for E in EXT]
CURCAP=8
def expand(cand,cur):
    nodes[0]+=1
    while cand:
        if len(cur)+len(cand)<=len(best[0]): return
        v=cand.pop()
        if any(((F[v]>>j)&1) for j in cur):
            pass
        else:
            tbad=False
            for j1,j2 in itertools.combinations(cur,2):
                if tuple(sorted((v,j1,j2))) in T2: tbad=True; break
            if not tbad:
                qbad=False
                for E in ESET:
                    if v in E:
                        if sum(1 for j in cur if j in E)>=3: qbad=True; break
                if not qbad:
                    nc=[u for u in cand if not ((F[v]>>u)&1)]
                    if len(cur)+1+len(nc)>len(best[0]):
                        expand(nc,cur|{v})
        if len(cur)+len(cand)<=len(best[0]): return
    if len(cur)>len(best[0]):
        best[0]=set(cur); print("new best",len(cur),sorted(cur),flush=True)
expand(list(range(n)),set())
dt=time.time()-t0
wit=sorted(off[order[k]] for k in best[0])
out={"max_off_size":len(best[0]),"witness_off_points":wit,
     "conic_points":sorted(C),"nodes":nodes[0],"seconds":dt,
     "n_forbidden_pairs":sum(bin(m).count("1") for m in fmask)//2,
     "n_unisecant_triples":len(T1)}
json.dump(out,open("output/artifacts/maxcap_result.json","w"),indent=1)
print(json.dumps(out,indent=1),flush=True)
