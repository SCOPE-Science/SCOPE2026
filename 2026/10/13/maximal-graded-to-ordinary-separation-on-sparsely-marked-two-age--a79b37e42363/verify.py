#!/usr/bin/env python3
"""Finite checks for graded and ordinary modal types of the bidiagonal S5xS5 grid.
Standard library only. The proof of the all-n theorem is independent of these finite tests.
"""
from collections import Counter
from itertools import combinations

def pack(signatures):
    ids = {}
    return tuple(ids.setdefault(x, len(ids)) for x in signatures)

def atom(n):
    return tuple(int(i == j or i == j + 1) for i in range(n) for j in range(n))

def signatures(n, counting):
    a = atom(n)
    T = pack(a)
    seq = [T]
    for _ in range(n + 3):
        if counting:
            rows = [tuple(sorted(Counter(T[i*n+j] for j in range(n)).items())) for i in range(n)]
            cols = [tuple(sorted(Counter(T[i*n+j] for i in range(n)).items())) for j in range(n)]
        else:
            rows = [frozenset(T[i*n+j] for j in range(n)) for i in range(n)]
            cols = [frozenset(T[i*n+j] for i in range(n)) for j in range(n)]
        new = pack([(T[i*n+j], rows[i], cols[j]) for i in range(n) for j in range(n)])
        if len(set(new)) == len(set(T)):
            break
        T = new
        seq.append(T)
    return seq

def partition(labels):
    return {frozenset(i for i,v in enumerate(labels) if v==c) for c in set(labels)}

def predicted(n,t):
    if t==0: return 2
    if t>=n-1: return n*n
    return (t+1)**2 + 3

def matching(adj):
    # bipartite matching, unlike histogram comparison used by signatures()
    n = len(adj)
    owner = [-1]*n
    def aug(i,used):
        for j in range(n):
            if adj[i][j] and not used[j]:
                used[j]=True
                if owner[j]<0 or aug(owner[j],used):
                    owner[j]=i
                    return True
        return False
    return all(aug(i,[False]*n) for i in range(n))

def pair_game(n,counting):
    n2=n*n
    p=atom(n)
    R={(x,y) for x in range(n2) for y in range(n2) if p[x]==p[y]}
    rr=lambda x: [x//n*n + j for j in range(n)]
    cc=lambda x: [i*n + x%n for i in range(n)]
    seq=[{frozenset([x,y]) for x,y in R}]
    for _ in range(n+3):
        Q=set()
        for x,y in R:
            okay=True
            for succ in (rr,cc):
                X=succ(x);Y=succ(y)
                adj=[[((a,b) in R) for b in Y] for a in X]
                if counting:
                    okay=matching(adj)
                else:
                    okay=all(any(row) for row in adj) and all(any(adj[i][j] for i in range(n)) for j in range(n))
                if not okay:break
            if okay:Q.add((x,y))
        if Q==R:break
        R=Q
        seq.append({frozenset([x,y]) for x,y in R})
    return R

def generated_algebra_by_depth(n):
    # Independent finite powerset semantics: constructs all Boolean combinations of
    # p and every cardinality-threshold modality applied to every definable set.
    # Only used for n<=4 to bound exponential cost.
    N=n*n
    support=sum((1<<k) for k,v in enumerate(atom(n)) if v)
    def boolean_closure(gens):
        vals=[0]*(N)
        for k in range(N):
            vals[k]=tuple(int((g>>k)&1) for g in gens)
        cell_groups={}
        for k,vs in enumerate(vals):cell_groups.setdefault(vs,0);cell_groups[vs]|=1<<k
        blocks=list(cell_groups.values())
        out={0}
        for b in blocks:out|={s|b for s in list(out)}
        return out,blocks
    sets,blocks=boolean_closure([support])
    sizes=[len(blocks)]
    for _ in range(n+1):
        gems=[]
        for subset in sets:
            for mode in (0,1):
                counts=[]
                for i in range(n):
                    for j in range(n):
                        counts.append(sum((subset>>(i*n+k if mode==0 else k*n+j))&1 for k in range(n)))
                for threshold in range(1,n+1):
                    bits=sum((1<<v) for v,c in enumerate(counts) if c>=threshold)
                    gems.append(bits)
        newsets,newblocks=boolean_closure([support]+gems)
        if len(newblocks)==len(blocks):break
        sets,blocks=newsets,newblocks
        sizes.append(len(blocks))
    return sizes

if __name__=='__main__':
    signature_levels=0
    for n in range(3,71):
        G=signatures(n,True)
        B=signatures(n,False)
        counts=[len(set(t)) for t in G]
        assert counts == [predicted(n,t) for t in range(n)] ,(n,counts)
        assert [len(set(t)) for t in B] == [2],(n,B)
        signature_levels += len(G)
    game_checks=0
    for n in range(2,8):
        for counting in (False,True):
            E=pair_game(n,counting)
            T=signatures(n,counting)[-1]
            expected={(x,y) for x in range(n*n) for y in range(n*n) if T[x]==T[y]}
            assert E==expected,(n,counting)
            game_checks += 1
    closure_checks=0
    for n in range(2,5):
        sizes=generated_algebra_by_depth(n)
        got=[len(set(T)) for T in signatures(n,True)]
        assert sizes==got,(n,sizes,got)
        closure_checks += 1
    print(f'VERIFY_OK 68 grid_sizes  {signature_levels} graded_levels  {game_checks} independent_pair_games  {closure_checks} direct_boolean_semantics')
