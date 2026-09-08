"""Exact max-C6-free edge count via branch-and-bound + heuristics. stdlib only."""
import itertools, sys, time, random

def build_edges(n):
    E = [(i,j) for i in range(n) for j in range(i+1,n)]
    idx = {e:k for k,e in enumerate(E)}
    return E, idx

def adj_from_inc(n, E, inc):
    adj=[[] for _ in range(n)]
    for k in range(len(E)):
        if (inc>>k)&1:
            a,b=E[k]; adj[a].append(b); adj[b].append(a)
    return adj

def has_5path(adj, u, v, L=5):
    # simple path of length exactly L from u to v
    # DFS with pruning
    n=len(adj)
    visited=[False]*n
    visited[u]=True
    found=False
    def dfs(x,d):
        nonlocal found
        if found: return
        if d==L:
            if x==v: found=True
            return
        # prune: remaining steps
        for w in adj[x]:
            if not visited[w]:
                # simple bound: none
                visited[w]=True
                dfs(w,d+1)
                visited[w]=False
                if found: return
    dfs(u,0)
    return found

def creates_c6(n,E,inc,a,b):
    adj=adj_from_inc(n,E,inc)
    return has_5path(adj,a,b,5)

def full_c6_check(n,E,inc):
    # independent full check: any 5-path closing an included edge
    adj=adj_from_inc(n,E,inc)
    M=len(E)
    for k in range(M):
        if (inc>>k)&1:
            a,b=E[k]
            # temporarily remove edge k
            adj[a].remove(b); adj[b].remove(a)
            r=has_5path(adj,a,b,5)
            adj[a].append(b); adj[b].append(a)
            if r: return True
    return False

def brute_c6_check(n,E,inc):
    # totally independent: enumerate all 6-sets and all 60 cycles
    S=set(k for k in range(len(E)) if (inc>>k)&1)
    for vs in itertools.combinations(range(n),6):
        v0=vs[0]
        for perm in itertools.permutations(vs[1:]):
            cyc=(v0,)+perm
            if cyc[1]>cyc[-1]: continue
            ok=True
            for t in range(6):
                a,b=cyc[t],cyc[(t+1)%6]
                if a>b: a,b=b,a
                from bisect import bisect
                if idxof.get((a,b),-1) not in S:
                    ok=False; break
            if ok: return True
    return False

idxof={}
def set_idx(E,idx): 
    global idxof; idxof=idx

def popcount(x): return bin(x).count('1')

def heuristic(n,E,trials=4000,seed=0):
    rng=random.Random(seed)
    M=len(E)
    best=0; bestm=0
    for _ in range(trials):
        order=list(range(M)); rng.shuffle(order)
        inc=0
        adj=[[] for _ in range(n)]
        for k in order:
            a,b=E[k]
            # test 5-path in current adj
            if not has_5path(adj,a,b,5):
                inc|=(1<<k); adj[a].append(b); adj[b].append(a)
        c=popcount(inc)
        if c>best: best=c; bestm=inc
    # local search: try add excluded edges in random order greedily
    return best,bestm

def bb_max(n,E,inc0=0,exc0=0,best0=0,time_limit=60,node_limit=None,verbose=False):
    M=len(E)
    ALL=(1<<M)-1
    best=best0; bestm=inc0
    t0=time.time()
    nodes=0; pruned=0
    # order edges statically? dynamic pick: first undecided
    # Use stack of (inc,exc)
    stack=[(inc0,exc0)]
    # cache adjacency? recompute per node
    while stack:
        if time.time()-t0>time_limit: break
        inc,exc=stack.pop()
        nodes+=1
        und=ALL^inc^exc
        # upper bound
        if popcount(inc)+popcount(und)<=best:
            pruned+=1; continue
        # unit propagation: force-exclude edges that create C6
        while True:
            adj=adj_from_inc(n,E,inc)
            forced=0
            for kk in range(M):
                if (und>>kk)&1:
                    a,b=E[kk]
                    if has_5path(adj,a,b,5):
                        forced|=(1<<kk)
            if forced==0: break
            exc|=forced; und=ALL^inc^exc
            if popcount(inc)+popcount(und)<=best:
                pruned+=1; break
        if popcount(inc)+popcount(und)<=best:
            continue
        und=ALL^inc^exc
        if und==0:
            c=popcount(inc)
            if c>best: best=c; bestm=inc
            continue
        # pick branch edge: lowest index und (or highest degree heuristic)
        # heuristic: pick und edge whose endpoints have highest degree in inc graph
        adj=adj_from_inc(n,E,inc)
        deg=[len(x) for x in adj]
        bk=-1; bs=-1
        for kk in range(M):
            if (und>>kk)&1:
                a,b=E[kk]
                s=deg[a]+deg[b]
                if s>bs: bs=s; bk=kk
        ebit=(1<<bk)
        # push exclude branch, then include branch (DFS include-first)
        stack.append((inc,exc|ebit))
        # include branch: quick conflict check (already know it doesn't create C6 due to propagation)
        stack.append((inc|ebit,exc))
        if node_limit and nodes>node_limit: break
    return best,bestm,{'nodes':nodes,'pruned':pruned,'timeout':(time.time()-t0>=time_limit)}

if __name__=='__main__':
    n=int(sys.argv[1]) if len(sys.argv)>1 else 8
    tl=float(sys.argv[2]) if len(sys.argv)>2 else 30
    E,idx=build_edges(n); set_idx(E,idx)
    hb,hm=heuristic(n,E,trials=2000,seed=1)
    print(f"n={n} M={len(E)} heur LB={hb}",flush=True)
    b,m,info=bb_max(n,E,best0=hb,time_limit=tl)
    print(f"n={n} BB best={b} info={info}",flush=True)
