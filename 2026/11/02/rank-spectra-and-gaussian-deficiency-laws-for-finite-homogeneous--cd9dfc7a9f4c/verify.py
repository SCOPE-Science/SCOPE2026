#!/usr/bin/env python3
"""Direct finite induced-subgraph isomorphism enumeration and group checks.
Uses only Python's standard library. No external files or services.
"""
from itertools import combinations, permutations
from collections import defaultdict,Counter
from math import comb, factorial, perm


def graph_rook():
    return 9, lambda i,j: i//3==j//3 or i%3==j%3

def graph_cycle5():
    return 5, lambda i,j: (i-j)%5 in (1,4)

def graph_parts(t,n,complement=False):
    return t*n, lambda i,j: (i//n==j//n) if complement else (i//n!=j//n)

def sig_of_subset(S,adj):
    b=0; k=0
    for u,i in enumerate(S):
        for j in S[u+1:]:
            b|=int(adj(i,j))<<k;k+=1
    return b

def permute_sig(pat,k,p):
    b=0; r=0
    # re-index adjacency along permutation p
    for i in range(k):
        for j in range(i+1,k):
            x=p[i];y=p[j]
            if x>y:x,y=y,x
            idx=x*(2*k-x-1)//2+(y-x-1)
            b|=((pat>>idx)&1)<<r
            r+=1
    return b

def all_rank_by_local_isomorphisms(n,adj):
    ranks=[]; types=[]
    for k in range(n+1):
        if not k:
            ranks.append(1);types.append(1);continue
        p_list=list(permutations(range(k)))
        cache={};classes=Counter();autos={}
        for S in combinations(range(n),k):
            pattern=sig_of_subset(S,adj)
            if pattern not in cache:
                canonical=None;aut=0
                for p in p_list:
                    rep=permute_sig(pattern,k,p)
                    if canonical is None or rep<canonical:canonical=rep
                    if rep==pattern:aut+=1
                cache[pattern]=(canonical,aut)
            cl,aut=cache[pattern]
            classes[cl]+=1;autos[cl]=aut
        ranks.append(sum(v*v*autos[cl] for cl,v in classes.items()))
        types.append(len(classes))
    return ranks,types

def theoretical(t,n):
    B=[comb(n,k)**2*factorial(k) for k in range(n+1)]
    out=[0]*(t*n+1)
    power=[1]
    for s in range(t+1):
        coeff=comb(t,s)*perm(t,s)
        for k,v in enumerate(power):out[k]+=coeff*v
        new=[0]*(len(power)+n)
        for i,a in enumerate(power):
            for j in range(1,n+1):new[i+j]+=a*B[j]
        power=new
    return out

def exceptional_group_rank(n,group):
    ans=[]
    for k in range(n+1):
        ans.append(sum(len(group)//sum(all(g[x]==x for x in S) for g in group)
                       for S in combinations(range(n),k)))
    return ans

def group_cycle5():
    return list({tuple((a+s*x)%5 for x in range(5)) for a in range(5) for s in (1,-1)})

def group_rook9():
    P=list(permutations(range(3)))
    return list({tuple(3*p[j]+q[i] if swap else 3*p[i]+q[j]
                       for i in range(3) for j in range(3))
                 for p in P for q in P for swap in (False,True)})

def verify():
    for name,n,adj,group in [
        ('cycle5',*graph_cycle5(),group_cycle5()),
        ('rook3x3',*graph_rook(),group_rook9())
    ]:
        brute,types=all_rank_by_local_isomorphisms(n,adj)
        via_group=exceptional_group_rank(n,group)
        assert brute==via_group,(name,brute,via_group)
        print(name,'rank',brute,'total',sum(brute),'induced_types',types)
    for t,n in [(1,1),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(4,1),(4,2)]:
        for complement in (False,True):
            N,adj=graph_parts(t,n,complement)
            brute,_=all_rank_by_local_isomorphisms(N,adj)
            expect=theoretical(t,n)
            assert brute==expect,(t,n,complement,brute,expect)
        print('multipartite',t,n,'total',sum(theoretical(t,n)))
    print('VERIFY_OK')
if __name__=='__main__':verify()
