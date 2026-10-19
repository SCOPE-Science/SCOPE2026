"""Independent finite checks for the width-two sorting-supersequence theorem.

Uses standard Python 3 only. Exhaustively scans endpoint pairings through n=6,
and breadth-first-searches every legal disjoint-adjacent-swap permutation
family through n=7. This is finite corroboration, not the infinite proof.
"""
from collections import deque
from functools import lru_cache
from itertools import permutations


def pairings(points):
    if not points:
        yield ()
        return
    a = points[0]
    for j in range(1, len(points)):
        b = points[j]
        for tail in pairings(points[1:j] + points[j+1:]):
            yield ((a, b),) + tail


def overlap(a, b):
    return max(a[0], b[0]) < min(a[1], b[1])


def good_ply2(I):
    # Distinct endpoints make the maximal ply visible immediately after a start.
    events = sorted((x, +1) for x, _ in I) + []
    events += [(y, -1) for _, y in I]
    count = 0
    for x, d in sorted(events):
        count += d
        if count > 2:
            return False
    return True


def build_word(I):
    n = len(I)
    G = [[j for j in range(n) if j != i and overlap(I[i], I[j])]
         for i in range(n)]
    color = [-1] * n
    for s in range(n):
        if color[s] >= 0:
            continue
        color[s] = 0
        Q = deque([s])
        while Q:
            u = Q.popleft()
            for v in G[u]:
                if color[v] < 0:
                    color[v] = color[u] ^ 1
                    Q.append(v)
                else:
                    assert color[v] != color[u]
    A = sorted((i for i in range(n) if color[i] == 0), key=lambda i:I[i][0])
    B = sorted((i for i in range(n) if color[i] == 1), key=lambda i:I[i][0])
    # Color classes are chains in the order of left endpoints.
    assert all(I[u][1] < I[v][0] for group in (A, B) for u, v in zip(group, group[1:]))
    bounds = {}
    for i in A:
        lo = sum(I[j][1] < I[i][0] for j in B)
        hi = len(B)-sum(I[i][1] < I[j][0] for j in B)
        assert 0 <= lo <= hi <= len(B)
        bounds[i] = lo, hi
    W = []
    for k in range(len(B)+1):
        W.extend(i for i in A if bounds[i][0] <= k <= bounds[i][1])
        if k < len(B):
            W.append(B[k])
    edges = sum(overlap(I[i], I[j]) for i in range(n) for j in range(i+1,n))
    assert len(W) == n+edges
    return W,edges


def is_subsequence(target, word):
    it = iter(word)
    return all(any(x == c for x in it) for c in target)


def linear_extensions(I):
    n=len(I)
    for p in permutations(range(n)):
        rank = [0]*n
        for k,x in enumerate(p):rank[x]=k
        if all(rank[i] < rank[j] for i in range(n) for j in range(n)
               if i != j and I[i][1] < I[j][0]):
            yield p


@lru_cache(None)
def adjacent_perms(n, i=0):
    if i == n:
        return ((),)
    ans = [ (i,)+p for p in adjacent_perms(n,i+1)]
    if i+1<n:
        ans += [(i+1,i)+p for p in adjacent_perms(n,i+2)]
    return tuple(ans)


def exact_min_length(targets):
    n = len(targets[0]); start=(0,)*len(targets); goal=(n,)*len(targets)
    queue=deque([start]); dist={start:0}
    while queue:
        current=queue.popleft()
        if current==goal:
            return dist[current], len(dist)
        for c in range(n):
            nxt=tuple(t+(t<n and p[t]==c) for t,p in zip(current,targets))
            if nxt not in dist:
                dist[nxt]=dist[current]+1
                queue.append(nxt)
    raise AssertionError('goal unreachable')


def main():
    total = 0
    feasible = 0
    tested_extensions = 0
    for n in range(1,7):
        local_total = local_feasible = local_extensions=0
        for pairing in pairings(tuple(range(2*n))):
            local_total+=1
            I=tuple(sorted(pairing))
            if not good_ply2(I):
                continue
            local_feasible+=1
            word, edges=build_word(I)
            components = n-edges
            assert len(word) == 2*n-components
            for p in linear_extensions(I):
                assert is_subsequence(p, word), (I, word, p)
                local_extensions+=1
        total += local_total
        feasible += local_feasible
        tested_extensions += local_extensions
        print('n=%s pairings=%s ply2=%s linear_extensions_checked=%s' % (n,local_total,local_feasible,local_extensions))
    print('total_pairings=%s total_ply2=%s total_extensions=%s' %
          (total,feasible,tested_extensions))
    for n in range(2,8):
        I=tuple((2*i,2*i+3) for i in range(n))
        word,edges=build_word(I)
        ps=adjacent_perms(n)
        assert edges==n-1 and all(is_subsequence(p,word) for p in ps)
        length,states=exact_min_length(ps)
        assert length == 2*n-1
        print('path_n=%s disjoint_swap_orders=%s min_length=%s BFS_states=%s' %
              (n,len(ps),length,states))
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    main()
