from itertools import product, combinations

TARGET = ("r", "c", "t", "f")
TARGET_R = {("r", "c"), ("c", "t"), ("c", "f")}

def build_frame(n, edges):
    nodes = ["rho"] + [f"q{j}" for j in range(len(edges))] + [f"x{i}" for i in range(n)]
    relation = set()
    for j, edge in enumerate(edges):
        relation.add(("rho", f"q{j}"))
        for v in edge:
            relation.add((f"q{j}", f"x{v}"))
    return nodes, relation

def is_surjective_pmorphism(nodes, relation, values):
    h = dict(zip(nodes, values))
    if set(values) != set(TARGET):
        return False
    for u, v in relation:
        if (h[u], h[v]) not in TARGET_R:
            return False
    successors = {u: [] for u in nodes}
    for u, v in relation:
        successors[u].append(v)
    for u in nodes:
        for a, b in TARGET_R:
            if h[u] == a and not any(h[v] == b for v in successors[u]):
                return False
    return True

def count_pmorphisms(n, edges):
    nodes, relation = build_frame(n, edges)
    return sum(is_surjective_pmorphism(nodes, relation, values)
               for values in product(TARGET, repeat=len(nodes)))

def count_colorings(n, edges):
    total = 0
    for bits in product((0, 1), repeat=n):
        if all(len({bits[v] for v in edge}) >= 2 for edge in edges):
            total += 1
    return total

checked = 0

for n in (3, 4):
    triples = [frozenset(c) for c in combinations(range(n), 3)]
    for mask in range(1, 1 << len(triples)):
        edges = [triples[i] for i in range(len(triples)) if (mask >> i) & 1]
        assert count_pmorphisms(n, edges) == count_colorings(n, edges)
        checked += 1

for n in (1, 2, 3):
    possible = []
    for mask in range(1, 1 << n):
        edge = frozenset(i for i in range(n) if (mask >> i) & 1)
        if len(edge) <= 3:
            possible.append(edge)
    for edge in possible:
        edges = [edge]
        assert count_pmorphisms(n, edges) == count_colorings(n, edges)
        checked += 1
    for i in range(len(possible)):
        for j in range(i + 1, len(possible)):
            edges = [possible[i], possible[j]]
            assert count_pmorphisms(n, edges) == count_colorings(n, edges)
            checked += 1

nae = [bits for bits in product((0, 1), repeat=3) if len(set(bits)) == 2]
assert len(nae) == 6
assert len(nae) not in {1, 2, 4, 8}

print("checked_instances", checked)
print("VERIFY_OK")
