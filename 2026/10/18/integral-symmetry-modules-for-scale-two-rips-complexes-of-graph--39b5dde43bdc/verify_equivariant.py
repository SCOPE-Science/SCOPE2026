#!/usr/bin/env python3
"""Independent finite character check of the canonical oriented-triangle H_2 lattice.
Every computation is finite; the all-graphs theorem relies on its proof.
"""
from itertools import combinations, permutations
from collections import Counter
from verify_total_graph import total_adj, clique_faces, triangle_list


def permutation_sign(seq):
    return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1


def trace_on_chains(faces, permutation):
    trace=Counter()
    for mask in faces:
        idx=[j for j in range(len(permutation)) if mask>>j&1]
        mapped=[permutation[j] for j in idx]
        if set(mapped)==set(idx):
            trace[len(idx)-1]+=permutation_sign(mapped)
    return sum((-1)**d*t for d,t in trace.items())


def check_kn(n):
    edges=list(combinations(range(n),2)); N=n+len(edges)
    e_idx={e:i for i,e in enumerate(edges)}
    faces=clique_faces(total_adj(n,edges))
    triangles=list(combinations(range(n),3))
    traces=Counter(); n_checks=0
    for g in permutations(range(n)):
        gp=list(g)+[n+e_idx[tuple(sorted((g[u],g[v])))] for u,v in edges]
        observed=trace_on_chains(faces,gp)-1
        predicted=0
        for t in triangles:
            v=[g[i] for i in t]
            if set(v)==set(t):predicted+=permutation_sign(v)
        assert observed==predicted,(n,g,observed,predicted)
        traces[observed]+=1; n_checks+=1
    return n_checks,dict(sorted(traces.items()))


def main():
    for n in range(3,7):
        count,traces=check_kn(n)
        print('K_%s: verified all %s permutations; H_2 character trace distribution %s'%(n,count,traces))
    print('Independent signed simplicial Lefschetz traces and oriented-triangle character formulas: PASS')

if __name__=='__main__':main()
