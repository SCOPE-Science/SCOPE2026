from itertools import combinations


def connected(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == n


def biconnected_edge_components(n, edges):
    adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i))
        adj[v].append((u, i))
    disc = [-1] * n
    low = [0] * n
    estack = []
    comps = []
    clock = 0

    def dfs(u, parent_edge):
        nonlocal clock
        disc[u] = low[u] = clock
        clock += 1
        for v, eid in adj[u]:
            if eid == parent_edge:
                continue
            if disc[v] == -1:
                estack.append(eid)
                dfs(v, eid)
                low[u] = min(low[u], low[v])
                if low[v] >= disc[u]:
                    comp = []
                    while True:
                        x = estack.pop()
                        comp.append(x)
                        if x == eid:
                            break
                    comps.append(comp)
            elif disc[v] < disc[u]:
                estack.append(eid)
                low[u] = min(low[u], disc[v])

    dfs(0, -1)
    return comps


def is_cactus(n, edges):
    if not connected(n, edges):
        return False
    for comp in biconnected_edge_components(n, edges):
        if len(comp) == 1:
            continue
        vertices = set()
        degree = {}
        for eid in comp:
            u, v = edges[eid]
            vertices.update((u, v))
            degree[u] = degree.get(u, 0) + 1
            degree[v] = degree.get(v, 0) + 1
        if len(comp) != len(vertices):
            return False
        if any(degree[v] != 2 for v in vertices):
            return False
    return True


def b_conflict_graph(edges):
    m = len(edges)
    adj = [set() for _ in range(m)]
    edge_set = {tuple(sorted(e)) for e in edges}
    for i in range(m):
        a, b = edges[i]
        for j in range(i + 1, m):
            c, d = edges[j]
            if len({a, b, c, d}) < 4:
                adj[i].add(j)
                adj[j].add(i)
                continue
            opposite = (
                tuple(sorted((a, c))) in edge_set
                and tuple(sorted((b, d))) in edge_set
            ) or (
                tuple(sorted((a, d))) in edge_set
                and tuple(sorted((b, c))) in edge_set
            )
            if opposite:
                adj[i].add(j)
                adj[j].add(i)
    return adj


def chromatic_number(adj):
    n = len(adj)
    if n == 0:
        return 0
    order = sorted(range(n), key=lambda v: len(adj[v]), reverse=True)
    greedy = [-1] * n
    upper = 0
    for v in order:
        used = {greedy[w] for w in adj[v] if greedy[w] >= 0}
        c = 0
        while c in used:
            c += 1
        greedy[v] = c
        upper = max(upper, c + 1)

    best = upper
    color = [-1] * n
    saturation = [set() for _ in range(n)]
    uncolored = set(range(n))

    def search(used_colors):
        nonlocal best
        if not uncolored:
            best = min(best, used_colors)
            return
        if used_colors >= best:
            return
        v = max(uncolored, key=lambda x: (len(saturation[x]), len(adj[x]), -x))
        forbidden = saturation[v]
        choices = [c for c in range(used_colors) if c not in forbidden]
        if used_colors < best - 1:
            choices.append(used_colors)
        uncolored.remove(v)
        for c in choices:
            color[v] = c
            touched = []
            for w in adj[v]:
                if w in uncolored and c not in saturation[w]:
                    saturation[w].add(c)
                    touched.append(w)
            search(max(used_colors, c + 1))
            for w in touched:
                saturation[w].remove(c)
            color[v] = -1
        uncolored.add(v)

    search(0)
    return best


def has_c4(n, edges):
    edge_set = {tuple(sorted(e)) for e in edges}
    for a, b, c, d in combinations(range(n), 4):
        for p in ((a, b, c, d), (a, b, d, c), (a, c, b, d)):
            if all(tuple(sorted((p[i], p[(i + 1) % 4]))) in edge_set for i in range(4)):
                return True
    return False


def is_cycle_graph(n, edges):
    if len(edges) != n:
        return False
    degree = [0] * n
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    return all(d == 2 for d in degree)


def predicted_value(n, edges):
    degree = [0] * n
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    delta = max(degree)
    if has_c4(n, edges):
        return max(delta, 4)
    if n % 2 == 1 and is_cycle_graph(n, edges):
        return 3
    return delta


def main():
    counts = {}
    total = 0
    histogram = {}
    for n in range(2, 7):
        pairs = list(combinations(range(n), 2))
        count = 0
        for mask in range(1 << len(pairs)):
            edges = [pairs[i] for i in range(len(pairs)) if (mask >> i) & 1]
            if not is_cactus(n, edges):
                continue
            count += 1
            total += 1
            exact = chromatic_number(b_conflict_graph(edges))
            expected = predicted_value(n, edges)
            if exact != expected:
                raise AssertionError((n, edges, exact, expected))
            histogram[(n, exact)] = histogram.get((n, exact), 0) + 1
        counts[n] = count
    print('ALL CHECKS PASSED')
    print('connected_labeled_cacti_by_order=' + repr(counts))
    print('total_connected_labeled_cacti=' + str(total))
    print('qB_histogram=' + repr(sorted(histogram.items())))


if __name__ == '__main__':
    main()
