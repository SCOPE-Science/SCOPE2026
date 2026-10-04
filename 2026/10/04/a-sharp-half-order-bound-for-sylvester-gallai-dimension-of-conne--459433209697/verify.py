import networkx as nx
from math import floor


def diameter_path(tree):
    start = next(iter(tree.nodes))
    dist = nx.single_source_shortest_path_length(tree, start)
    a = max(dist, key=dist.get)
    paths = nx.single_source_shortest_path(tree, a)
    b = max(paths, key=lambda x: len(paths[x]))
    return paths[b]


def reduction_step(tree):
    path = diameter_path(tree)
    v0, v1 = path[0], path[1]
    assert tree.degree(v0) == 1
    if tree.degree(v1) == 2:
        removed = [v0, v1]
        anchor = path[2]
        kind = "pendant_path"
    else:
        leaves = [w for w in tree.neighbors(v1) if tree.degree(w) == 1]
        assert len(leaves) >= 2
        removed = leaves[:2]
        anchor = v1
        kind = "sibling_leaves"
    smaller = tree.copy()
    smaller.remove_nodes_from(removed)
    assert smaller.number_of_nodes() == tree.number_of_nodes() - 2
    assert nx.is_tree(smaller)
    assert anchor in smaller
    return smaller, kind


def verify_tree(tree):
    original_n = tree.number_of_nodes()
    steps = 0
    kinds = []
    while tree.number_of_nodes() >= 5:
        tree, kind = reduction_step(tree)
        kinds.append(kind)
        steps += 1
    assert tree.number_of_nodes() in (3, 4)
    reconstructed_dimension = 1 + steps
    assert reconstructed_dimension == floor((original_n - 1) / 2)
    return kinds


def main():
    counts = []
    cases = 0
    reductions = {"pendant_path": 0, "sibling_leaves": 0}
    for n in range(3, 13):
        trees = list(nx.generators.nonisomorphic_trees(n))
        counts.append((n, len(trees)))
        for tree in trees:
            kinds = verify_tree(tree)
            cases += 1
            for kind in kinds:
                reductions[kind] += 1
    print("ALL CHECKS PASSED")
    print(f"tree_types_checked={cases}")
    print(f"counts={counts}")
    print(f"reduction_steps={reductions}")


if __name__ == "__main__":
    main()
