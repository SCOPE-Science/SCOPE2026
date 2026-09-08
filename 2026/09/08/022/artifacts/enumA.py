"""Enumerator A: left-to-right backtracking with prefix pruning + inversion tracking."""
import sys, json, itertools

FORBIDDEN = [(1,3,2,4),(1,2,4,3),(1,4,3,2)]

def rank_of_4(a,b,c,d):
    # return relative order tuple of 4 distinct values
    vals = [a,b,c,d]
    s = sorted(vals)
    r = {v:i+1 for i,v in enumerate(s)}
    return (r[a],r[b],r[c],r[d])

FORBSET = set(FORBIDDEN)

def contains_forbidden_with_last(perm):
    """perm is list; check all quadruples ending at last position. Return True if forbidden found."""
    m = len(perm)
    if m < 4: return False
    d = perm[-1]
    # iterate triples of earlier indices
    for i in range(m-1):
        a = perm[i]
        for j in range(i+1, m-1):
            b = perm[j]
            for k in range(j+1, m-1):
                c = perm[k]
                if FORBSET.__contains__(rank_of_4(a,b,c,d)):
                    return True
    return False

def enumerate_n(n):
    from collections import Counter
    dist = Counter()
    total = 0
    # stack of (perm_list, used_bitmask, inv)
    # iterative DFS
    # use lists
    count_nodes = 0
    def dfs(perm, used, inv):
        nonlocal total, count_nodes
        m = len(perm)
        if m == n:
            dist[inv] += 1
            total += 1
            return
        for v in range(1, n+1):
            bit = 1 << v
            if used & bit: continue
            # new inversions added = # of previous elements > v
            add = 0
            for u in perm:
                if u > v: add += 1
            perm.append(v)
            count_nodes += 1
            if not contains_forbidden_with_last(perm):
                dfs(perm, used | bit, inv + add)
            perm.pop()
    dfs([], 0, 0)
    return total, dict(dist), count_nodes

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv)>1 else 8
    total, dist, nodes = enumerate_n(n)
    print(f"n={n} total={total} nodes={nodes}")
    ks = sorted(dist)
    print(f"kmax={max(ks)} nperms_check={sum(dist.values())}")
    with open(f"distA_n{n}.json","w") as f:
        json.dump({str(k):dist[k] for k in sorted(dist)}, f)
