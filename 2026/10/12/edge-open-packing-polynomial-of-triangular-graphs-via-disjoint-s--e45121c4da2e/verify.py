"""Independent finite checks for the edge-open-packing polynomial of L(K_n).

The first oracle constructs the graph and checks the *third-edge* definition,
without using the path-block description. It enumerates every packing for
2 <= n <= 8 and separately checks each packing's path-block profile.
These finite checks support, but do not replace, the mathematical proof.
"""
from itertools import combinations
from math import comb, factorial


def expected_profiles(n):
    profiles = {}
    for a in range(n // 3 + 1):
        for b in range(n // 4 + 1):
            h = n - 3 * a - 4 * b
            if h >= 0:
                profiles[(a, b)] = (
                    factorial(n) //
                    (factorial(h) * factorial(a) * factorial(b) * 2**(a+b))
                )
    return profiles


def expected_coefficients(n):
    coefficients = {}
    for (a, b), count in expected_profiles(n).items():
        coefficients[a+2*b] = coefficients.get(a+2*b, 0) + count
    return coefficients


def classify_original_paths(n, chosen, line_vertices, line_edges):
    used_line_vertices = set()
    for t in chosen:
        used_line_vertices.update(line_edges[t])
    selected_original_edges = [line_vertices[v] for v in used_line_vertices]
    neighbors = [set() for _ in range(n)]
    for u, v in selected_original_edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    marked = set()
    a = b = 0
    for vertex in range(n):
        if vertex in marked or not neighbors[vertex]:
            continue
        stack, component = [vertex], set()
        while stack:
            v = stack.pop()
            if v in component:
                continue
            component.add(v)
            stack.extend(neighbors[v] - component)
        marked |= component
        degrees = sorted(len(neighbors[v]) for v in component)
        edge_count = sum(degrees) // 2
        if len(component) == 3 and edge_count == 2 and degrees == [1, 1, 2]:
            a += 1
        elif len(component) == 4 and edge_count == 3 and degrees == [1, 1, 2, 2]:
            b += 1
        else:
            raise AssertionError((n, chosen, degrees))
    assert a + 2*b == len(chosen)
    return a, b


def exhaustive_oracle(n):
    line_vertices = list(combinations(range(n), 2))
    line_edges = [
        (i, j) for i, j in combinations(range(len(line_vertices)), 2)
        if not set(line_vertices[i]).isdisjoint(line_vertices[j])
    ]
    line_edge_sets = [set(edge) for edge in line_edges]
    m = len(line_edges)
    conflict = [0] * m
    # Literal definition: a third edge of L(K_n) joins one endpoint
    # of each of the two tested edges. Identical endpoints do not form
    # a joining edge; both endpoints of the third edge are considered.
    for i, ei in enumerate(line_edges):
        for j in range(i+1, m):
            ej = line_edges[j]
            violates = any(
                t != ei and t != ej and (
                    (t[0] in line_edge_sets[i] and t[1] in line_edge_sets[j]) or
                    (t[1] in line_edge_sets[i] and t[0] in line_edge_sets[j])
                )
                for t in line_edges
            )
            if violates:
                conflict[i] |= 1 << j
                conflict[j] |= 1 << i
    profiles = {}
    visited_nodes = 0
    def search(mask, chosen):
        nonlocal visited_nodes
        visited_nodes += 1
        if mask == 0:
            profile = classify_original_paths(n, chosen, line_vertices, line_edges)
            profiles[profile] = profiles.get(profile, 0) + 1
            return
        bit = mask & -mask
        i = bit.bit_length()-1
        search(mask ^ bit, chosen)
        search((mask ^ bit) & ~conflict[i], chosen+(i,))
    search((1 << m)-1, ())
    assert profiles == expected_profiles(n), (n, profiles, expected_profiles(n))
    return m, visited_nodes, profiles


def multiply_shift_add(dst, src, shift, factor):
    for k, v in enumerate(src):
        if k+shift >= len(dst):
            dst.extend([0] * (k+shift+1-len(dst)))
        dst[k+shift] += factor*v


def recurrence_checks(N=60):
    ps = [[1]]
    for n in range(N):
        nxt = []
        multiply_shift_add(nxt, ps[n], 0, 1)
        if n >= 2:
            multiply_shift_add(nxt, ps[n-2], 1, 3*comb(n,2))
        if n >= 3:
            multiply_shift_add(nxt, ps[n-3], 2, 12*comb(n,3))
        ps.append(nxt)
    for n in range(N+1):
        expected = expected_coefficients(n)
        assert [expected.get(k, 0) for k in range(len(ps[n]))] == ps[n], n
        q,r=divmod(n,4)
        degree=n//2 - (r==2)
        assert len(ps[n])-1 == degree
        if r in (0,1):
            count=factorial(n)//(2**q*factorial(q))
        elif r==2:
            count=factorial(n)//(2**(q+1)*factorial(q))
            if q:
                count+=factorial(n)//(2**(q+2)*factorial(q-1))
        else:
            count=factorial(n)//(2**(q+1)*factorial(q))
        assert ps[n][-1]==count, (n,count,ps[n][-1])
    return ps


def main():
    total=0
    for n in range(2,9):
        m, nodes, profiles=exhaustive_oracle(n)
        cases=sum(profiles.values())
        total += cases
        coeffs=expected_coefficients(n)
        print('n=%d line_edges=%d candidate_independent_sets=%d decision_nodes=%d polynomial=%s'
              %(n,m,cases,nodes,[coeffs.get(k,0) for k in range(max(coeffs)+1)]))
    ps=recurrence_checks(60)
    print('Full third-edge oracle checked %d distinct EOP sets across n=2..8.'%total)
    print('Recurrence, coefficient sum, degree and maximum multiplicity agree for n=0..60.')
    print('Representative n=10 degree=%d maximum_coefficient=%d'%(len(ps[10])-1,ps[10][-1]))
    print('VERIFY_OK')

if __name__=='__main__':
    main()
