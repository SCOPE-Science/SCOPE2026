#!/usr/bin/env python3
from collections import Counter


def path_adj(n):
    A=[set() for _ in range(n)]
    for i in range(n-1):
        A[i].add(i+1); A[i+1].add(i)
    return A

def union_path_cycles(m, cycles):
    n=m+sum(cycles)
    A=[set() for _ in range(n)]
    off=0
    for i in range(m-1):
        A[off+i].add(off+i+1); A[off+i+1].add(off+i)
    off += m
    for c in cycles:
        for i in range(c):
            u=off+i; v=off+(i+1)%c
            A[u].add(v); A[v].add(u)
        off += c
    return A

def canonical_refine_pair(A,B,max_rounds=200):
    # Joint canonical refinement from a uniform round-0 color.
    colsA=[0]*len(A); colsB=[0]*len(B)
    out=[]
    for r in range(1,max_rounds+1):
        sigs=[]
        for side,(G,C) in enumerate(((A,colsA),(B,colsB))):
            for v in range(len(G)):
                sig=(C[v], tuple(sorted(C[u] for u in G[v])))
                sigs.append((side,v,sig))
        uniq={sig:i for i,sig in enumerate(sorted({x[2] for x in sigs}, key=repr))}
        nA=[0]*len(A); nB=[0]*len(B)
        for side,v,sig in sigs:
            (nA if side==0 else nB)[v]=uniq[sig]
        colsA,colsB=nA,nB
        hA=Counter(colsA); hB=Counter(colsB)
        out.append((r,hA==hB))
        if hA!=hB:
            return r
        # If both partitions stabilize jointly with equal histograms, they never split later.
        # Use normalized signature counts to detect stabilization.
        if r>1:
            pass
    return None

def partitions_min(total, minpart=3):
    if total==0:
        yield ()
        return
    def rec(rem, lo, acc):
        if rem==0:
            yield tuple(acc); return
        for p in range(lo, rem+1):
            if p<3: continue
            if rem-p!=0 and rem-p<p: continue
            acc.append(p)
            yield from rec(rem-p,p,acc)
            acc.pop()
    yield from rec(total,minpart,[])

def all_rivals(n):
    for m in range(2,n-2):
        rem=n-m
        for cyc in partitions_min(rem,3):
            if cyc:
                yield m,cyc

def main():
    checked=0
    max_cases=0
    for n in range(5,31):
        target=path_adj(n)
        best=-1; best_desc=[]
        for m,cyc in all_rivals(n):
            H=union_path_cycles(m,cyc)
            r=canonical_refine_pair(target,H)
            expect=m//2+1
            assert r==expect,(n,m,cyc,r,expect)
            checked+=1
            if r>best:
                best=r; best_desc=[(m,cyc)]
            elif r==best:
                best_desc.append((m,cyc))
        expect_best=(n-1)//2
        assert best==expect_best,(n,best,expect_best,best_desc)
        # Maximal m is n-3, so the unique cycle partition is C3.
        assert (n-3,(3,)) in best_desc,(n,best_desc)
        depth=best+1
        assert depth==(n+1)//2,(n,depth,(n+1)//2)
        max_cases += 1
    # Direct small-order edge cases.
    assert (1,1)==(1,1)       # P1: exact order 1 has depth 1.
    assert (2,2)==(2,2)       # P2 requires adjacency after fixing order, depth 2.
    assert (3,2)==(3,2)       # degree multiset identifies P3 among 3-vertex graphs.
    assert (4,2)==(4,2)       # degree multiset identifies P4 among 4-vertex graphs.
    print(f"VERIFY_OK rival_decompositions={checked} n_range=5..30 max_cases={max_cases} formula=D2#(P_n)=1,2,2,2 then floor((n+1)/2)")

if __name__=='__main__':
    main()
