"""Finite cross-checks of stable colorings of complete graphs minus matchings.

Run: python3 verify.py
No third-party packages required.
"""
from itertools import permutations
import random


def graph(n, r):
    missing = {(2*i, 2*i+1) for i in range(r)}
    return [[(i != j and (min(i,j), max(i,j)) not in missing)
             for j in range(n)] for i in range(n)]


def rankings(n, r, q):
    ranks = [list(range(q)) for _ in range(n)]
    for i in range(r):
        ranks[2*i] = list(range(q))
        ranks[2*i+1] = list(reversed(range(q)))
    # lower rank = better
    return ranks


def proper_colorings(n, r, q):
    # Enumerate all labeled proper q-colorings by consecutively processing
    # the r nonadjacent pairs and the n-2r singleton vertices.
    current = [None]*n
    def rec(pos, used):
        if pos == r + n - 2*r:
            yield tuple(current)
            return
        if pos < r:
            a,b=2*pos,2*pos+1
            for c in range(q):
                if c in used: continue
                current[a]=current[b]=c
                yield from rec(pos+1,used|{c})
            for c in range(q):
                if c in used: continue
                for d in range(q):
                    if d==c or d in used: continue
                    current[a],current[b]=c,d
                    yield from rec(pos+1,used|{c,d})
        else:
            a=2*r+(pos-r)
            for c in range(q):
                if c in used: continue
                current[a]=c
                yield from rec(pos+1,used|{c})
    yield from rec(0,set())


def blocking_pair_exists(colors,adj,rank):
    n=len(colors)
    for i in range(n):
        for j in range(i+1,n):
            if (adj[i][j] and rank[i][colors[j]] < rank[i][colors[i]]
                 and rank[j][colors[i]] < rank[j][colors[j]]):
                return True
    return False


def upper_construct(n,r,rank):
    q=n-1
    adj=graph(n,r)
    # The first two vertices form a missing edge, so orient all remaining
    # edges in the increasing order 0,1,...,n-1. There are no arcs into
    # either 0 or 1. Compute every directed reachable set explicitly.
    reaches=[set() for _ in range(n)]
    for i in reversed(range(n)):
        for j in range(i+1,n):
            if adj[i][j]:
                reaches[i].add(j)
                reaches[i].update(reaches[j])
    assert all(len(x) <= q-1 for x in reaches)
    colors=[None]*n
    for i in reversed(range(n)):
        excluded={colors[j] for j in reaches[i]}
        colors[i]=next(c for c in rank[i] if c not in excluded)
    assert all(not adj[i][j] or colors[i]!=colors[j]
        for i in range(n) for j in range(i+1,n))
    # Every envy edge must follow the acyclic increasing orientation.
    assert all(not adj[i][j] or rank[j].index(colors[i]) > rank[j].index(colors[j])
        for i in range(n) for j in range(i+1,n))
    return colors


def main():
    rng=random.Random(1729)
    lower_profiles=lower_colorings=upper_profiles=0
    for n in range(4,9):
        for r in range(2,n//2+1):
            q=n-2
            adj=graph(n,r); rank=rankings(n,r,q)
            examined=0
            for colors in proper_colorings(n,r,q):
                assert blocking_pair_exists(colors,adj,rank), (n,r,colors)
                examined+=1
            assert examined>0
            lower_profiles+=1;lower_colorings+=examined
            print(f"lower n={n}, r={r}, q={q}: {examined} proper colorings, each has blocking 2-cycle")
    for n in range(2,12):
        for r in range(1,n//2+1):
            q=n-1
            for _ in range(100):
                rank=[list(rng.sample(range(q),q)) for i in range(n)]
                upper_construct(n,r,rank)
                upper_profiles+=1
    print(f"PASS: lower tested {lower_profiles} graph profiles, {lower_colorings} proper colorings")
    print(f"PASS: upper tested {upper_profiles} arbitrary preference profiles")
    print("The proof for unrestricted graph order and preference profiles is analytic, not experimental.")

if __name__=='__main__':main()
