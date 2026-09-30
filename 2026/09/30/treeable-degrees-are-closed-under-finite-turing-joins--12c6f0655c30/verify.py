from itertools import product

DEPTH = 3
LEAVES = [tuple((n >> i) & 1 for i in range(DEPTH)) for n in range(2 ** DEPTH)]


def prefix_closure(leaves):
    tree = {()}
    for leaf in leaves:
        for k in range(1, len(leaf) + 1):
            tree.add(leaf[:k])
    return tree


def paths(tree, depth):
    return sorted(node for node in tree if len(node) == depth)


def pair_code(x, y):
    out = []
    for a, b in zip(x, y):
        out.extend((a, b))
    return tuple(out)


def product_tree(T, S, depth):
    leaves = [pair_code(x, y) for x in paths(T, depth) for y in paths(S, depth)]
    return prefix_closure(leaves)

families = []
for mask in range(1, 1 << len(LEAVES)):
    selected = [LEAVES[i] for i in range(len(LEAVES)) if (mask >> i) & 1]
    families.append(prefix_closure(selected))

checked = 0
for T in families:
    PT = paths(T, DEPTH)
    for S in families:
        PS = paths(S, DEPTH)
        U = product_tree(T, S, DEPTH)
        PU = paths(U, 2 * DEPTH)
        expected = sorted(pair_code(x, y) for x in PT for y in PS)
        assert PU == expected
        assert (len(PU) == 1) == (len(PT) == 1 and len(PS) == 1)
        checked += 1

assert checked == 255 * 255
print("VERIFY_OK", checked)
