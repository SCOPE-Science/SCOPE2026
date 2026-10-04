from functools import lru_cache
from itertools import combinations

def partitions(n, maxpart=None):
    if n==0:
        yield ()
        return
    if maxpart is None or maxpart>n: maxpart=n
    for a in range(maxpart,0,-1):
        for rest in partitions(n-a,a):
            yield (a,)+rest

def cyclic_word(counts):
    counts=tuple(counts)
    r=len(counts)
    if sum(counts)==1:
        return [next(i for i,c in enumerate(counts) if c)]
    for first in range(r):
        if counts[first]==0: continue
        cc=list(counts); cc[first]-=1
        @lru_cache(None)
        def rec(state,prev):
            rem=sum(state)
            if rem==0:
                return () if prev!=first else None
            for x,c in sorted(enumerate(state), key=lambda z:-z[1]):
                if c and x!=prev and not (rem==1 and x==first):
                    ns=list(state); ns[x]-=1
                    ans=rec(tuple(ns),x)
                    if ans is not None:
                        return (x,)+ans
            return None
        tail=rec(tuple(cc),first)
        if tail is not None:
            w=[first]+list(tail)
            if len(w)<=1 or all(w[i]!=w[(i+1)%len(w)] for i in range(len(w))): return w
    return None

def build(parts):
    N=sum(parts); r=len(parts)
    if r<2: raise ValueError
    # only our tied-maximum construction, except bipartite omitted
    if r==2 or parts.count(max(parts))<2: return None
    if N%2:
        w=cyclic_word(parts)
        assert w is not None
        lab=[None]*N
        by=[[] for _ in parts]
        for x,a in enumerate(w): by[a].append(x); lab[x]=a
        def col(u,v): return (u+v)%N
        verts=list(range(N)); inf=None; mod=N
    else:
        s=min(parts); p0=parts.index(s); q=N-1
        by=[[] for _ in parts]
        S0=[3*j for j in range(s-1)]
        by[p0]=S0[:] # infinity also in p0, tracked separately
        other_idx=[i for i in range(r) if i!=p0]
        other_counts=[parts[i] for i in other_idx]
        Hcycle=[]; x=0
        for _ in range(q): Hcycle.append(x); x=(x+2)%q
        if not S0:
            w=cyclic_word(other_counts); assert w is not None
            for pos,a in zip(Hcycle,w): by[other_idx[a]].append(pos)
        else:
            S=set(S0)
            cut=next(i for i,x in enumerate(Hcycle) if x in S)
            seq=Hcycle[cut+1:]+Hcycle[:cut+1]
            runs=[]; run=[]
            for x in seq:
                if x in S:
                    if run: runs.append(run); run=[]
                else: run.append(x)
            if run: runs.append(run)
            order=[x for run in runs for x in run]
            w=cyclic_word(other_counts); assert w is not None
            assert len(order)==len(w)
            for pos,a in zip(order,w): by[other_idx[a]].append(pos)
        inv2=pow(2,-1,q)
        def col(u,v):
            if u=='I': return v
            if v=='I': return u
            return ((u+v)*inv2)%q
        verts=list(range(q))+['I']; inf='I'; mod=q
    # map part membership
    pm={}
    for i,S in enumerate(by):
        for x in S: pm[x]=i
    if inf is not None: pm[inf]=p0
    assert len(pm)==N
    # graph edges and colors, properness
    inc={v:{} for v in verts}
    for ai,u in enumerate(verts):
        for v in verts[ai+1:]:
            if pm[u]==pm[v]: continue
            c=col(u,v)
            assert c not in inc[u] and c not in inc[v]
            inc[u][c]=v; inc[v][c]=u
    # every incident color set weak-near-interval: no run of >=2 missing between min/max
    for v in verts:
        A=sorted(inc[v])
        if not A: continue
        aset=set(A)
        missing=[z for z in range(A[0],A[-1]+1) if z not in aset]
        for z in missing:
            assert z+1 not in missing, (parts,v,A,missing)
    return True

def main():
    tested=0; edges=0
    for N in range(3,17):
        for parts in partitions(N):
            if len(parts)<2 or len(parts)==2 or parts.count(max(parts))<2: continue
            build(parts); tested+=1
            edges += sum(parts[i]*parts[j] for i in range(len(parts)) for j in range(i+1,len(parts)))
    print(f'ALL CHECKS PASSED; tied_max_types={tested}; total_edges_checked={edges}; max_order=16')
if __name__=='__main__': main()
