from itertools import combinations, permutations, product
from collections import defaultdict


def connected_tree(n, edges):
    if len(edges) != n - 1:
        return False
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


def rooted_tree_data(n, tree_edges, root):
    adj = [[] for _ in range(n)]
    for u, v in tree_edges:
        adj[u].append(v)
        adj[v].append(u)
    parent = [-1] * n
    depth = [0] * n
    children = [[] for _ in range(n)]
    parent[root] = root
    stack = [root]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                depth[v] = depth[u] + 1
                children[u].append(v)
                stack.append(v)
    return parent, depth, children


def is_ancestor(parent, anc, v):
    while True:
        if v == anc:
            return True
        if parent[v] == v:
            return False
        v = parent[v]


def contour(root, ordered_children):
    out = []

    def visit(u):
        out.append(u)
        for v in ordered_children[u]:
            visit(v)
            out.append(u)

    visit(root)
    return out


def klx_of_ordered_dfs(n, graph_edges, tree_edges, root, ordered_children):
    tree_set = {tuple(sorted(e)) for e in tree_edges}
    parent, depth, _ = rooted_tree_data(n, tree_edges, root)
    for u, v in graph_edges:
        if tuple(sorted((u, v))) in tree_set:
            continue
        if depth[u] > depth[v]:
            desc, anc = u, v
        else:
            desc, anc = v, u
        if not is_ancestor(parent, anc, desc):
            return None

    tour = contour(root, ordered_children)
    occurrences = defaultdict(list)
    for pos, v in enumerate(tour):
        occurrences[v].append(pos)

    arcs = []
    for u, v in graph_edges:
        if tuple(sorted((u, v))) in tree_set:
            continue
        if depth[u] > depth[v]:
            desc, anc = u, v
        else:
            desc, anc = v, u
        start = occurrences[desc][-1]
        end = next(pos for pos in occurrences[anc] if pos > start)
        arcs.append((start, end))

    best = 0
    for child in range(n):
        if child == root:
            continue
        par = parent[child]
        return_positions = [
            i
            for i in range(len(tour) - 1)
            if tour[i] == child and tour[i + 1] == par
        ]
        assert len(return_positions) == 1
        pos = return_positions[0]
        best = max(best, sum(start <= pos < end for start, end in arcs))
    return best


def brute_klx(n, graph_edges):
    best = None
    for tree_edges in combinations(graph_edges, n - 1):
        if not connected_tree(n, tree_edges):
            continue
        for root in range(n):
            parent, depth, children = rooted_tree_data(n, tree_edges, root)
            tree_set = {tuple(sorted(e)) for e in tree_edges}
            valid = True
            for u, v in graph_edges:
                if tuple(sorted((u, v))) in tree_set:
                    continue
                if depth[u] > depth[v]:
                    desc, anc = u, v
                else:
                    desc, anc = v, u
                if not is_ancestor(parent, anc, desc):
                    valid = False
                    break
            if not valid:
                continue

            branch_vertices = [u for u in range(n) if len(children[u]) > 1]
            choices = [list(permutations(children[u])) for u in branch_vertices]
            for selected in product(*choices) if choices else [()]:
                ordered = [list(ch) for ch in children]
                for u, ch in zip(branch_vertices, selected):
                    ordered[u] = list(ch)
                value = klx_of_ordered_dfs(
                    n, graph_edges, tree_edges, root, ordered
                )
                if value is not None and (best is None or value < best):
                    best = value
    return best


def predicted_biclique(a, b):
    if a > b:
        a, b = b, a
    if a == 1:
        return 0
    if b <= 3 * a - 2:
        value = ((a + b) ** 2) // 8 - 1
        if a == b and a % 2 == 1:
            value += 1
        return value
    return (a - 1) * (b - a + 2) - 1


def predicted_clique(n):
    if n <= 1:
        return 0
    return (n * n) // 4 - 1


def complete_bipartite_edges(a, b):
    return [(i, a + j) for i in range(a) for j in range(b)]


def complete_edges(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


checked = []
for a in range(1, 4):
    for b in range(a, 7 - a + 1):
        if a + b > 7:
            continue
        edges = complete_bipartite_edges(a, b)
        actual = brute_klx(a + b, edges)
        expected = predicted_biclique(a, b)
        assert actual == expected, (a, b, actual, expected)
        checked.append((a, b, actual))

for n in range(2, 9):
    edges = complete_edges(n)
    values = set()
    for order in permutations(range(n)):
        tree_edges = list(zip(order, order[1:]))
        ordered = [[] for _ in range(n)]
        for u, v in tree_edges:
            ordered[u].append(v)
        value = klx_of_ordered_dfs(n, edges, tree_edges, order[0], ordered)
        values.add(value)
    assert values == {predicted_clique(n)}, (n, values)

print("complete bipartite cases:", len(checked))
print("biclique values:", checked)
print("cliques checked: K_2 through K_8")
print("all checks passed")
