"""v2: symmetry-fixed (max-degree vertex 0, N(0)={1..d}), degree caps, decision BB."""
import itertools, sys, time, random

def build(n):
    E=[(i,j) for i in range(n) for j in range(i+1,n)]
    idx={e:k for k,e in enumerate(E)}
    return E,idx

def adjlist(n,E,inc):
    adj=[[] for _ in range(n)]
    for k,(a,b) in enumerate(E):
        if (inc>>k)&1: adj[a].append(b); adj[b].append(a)
    return adj

def adjmask(n,E,inc):
    m=[0]*n
    for k,(a,b) in enumerate(E):
        if (inc>>k)&1:
            m[a]|=(1<<b); m[b]|=(1<<a)
    return m

def has_k_path_mask(am, u, v, L):
    # simple path length exactly L from u to v, n<=14. DFS with bitmask visited.
    n=len(am)
    found=False
    def dfs(x,d,vis):
        nonlocal found
        if found: return
        if d==L:
            if x==v: found=True
            return
        # prune by remaining: need at least (L-d) steps; simple connectivity prune skip
        nb=am[x]&~vis
        while nb and not found:
            lsb=nb&(-nb); w=(lsb.bit_length()-1)
            dfs(w,d+1,vis|lsb)
            nb^=lsb
    dfs(u,0,1<<u)
    return found

def creates_c6(am,a,b):
    return has_k_path_mask(am,a,b,5)

def full_check(n,E,inc):
    am=adjmask(n,E,inc)
    M=len(E)
    for k,(a,b) in enumerate(E):
        if (inc>>k)&1:
            am[a]^=(1<<b); am[b]^=(1<<a)
            r=has_k_path_mask(am,a,b,5)
            am[a]^=(1<<b); am[b]^=(1<<a)
            if r: return True
    return False

def popcount(x): return bin(x).count('1')

def degvec(n,E,inc,exc=None):
    d=[0]*n; u=[0]*n
    for k,(a,b) in enumerate(E):
        if (inc>>k)&1: d[a]+=1; d[b]+=1
        elif exc is None or not ((exc>>k)&1): u[a]+=1; u[b]+=1
    return d,u

def heuristic(n,E,trials=6000,seed=0):
    import random
    rng=random.Random(seed)
    M=len(E); best=0; bestm=0
    for _ in range(trials):
        order=list(range(M)); rng.shuffle(order)
        inc=0; am=[0]*n
        for k in order:
            a,b=E[k]
            if not has_k_path_mask(am,a,b,5):
                inc|=(1<<k); am[a]|=(1<<b); am[b]|=(1<<a)
        c=popcount(inc)
        if c>best: best=c; bestm=inc
    return best,bestm

def bb_fixed_d(n,E,d,T,time_limit,nodes_state):
    """Decide: exists C6-free supergraph with >=T edges extending fix?
    fix: edges (0,i) i<=d included; (0,i) i>d excluded; deg<=d for all.
    Return (found_mask or None, nodes). DFS include-first with cardinality+degree+C6 pruning."""
    M=len(E); idx={e:k for k,e in enumerate(E)}
    inc0=0; exc0=0
    for i in range(1,n):
        k=idx[(0,i)]
        if i<=d: inc0|=(1<<k)
        else: exc0|=(1<<k)
    ALL=(1<<M)-1
    t0=nodes_state['t0']; tl=time_limit
    stack=[(inc0,exc0)]
    nodes=0
    # precompute incident lists
    incid=[[] for _ in range(n)]
    for k,(a,b) in enumerate(E):
        incid[a].append(k); incid[b].append(k)
    while stack:
        if time.time()-t0>tl:
            nodes_state['timeout']=True; return None,nodes
        inc,exc=stack.pop(); nodes+=1
        # degree cap check
        # quick: compute degs only of inc
        if popcount(inc)+popcount(ALL^inc^exc)<T: continue
        # degree overfull prune
        over=False
        for v in range(n):
            dg=0
            for k in incid[v]:
                if (inc>>k)&1: dg+=1
            if dg>d: over=True; break
        if over: continue
        # propagate: C6-forcing exclusions + degree-cap exclusions
        while True:
            if time.time()-t0>tl:
                nodes_state['timeout']=True; return None,nodes
            und=ALL^inc^exc
            if popcount(inc)+popcount(und)<T: break
            am=adjmask(n,E,inc)
            # degree caps: vertices at cap -> exclude remaining und there
            forced=0
            for v in range(n):
                dg=sum(1 for k in incid[v] if (inc>>k)&1)
                if dg==d:
                    for k in incid[v]:
                        if (und>>k)&1: forced|=(1<<k)
                elif dg>d:
                    forced=-1; break
            if forced==-1: break
            # C6 forcing: und edge creating C6 must be excluded
            u2=und&~forced
            f2=0
            for k in range(M):
                if (u2>>k)&1:
                    a,b=E[k]
                    if has_k_path_mask(am,a,b,5): f2|=(1<<k)
            forced|=f2
            if forced==0: break
            exc|=forced
            und=ALL^inc^exc
            if popcount(inc)+popcount(und)<T: break
        und=ALL^inc^exc
        if popcount(inc)+popcount(und)<T: continue
        # degree overfull recheck
        bad=False
        for v in range(n):
            if sum(1 for k in incid[v] if (inc>>k)&1)>d: bad=True; break
        if bad: continue
        if und==0:
            if popcount(inc)>=T and not full_check(n,E,inc):
                return inc,nodes
            continue
        # branch choice: und edge with max deg sum
        am=adjmask(n,E,inc)
        degs=[popcount(am[v]) for v in range(n)]
        bk=-1; bs=-1
        for k in range(M):
            if (und>>k)&1:
                a,b=E[k]; s=degs[a]+degs[b]
                if s>bs: bs=s; bk=k
        ebit=(1<<bk)
        stack.append((inc,exc|ebit))
        stack.append((inc|ebit,exc))
    return None,nodes

def prove_opt(n,E,LB,time_limit=120,verbose=True):
    # try T=LB+1, LB+2, ... : if UNSAT then ex=LB (given LB achievable)
    # symmetry: d ranges over feasible max degrees: ceil(2*LB/n) <= d <= min(n-1, LB)
    import math, time
    lb=LB
    T=lb+1
    # upper trivial: total edges
    M=len(E)
    state={'t0':time.time(),'timeout':False}
    # determine d range for T
    dmin=max(0,math.ceil(2*T/n - 1e-9))
    results={}
    # First: attempt T=LB+1 across all d
    total_nodes=0
    for d in range(dmin,min(n-1,T)+1):
        if time.time()-state['t0']>time_limit: state['timeout']=True; break
        f,nd=bb_fixed_d(n,E,d,T,time_limit,state)
        total_nodes+=nd
        results[d]=(f is not None)
        if verbose: print(f"  n={n} T={T} d={d}: {'SAT' if f is not None else 'UNSAT'} nodes={nd}",flush=True)
        if f is not None:
            return {'sat':True,'mask':f,'d':d,'nodes':total_nodes,'T':T,'timeout':state['timeout']}
    return {'sat':False,'nodes':total_nodes,'T':T,'timeout':state['timeout'],'per_d':results}

if __name__=='__main__':
    n=int(sys.argv[1]); tl=float(sys.argv[2]) if len(sys.argv)>2 else 60
    E,idx=build(n)
    hb,hm=heuristic(n,E,trials=4000,seed=2)
    print(f"n={n} heur LB={hb}",flush=True)
    r=prove_opt(n,E,hb,time_limit=tl)
    print(r,flush=True)
