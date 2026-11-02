"""Independent exhaustive checks of finite deterministic ternary frames."""
from itertools import product


def satisfies_axioms(n, rows):
    for u in range(n):
        if rows[u] is None:
            continue
        v, w = rows[u]
        # The source-persistence clause.
        for future in range(u, n):
            pair = rows[future]
            if pair is None or pair[0] < v or pair[1] < w:
                return False
        # Exact target-extension clause (not a closure approximation).
        for v_next in range(v, n):
            for w_next in range(w, n):
                if not any(rows[future] == (v_next, w_next)
                           for future in range(u, n)):
                    return False
    return True


def normal_form(n, rows):
    active = [u for u, pair in enumerate(rows) if pair is not None]
    if not active:
        return True
    first = active[0]
    if active != list(range(first, n)):
        return False
    tail = rows[first:]
    left = all(pair[1] == n - 1 for pair in tail)
    right = all(pair[0] == n - 1 for pair in tail)
    if not (left or right):
        return False
    changing = ([pair[0] for pair in tail] if left else
                [pair[1] for pair in tail])
    return (changing[-1] == n - 1 and
            all(b - a in (0, 1) for a, b
                in zip(changing, changing[1:])))


def target_symmetric(rows):
    # A single output per row must be diagonal to be symmetric.
    return all(pair is None or pair[0] == pair[1] for pair in rows)


def main():
    tested = 0
    for n in range(1, 5):
        options = [None] + list(product(range(n), repeat=2))
        total = symmetric = serial = 0
        for rows in product(options, repeat=n):
            tested += 1
            has_axioms = satisfies_axioms(n, rows)
            has_form = normal_form(n, rows)
            assert has_axioms == has_form, (n, rows)
            if has_axioms:
                total += 1
                symmetric += target_symmetric(rows)
                serial += all(pair is not None for pair in rows)
        assert total == 2 ** (n + 1) - n - 1, (n, total)
        assert serial == 2 ** n - 1, (n, serial)
        assert symmetric == n + 1, (n, symmetric)
        print(f"order={n}, frames={total}, total={serial}, symmetric={symmetric}")
    print(f"candidates={tested}")
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    main()
