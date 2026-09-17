from itertools import combinations


def choose_x(h: int):
    assert h >= 2
    xs = [None] * h  # use indices 1..h-1
    xs[1] = 2*h + 1
    for i in range(2, h):
        d = xs[i-1] + 1
        while True:
            J = {d+i, d+2*i, d+i+2*h}
            ok = True
            for k in range(1, i):
                old = {xs[k]+k, xs[k]+2*k, xs[k]+k+2*h}
                if J & old:
                    ok = False
                    break
            if ok:
                xs[i] = d
                break
            d += 1
    return xs


def build_auxiliary(h: int):
    xs = choose_x(h)
    xlast = xs[h-1]
    L = 2*xlast + 2*h + 1
    P = {}
    for i in range(1, h):
        y = 2*xlast + 1 - xs[i]
        P[i] = [xs[i], i, 2*h-i, y]
        assert sum(P[i]) == L
    P[h] = [L]
    return xs, P, L


def build_barrycade(h: int):
    xs, P, L = build_auxiliary(h)
    n = 14*h - 13

    rows = {i: [i] + P[i][:] for i in range(1, h+1)}

    # h-1 cyclic rounds. Residue 0 is interpreted as h.
    for j in range(1, h):
        rows[j].append(h)
        for i in range(1, h+1):
            r = (i-j) % h
            if r == 0:
                r = h
            rows[i].extend(P[r])

    # Delete row h, as in the construction.
    rows.pop(h)

    # Determine which lengths are already used in every surviving row.
    common = set(rows[1])
    for i in range(2, h):
        common &= set(rows[i])

    # At this point every surviving row contains exactly the same *set* of
    # lengths except that row i has its own duplicated i. Append every unused
    # common length other than the reserved 2h.
    used_union = set()
    for row in rows.values():
        used_union |= set(row)
    # We only append lengths absent from all rows; the construction guarantees
    # the same base set across rows.
    fillers = [ell for ell in range(1, n+1) if ell not in used_union and ell != 2*h]
    for ell in fillers:
        for i in range(1, h):
            rows[i].append(ell)

    # Align totals.
    for i in range(1, h):
        rows[i].append(2*h - i)

    # Replace one consecutive (i, 2h-i) pair inside the copy of P_i by 2h.
    for i in range(1, h):
        row = rows[i]
        target = [i, 2*h-i]
        pos = None
        for j in range(len(row)-1):
            if row[j:j+2] == target:
                # There is exactly one such consecutive pair, inside P_i.
                pos = j
                break
        assert pos is not None
        rows[i] = row[:pos] + [2*h] + row[pos+2:]

    return n, rows, xs, P, L


def verify(h: int):
    n, rows, xs, P, L = build_barrycade(h)
    target = list(range(1, n+1))
    prefix_sets = {}
    for i, row in rows.items():
        assert sorted(row) == target, (h, i, "not permutation")
        s = 0
        pref = set()
        for x in row[:-1]:
            s += x
            assert s not in pref
            pref.add(s)
        prefix_sets[i] = pref

    for i, j in combinations(prefix_sets, 2):
        inter = prefix_sets[i] & prefix_sets[j]
        assert not inter, (h, i, j, min(inter) if inter else None)

    # Check the sharper deterministic bound as well.
    assert xs[h-1] <= 6*h - 7
    assert L <= 14*h - 13
    return {
        "h": h,
        "n": n,
        "height": h-1,
        "x_last": xs[h-1],
        "max_aux_block": max(max(p) for p in P.values()),
        "L": L,
    }


if __name__ == "__main__":
    tests = list(range(2, 15)) + [15, 20, 25, 30, 40, 50, 75, 100]
    for h in tests:
        result = verify(h)
        print(result)
