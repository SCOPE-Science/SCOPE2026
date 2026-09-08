"""Independent verifier: replays maximal-fiber witnesses and spot-checks the census.
Stdlib only. Usage: python3 verify.py  (run inside output/artifacts/)
Checks:
 V1 witness tables have claimed margins.
 V2 every consecutive path step is a single 2x2 Diaconis-Sturmfels move.
 V3 path length == claimed diameter and is shortest (BFS from endpoint A over fiber).
 V4 fiber sizes recomputed by an independent nested-loop enumerator agree.
 V5 spot-check diameters of sampled classes (incl. uniform (6,6,6) and (4,4,4)x(3,3,3,3)).
 V6 per-class CSV row counts (9331 / 7140) and diameter-histogram totals agree.
"""
import json, csv, itertools, collections

def moveset(nr, nc):
    M=[]
    for i1 in range(nr):
        for i2 in range(i1+1,nr):
            for j1 in range(nc):
                for j2 in range(j1+1,nc):
                    for s in (1,-1):
                        d={}; d[(i1,j1)]=s; d[(i2,j2)]=s; d[(i1,j2)]=-s; d[(i2,j1)]=-s
                        M.append(d)
    return M

def fiber_bruteforce(r,c,nr,nc):
    """Independent enumerator: iterate all tables with row sums r via compositions, filter cols."""
    def comps(total, k):
        if k==1: yield (total,); return
        for v in range(total+1):
            for t in comps(total-v, k-1): yield (v,)+t
    out=[]
    for rows in itertools.product(*[list(comps(s,nc)) for s in r]):
        ok=True
        for j in range(nc):
            if sum(rows[i][j] for i in range(nr))!=c[j]: ok=False; break
        if ok: out.append(tuple(x for row in rows for x in row))
    return out

def bfs_dist(A, adj):
    from collections import deque
    dist={A:0}; dq=collections.deque([A])
    while dq:
        u=dq.popleft()
        for w in adj[u]:
            if w not in dist: dist[w]=dist[u]+1; dq.append(w)
    return dist

def check_witness(label, nr, nc):
    d=json.load(open(f"census_{label}.json"))
    w=d["maxinfo"]; r=tuple(w["r"]); c=tuple(w["c"])
    path=[tuple(t) for t in w["path"]]
    M=moveset(nr,nc)
    # V1 margins
    for t in [tuple(w["endpoints"][0]), tuple(w["endpoints"][1])]+path:
        rr=[sum(t[i*nc+j] for j in range(nc)) for i in range(nr)]
        cc=[sum(t[i*nc+j] for i in range(nr)) for j in range(nc)]
        assert tuple(rr)==r and tuple(cc)==c, f"V1 margin fail {t}"
    # V2 steps are single moves
    for a,b in zip(path,path[1:]):
        diff=tuple(bb-aa for aa,bb in zip(a,b))
        nz={k:v for k,v in enumerate(diff) if v!=0}
        assert len(nz)==4 and sorted(nz.values())==[-1,-1,1,1], f"V2 move fail {a}->{b}"
        cells=[(k//nc,k%nc) for k in nz]
        rs=sorted(x for x,y in cells); cs=sorted(y for x,y in cells)
        assert rs[0]==rs[1] and rs[2]==rs[3] and rs[0]!=rs[2] and cs[0]==cs[1] and cs[2]==cs[3] and cs[0]!=cs[2], "V2 rectangle fail"
    # V3 shortest: BFS over full fiber from A must reach B at distance len(path)-1, and cover fiber
    fib=fiber_bruteforce(r,c,nr,nc)
    assert len(fib)==w["size"], f"V4 size {len(fib)} vs {w['size']}"
    S=set(fib); idx={t:k for k,t in enumerate(fib)}
    adj={t:[] for t in fib}
    for t in fib:
        for m in M:
            u=list(t)
            ok=True
            for (i,j),dv in m.items():
                if u[i*nc+j]+dv<0: ok=False; break
            if ok:
                for (i,j),dv in m.items(): u[i*nc+j]+=dv
                u2=tuple(u)
                if u2 in S: adj[t].append(u2)
                for (i,j),dv in m.items(): u[i*nc+j]-=dv
    A=tuple(w["endpoints"][0]); B=tuple(w["endpoints"][1])
    dist=bfs_dist(A,adj)
    assert len(dist)==len(fib), "fiber disconnected on replay"
    assert dist[B]==w["diam"]==len(path)-1, f"V3 diam {dist[B]} vs {w['diam']}"
    for a,b in zip(path,path[1:]):
        assert b in adj[a], "path step not an edge"
    print(f"[{label}] witness OK: r={list(r)} c={list(c)} size={len(fib)} diam={dist[B]} pathlen={len(path)}")
    return len(fib), dist[B]

def check_spots():
    M33=moveset(3,3); M34=moveset(3,4)
    spots=[("3x3",3,3,(6,6,6),(6,6,6),406,12),
           ("3x3",3,3,(2,2,2),(2,2,2),21,4),
           ("3x4",3,4,(4,4,4),(3,3,3,3),415,6)]
    for lab,nr,nc,r,c,es,ed in spots:
        fib=fiber_bruteforce(r,c,nr,nc)
        assert len(fib)==es, f"{lab}{r}{c} size {len(fib)} vs {es}"
        S=set(fib); M=M33 if lab=="3x3" else M34
        adj={t:[] for t in fib}
        for t in fib:
            for m in M:
                u=list(t); ok=True
                for (i,j),dv in m.items():
                    if u[i*nc+j]+dv<0: ok=False; break
                if ok:
                    for (i,j),dv in m.items(): u[i*nc+j]+=dv
                    u2=tuple(u)
                    if u2 in S: adj[t].append(u2)
                    for (i,j),dv in m.items(): u[i*nc+j]-=dv
        d0=bfs_dist(fib[0],adj)
        assert len(d0)==len(fib), f"{lab}{r}{c} disconnected"
        dd=max(max(bfs_dist(t,adj).values()) for t in fib)
        # full all-pairs for small ones only; for 406/415 use eccentricity bound check via sampling + BFS from witness ends
        print(f"[{lab}] spot r={list(r)} c={list(c)} size={len(fib)} diam={dd} (expect {ed})")
        assert dd==ed, f"diam mismatch {dd} vs {ed}"

def check_tables():
    for lab,exp in [("3x3",9331),("3x4",7140)]:
        rows=list(open(f"table_{lab}.csv").read().strip().split("\n"))
        assert len(rows)-1==exp, f"{lab} rows {len(rows)-1} vs {exp}"
        d=json.load(open(f"census_{lab}.json"))
        assert d["disconnected"]==0
        assert sum(d["diam_hist"].values())==exp
        assert sum(d["size_hist"].values())==exp
        assert d["classes"]==exp
        print(f"[{lab}] table OK: {exp} classes, 0 disconnected, hist totals agree")

if __name__=="__main__":
    check_tables()
    s1,d1=check_witness("3x3",3,3)
    s2,d2=check_witness("3x4",3,4)
    check_spots()
    print(f"VERIFY_OK sizes=({s1},{s2}) diams=({d1},{d2})")
