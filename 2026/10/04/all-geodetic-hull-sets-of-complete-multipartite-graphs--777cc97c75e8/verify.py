from itertools import combinations
from math import comb
from collections import Counter

def partitions(n, minimum=1):
    if n == 0:
        yield ()
        return
    for first in range(minimum, n + 1):
        for rest in partitions(n - first, first):
            yield (first,) + rest

def build_graph(parts):
    part_of=[]
    for i,m in enumerate(parts):
        part_of.extend([i]*m)
    n=len(part_of)
    adj=[[False]*n for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if u != v and part_of[u] != part_of[v]:
                adj[u][v]=True
    return part_of, adj

def all_distances(adj):
    n=len(adj)
    inf=10**9
    d=[[inf]*n for _ in range(n)]
    for s in range(n):
        d[s][s]=0
        q=[s]
        for u in q:
            for v,a in enumerate(adj[u]):
                if a and d[s][v] == inf:
                    d[s][v]=d[s][u]+1
                    q.append(v)
    return d

def geodetic_hull(mask, d):
    n=len(d)
    h={v for v in range(n) if (mask >> v) & 1}
    while True:
        nxt=set(h)
        for u in h:
            for v in h:
                uv=d[u][v]
                for w in range(n):
                    if d[u][w] + d[w][v] == uv:
                        nxt.add(w)
        if nxt == h:
            return h
        h=nxt

def predicted_hull(mask, parts, part_of):
    counts=[0]*len(parts)
    for v,i in enumerate(part_of):
        if (mask >> v) & 1:
            counts[i]+=1
    nontrivial=sum(m >= 2 for m in parts)
    n=len(part_of)
    if nontrivial >= 2:
        return any(c >= 2 for c in counts)
    if nontrivial == 1:
        i=next(i for i,m in enumerate(parts) if m >= 2)
        return counts[i] == parts[i]
    return mask == (1 << n) - 1

def bad_coefficients(parts, n):
    # coefficient vector of product_i (1+n_i x)
    dp=[1]+[0]*n
    for m in parts:
        nxt=dp[:]
        for k in range(n):
            if dp[k]:
                nxt[k+1]+=dp[k]*m
        dp=nxt
    return dp

def main():
    profiles=subset_checks=hull_sets=coefficient_checks=minimum_checks=0
    for n in range(2,10):
        for parts in partitions(n):
            if len(parts) < 2:
                continue
            profiles += 1
            part_of,adj=build_graph(parts)
            d=all_distances(adj)
            coeff=Counter()
            observed_min=None
            for mask in range(1 << n):
                actual=len(geodetic_hull(mask,d)) == n
                predicted=predicted_hull(mask,parts,part_of)
                subset_checks += 1
                assert actual == predicted, (parts,mask,actual,predicted)
                if actual:
                    s=mask.bit_count()
                    coeff[s]+=1
                    hull_sets += 1
                    observed_min=s if observed_min is None else min(observed_min,s)
            nontrivial=sum(m >= 2 for m in parts)
            bad=bad_coefficients(parts,n)
            for s in range(n+1):
                if nontrivial >= 2:
                    expected=comb(n,s)-bad[s]
                elif nontrivial == 1:
                    m=next(m for m in parts if m >= 2)
                    expected=comb(n-m,s-m) if m <= s <= n else 0
                else:
                    expected=1 if s == n else 0
                coefficient_checks += 1
                assert coeff[s] == expected, (parts,s,coeff[s],expected)
            expected_min=(2 if nontrivial >= 2 else
                          next(m for m in parts if m >= 2) if nontrivial == 1 else n)
            minimum_checks += 1
            assert observed_min == expected_min, (parts,observed_min,expected_min)
    print(f"VERIFY_OK profiles={profiles} subset_checks={subset_checks} hull_sets={hull_sets} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} max_order=9")

if __name__ == '__main__':
    main()
