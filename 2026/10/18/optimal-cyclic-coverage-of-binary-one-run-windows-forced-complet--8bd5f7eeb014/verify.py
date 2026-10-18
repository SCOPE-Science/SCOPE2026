#!/usr/bin/env python3
"""Verify shortest cyclic covers of binary one-run words. Standard library only.

Usage: python3 verify.py
Every finite test is supplementary to the unbounded combinatorial proof.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product


def linear_one_run(k):
    return {'0'*k} | {
        '0'*a + '1'*b + '0'*(k-a-b)
        for b in range(1,k+1) for a in range(k-b+1)
    }


def circular_one_run(k):
    out = {'0'*k, '1'*k}
    for b in range(1,k):
        base='1'*b+'0'*(k-b)
        for shift in range(k):
            out.add(base[shift:]+base[:shift])
    return out


def cyclic_factors(word,k):
    N=len(word)
    return [''.join(word[(i+j)%N] for j in range(k)) for i in range(N)]


def eulerian_word(k):
    words=circular_one_run(k)
    outgoing=defaultdict(list)
    for w in words:
        outgoing[w[:-1]].append((w[1:],w[-1]))
    for row in outgoing.values():
        row.sort(reverse=True)
    initial='0'*(k-1)
    stack=[(initial,None)]
    backwards=[]
    while stack:
        v=stack[-1][0]
        if outgoing[v]:
            to,bit=outgoing[v].pop()
            stack.append((to,bit))
        else:
            _,bit=stack.pop()
            if bit is not None:
                backwards.append(bit)
    word=''.join(reversed(backwards))
    assert len(word)==k*k-k+2
    observed=cyclic_factors(word,k)
    assert len(set(observed))==len(observed)
    assert set(observed)==words
    return word


def overlap_distance(source,target,k):
    n=k-1
    for steps in range(1,n+1):
        if source[steps:]==target[:n-steps]:
            return steps
    raise AssertionError('de Bruijn distance upper bound failed')


def min_assignment_cost(k):
    if k==2: return 0
    n=k-1
    negative=['1'*i+'0'*(n-i) for i in range(1,n)]
    positive=['0'*(n-i)+'1'*i for i in range(1,n)]
    m=len(negative)
    weights=[[overlap_distance(a,b,k) for b in positive] for a in negative]
    dp=[10**9]*(1<<m)
    dp[0]=0
    for mask in range(1<<m):
        row=mask.bit_count()
        if row==m:continue
        for j in range(m):
            if not(mask>>j&1):
                nextmask=mask|1<<j
                dp[nextmask]=min(dp[nextmask],dp[mask]+weights[row][j])
    return dp[-1]


def rooted_tour_count(k):
    arcs=sorted(circular_one_run(k)); ids={w:i for i,w in enumerate(arcs)}
    outbound=defaultdict(list)
    for w,i in ids.items():
        outbound[w[:-1]].append((w[1:],i))
    r='0'*(k-1)
    goal=(1<<len(arcs))-1
    init=1<<ids['0'*k]
    @lru_cache(None)
    def dfs(vertex,mask):
        if mask==goal:return int(vertex==r)
        return sum(dfs(to,mask|(1<<edge)) for to,edge in outbound[vertex]
                   if not(mask>>edge&1))
    return dfs(r,init)


def exhaustive_rooted_covers(k):
    required=linear_one_run(k)
    target=circular_one_run(k)
    optimum=k*k-k+2
    total=0
    for length in range(k,optimum+1):
        matching=0
        # Any valid circle has 0^k. Rotate so that this word starts at 0.
        for suffix_num in range(1<<(length-k)):
            suffix=format(suffix_num,'0'+str(length-k)+'b') if length>k else ''
            word='0'*k+suffix
            obs=set(cyclic_factors(word,k))
            if required.issubset(obs):
                matching+=1
                assert length==optimum, (k,length,word)
                assert obs==target, (k,length,word)
        if length==optimum:
            total=matching
        else:
            assert matching==0,(k,length,matching)
    assert total==2**(k-2),(k,total)
    return total


def verify():
    for k in range(2,19):
        required=linear_one_run(k)
        circular=circular_one_run(k)
        extras={'1'*a+'0'*b+'1'*c
                for a in range(1,k-1)
                for b in range(1,k-a)
                for c in [k-a-b] if c>=1}
        assert len(required)==1+k*(k+1)//2
        assert len(circular)==k*k-k+2
        assert len(extras)==(k-1)*(k-2)//2
        assert circular==required|extras
        assert not(required&extras)
        host=eulerian_word(k)
        assert len(host)==len(circular)
        if k<=14:
            # Independent min-cost matching of all imbalance vertices.
            assert min_assignment_cost(k)==len(extras),k
        if k<=11:
            # Independent exact Eulerian-circuit count in the prescribed arc graph.
            assert rooted_tour_count(k)==2**(k-2),k
    for k in range(2,6):
        exhaustive_rooted_covers(k)
    print('VERIFY_OK construction_k=2..18 assignment_k=2..14 '
          'rooted_euler_counts_k=2..11 exhaustive_all_shorter_hosts_k=2..5')

if __name__=='__main__':verify()
