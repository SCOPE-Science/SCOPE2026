from itertools import product
from math import comb


def vertices(ns):
    return [(i, j) for i, n in enumerate(ns) for j in range(n)]


def adjacent(u, v):
    return u[0] != v[0]


def total_dominating(ns, chosen):
    chosen = set(chosen)
    return all(any(adjacent(u, v) for v in chosen) for u in vertices(ns))


def secure_total(ns, chosen):
    chosen = set(chosen)
    if not total_dominating(ns, chosen):
        return False
    for u in vertices(ns):
        if u in chosen:
            continue
        if not any(
            adjacent(u, v) and total_dominating(ns, (chosen - {v}) | {u})
            for v in chosen
        ):
            return False
    return True


def structural(ns, chosen):
    counts = [0] * len(ns)
    for v in chosen:
        counts[v[0]] += 1
    support = [i for i, value in enumerate(counts) if value]
    if len(support) < 2:
        return False
    if len(support) >= 3:
        return True
    i, j = support
    return ((counts[i] == ns[i] or counts[j] >= 2)
            and (counts[j] == ns[j] or counts[i] >= 2))


def polynomial_from_formula(ns):
    n = sum(ns)
    coeff = [comb(n, k) for k in range(n + 1)]
    coeff[0] -= 1
    # Subtract subsets supported in exactly one part.
    for size in ns:
        for k in range(1, size + 1):
            coeff[k] -= comb(size, k)
    # Subtract the insecure two-part supports.  For each part i, U_i
    # counts nonempty proper selections in i and N-n_i choices of a
    # singleton defender part vertex outside i.  Pairwise double counting
    # occurs exactly when both selected parts are non-singleton and both
    # selected counts equal one, so add those intersections back.
    for i, size in enumerate(ns):
        outside = n - size
        for k in range(1, size):
            coeff[k + 1] -= outside * comb(size, k)
    for i in range(len(ns)):
        if ns[i] < 2:
            continue
        for j in range(i + 1, len(ns)):
            if ns[j] >= 2:
                coeff[2] += ns[i] * ns[j]
    return coeff


def polynomial_by_profiles(ns):
    n = sum(ns)
    coeff = [0] * (n + 1)
    for counts in product(*[range(size + 1) for size in ns]):
        support = [i for i, value in enumerate(counts) if value]
        ok = False
        if len(support) >= 3:
            ok = True
        elif len(support) == 2:
            i, j = support
            ok = ((counts[i] == ns[i] or counts[j] >= 2)
                  and (counts[j] == ns[j] or counts[i] >= 2))
        if ok:
            ways = 1
            for size, count in zip(ns, counts):
                ways *= comb(size, count)
            coeff[sum(counts)] += ways
    return coeff


def main():
    graph_types = 0
    subset_checks = 0
    coefficient_checks = 0
    max_order = 0
    for r in range(2, 6):
        for ns in product(range(1, 5), repeat=r):
            if sum(ns) > 9:
                continue
            graph_types += 1
            max_order = max(max_order, sum(ns))
            verts = vertices(ns)
            brute = [0] * (sum(ns) + 1)
            for mask in range(1 << len(verts)):
                chosen = {verts[i] for i in range(len(verts)) if (mask >> i) & 1}
                direct = secure_total(ns, chosen)
                classified = structural(ns, chosen)
                subset_checks += 1
                if direct != classified:
                    raise AssertionError((ns, chosen, direct, classified))
                if direct:
                    brute[len(chosen)] += 1
            formula = polynomial_from_formula(ns)
            profile = polynomial_by_profiles(ns)
            if brute != formula or brute != profile:
                raise AssertionError((ns, brute, formula, profile))
            coefficient_checks += len(brute)
    print(
        f"VERIFY_OK graph_types={graph_types} subset_checks={subset_checks} "
        f"coefficient_checks={coefficient_checks} max_order={max_order}"
    )


if __name__ == "__main__":
    main()
