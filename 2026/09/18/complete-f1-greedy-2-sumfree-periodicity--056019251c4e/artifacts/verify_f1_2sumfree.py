"""Finite verification for the f=1 greedy strict 2-sumfree formulas."""

def predicted(g, nmax):
    s = set()
    if g % 2:
        if g == 3:
            s.update(range(1, nmax + 1, 2))
        else:
            s.add(1)
            s.update(range(g, nmax + 1, 2))
        return s

    if g == 2:
        s.update((1, 2))
        s.update(n for n in range(3, nmax + 1) if n % 3 == 1)
        return s

    if g == 4:
        s.update((1, 4, 6, 8))
        r = {1, 4, 6, 11}
        s.update(n for n in range(9, nmax + 1) if n % 12 in r)
        return s

    if g == 6:
        s.update((1, 6, 8, 10, 12))
        r = {1, 6, 8}
        s.update(n for n in range(13, nmax + 1) if n % 9 in r)
        return s

    m = 4 * g + 3
    r = {1, 3, 4 * g, 4 * g + 2}
    r.update(range(g, 2 * g, 2))
    r.update(range(2 * g + 5, 3 * g + 2, 2))
    s.add(1)
    s.update(range(g, 2 * g + 1, 2))
    s.add(2 * g + 3)
    s.update(n for n in range(2 * g + 4, nmax + 1) if n % m in r)
    return s


def greedy(g, nmax):
    chosen = [1, g]
    chosen_set = {1, g}
    forbidden = {1 + g}
    for n in range(g + 1, nmax + 1):
        if n not in forbidden:
            for a in chosen:
                forbidden.add(a + n)
            chosen.append(n)
            chosen_set.add(n)
    return chosen_set


def even_residue_data(g):
    m = 4 * g + 3
    r = {1, 3, 4 * g, 4 * g + 2}
    r.update(range(g, 2 * g, 2))
    r.update(range(2 * g + 5, 3 * g + 2, 2))
    e = {1, g, 2 * g, 2 * g + 3}
    return m, r, e


def main():
    for g in range(2, 121):
        if g % 2:
            m = 2
        else:
            m = {2: 3, 4: 12, 6: 9}.get(g, 4 * g + 3)
        nmax = max(500, 12 * m)
        assert greedy(g, nmax) == predicted(g, nmax)

    for g in range(8, 201, 2):
        m, r, e = even_residue_data(g)
        assert all((a + b) % m not in r for a in r for b in r)
        covered = set()
        for x in e:
            covered.update((x + y) % m for y in r)
        assert covered == set(range(m)) - r
        assert len(r) == g + 3

    print("direct_greedy_formula_checks: PASS (2 <= g <= 120)")
    print("comparison_depth: at least 12 eventual characteristic periods")
    print("even_residue_identities: PASS (8 <= g <= 200, g even)")
    print("checked identities: (R+R) intersect R = empty; union_{e in E}(e+R) = complement(R)")
    print("cardinality_check: |R| = g+3")


if __name__ == "__main__":
    main()
