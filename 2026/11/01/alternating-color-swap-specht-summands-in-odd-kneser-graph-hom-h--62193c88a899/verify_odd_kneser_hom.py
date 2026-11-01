#!/usr/bin/env python3
"""Independent finite character and cycle-kernel tests for odd Kneser Hom complexes."""
from itertools import combinations, permutations
from collections import deque
from math import factorial, prod, comb


def partitions(n, bound=None):
    if n == 0:
        yield ()
        return
    if bound is None:
        bound = n
    for i in range(min(n, bound), 0, -1):
        for rest in partitions(n-i, i):
            yield (i,) + rest


def hook_dim(shape):
    hooks = prod(shape[i]-j+sum(shape[ii] > j for ii in range(i+1,len(shape)))
                 for i in range(len(shape)) for j in range(shape[i]))
    return factorial(sum(shape))//hooks


def sign_perm(p):
    return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1


def specht_character(shape, ctype):
    # Frobenius's alternant coefficient formula, using three variables.
    target = (shape[0]+2,shape[1]+1,shape[2])
    coeff = {(0,0,0):1}
    for length in ctype:
        nxt={}
        for v,c in coeff.items():
            for j in range(3):
                w=list(v);w[j]+=length;w=tuple(w)
                nxt[w]=nxt.get(w,0)+c
        coeff=nxt
    z=0
    for p in permutations(range(3)):
        powers=tuple((2,1,0)[p[i]] for i in range(3))
        rem=tuple(target[i]-powers[i] for i in range(3))
        z += sign_perm(p)*coeff.get(rem,0)
    return z


def k_subset_count(cycles,k):
    dp=[0]*(k+1);dp[0]=1
    for l in cycles:
        for j in range(k,l-1,-1):dp[j]+=dp[j-l]
    return dp[k]


def actual_characters(k, cycles):
    n=2*k+1
    ones=cycles.count(1)
    vfix=k_subset_count(cycles,k)
    other=list(cycles)
    if ones:
        other.remove(1)
    efix=ones*k_subset_count(other,k) if ones else 0
    # The complement of the leftover fixed vertex is a disjoint union of permutation cycles.
    sig=1-2*vfix+efix
    cross=2**(len(cycles)-1) if ones==1 and all(l%2==0 for l in cycles if l!=1) else 0
    return sig,1-cross


def check(k):
    n=2*k+1
    A=tuple(combinations(range(n),k));p={u:i for i,u in enumerate(A)}
    V=len(A);adj=[set() for _ in range(2*V)];E=0
    for a in A:
        i=p[a];remainder=set(range(n))-set(a)
        for b in combinations(sorted(remainder),k):
            j=V+p[b];adj[i].add(j);adj[j].add(i);E+=1
    seen={0};queue=deque([0])
    while queue:
        i=queue.popleft()
        for j in adj[i]-seen:
            seen.add(j);queue.append(j)
    assert len(seen)==2*V
    shapes=[(2*k-j,j,1) for j in range(1,k+1)]
    dims=[hook_dim(x) for x in shapes]
    assert sum(dims)==E-2*V+1
    tested=0
    for ctype in partitions(n):
        lhs=actual_characters(k,ctype)
        chars=[specht_character(x,ctype) for x in shapes]
        rhs=(sum(chars),sum((-1)**(j+1)*chars[j-1] for j in range(1,k+1)))
        assert lhs==rhs, (k,ctype,lhs,rhs)
        tested+=1
    print(f'k={k}: {2*V} graph vertices, {E} edges, H1 rank={sum(dims)}, Specht dimensions={dims}, tested {tested} character cycle-types for both color-swap parities')


if __name__=='__main__':
    for k in range(2,6):check(k)
