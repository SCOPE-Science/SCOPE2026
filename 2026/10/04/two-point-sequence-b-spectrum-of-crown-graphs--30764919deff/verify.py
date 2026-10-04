#!/usr/bin/env python3
from collections import defaultdict

def crown(n):
    # vertices 0..n-1 are a_i; n..2n-1 are b_i
    N=2*n
    adj=[set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i].add(n+j); adj[n+j].add(i)
    return adj

def partitions_rgs(N):
    a=[0]*N
    yield tuple(a)
    def rec(pos, mx):
        if pos==N:
            yield tuple(a); return
        for x in range(mx+2):
            a[pos]=x
            yield from rec(pos+1,max(mx,x))
    # first entry fixed 0; recursively fill rest
    yield from rec(1,0)

def proper_and_counts(adj, p):
    N=len(adj); k=max(p)+1
    classes=[[] for _ in range(k)]
    for v,c in enumerate(p): classes[c].append(v)
    # proper
    for v in range(N):
        cv=p[v]
        if any(p[w]==cv for w in adj[v]): return None
    counts=[0]*k
    used=set(range(k))
    for v in range(N):
        seen={p[v]}
        seen.update(p[w] for w in adj[v])
        if seen==used: counts[p[v]]+=1
    return counts

def classify(n,p):
    k=max(p)+1
    classes=[[] for _ in range(k)]
    for v,c in enumerate(p): classes[c].append(v)
    kinds=[]
    for C in classes:
        A=[v for v in C if v<n]; B=[v-n for v in C if v>=n]
        if A and not B: kinds.append('A')
        elif B and not A: kinds.append('B')
        elif len(A)==1 and len(B)==1 and A[0]==B[0]: kinds.append('P')
        else: kinds.append('X')
    return tuple(sorted(kinds))

def main():
    total_parts=0; proper_parts=0; good_parts=0
    details=[]
    for n in range(3,6):
        adj=crown(n)
        spectrum=set(); good_by_k=defaultdict(int); kinds_by_k=defaultdict(set)
        # partitions_rgs yields duplicate all-zero once; avoid by set? easier custom seen
        seen=set()
        for p in partitions_rgs(2*n):
            if p in seen: continue
            seen.add(p); total_parts+=1
            counts=proper_and_counts(adj,p)
            if counts is None: continue
            proper_parts+=1
            if min(counts)>=2:
                k=len(counts); spectrum.add(k); good_by_k[k]+=1; good_parts+=1
                kinds_by_k[k].add(classify(n,p))
        expected={2,n}
        assert spectrum==expected,(n,spectrum)
        assert good_by_k[2]==1 and good_by_k[n]==1,(n,good_by_k)
        assert kinds_by_k[2]=={('A','B')},(n,kinds_by_k[2])
        assert kinds_by_k[n]=={tuple(['P']*n)},(n,kinds_by_k[n])
        details.append((n,sorted(spectrum),dict(good_by_k)))
    print('ALL CHECKS PASSED; n_range=3..5; set_partitions=%d; proper_partitions=%d; realizing_partitions=%d; details=%s' % (total_parts,proper_parts,good_parts,details))
if __name__=='__main__': main()
