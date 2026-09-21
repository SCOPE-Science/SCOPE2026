from fractions import Fraction
from itertools import combinations


def rank_fraction(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        a[r] = [x / p for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [a[i][j] - q * a[r][j] for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r


def is_connected(n, edges):
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


def is_bipartite(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    color = [None] * n
    for s in range(n):
        if color[s] is not None:
            continue
        color[s] = 0
        stack = [s]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if color[v] is None:
                    color[v] = 1 - color[u]
                    stack.append(v)
                elif color[v] == color[u]:
                    return False
    return True


def unsigned_incidence(n, edges):
    out = []
    for u, v in edges:
        row = [0] * n
        row[u] = 1
        row[v] = 1
        out.append(row)
    return out


def exhaustive_rank_checks(max_n=6):
    total = 0
    nonbip = 0
    minimal_edge_checks = 0
    for n in range(2, max_n + 1):
        possible = list(combinations(range(n), 2))
        min_nonbip_edges = None
        for mask in range(1, 1 << len(possible)):
            edges = [possible[i] for i in range(len(possible)) if (mask >> i) & 1]
            if not is_connected(n, edges):
                continue
            total += 1
            bip = is_bipartite(n, edges)
            r = rank_fraction(unsigned_incidence(n, edges))
            expected = n - 1 if bip else n
            assert r == expected, (n, edges, r, expected)
            if not bip:
                nonbip += 1
                if min_nonbip_edges is None or len(edges) < min_nonbip_edges:
                    min_nonbip_edges = len(edges)
        if n >= 3:
            assert min_nonbip_edges == n, (n, min_nonbip_edges)
            minimal_edge_checks += 1
    return total, nonbip, minimal_edge_checks


def triangle_product_check():
    # Laplace(0,b_i) characteristic functions at t=2 are positive rationals:
    # phi_i(t) = 1/(1+b_i^2 t^2).
    t = Fraction(2)
    scales = [Fraction(1), Fraction(2), Fraction(3)]
    phi = [1 / (1 + b * b * t * t) for b in scales]
    psi12 = phi[0] * phi[1]
    psi13 = phi[0] * phi[2]
    psi23 = phi[1] * phi[2]
    # The triangle formula gives phi_1^2 = psi_12 psi_13 / psi_23.
    assert psi12 * psi13 / psi23 == phi[0] * phi[0]
    assert psi12 * psi23 / psi13 == phi[1] * phi[1]
    assert psi13 * psi23 / psi12 == phi[2] * phi[2]
    return phi, (psi12, psi13, psi23)


def gaussian_bipartite_alias_check():
    # Path 0-1-2 is bipartite with parts {0,2} and {1}.
    variances = [Fraction(7), Fraction(11), Fraction(13)]
    c = Fraction(2)
    shifted = [variances[0] + c, variances[1] - c, variances[2] + c]
    assert variances[0] + variances[1] == shifted[0] + shifted[1]
    assert variances[1] + variances[2] == shifted[1] + shifted[2]

    # If only Y_0 = X + error_0 is also observed, compensate in latent variance.
    tau2 = Fraction(17)
    tau2_shifted = tau2 - c
    assert tau2 + variances[0] == tau2_shifted + shifted[0]
    assert min(shifted + [tau2_shifted]) > 0
    return variances, shifted, tau2, tau2_shifted


if __name__ == "__main__":
    total, nonbip, minchecks = exhaustive_rank_checks()
    phi, psi = triangle_product_check()
    v, vp, tau, taup = gaussian_bipartite_alias_check()
    print(f"connected_graph_rank_checks={total}")
    print(f"nonbipartite_connected_graphs_checked={nonbip}")
    print(f"minimal_edge_counts_checked={minchecks}")
    print(f"triangle_phi={phi}")
    print(f"triangle_edge_products={psi}")
    print(f"gaussian_variances={v}")
    print(f"gaussian_shifted_variances={vp}")
    print(f"latent_variance_pair=({tau}, {taup})")
    print("status=PASS")
