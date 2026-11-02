"""Exact finite checks for distortion and cut balance in tensor-product clique graphs.
Only Python's standard library is needed. Analytical all-n proof is in RESULT.md.
"""
from collections import deque
from fractions import Fraction
from itertools import combinations, permutations
from random import Random

COUNTS = {"distance_pairs": 0, "cut_certificates": 0, "embedding_pairs": 0}


def bits_of_cut(mask, n):
    k = mask.bit_count()
    rows = [sum((mask >> (i*n+j)) & 1 for j in range(n)) for i in range(n)]
    cols = [sum((mask >> (i*n+j)) & 1 for i in range(n)) for j in range(n)]
    u = sum(r*(n-r) for r in rows)
    v = sum(c*(n-c) for c in cols)
    t = k*(n*n-k)
    w = t-u-v
    return k,rows,cols,u,v,w,t


def check_cut(mask, n):
    k, rows, cols, u, v, w, t = bits_of_cut(mask,n)
    assert w >= 0
    defect = 2*t-n*(u+v)
    sos = sum((n*r-k)**2 for r in rows)+sum((n*c-k)**2 for c in cols)
    assert n*defect == sos and defect >= 0
    equal = defect == 0
    regular = len(set(rows))==1 and len(set(cols))==1 and rows[0]==cols[0]
    assert equal == regular
    if 0 < k < n*n and equal:
        assert 1 <= rows[0] <= n-1
    COUNTS['cut_certificates'] += 1


def graph_distances(n):
    nn=n*n
    adj=[[] for _ in range(nn)]
    for i in range(n):
        for j in range(n):
            for a in range(n):
                for b in range(n):
                    if a != i and b != j:
                        adj[i*n+j].append(a*n+b)
    assert all(len(z)==(n-1)*(n-1) for z in adj)
    for x in range(nn):
        dist=[-1]*nn; dist[x]=0
        q=deque([x])
        while q:
            y=q.popleft()
            for z in adj[y]:
                if dist[z]==-1:
                    dist[z]=dist[y]+1;q.append(z)
        for y in range(nn):
            if x == y: target=0
            elif x//n != y//n and x%n != y%n:target=1
            else:target=2
            assert dist[y] == target
            COUNTS['distance_pairs'] += 1


def check_embedding(n):
    perms=list(permutations(range(n)))
    number=len(perms)
    for i in range(n):
        for j in range(n):
            for a in range(n):
                for b in range(n):
                    if (i,j)>=(a,b):continue
                    selected=0
                    for pi in perms:
                        selected += (int(pi[i]==j) != int(pi[a]==b))
                    emb=Fraction(n*selected,number)
                    if i==a or j==b: desired=Fraction(2)
                    else: desired=Fraction(2*(n-2), n-1)
                    assert emb==desired, (n,(i,j),(a,b),emb,desired)
                    COUNTS['embedding_pairs'] += 1


def main():
    rng=Random(20261029)
    for n in range(3,9): graph_distances(n)
    for n in (3,4):
        for mask in range(1 << (n*n)): check_cut(mask,n)
    for n in range(5,13):
        masks=[0,1,(1<<(n*n))-1]
        for k in (1,n-1,n,n+1,n*n//2):
            for _ in range(150):
                positions=rng.sample(range(n*n),min(k,n*n))
                masks.append(sum(1<<x for x in positions))
        for _ in range(1000):
            masks.append(rng.getrandbits(n*n))
        # Each cyclic shift gives a perfect-matching cut of size n.
        match=sum(1 << (i*n+((i+1)%n)) for i in range(n))
        masks.append(match)
        check_cut(match,n)
        assert bits_of_cut(match,n)[1] == [1]*n
        assert bits_of_cut(match,n)[2] == [1]*n
        for mask in masks: check_cut(mask,n)
    for n in range(3,7):check_embedding(n)
    print('CHECK_OK',COUNTS)

if __name__=='__main__':main()
