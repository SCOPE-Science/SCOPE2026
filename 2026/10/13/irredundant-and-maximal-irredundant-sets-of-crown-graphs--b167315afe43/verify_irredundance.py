#!/usr/bin/env python3
from math import comb


def closed_neighborhoods(n):
    N = []
    for v in range(2 * n):
        s = {v}
        if v < n:
            i = v
            s.update(n + j for j in range(n) if j != i)
        else:
            j = v - n
            s.update(i for i in range(n) if i != j)
        N.append(s)
    return N


def direct_irredundant(n, mask, N):
    S = {v for v in range(2 * n) if (mask >> v) & 1}
    for v in S:
        if not any((N[z] & S) == {v} for z in N[v]):
            return False
    return True


def classified_irredundant(n, mask):
    I = {i for i in range(n) if (mask >> i) & 1}
    J = {i for i in range(n) if (mask >> (n + i)) & 1}
    if not I or not J:
        return True
    if I & J:
        return len(I) == len(J) == 1 and I == J
    p, q = len(I), len(J)
    if (p, q) == (1, 1):
        return True
    if (p, q) in {(1, 2), (2, 1)}:
        return n >= 4
    if (p, q) == (2, 2):
        return True
    return False


def predicted_all(n):
    d = {}
    def add(k, c):
        d[k] = d.get(k, 0) + c
    for k in range(n + 1):
        add(k, 2 * comb(n, k))
    d[0] -= 1
    add(2, n * n)
    if n >= 4:
        add(3, n * (n - 1) * (n - 2))
        add(4, 6 * comb(n, 4))
    return {k: v for k, v in d.items() if v}


def predicted_maximal(n):
    d = {}
    def add(k, c):
        d[k] = d.get(k, 0) + c
    if n == 3:
        add(2, 9)
        add(3, 2)
    else:
        add(2, n)
        add(4, 6 * comb(n, 4))
        add(n, 2)
    return {k: v for k, v in d.items() if v}


def main():
    subset_checks = 0
    private_neighbor_checks = 0
    maximality_checks = 0
    coefficient_checks = 0
    classification_checks = 0
    for n in range(3, 9):
        N = closed_neighborhoods(n)
        direct = {}
        maximal = {}
        for mask in range(1 << (2 * n)):
            subset_checks += 1
            ok = direct_irredundant(n, mask, N)
            private_neighbor_checks += mask.bit_count()
            pred = classified_irredundant(n, mask)
            classification_checks += 1
            assert ok == pred, (n, mask, ok, pred)
            if not ok:
                continue
            k = mask.bit_count()
            direct[k] = direct.get(k, 0) + 1
            ismax = True
            for v in range(2 * n):
                if not ((mask >> v) & 1):
                    maximality_checks += 1
                    if direct_irredundant(n, mask | (1 << v), N):
                        ismax = False
                        break
            if ismax:
                maximal[k] = maximal.get(k, 0) + 1
        pa = predicted_all(n)
        pm = predicted_maximal(n)
        coefficient_checks += len(set(pa) | set(direct)) + len(set(pm) | set(maximal))
        assert direct == pa, (n, direct, pa)
        assert maximal == pm, (n, maximal, pm)
        assert min(maximal) == 2
        assert max(maximal) == n
    print(
        'VERIFY_OK '
        f'n_range=3..8 subset_checks={subset_checks} '
        f'private_neighbor_checks={private_neighbor_checks} '
        f'classification_checks={classification_checks} '
        f'maximality_checks={maximality_checks} '
        f'coefficient_checks={coefficient_checks} max_order=16'
    )


if __name__ == '__main__':
    main()
