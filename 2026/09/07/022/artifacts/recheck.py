"""Independent recheck: replays all logs, recomputes canonical/BFS, asserts closure/growth."""
import csv, sys
sys.path.insert(0,'.')
import numpy as np, itertools, collections
pairs=[(i,j) for i in range(5) for j in range(i+1,5)]
pair_to_col={p:k for k,p in enumerate(pairs)}
perms=list(itertools.permutations(range(5)))
def mutate(B,k):
    n=B.shape[0]
    Bp=B.copy()
    for i in range(n):
        for j in range(n):
            if i==k or j==k:
                Bp[i,j]=-B[i,j]
            else:
                Bp[i,j]=B[i,j]+(abs(int(B[i,k]))*int(B[k,j])+int(B[i,k])*abs(int(B[k,j])))//2
    return Bp
def key(B): return tuple(int(x) for x in B.reshape(-1))
def canon(B):
    best=None
    for p in perms:
        P=np.array(p)
        Bp=B[np.ix_(P,P)]
        k=key(Bp)
        if best is None or k<best:
            best=k
    return best
def triple(B,i,j,k):
    p=abs(int(B[i,j])); q=abs(int(B[j,k])); r=abs(int(B[k,i]))
    if p==0 or q==0 or r==0:
        cyc=False
    else:
        s1=1 if B[i,j]>0 else -1; s2=1 if B[j,k]>0 else -1; s3=1 if B[k,i]>0 else -1
        cyc=(s1==s2==s3)
    C=p*p+q*q+r*r-p*q*r
    return p,q,r,cyc,C

print("== recheck representatives ==")
reps=[]
with open("artifacts/representatives.csv") as f:
    r=csv.DictReader(f)
    for row in r:
        reps.append(row)
print(f"{len(reps)} classes")
assert len(reps)==7, "expected 7"
# verify lex-min + closure + order
for row in reps:
    v=list(map(int,row["lexmin_vals_10"].split(";")))
    B=np.zeros((5,5),dtype=int)
    for k,(a,b) in enumerate(pairs):
        B[a,b]=v[k]; B[b,a]=-v[k]
    # lex-min check
    assert key(B)==canon(B), f"rep {row['class_id']} not lex-min among S5 orbit!"
    # BFS closure within bound 2
    start=key(B)
    vis={start:B.copy()}
    from collections import deque
    q=deque([start])
    while q:
        cur=q.popleft()
        Bc=vis[cur]
        for kk in range(5):
            Bp=mutate(Bc,kk)
            assert int(np.max(np.abs(Bp)))<=20 or True  # allow big? For finite should stay <=2
            if int(np.max(np.abs(Bp)))>2:
                raise AssertionError(f"rep {row['class_id']} exceeds bound 2 -> not finite!")
            kkp=key(Bp)
            if kkp not in vis:
                vis[kkp]=Bp
                q.append(kkp)
    assert len(vis)==int(row["N_labeled"]), f"order mismatch {row['class_id']}: {len(vis)} vs {row['N_labeled']}"
    print(f"class {row['class_id']}: N={len(vis)} OK lex-min+closed")

print("== recheck distinctness (canonical sets disjoint) ==")
# recompute canonical sets for each rep's component (reuse BFS above? redo quickly with sets)
cans_list=[]
for row in reps:
    v=list(map(int,row["lexmin_vals_10"].split(";")))
    B=np.zeros((5,5),dtype=int)
    for k,(a,b) in enumerate(pairs):
        B[a,b]=v[k]; B[b,a]=-v[k]
    start=key(B)
    vis={start:B.copy()}
    from collections import deque
    q=deque([start])
    while q:
        cur=q.popleft()
        Bc=vis[cur]
        for kk in range(5):
            Bp=mutate(Bc,kk)
            kkp=key(Bp)
            if kkp not in vis:
                vis[kkp]=Bp
                q.append(kkp)
    s=set(canon(vis[k]) for k in vis)
    cans_list.append(s)
    print(f"class {row['class_id']}: {len(s)} orbits")
for i in range(len(cans_list)):
    for j in range(i+1,len(cans_list)):
        assert cans_list[i].isdisjoint(cans_list[j]), f"classes {i},{j} overlap!"
print("disjoint OK")

print("== recheck Wfin D5 ==")
# load adj + log, verify closure (no missing neighbors) and path replay
nodes={}
with open("artifacts/Wfin_D5_log.csv") as f:
    r=csv.DictReader(f)
    for row in r:
        nodes[int(row["node_id"])]=row
assert len(nodes)==2184
# pick rep (dist 0)
rep_row=[row for row in nodes.values() if int(row["dist_from_rep"])==0][0]
rep_key=tuple(map(int,rep_row["flat25"].split(";")))
Brep=np.array(rep_key,dtype=int).reshape(5,5)
# verify each node's path replays
for nid,row in nodes.items():
    flat=tuple(map(int,row["flat25"].split(";")))
    path=[] if row["path_mutations"]=="" else list(map(int,row["path_mutations"].split(",")))
    assert len(path)==int(row["dist_from_rep"])
    B=Brep.copy()
    for kk in path:
        B=mutate(B,kk)
    assert key(B)==flat, f"Wfin node {nid} replay failed"
print("Wfin paths OK (2184 nodes)")
# closure: load adj, verify each node's 5 mutants present
adj={}
with open("artifacts/Wfin_D5_adj.csv") as f:
    r=csv.DictReader(f)
    for row in r:
        adj[int(row["node_id"])]=row
key_to_id={tuple(map(int,row["flat25"].split(";"))):int(row["node_id"]) for row in nodes.values()}
for nid,row in adj.items():
    flat=tuple(map(int,row["flat25"].split(";")))
    B=np.array(flat,dtype=int).reshape(5,5)
    for kk in range(5):
        Bp=mutate(B,kk)
        assert key(Bp) in key_to_id, f"Wfin closure failed at {nid} mut {kk} max {np.max(np.abs(Bp))}"
        assert int(np.max(np.abs(Bp)))<=2
print("Wfin closure OK (all 5*2184 neighbors inside, max<=2)")

print("== recheck Winf ==")
steps=[]
with open("artifacts/Winf_log.csv") as f:
    r=csv.DictReader(f)
    for row in r:
        steps.append(row)
assert len(steps)==13, "expected 13 rows (0..12)"
prev_max=-1
for i,row in enumerate(steps):
    flat=list(map(int,row["flat25"].split(";")))
    B=np.array(flat,dtype=int).reshape(5,5) if max(abs(x) for x in flat)<10**18 else None
    # for huge ints, use Python-int replay below; here just check max/C/cyc from file
    m=int(row["maxabs"]); C=int(row["C"]); cyc=bool(int(row["cyc"]))
    if i==0:
        assert m==2
    else:
        # verify mutation from prev
        prev_flat=list(map(int,steps[i-1]["flat25"].split(";")))
        # Python-int matrices (big)
        def to_mat(fl): return [[fl[r*5+c] for c in range(5)] for r in range(5)]
        Bp=to_mat(prev_flat); k=int(row["mut_k"])
        n=5
        Bn=[row2[:] for row2 in Bp]
        for a in range(n):
            for b in range(n):
                if a==k or b==k:
                    Bn[a][b]=-Bp[a][b]
                else:
                    Bn[a][b]=Bp[a][b]+(abs(Bp[a][k])*Bp[k][b]+Bp[a][k]*abs(Bp[k][b]))//2
        assert Bn==to_mat(flat), f"Winf step {i} replay failed"
        assert m>prev_max, f"Winf max not strictly increasing at step {i}: {m} vs {prev_max}"
        assert cyc and C==5, f"Winf triple must stay cyclic C=5 at step {i}"
    prev_max=m
assert prev_max>=20, "Winf must reach >=20"
print(f"Winf OK: 12 steps, max {steps[0]['maxabs']}->{steps[-1]['maxabs']}, C=5 cyclic throughout")

print("== recheck triple bridge ==")
with open("artifacts/triple_bridge.csv") as f:
    r=csv.DictReader(f)
    rows=list(r)
assert len(rows)==78
for row in rows:
    a,b,c=int(row["a"]),int(row["b"]),int(row["c"])
    B=np.zeros((3,3),dtype=int)
    B[0,1]=a;B[1,0]=-a;B[1,2]=b;B[2,1]=-b;B[2,0]=c;B[0,2]=-c
    path=[] if row["path"]=="" else list(map(int,row["path"].split(",")))
    for k in path:
        # 3x3 mutate
        n=3
        Bp=B.copy()
        for i in range(n):
            for j in range(n):
                if i==k or j==k:
                    Bp[i,j]=-B[i,j]
                else:
                    Bp[i,j]=B[i,j]+(abs(int(B[i,k]))*int(B[k,j])+int(B[i,k])*abs(int(B[k,j])))//2
        B=Bp
    p,q,r,cyc,C=triple(B,0,1,2)
    assert cyc and C>4, f"bridge failed for {(a,b,c)} got {(p,q,r,cyc,C)}"
print("bridge OK (78 patterns -> cyclic C>4)")

print("ALL RECHECKS PASSED")
