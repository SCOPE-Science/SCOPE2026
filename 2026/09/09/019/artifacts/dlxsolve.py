"""Deterministic + randomized exact-cover solver over bitmask columns (stdlib only)."""


def solve_first(ncols, rows, rng, max_nodes=200000):
    """Randomized MRV exact cover. rows: list of int masks. Returns list of row idx or None."""
    full = (1 << ncols) - 1
    col_rows = [[] for _ in range(ncols)]
    for i, m in enumerate(rows):
        mm = m
        while mm:
            b = mm & (-mm)
            col_rows[b.bit_length() - 1].append(i)
            mm ^= b
    nodes = [0]

    def rec(uncovered, chosen):
        nodes[0] += 1
        if nodes[0] > max_nodes:
            return None
        if uncovered == 0:
            return list(chosen)
        # MRV column
        best_c, best_rs, best_n = -1, None, None
        u = uncovered
        while u:
            b = u & (-u)
            c = b.bit_length() - 1
            rs = [i for i in col_rows[c] if rows[i] & ~uncovered == 0]
            if not rs:
                return None
            if best_n is None or len(rs) < best_n:
                best_n, best_c, best_rs = len(rs), c, rs
                if best_n == 1:
                    break
            u ^= b
        order = list(best_rs)
        rng.shuffle(order)
        for i in order:
            chosen.append(i)
            r = rec(uncovered & ~rows[i], chosen)
            if r is not None:
                return r
            chosen.pop()
        return None

    return rec(full, [])


def solve_all(ncols, rows, callback, cap=None, progress_every=0):
    """Deterministic MRV enumeration. callback(chosen_list matured). Returns solution count."""
    full = (1 << ncols) - 1
    col_rows = [[] for _ in range(ncols)]
    for i, m in enumerate(rows):
        mm = m
        while mm:
            b = mm & (-mm)
            col_rows[b.bit_length() - 1].append(i)
            mm ^= b
    count = [0]
    chosen = []
    stop = [False]

    def rec(uncovered):
        if stop[0]:
            return
        if uncovered == 0:
            count[0] += 1
            callback(list(chosen))
            if cap is not None and count[0] >= cap:
                stop[0] = True
            return
        best_c, best_rs, best_n = -1, None, None
        u = uncovered
        while u:
            b = u & (-u)
            c = b.bit_length() - 1
            rs = [i for i in col_rows[c] if rows[i] & ~uncovered == 0]
            if not rs:
                return
            if best_n is None or len(rs) < best_n:
                best_n, best_c, best_rs = len(rs), c, rs
                if best_n == 1:
                    break
            u ^= b
        for i in best_rs:
            chosen.append(i)
            rec(uncovered & ~rows[i])
            chosen.pop()
            if stop[0]:
                return

    rec(full)
    return count[0]
