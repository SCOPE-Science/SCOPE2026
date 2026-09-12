"""Enumerate the 20 six-cycles of the Desargues base G(10,3) by two independent
algorithms (directed DFS cycle search; induced-C6 subset test), build the
GF(2) parity system over the 11 co-tree variables, and prove exactly one of
the 2048 switching classes unfolds every 6-cycle. Prints the census."""
import itertools
import json
from collections import deque

N = 20
EDGES = []
for i in range(10):
    EDGES.append((i, (i + 1) % 10))
    EDGES.append((i, 10 + i))
    EDGES.append((10 + i, 10 + ((i + 3) % 10)))
EDGE_INDEX = {tuple(sorted(e)): i for i, e in enumerate(EDGES)}
ADJ = {v: sorted(w for w in range(N) if tuple(sorted((v, w))) in EDGE_INDEX)
       for v in range(N)}


def spanning_tree():
    tree = set()
    seen = {0}
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for w in ADJ[u]:
            if w not in seen:
                seen.add(w)
                tree.add(EDGE_INDEX[tuple(sorted((u, w)))])
                queue.append(w)
    assert len(tree) == N - 1
    return tree


def cycles_dfs():
    found = set()

    def dfs(start, cur, depth, path, visited):
        if depth == 6:
            if start in ADJ[cur]:
                rots = [tuple(path[(i + j) % 6] for j in range(6))
                        for i in range(6)]
                rev = tuple(reversed(path))
                rots += [tuple(rev[(i + j) % 6] for j in range(6))
                         for i in range(6)]
                found.add(min(rots))
            return
        for w in ADJ[cur]:
            if w == start or w in visited:
                continue
            visited.add(w)
            path.append(w)
            dfs(start, w, depth + 1, path, visited)
            path.pop()
            visited.remove(w)

    for s in range(N):
        dfs(s, s, 1, [s], {s})
    return sorted(found)


def cycles_subset():
    out = []
    for combo in itertools.combinations(range(N), 6):
        S = set(combo)
        if any(sum(1 for w in ADJ[v] if w in S) != 2 for v in S):
            continue
        seen = {combo[0]}
        stack = [combo[0]]
        while stack:
            u = stack.pop()
            for w in ADJ[u]:
                if w in S and w not in seen:
                    seen.add(w)
                    stack.append(w)
        if len(seen) == 6:
            out.append(combo)
    return out


def solve_gf2(mat, rhs):
    rows = [row[:] + [b] for row, b in zip(mat, rhs)]
    nrows, ncols = len(rows), len(mat[0])
    where = [-1] * ncols
    row = 0
    for col in range(ncols):
        sel = next((i for i in range(row, nrows) if rows[i][col] == 1), -1)
        if sel < 0:
            continue
        rows[row], rows[sel] = rows[sel], rows[row]
        where[col] = row
        for i in range(nrows):
            if i != row and rows[i][col] == 1:
                for j in range(col, ncols + 1):
                    rows[i][j] ^= rows[row][j]
        row += 1
    if any(rows[i][ncols] == 1 for i in range(row, nrows)):
        return None
    return [rows[where[j]][ncols] if where[j] >= 0 else 0 for j in range(ncols)]


def main():
    tree = spanning_tree()
    cotree = sorted(i for i in range(len(EDGES)) if i not in tree)
    cyc_dfs = cycles_dfs()
    cyc_sub = cycles_subset()
    assert len(cyc_dfs) == 20, len(cyc_dfs)
    assert sorted(tuple(sorted(c)) for c in cyc_dfs) == sorted(cyc_sub)
    edge_lists = []
    for c in cyc_dfs:
        edge_lists.append([EDGE_INDEX[tuple(sorted((c[j], c[(j + 1) % 6])))]
                           for j in range(6)])
    mat = [[1 if cotree[j] in el else 0 for j in range(len(cotree))]
           for el in edge_lists]
    sol = solve_gf2(mat, [1] * len(edge_lists))
    assert sol is not None
    sols = [mm for mm in range(2048)
            if all(sum(1 for e in el
                       if e not in tree and (mm >> cotree.index(e)) & 1) % 2 == 1
                   for el in edge_lists)]
    assert len(sols) == 1
    mask = sols[0]
    assert mask == sum(v << j for j, v in enumerate(sol))
    print("dfs cycles:", len(cyc_dfs), "subset C6 sets:", len(cyc_sub))
    print("unique all-unfolding mask:", mask)
    with open("artifacts/girth_census.json", "w") as f:
        json.dump({"num_six_cycles": 20, "num_four_cycles": 0,
                   "six_cycles": [list(c) for c in cyc_dfs],
                   "cotree": cotree, "tree_edges": sorted(tree),
                   "unfolding_mask": mask}, f, indent=1)


if __name__ == "__main__":
    main()
