"""Independent exact finite-field checks for central first-jet local algebras.

For each test graph, row-reduce the unsigned edge-incidence equations
u_i+u_j=0 over F_p. Substitute a nullspace basis into the quadratic
edge equations u_i*u_j, and verify the resulting ideal is exactly
(t_1^2,...,t_b^2), with b predicted from graph components.
This finite test corroborates, but does not prove, the all-graph theorem.
"""
from itertools import combinations


def graph_components(n, edges):
    adj = [set() for _ in range(n)]
    for i, j in edges:
        adj[i].add(j); adj[j].add(i)
    if any(not neighbors for neighbors in adj):
        return None
    seen = set(); parts = []
    for start in range(n):
        if start in seen: continue
        stack = [start]; colors = {start: 0}; vertices = []
        bipartite = True
        while stack:
            i = stack.pop()
            if i in seen: continue
            seen.add(i); vertices.append(i)
            for j in adj[i]:
                if j not in colors:
                    colors[j] = 1 - colors[i]; stack.append(j)
                elif colors[j] == colors[i]:
                    bipartite = False
        parts.append((vertices, bipartite))
    return parts


def nullspace_basis(n, edges, prime):
    matrix = []
    for i, j in edges:
        row = [0] * n; row[i] += 1; row[j] += 1
        matrix.append([v % prime for v in row])
    pivot_cols = []
    rowindex = 0
    for col in range(n):
        pivot = next((i for i in range(rowindex, len(matrix)) if matrix[i][col]), None)
        if pivot is None: continue
        matrix[rowindex], matrix[pivot] = matrix[pivot], matrix[rowindex]
        inv = pow(matrix[rowindex][col], -1, prime)
        matrix[rowindex] = [(v * inv) % prime for v in matrix[rowindex]]
        for k in range(len(matrix)):
            if k == rowindex: continue
            coeff = matrix[k][col]
            if coeff:
                matrix[k] = [(a - coeff*b) % prime for a,b in zip(matrix[k],matrix[rowindex])]
        pivot_cols.append(col); rowindex += 1
        if rowindex == len(matrix): break
    free = [j for j in range(n) if j not in pivot_cols]
    basis = []
    for c in free:
        x = [0] * n; x[c] = 1
        for row, pivot in enumerate(pivot_cols):
            x[pivot] = (-matrix[row][c]) % prime
        for i,j in edges:
            assert (x[i]+x[j]) % prime == 0
        basis.append(x)
    return basis


def verify_graph(n, edges, prime):
    parts = graph_components(n, edges)
    if parts is None: return False
    expected_b = len(parts) if prime == 2 else sum(1 for _, bip in parts if bip)
    kernel = nullspace_basis(n, edges, prime)
    assert len(kernel) == expected_b, (n, edges, prime, 'nullity', len(kernel), expected_b)
    square_present = set()
    for i,j in edges:
        # Coefficients of the edge quadratic after substituting a nullspace basis.
        for a in range(len(kernel)):
            for b in range(a+1,len(kernel)):
                cross = kernel[a][i]*kernel[b][j] + kernel[b][i]*kernel[a][j]
                assert cross % prime == 0, (n, edges, prime, 'cross term')
            diag = (kernel[a][i]*kernel[a][j]) % prime
            if diag:
                square_present.add(a)
        # Every edge product is a scalar multiple of an individual variable square.
        support = sum(bool(kernel[a][i]*kernel[a][j] % prime) for a in range(len(kernel)))
        assert support <= 1, (n, edges, prime, 'mixed square')
    assert square_present == set(range(len(kernel))), (n, edges, prime, square_present)
    # The independent square-zero parameters yield 2**len(kernel) monomials.
    return True


def run():
    cases = 0
    for n in range(2,6):
        all_edges = list(combinations(range(n), 2))
        for mask in range(1, 1 << len(all_edges)):
            edges = [e for bit,e in enumerate(all_edges) if mask >> bit & 1]
            if graph_components(n,edges) is None: continue
            for prime in (2,3,5):
                assert verify_graph(n, edges, prime)
                cases += 1
    # More varied six-vertex examples, including disjoint bipartite/nonbipartite components.
    extras = [
        [(0,1),(1,2),(2,0),(3,4),(4,5),(5,3)],
        [(0,1),(1,2),(2,0),(3,4),(4,5)],
        [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)],
        [(0,1),(0,2),(0,3),(0,4),(0,5)],
        [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),(0,3)],
    ]
    for edges in extras:
        for prime in (2,3,5):
            assert verify_graph(6,edges,prime)
            cases += 1
    print('EXACT_IDEAL_CHECK_OK', 'cases=',cases, 'primes=2,3,5',
          'graphs=all isolate-free graphs on 2-5 vertices plus five six-vertex examples')


if __name__ == '__main__':
    run()
