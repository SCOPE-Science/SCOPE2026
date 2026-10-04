#!/usr/bin/env python3
from functools import lru_cache
from itertools import product
from math import comb, factorial


def graph(parts):
    labels=[]
    for i,a in enumerate(parts): labels += [i]*a
    n=len(labels)
    N=[]
    for v in range(n):
        mask=1<<v
        for u in range(n):
            if labels[u] != labels[v]: mask |= 1<<u
        N.append(mask)
    return labels,N


def brute(parts):
    labels,N=graph(parts); n=len(labels)
    @lru_cache(None)
    def f(sel,dom):
        best=0
        for v in range(n):
            if not (sel>>v)&1 and (N[v] & ~dom):
                best=max(best,1+f(sel|(1<<v),dom|N[v]))
        return best
    g=f(0,0)
    seqs=[]
    def rec(sel,dom,seq):
        if len(seq)==g:
            seqs.append(tuple(seq)); return
        rem=g-len(seq)
        for v in range(n):
            if not (sel>>v)&1 and (N[v] & ~dom):
                if 1+f(sel|(1<<v),dom|N[v])==rem:
                    rec(sel|(1<<v),dom|N[v],seq+[v])
    rec(0,0,[])
    sets={tuple(sorted(s)) for s in seqs}
    return g,seqs,sets,labels


def predicted(parts):
    N=sum(parts); m=max(parts); t=sum(a==m for a in parts)
    if m==1:
        return m, N, N
    seq_count=t*factorial(m)*(N-m+1)
    if m==2:
        s=sum(a==1 for a in parts)
        set_count=comb(N,2)-comb(s,2)
    else:
        set_count=t*(1+m*(N-m))
    return m,seq_count,set_count


def classified(seq,labels,parts):
    m=max(parts)
    if len(seq)!=m: return False
    p=labels[seq[0]]
    if parts[p]!=m: return False
    if all(labels[v]==p for v in seq):
        return len(set(seq))==m
    if m<2: return False
    return (all(labels[v]==p for v in seq[:-1])
            and labels[seq[-1]]!=p
            and len(set(seq))==m)


def main():
    cases=0
    for r in range(2,5):
        for parts in product(range(1,4), repeat=r):
            if sum(parts)>8: continue
            g,seqs,sets,labels=brute(parts)
            pg,pc,ps=predicted(parts)
            assert g==pg, (parts,g,pg)
            assert len(seqs)==pc, (parts,len(seqs),pc)
            assert len(sets)==ps, (parts,len(sets),ps)
            assert all(classified(s,labels,parts) for s in seqs), parts
            cases += 1
    print(f"VERIFY_OK cases={cases}")

if __name__ == '__main__': main()
