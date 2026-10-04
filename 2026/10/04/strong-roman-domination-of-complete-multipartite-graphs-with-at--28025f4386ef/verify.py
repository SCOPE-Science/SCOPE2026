from __future__ import annotations


def profiles_of_order(n: int):
    def rec(rem: int, lo: int, pref: list[int]):
        if rem == 0:
            if len(pref) >= 3:
                yield tuple(pref)
            return
        for x in range(lo, rem + 1):
            yield from rec(rem - x, x, pref + [x])
    yield from rec(n, 1, [])


def bounded_vectors(length: int, max_label: int, budget: int, pref=None):
    if pref is None:
        pref = []
    if length == 0:
        yield tuple(pref)
        return
    for x in range(min(max_label, budget) + 1):
        yield from bounded_vectors(length - 1, max_label, budget - x, pref + [x])


def is_strong_roman(profile: tuple[int, ...], labels: tuple[int, ...]) -> bool:
    part = []
    for i, size in enumerate(profile):
        part.extend([i] * size)
    zeros = [v for v, x in enumerate(labels) if x == 0]
    if not zeros:
        return True
    for v in zeros:
        defended = False
        for w, label in enumerate(labels):
            if part[w] == part[v] or label < 2:
                continue
            zero_neighbors = sum(1 for u in zeros if part[u] != part[w])
            required = 1 + (zero_neighbors + 1) // 2
            if label >= required:
                defended = True
                break
        if not defended:
            return False
    return True


def claimed_gamma(profile: tuple[int, ...]) -> int:
    n = sum(profile)
    m = min(profile)
    return (n + m + 1) // 2


def explicit_witness(profile: tuple[int, ...]) -> tuple[int, ...]:
    n = sum(profile)
    m = profile[0]
    delta = n - m
    defender = 1 + (delta + 1) // 2
    labels = [defender] + [1] * (m - 1)
    labels.extend([0] * (n - m))
    return tuple(labels)


def main():
    profiles = 0
    labelings = 0
    feasible_at_or_below = 0
    witness_checks = 0
    for n in range(3, 11):
        for profile in profiles_of_order(n):
            profiles += 1
            gamma = claimed_gamma(profile)
            delta = n - min(profile)
            max_label = 1 + (delta + 1) // 2
            best = None
            for labels in bounded_vectors(n, max_label, gamma):
                labelings += 1
                if is_strong_roman(profile, labels):
                    feasible_at_or_below += 1
                    weight = sum(labels)
                    if best is None or weight < best:
                        best = weight
            assert best == gamma, (profile, gamma, best)
            witness = explicit_witness(profile)
            assert sum(witness) == gamma, (profile, witness, gamma)
            assert max(witness) <= max_label, (profile, witness, max_label)
            assert is_strong_roman(profile, witness), (profile, witness)
            witness_checks += 1
    print(f"VERIFY_OK profiles={profiles} labelings={labelings} feasible_at_or_below={feasible_at_or_below} witness_checks={witness_checks} max_order=10")


if __name__ == '__main__':
    main()
