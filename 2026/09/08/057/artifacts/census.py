"""Full fiber-diameter census for 3x3 (margins 0..6) and 3x4 (margins 0..4).
Stdlib only. Enumerates every (row,col) margin class, enumerates the fiber
(all nonnegative integer tables with those margins), builds the fiber graph
under Diaconis-Sturmfels 2x2 moves, BFS-certifies connectivity, computes exact
diameter by all-pairs BFS, tracks the maximal-diameter fiber with witness path.
"""
import json, itertools, collections, time

def gen_moves(nrows, ncols):
    moves = []
    for i1 in range(nrows):
        for i2 in range(i1+1, nrows):
            for j1 in range(ncols):
                for j2 in range(j1+1, ncols):
                    d = {}
                    d[(i1,j1)]=1; d[(i2,j2)]=1; d[(i1,j2)]=-1; d[(i2,j1)]=-1
                    moves.append(d)
                    moves.append({k:-v for k,v in d.items()})
    return moves

def enumerate_fiber(r, c, nrows, ncols):
    # recursive over cells with remaining-sum pruning
    cells = [(i,j) for i in range(nrows) for j in range(ncols)]
    rem_r = list(r); rem_c = list(c)
    # order cells row-major
    out = []
    cur = [0]*(nrows*ncols)
    # precompute remaining cell counts per row/col for pruning bounds
    def rec(k):
        if k == len(cells):
            if all(x==0 for x in rem_r) and all(x==0 for x in rem_c):
                out.append(tuple(cur))
            return
        i,j = cells[k]
        # is this last cell of row i / col j?
        last_in_row = all(c2[0]!=i for c2 in cells[k+1:])
        last_in_col = all(c2[1]!=j for c2 in cells[k+1:])
        lo = 0
        hi = min(rem_r[i], rem_c[j])
        if last_in_row and last_in_col:
            vals = [rem_r[i]] if rem_r[i]==rem_c[j] and rem_r[i]<=hi else []
        elif last_in_row:
            vals = [rem_r[i]] if rem_r[i]<=rem_c[j] else []
        elif last_in_col:
            vals = [rem_c[j]] if rem_c[j]<=rem_r[i] else []
        else:
            vals = range(lo, hi+1)
        for v in vals:
            rem_r[i]-=v; rem_c[j]-=v; cur[k]=v
            rec(k+1)
            rem_r[i]+=v; rem_c[j]+=v
    rec(0)
    return out

def neighbors(t, moves, nrows, ncols):
    nb = []
    for d in moves:
        ok = True
        for (i,j),dv in d.items():
            if t[i*ncols+j]+dv < 0:
                ok=False; break
        if ok:
            l = list(t)
            for (i,j),dv in d.items():
                l[i*ncols+j]+=dv
            nb.append(tuple(l))
    return nb

def bfs_diam(fiber, moves, nrows, ncols):
    idx = {t:k for k,t in enumerate(fiber)}
    n = len(fiber)
    # adjacency
    adj = [neighbors(t, moves, nrows, ncols) for t in fiber]
    adj = [[idx[u] for u in a] for a in adj]
    # connectivity + all-pairs diameter
    from collections import deque
    maxd = 0
    pair = (0,0)
    for s in range(n):
        dist = [-1]*n; dist[s]=0
        dq = deque([s])
        while dq:
            u = dq.popleft()
            for w in adj[u]:
                if dist[w]<0:
                    dist[w]=dist[u]+1; dq.append(w)
        if any(d<0 for d in dist):
            return (False, None, None, adj)
        for t in range(n):
            if dist[t]>maxd:
                maxd=dist[t]; pair=(s,t)
    return (True, maxd, pair, adj)

def shortest_path(fiber_idx_pair, adj, n):
    from collections import deque
    s,t = fiber_idx_pair
    prev = [-1]*n; prev[s]=s
    dq=deque([s])
    while dq:
        u=dq.popleft()
        if u==t: break
        for w in adj[u]:
            if prev[w]<0:
                prev[w]=u; dq.append(w)
    path=[t]
    while path[-1]!=s:
        path.append(prev[path[-1]])
    path.reverse()
    return path

def run_case(nrows, ncols, bound, label):
    t0=time.time()
    moves = gen_moves(nrows, ncols)
    rvecs = list(itertools.product(range(bound+1), repeat=nrows))
    cvecs = list(itertools.product(range(bound+1), repeat=ncols))
    c_by_sum = collections.defaultdict(list)
    for c in cvecs:
        c_by_sum[sum(c)].append(c)
    nclasses=0; disconnected=0
    size_hist=collections.Counter(); diam_hist=collections.Counter()
    maxd=-1; maxinfo=None
    maxsize=0; maxsize_info=None
    rows_out=[]
    for r in rvecs:
        for c in c_by_sum[sum(r)]:
            nclasses+=1
            fiber = enumerate_fiber(r,c,nrows,ncols)
            ok,d,pair,adj = bfs_diam(fiber,moves,nrows,ncols)
            if not ok:
                disconnected+=1
                rows_out.append((r,c,len(fiber),-1))
                continue
            size_hist[len(fiber)]+=1; diam_hist[d]+=1
            rows_out.append((r,c,len(fiber),d))
            if len(fiber)>maxsize:
                maxsize=len(fiber); maxsize_info=(r,c,d)
            if d>maxd:
                maxd=d
                fi={t:k for k,t in enumerate(fiber)}
                path_idx=shortest_path(pair,adj,len(fiber))
                maxinfo={"r":list(r),"c":list(c),"size":len(fiber),"diam":d,
                         "endpoints":[list(fiber[path_idx[0]]),list(fiber[path_idx[-1]])],
                         "path": [list(fiber[k]) for k in path_idx]}
    dt=time.time()-t0
    return {"label":label,"nrows":nrows,"ncols":ncols,"bound":bound,
            "moves":len(moves),"classes":nclasses,"disconnected":disconnected,
            "maxsize":maxsize,"maxsize_info":(list(maxsize_info[0]),list(maxsize_info[1]),maxsize_info[2]) if maxsize_info else None,
            "maxdiam":maxd,"maxinfo":maxinfo,
            "size_hist":{str(k):v for k,v in sorted(size_hist.items())},
            "diam_hist":{str(k):v for k,v in sorted(diam_hist.items())},
            "rows":rows_out,"seconds":dt}

if __name__=="__main__":
    res33 = run_case(3,3,6,"3x3")
    print("3x3 done", res33["classes"], "disc:",res33["disconnected"],"maxd:",res33["maxdiam"],"maxsize:",res33["maxsize"],"t=",round(res33["seconds"],1))
    res34 = run_case(3,4,4,"3x4")
    print("3x4 done", res34["classes"], "disc:",res34["disconnected"],"maxd:",res34["maxdiam"],"maxsize:",res34["maxsize"],"t=",round(res34["seconds"],1))
    for res in (res33,res34):
        rows=res.pop("rows")
        fn = f"output/artifacts/census_{res['label']}.json"
        with open(fn,"w") as f:
            json.dump(res,f)
        # compact per-class table csv
        with open(f"output/artifacts/table_{res['label']}.csv","w") as f:
            f.write("r,c,size,diam\n")
            for (r,c,s,d) in rows:
                f.write(f"{''.join(map(str,r))},{''.join(map(str,c))},{s},{d}\n")
    print("saved")
