"""Standalone integer-arithmetic checks for finite matching-metric Lipschitz polytopes.
All test instances are finite; this program is not a proof for arbitrary sizes.
Run: python matching_facet_checker.py
"""
from itertools import product


def prufer_trees(n):
    """Generate every labeled spanning tree via the Pruefer bijection."""
    if n == 2:
        yield [(0, 1)]
        return
    for sequence in product(range(n), repeat=n - 2):
        degree = [1] * n
        for v in sequence:
            degree[v] += 1
        edges = []
        for v in sequence:
            leaf = min(i for i, d in enumerate(degree) if d == 1)
            edges.append((leaf, v))
            degree[leaf] -= 1
            degree[v] -= 1
        last = [i for i, d in enumerate(degree) if d == 1]
        edges.append((last[0], last[1]))
        yield edges


def exhaustive_vertices(n, lengths, scale):
    # Short pairs are (0,1), (2,3), ... . All other distances are scale.
    d = [[0 if i == j else scale for j in range(n)] for i in range(n)]
    for j, v in enumerate(lengths):
        d[2*j][2*j+1] = d[2*j+1][2*j] = v
    edges = [(i, j) for i in range(n) for j in range(i+1, n)]
    out = set()
    for tree in prufer_trees(n):
        neighbors = [[] for _ in range(n)]
        for idx, (u, v) in enumerate(tree):
            neighbors[u].append((v, idx, d[u][v]))
            neighbors[v].append((u, idx, d[u][v]))
        for directions in product((-1, 1), repeat=n-1):
            values = [None] * n
            values[0] = 0
            stack = [0]
            while stack:
                v = stack.pop()
                for w, idx, length in neighbors[v]:
                    if values[w] is None:
                        a, b = tree[idx]
                        increment = directions[idx] * length
                        values[w] = values[v] + (increment if v == a else -increment)
                        stack.append(w)
            if all(abs(values[i]-values[j]) <= d[i][j] for i,j in edges):
                out.add(tuple(values))
    return out


def classified_vertices(n, lengths, scale):
    k = len(lengths)
    sides = k + (n - 2*k)
    result = set()
    for upper_lower in product((0,1), repeat=sides):
        if not (0 in upper_lower and 1 in upper_lower):
            continue
        for ternary in product((0,1,2), repeat=k):
            vals = []
            for i, w in enumerate(lengths):
                side = upper_lower[i]
                if side == 0:
                    vals.extend([(0,0),(0,w),(w,0)][ternary[i]])
                else:
                    vals.extend([(scale,scale),(scale,scale-w),(scale-w,scale)][ternary[i]])
            vals.extend([scale*z for z in upper_lower[k:]])
            result.add(tuple(v-vals[0] for v in vals))
    return result


def run():
    checked = 0
    cases = [([12,24,36],60), ([30,45,50],60), ([54,42,48],60)]
    for n in range(3,7):
        for k in range(0,n//2 + 1):
            for values, scale in cases:
                lengths = values[:k]
                exact = exhaustive_vertices(n,lengths,scale)
                explicit = classified_vertices(n,lengths,scale)
                expected = (3**k)*(2**(n-k)-2)
                assert exact == explicit, (n,k,lengths,len(exact),len(explicit),len(exact ^ explicit))
                assert len(exact) == expected, (n,k,lengths,len(exact),expected)
                checked += 1
    print(f"PASS: {checked} exact finite cases; every enumerated vertex matches the classification.")
    print("Sizes n=3,...,6; 0<=k<=floor(n/2); three rational length settings.")

if __name__ == '__main__':
    run()
