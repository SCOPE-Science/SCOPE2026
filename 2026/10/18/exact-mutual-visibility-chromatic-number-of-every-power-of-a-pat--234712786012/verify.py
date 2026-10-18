"""BFS verification of mutual-visibility colorings of powers of paths."""
from collections import deque
from functools import lru_cache
from itertools import combinations


def adjacency(n, radius):
    return [tuple(j for j in range(max(0, i-radius), min(n, i+radius+1))
                  if i != j) for i in range(n)]


def shortest(adj, start, target, forbidden=frozenset()):
    queue = deque([(start, 0)])
    seen = {start}
    while queue:
        u, length = queue.popleft()
        if u == target:
            return length
        for v in adj[u]:
            if v not in seen and v not in forbidden:
                seen.add(v)
                queue.append((v, length+1))
    return None


def mutually_visible(adj, vertices):
    blocked = set(vertices)
    for x, y in combinations(vertices, 2):
        if shortest(adj, x, y) != shortest(adj, x, y, blocked-{x, y}):
            return False
    return True


def proposed(n, k):
    if n <= k+1:
        return [list(range(n))]
    if n <= 2*k:
        return [list(range(k)), list(range(k,n))]
    t = (n+2*k-1)//(2*k)
    return [[x for x in list(range(i*k, (i+1)*k)) +
             list(range((t+i)*k, (t+i+1)*k)) if x < n]
            for i in range(t) if i*k < n]


def formula(n, k):
    if n <= k+1:
        return 1
    return max(2, (n+2*k-1)//(2*k))


def main():
    classes = 0
    verified_pairs = 0
    for k in range(1,9):
        for n in range(1,66):
            adj = adjacency(n, k)
            groups = proposed(n, k)
            assert len(groups) == formula(n,k), (n,k,len(groups))
            assert sorted(x for group in groups for x in group) == list(range(n)), (n,k)
            for group in groups:
                assert mutually_visible(adj, group), (n,k,group)
                classes += 1
                verified_pairs += len(group)*(len(group)-1)//2
    print(f'CONSTRUCTIONS_OK parameters=520 groups={classes} pair_checks={verified_pairs}')

    case_count = 0
    examined = 0
    for k in range(1,5):
        for n in range(1,11):
            adj = adjacency(n,k)
            allowed = []
            for z in range(1,min(n,2*k)+1):
                for sample in combinations(range(n),z):
                    examined += 1
                    if mutually_visible(adj,sample):
                        allowed.append(sum(1<<v for v in sample))
            by_first = [[m for m in allowed if (m>>u)&1] for u in range(n)]
            @lru_cache(None)
            def optimum(left):
                if left == 0:
                    return 0
                first = (left & -left).bit_length()-1
                return 1+min(optimum(left ^ m) for m in by_first[first] if (left&m)==m)
            result = optimum((1<<n)-1)
            assert result == formula(n,k), (n,k,result)
            case_count += 1
    print(f'EXACT_PARTITIONS_OK cases={case_count} candidates_examined={examined}')
    print('VERIFICATION_OK')

if __name__ == '__main__':
    main()
