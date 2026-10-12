from itertools import combinations
from collections import deque

def balanced_spider(q):
    # Center c=0. Arm i is c-u_i-v_i-w_i.
    n = 1 + 3*q
    adj = [set() for _ in range(n)]
    for i in range(q):
        u = 1 + 3*i
        v = u + 1
        w = u + 2
        for a,b in ((0,u),(u,v),(v,w)):
            adj[a].add(b)
            adj[b].add(a)
    return adj

def all_distances(adj):
    D = []
    for s in range(len(adj)):
        d = [-1]*len(adj)
        d[s] = 0
        queue = deque([s])
        while queue:
            x = queue.popleft()
            for y in adj[x]:
                if d[y] < 0:
                    d[y] = d[x] + 1
                    queue.append(y)
        D.append(d)
    return D

def is_distance_equalizer(D, mask):
    outside = [x for x in range(len(D)) if not ((mask >> x) & 1)]
    selected = [x for x in range(len(D)) if (mask >> x) & 1]
    for i in range(len(outside)):
        x = outside[i]
        for y in outside[i+1:]:
            if not any(D[s][x] == D[s][y] for s in selected):
                return False
    return True

def predicted_bases(q):
    # Odd bipartition B={u_i,w_i}; and q bases A union (U\{u_j}).
    B = 0
    A = 1 << 0
    U = 0
    for i in range(q):
        u = 1 + 3*i
        v = u + 1
        w = u + 2
        B |= (1 << u) | (1 << w)
        A |= 1 << v
        U |= 1 << u
    out = {B}
    for j in range(q):
        u_j = 1 + 3*j
        out.add(A | (U & ~(1 << u_j)))
    return out

subset_trials = 0
basis_trials = 0

for q in range(3, 7):
    adj = balanced_spider(q)
    D = all_distances(adj)
    n = len(adj)
    target = 2*q

    for mask in range(1 << n):
        k = mask.bit_count()
        if k > target:
            continue
        subset_trials += 1
        good = is_distance_equalizer(D, mask)
        if k < target:
            assert not good, (q, "smaller", k, mask)
        elif good:
            basis_trials += 1

    actual = {
        mask for mask in range(1 << n)
        if mask.bit_count() == target and is_distance_equalizer(D, mask)
    }
    expected = predicted_bases(q)
    assert actual == expected, (q, len(actual), len(expected))
    assert len(actual) == q + 1

print("VERIFY_OK")
print("parameters_q_checked =", list(range(3, 7)))
print("subset_trials_size_at_most_2q =", subset_trials)
print("minimum_bases_checked =", basis_trials)
print("all smaller sets failed")
print("all minimum sets matched the q+1 structural bases")
