#!/usr/bin/env python3
"""Independent finite checks for complete-bipartite general-position polynomial unimodality.

Finite checks supplement, and cannot replace, the parameter-uniform proof in RESULT.md.
Uses only the Python standard library.
"""
from collections import deque
from math import comb

EXCEPTIONS = {(8,4),(8,5),(8,6),(8,7),(8,8),(9,6),(9,7)}


def choose(n,k):
    return comb(n,k) if 0 <= k <= n else 0


def predicted(m,n):
    assert m>=n>=1
    size=m+n
    return [1,size,comb(size,2)] + [choose(m,k)+choose(n,k) for k in range(3,m+1)]


def is_unimodal(coeff):
    phase=0
    for p,q in zip(coeff,coeff[1:]):
        if phase==1 and q>p:
            return False
        if q<p:
            phase=1
    return True


def graph_metric_polynomial(m,n):
    """Definition-level BFS distances + forbidden geodesic triples + exhaustive subsets."""
    vcount=m+n
    nbr=[[] for _ in range(vcount)]
    for i in range(m):
        for j in range(m,m+n):
            nbr[i].append(j)
            nbr[j].append(i)
    dist=[]
    for root in range(vcount):
        ds=[-1]*vcount
        ds[root]=0
        todo=deque([root])
        while todo:
            u=todo.popleft()
            for v in nbr[u]:
                if ds[v]<0:
                    ds[v]=ds[u]+1
                    todo.append(v)
        assert all(x>=0 for x in ds)
        dist.append(ds)
    bad_pairs=[[] for _ in range(vcount)]
    for i in range(vcount):
        for j in range(i+1,vcount):
            for k in range(j+1,vcount):
                if (dist[i][k]==dist[i][j]+dist[j][k]
                    or dist[i][j]==dist[i][k]+dist[k][j]
                    or dist[j][k]==dist[j][i]+dist[i][k]):
                    bad_pairs[i].append((1<<j)|(1<<k))
                    bad_pairs[j].append((1<<i)|(1<<k))
                    bad_pairs[k].append((1<<i)|(1<<j))
    invalid=bytearray(1<<vcount)
    counts=[0]*(vcount+1)
    counts[0]=1
    for mask in range(1,1<<vcount):
        bit=mask&(-mask)
        v=bit.bit_length()-1
        rest=mask^bit
        if invalid[rest]:
            invalid[mask]=1
        else:
            for pair in bad_pairs[v]:
                if pair & rest==pair:
                    invalid[mask]=1
                    break
        if not invalid[mask]:
            counts[mask.bit_count()]+=1
    while counts and counts[-1]==0:
        counts.pop()
    return counts


def check():
    total_bruteforce=0
    pairs=[]
    for m in range(1,8):
        for n in range(1,m+1):
            pairs.append((m,n))
    pairs += [(8,4),(8,5),(8,6),(8,7),(8,8),(9,6),(9,7),(9,9)]
    for m,n in pairs:
        direct=graph_metric_polynomial(m,n)
        expected=predicted(m,n)
        assert direct==expected,(m,n,direct,expected)
        assert is_unimodal(direct)==((m,n) not in EXCEPTIONS),(m,n)
        total_bruteforce +=1<<(m+n)
    print('BFS_GEODESIC_SUBSETS_OK',len(pairs),'boards',total_bruteforce,'vertex subsets')

    for m in range(1,151):
        for n in range(1,m+1):
            a=predicted(m,n)
            assert is_unimodal(a)==((m,n) not in EXCEPTIONS),(m,n)
            tail=[choose(m,k)+choose(n,k) for k in range(m+1)]
            assert all(tail[k]**2>=tail[k-1]*tail[k+1] for k in range(1,m))
            d=m-n
            # Independently check the factorization (1+x)^n[1+(1+x)^(m-n)].
            b=[2]+[choose(d,k) for k in range(1,d+1)]
            conv=[sum(choose(n,j)*b[k-j] for j in range(max(0,k-d),min(k,n)+1)) for k in range(m+1)]
            assert conv==tail
    print('PARAMETER_SWEEP_OK',11325,'unimodality, tail log-concavity, convolution identities')
    for m in (8,9,10):
        values=[(n,choose(m,3)+choose(n,3)-choose(m+n,2),choose(m,4)+choose(n,4)-choose(m,3)-choose(n,3)) for n in range(1,m+1)]
        print('BOUNDARY',m,values)
    print('VERIFY_OK')

if __name__=='__main__':
    check()
