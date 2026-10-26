"""Independent exhaustive checks of exact full-memory lazy-rule transition counts."""
from collections import Counter
from itertools import product


def add(x, y, moduli):
    return tuple((a + b) % m for a, b, m in zip(x, y, moduli))


def all_subgroups(group, moduli):
    zero = group[0]
    found = {frozenset([zero])}
    frontier = [frozenset([zero])]
    while frontier:
        H = frontier.pop()
        for g in group:
            if g in H:
                continue
            span = set(H)
            cur = zero
            while True:
                cur = add(cur, g, moduli)
                span.update(add(cur, h, moduli) for h in H)
                if cur == zero:
                    break
            J = frozenset(span)
            if J not in found:
                found.add(J)
                frontier.append(J)
    return sorted(found, key=lambda s: (len(s), tuple(sorted(s))))


def verify(moduli, q):
    group = list(product(*(range(m) for m in moduli)))
    n = len(group)
    idx = {g: i for i, g in enumerate(group)}
    shifts = [[idx[add(g, h, moduli)] for g in group] for h in group]
    subgroups = all_subgroups(group, moduli)
    mcount = Counter()
    transitions = Counter()
    for x in product(range(q), repeat=n):
        H = frozenset(group[j] for j, shift in enumerate(shifts)
                      if all(x[i] == x[shift[i]] for i in range(n)))
        assert H in subgroups
        mcount[H] += 1
        for a in range(q):
            if a == x[0]:
                continue
            y = list(x)
            for h in H:
                y[idx[h]] = a
            K = frozenset(group[j] for j, shift in enumerate(shifts)
                          if all(y[i] == y[shift[i]] for i in range(n)))
            assert H.issubset(K)
            transitions[H, K] += 1
    assertions = 0
    for H in subgroups:
        invariant = q ** (n // len(H))
        assert invariant == sum(mcount[K] for K in subgroups if H.issubset(K))
        expected_diagonal = (q - 1) * (2 * mcount[H] - invariant)
        assert transitions[H, H] == expected_diagonal, (moduli, q, H, 'diagonal')
        assertions += 2
        for K in subgroups:
            if H < K:
                assert transitions[H, K] == (q - 1) * mcount[K], (moduli, q, H, K)
                assertions += 1
    return n, len(subgroups), assertions


def main():
    cases = [(m, 2) for m in [(2,), (3,), (4,), (5,), (6,), (8,), (2, 2),
                                (2, 3), (2, 4), (2, 2, 2), (3, 3)]]
    cases += [(m, 3) for m in [(2,), (3,), (4,), (2, 2), (2, 3), (2, 2, 2)]]
    checks = 0
    for mods, q in cases:
        n, subcount, k = verify(mods, q)
        checks += k
        print(f'PASS G={mods} q={q} N={n} subgroups={subcount} identities={k}')
    print(f'ALL PASS: {len(cases)} group/alphabet systems; {checks} counting identities.')


if __name__ == '__main__':
    main()
