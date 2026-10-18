"""Exact finite contact-network percolation susceptibility verification.

Python 3.10+ standard library. Prints a JSON certificate using integer arithmetic.
"""
import itertools
import json
from collections import defaultdict
from math import comb


def all_edges(n):
    return tuple(itertools.combinations(range(n), 2))


def graph_is_connected(n, edge_set):
    if n == 1:
        return True
    visited = {0}
    while True:
        nxt = visited | {v for a, b in edge_set for v in (a, b) if a in visited or b in visited}
        if nxt == visited:
            return len(visited) == n
        visited = nxt


def canonical_key(n, edge_set):
    # Labeled-simple-graph isomorphism is exhausted by all n! permutations.
    E = {tuple(sorted(e)) for e in edge_set}
    pairs = all_edges(n)
    best = None
    for perm in itertools.permutations(range(n)):
        code = sum((1 << k) for k, (a, b) in enumerate(pairs)
                   if tuple(sorted((perm[a], perm[b]))) in E)
        if best is None or code < best:
            best = code
    return best


def degree_profile(n, edge_set):
    d = [0]*n
    for a, b in edge_set:
        d[a] += 1
        d[b] += 1
    return tuple(sorted(d))


def percolation_numerator(n, edge_set):
    """Power coefficients of n times expected size of a uniform seed's open cluster.

    For each edge subset F, its contribution before expansion is
    (sum_C |C|^2) p^|F| (1-p)^(|E|-|F|).
    """
    edges = tuple(edge_set)
    m = len(edges)
    by_active = [0] * (m+1)
    for bits in range(1 << m):
        parent = list(range(n))
        size = [1]*n
        def root(x):
            while parent[x] != x:
                x = parent[x]
            return x
        k = 0
        for e, (a, b) in enumerate(edges):
            if (bits >> e) & 1:
                k += 1
                a, b = root(a), root(b)
                if a != b:
                    parent[a] = b
                    size[b] += size[a]
        by_active[k] += sum(size[v]**2 for v in range(n) if parent[v] == v)
    coefficients = [0]*(m+1)
    for k, value in enumerate(by_active):
        for j in range(m-k+1):
            coefficients[k+j] += value*comb(m-k,j)*(-1 if j%2 else 1)
    return tuple(coefficients), tuple(by_active)


def multiply(*polynomials):
    a = [1]
    for polynomial in polynomials:
        nxt = [0]*(len(a)+len(polynomial)-1)
        for i, c in enumerate(a):
            for j, d in enumerate(polynomial):
                nxt[i+j] += c*d
        a = nxt
    return tuple(a)


def sub(a,b):
    return tuple((a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b))))


def tally_small():
    profiles_by_n = {}
    connected_labeled = {}
    representatives = {}
    for n in range(1,6):
        pairs = all_edges(n)
        seen = {}
        connected = 0
        for mask in range(1 << len(pairs)):
            edges = tuple(e for j,e in enumerate(pairs) if mask >> j & 1)
            if not graph_is_connected(n, edges):
                continue
            connected += 1
            key = canonical_key(n, edges)
            seen.setdefault(key,edges)
        connected_labeled[str(n)] = connected
        representatives[n] = tuple(seen.values())
        profiles = defaultdict(list)
        for edges in seen.values():
            profiles[degree_profile(n,edges)].append(edges)
        profiles_by_n[n] = profiles
    return profiles_by_n, connected_labeled, representatives


def path_pair_formula_numerator(n, roots, depths, cycle):
    """Independent two-terminal reliability formula for one-cycle graphs.

    Every branch is a path attached to its core root. This covers both
    explicit six-vertex examples and does not enumerate edge states.
    """
    assert len(roots)==len(depths)==n
    pos={v:j for j,v in enumerate(cycle)}
    c=len(cycle)
    # Polynomial coefficients of n times the uniform-seed expectation.
    ans=[n]
    def addterm(k,coefficient):
        while len(ans)<=k:ans.append(0)
        ans[k]+=coefficient
    for u,v in itertools.combinations(range(n),2):
        t=depths[u]+depths[v]
        if roots[u]==roots[v]:
            addterm(abs(depths[u]-depths[v]),2)
        else:
            d=abs(pos[roots[u]]-pos[roots[v]])
            addterm(t+d,2)
            addterm(t+c-d,2)
            addterm(t+c,-2)
    return tuple(ans)


def main():
    ps, labeled, reps = tally_small()
    assert [len(reps[n]) for n in range(1,6)] == [1,1,2,6,21]
    ambiguities = []
    for n in range(1,6):
        for degrees, group in ps[n].items():
            if len(group)<2:
                continue
            assert n == 5 and len(group) == 2
            a,_=percolation_numerator(n,group[0])
            b,_=percolation_numerator(n,group[1])
            delta=sub(a,b)
            # Unordered signs are irrelevant. The two complete differences
            # have the following factors, each of fixed sign on 0<p<1.
            patterns={
              (1,2,2,2,3):multiply((0,0,0,1),(-1,1),(5,1)),
              (2,2,2,3,3):multiply((0,0,0,1),(-1,1),(-1,1),(5,1)),
            }
            assert degrees in patterns
            pattern=patterns[degrees]
            # Compared polynomials are n*expectation; factor magnitude is 2.
            assert delta==tuple(2*x for x in pattern) or delta==tuple(-2*x for x in pattern)
            ambiguities.append({'degrees':list(degrees), 'unlabeled_graphs':2,
                 'absolute_difference_n_times_mean_factor':
                 '2 p^3 (1-p) (p+5)' if degrees==(1,2,2,2,3) else
                 '2 p^3 (1-p)^2 (p+5)'})
    assert len(ambiguities)==2
    A=((0,4),(0,5),(1,3),(1,4),(2,3),(2,4)) # C4 plus length-two tail
    B=((0,1),(0,4),(1,2),(1,5),(2,3),(3,4)) # C5 plus leaf
    assert graph_is_connected(6,A) and graph_is_connected(6,B)
    assert degree_profile(6,A)==degree_profile(6,B)==(1,2,2,2,2,3)
    pa,ba=percolation_numerator(6,A)
    pb,bb=percolation_numerator(6,B)
    assert pa==path_pair_formula_numerator(6,(4,1,2,3,4,4),(1,0,0,0,0,2),(1,3,2,4))
    assert pb==path_pair_formula_numerator(6,(0,1,2,3,4,1),(0,0,0,0,0,1),(0,1,2,3,4))
    diff=sub(pa,pb)
    expected=multiply((0,0,0,1),(-1,1),(-1,8,1))
    assert diff==tuple(2*x for x in expected)
    # Therefore (mean_A-mean_B)=(1/3) p^3 (p-1)(p^2+8p-1).
    # The bracket is strictly increasing on [0,1], from -1 to +8.
    # Its unique zero is sqrt(17)-4 in (0,1).
    assert sum(diff)==0
    assert diff[0]==diff[1]==diff[2]==0
    print(json.dumps({
       'method':'exhaustive labeled simple graphs n<=5 / canonical isomorphism / exact edge-state component sum',
       'connected_labeled_counts':labeled,
       'connected_unlabeled_counts':{str(n):len(reps[n]) for n in range(1,6)},
       'ambiguous_degree_profiles_on_n_le_5':ambiguities,
       'six_vertex_witness':{
          'A_edges':[list(x) for x in A], 'B_edges':[list(x) for x in B],
          'common_sorted_degrees':list(degree_profile(6,A)),
          'A_edge_state_component_sums_by_open_edge_count':list(ba),
          'B_edge_state_component_sums_by_open_edge_count':list(bb),
          'A_power_coefficients_of_n_times_mean':list(pa),
          'B_power_coefficients_of_n_times_mean':list(pb),
          'difference_power_coefficients_of_n_times_mean':list(diff),
          'difference_factor':'2 p^3 (p-1)(p^2+8p-1)',
          'independent_method':'unicyclic path-pair reliability formula',
          'unique_interior_crossing':'sqrt(17)-4'
       },'checks':'PASS'
    },sort_keys=True,separators=(',',':')))

if __name__=='__main__':
    main()
