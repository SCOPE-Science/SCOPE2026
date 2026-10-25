from itertools import combinations, permutations
from fractions import Fraction

# Enumerate all labelled simple graphs on at most four vertices. For each graph,
# compute its maximum subgraph density. For a fixed vertex set, the densest
# subgraph is induced, so enumerating vertex subsets is sufficient.
def graph_edges(n, mask):
    pairs = list(combinations(range(n), 2))
    return {pairs[i] for i in range(len(pairs)) if (mask >> i) & 1}

def max_density(n, edges):
    best = Fraction(0, 1)
    for r in range(2, n + 1):
        for verts in combinations(range(n), r):
            S = set(verts)
            e = sum(1 for a, b in edges if a in S and b in S)
            if e:
                best = max(best, Fraction(e, r))
    return best

def automorphisms(n, edges):
    E = {tuple(sorted(e)) for e in edges}
    count = 0
    for p in permutations(range(n)):
        mapped = {tuple(sorted((p[a], p[b]))) for a, b in E}
        if mapped == E:
            count += 1
    return count

all_max_densities = set()
for n in range(1, 5):
    for mask in range(1 << (n * (n - 1) // 2)):
        all_max_densities.add(max_density(n, graph_edges(n, mask)))
positive_densities = {x for x in all_max_densities if x > 0}
expected_densities = {Fraction(1,2), Fraction(2,3), Fraction(3,4), Fraction(1,1), Fraction(5,4), Fraction(3,2)}
assert positive_densities == expected_densities, (positive_densities, expected_densities)

patterns = {
    "K4": (4, {(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)}, Fraction(3,2), 24, Fraction(2,3)),
    "diamond": (4, {(0,1),(0,2),(0,3),(1,2),(1,3)}, Fraction(5,4), 4, Fraction(4,5)),
    "K3": (3, {(0,1),(0,2),(1,2)}, Fraction(1,1), 6, Fraction(1,1)),
    "P4": (4, {(0,1),(1,2),(2,3)}, Fraction(3,4), 2, Fraction(4,3)),
    "P3": (3, {(0,1),(1,2)}, Fraction(2,3), 2, Fraction(3,2)),
    "K2": (2, {(0,1)}, Fraction(1,2), 2, Fraction(2,1)),
}
for name, (n, edges, dens, aut, alpha) in patterns.items():
    assert max_density(n, edges) == dens, (name, max_density(n, edges), dens)
    assert automorphisms(n, edges) == aut, (name, automorphisms(n, edges), aut)
    assert Fraction(1,1) / dens == alpha
    # Every proper vertex-subset subgraph has strictly smaller edge density.
    for r in range(1, n):
        for verts in combinations(range(n), r):
            S = set(verts)
            e = sum(1 for a, b in edges if a in S and b in S)
            assert Fraction(e, r) < dens, (name, verts, Fraction(e, r), dens)

ordered = ["K4", "diamond", "K3", "P4", "P3", "K2"]
expected_alpha = [Fraction(2,3), Fraction(4,5), Fraction(1,1), Fraction(4,3), Fraction(3,2), Fraction(2,1)]
assert [patterns[k][4] for k in ordered] == expected_alpha
print("VERIFIED density set:", ", ".join(str(x) for x in sorted(positive_densities)))
print("VERIFIED six critical exponents and automorphism counts:")
for name in ordered:
    n, edges, dens, aut, alpha = patterns[name]
    print(f"{name}: v={n}, e={len(edges)}, rho_max={dens}, alpha={alpha}, |Aut|={aut}, Poisson_mean={Fraction(1, aut)}")
print("VERIFICATION_OK")
