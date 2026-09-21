from itertools import combinations, product


def construction(d):
    assert d >= 1
    names = ["C", "Cp"] + [f"A{i}" for i in range(1, d + 1)] + [f"D{j}" for j in range(1, d)]
    rows = []
    for z in names[2:]:
        rows.append({z})
    for i in range(1, d + 1):
        rows.append({"C", f"A{i}"})
    for j in range(1, d):
        rows.append({"Cp", f"D{j}"})
    return names, rows


def column_masks(names, rows):
    masks = []
    for name in names:
        mask = 0
        for r, support in enumerate(rows):
            if name in support:
                mask |= 1 << r
        masks.append(mask)
    return masks


def union_mask(masks, subset):
    out = 0
    for i in subset:
        out |= masks[i]
    return out


def exact_k_separable(masks, k):
    seen = {}
    for subset in combinations(range(len(masks)), k):
        u = union_mask(masks, subset)
        if u in seen:
            return False
        seen[u] = subset
    return True


def d_disjunct(masks, d):
    n = len(masks)
    for c in range(n):
        others = [i for i in range(n) if i != c]
        for subset in combinations(others, d):
            if masks[c] & ~union_mask(masks, subset) == 0:
                return False
    return True


def append_row(masks, bits):
    bit = 1 << max((m.bit_length() for m in masks), default=0)
    return [m | (bit if b else 0) for m, b in zip(masks, bits)]


def no_one_row_completion(masks, d):
    n = len(masks)
    for bits in product((0, 1), repeat=n):
        if d_disjunct(append_row(masks, bits), d):
            return False
    return True


def verify_symbolic_witnesses(d, names, masks):
    idx = {name: i for i, name in enumerate(names)}
    A = tuple(idx[f"A{i}"] for i in range(1, d + 1))
    D = tuple(idx[f"D{j}"] for j in range(1, d))
    C, Cp = idx["C"], idx["Cp"]
    assert masks[C] & ~union_mask(masks, A) == 0
    second_cover = (C,) + D
    assert len(second_cover) == d
    assert masks[Cp] & ~union_mask(masks, second_cover) == 0


for d in range(2, 7):
    names, rows = construction(d)
    masks = column_masks(names, rows)
    assert len(names) == 2 * d + 1
    assert len(rows) == 4 * d - 2
    assert exact_k_separable(masks, 2 * d - 1)
    assert not d_disjunct(masks, d)
    verify_symbolic_witnesses(d, names, masks)
    assert no_one_row_completion(masks, d)
    idx = {name: i for i, name in enumerate(names)}
    row_c = tuple(1 if i == idx["C"] else 0 for i in range(len(names)))
    row_cp = tuple(1 if i == idx["Cp"] else 0 for i in range(len(names)))
    with_two = append_row(append_row(masks, row_c), row_cp)
    assert d_disjunct(with_two, d)
    print(f"d={d}: n={len(names)}, rows={len(rows)}, exact_{2*d-1}_separable=yes, minimum_appended_rows_for_d_disjunct=2")

print("all checks passed")
