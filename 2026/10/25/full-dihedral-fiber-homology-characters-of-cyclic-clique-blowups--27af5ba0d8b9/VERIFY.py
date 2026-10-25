"""Self-contained exact checks for clique-fiber cycle independence homology.

The script reconstructs every simplex, computes boundary ranks over F_2,
and compares with the closed integral sphere-multiplicity formula.
It also checks virtual characters under fiberwise permutations.
"""
from itertools import combinations, product
from collections import Counter
from math import comb


def independent_masks(m):
    return [mask for mask in range(1 << m)
            if not any((mask >> i & 1) and (mask >> ((i + 1) % m) & 1)
                       for i in range(m))]


def base_link_betti(m, S):
    # The empty face gives the ordinary independence complex of a cycle.
    if not S:
        t, r = divmod(m, 3)
        if r == 0:
            return {t - 1: 2}
        return {(t - 1 if r == 1 else t): 1}
    S = sorted(S)
    gaps = [(S[(i + 1) % len(S)] - S[i]) % m for i in range(len(S))]
    if len(S) == 1:
        gaps = [m]
    assert all(d >= 2 for d in gaps)
    runs = [max(d - 3, 0) for d in gaps]
    if any(a % 3 == 1 for a in runs):
        return {}
    dimension = sum((a + 1) // 3 for a in runs) - 1
    return {dimension: 1}


def formula(m, q):
    result = Counter()
    for mask in independent_masks(m):
        S = [i for i in range(m) if mask >> i & 1]
        for d, b in base_link_betti(m, S).items():
            result[d + len(S)] += b * (q - 1) ** len(S)
    return {p: b for p, b in sorted(result.items()) if b}


def all_faces(m, q):
    d = {}
    for mask in independent_masks(m):
        S = [i for i in range(m) if mask >> i & 1]
        for cc in product(range(q), repeat=len(S)):
            face = tuple(i * q + c for i, c in zip(S, cc))
            d.setdefault(len(S) - 1, []).append(face)
    return d


def rank_F2(columns):
    pivots = {}
    for x in columns:
        while x:
            p = x.bit_length() - 1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                break
    return len(pivots)


def homology_F2(m, q):
    levels = all_faces(m, q)
    ranks = {}
    for p in sorted(levels):
        if p == -1:
            continue
        lower = {f: i for i, f in enumerate(levels[p - 1])}
        columns = []
        for face in levels[p]:
            column = 0
            for i in range(len(face)):
                f2 = face[:i] + face[i + 1:]
                column ^= 1 << lower[f2]
            columns.append(column)
        ranks[p] = rank_F2(columns)
    betti = {}
    for p in sorted(levels):
        if p < 0:
            continue
        b = len(levels[p]) - ranks[p] - ranks.get(p + 1, 0)
        if b:
            betti[p] = b
    return betti


def char_formula(m, fixed_counts):
    output = Counter()
    for mask in independent_masks(m):
        S = [i for i in range(m) if mask >> i & 1]
        chi_U = 1
        for i in S:
            chi_U *= fixed_counts[i] - 1
        for d, b in base_link_betti(m, S).items():
            output[d + len(S)] += b * chi_U
    return dict(output)


def char_euler_chain(m, fixed_counts):
    value = 0
    for mask in independent_masks(m):
        S = [i for i in range(m) if mask >> i & 1]
        t = 1
        for i in S:
            t *= fixed_counts[i]
        value += (-1) ** (len(S) - 1) * t
    return value


def main():
    checked = 0
    for m, q in [(m, 2) for m in range(3, 11)] + [(m, 3) for m in range(3, 9)]:
        actual = homology_F2(m, q)
        predicted = formula(m, q)
        assert actual == predicted, (m, q, actual, predicted)
        checked += 1
    print('EXACT_MOD2_HOMOLOGY_MATCHES_WEDGE_FORMULA', checked)
    cases = 0
    for m in range(3, 15):
        for q in [2, 3, 4]:
            # All of the listed fixed-point counts occur for permutations of q elements.
            counts = list(range(q + 1))
            counts.remove(q - 1)
            for j in range(37):
                f = [counts[(i * i + 3 * i + 5 * j + i * j) % len(counts)]
                     for i in range(m)]
                predicted = sum((-1) ** d * tr for d, tr in char_formula(m, f).items())
                actual = char_euler_chain(m, f)
                assert predicted == actual, (m, q, j, predicted, actual)
                cases += 1
    print('FIBER_PERMUTATION_LEFSCHETZ_IDENTITIES_VERIFIED', cases)
    for m in range(3, 11):
        print('SAMPLE_BETTI',m,2,formula(m,2))
    print('CYCLE_CLIQUE_BLOWUP_VERIFICATION_OK')

if __name__ == '__main__':
    main()


def permutation_sign(values):
    return -1 if sum(values[i] > values[j] for i in range(len(values))
                     for j in range(i + 1, len(values))) % 2 else 1


def trace_C(m, q, tau, fiber, p):
    total = 0
    for face in all_faces(m, q).get(p, []):
        image = [q * tau[v // q] + fiber[v // q][v % q] for v in face]
        if sorted(image) == list(face):
            total += permutation_sign(image)
    return total


def cycles_on_subset(S, tau):
    unseen = set(S)
    result = []
    while unseen:
        i = min(unseen)
        cyc = []
        j = i
        while j in unseen:
            unseen.remove(j)
            cyc.append(j)
            j = tau[j]
        assert j == i
        result.append(cyc)
    return result


def trace_link_C(m, S, tau, p):
    if p == -1:
        return 1
    if p < -1:
        return 0
    forb = set(S)
    for i in S:
        forb.update([(i - 1) % m, (i + 1) % m])
    total = 0
    for mask in independent_masks(m):
        J = [i for i in range(m) if mask >> i & 1]
        if len(J) != p + 1 or forb.intersection(J):
            continue
        image = [tau[i] for i in J]
        if sorted(image) == J:
            total += permutation_sign(image)
    return total


def predicted_trace_C(m, q, tau, fiber, p):
    total = 0
    for mask in independent_masks(m):
        S = [i for i in range(m) if mask >> i & 1]
        if sorted(tau[i] for i in S) != S:
            continue
        orientation = permutation_sign([tau[i] for i in S])
        tr_U = 1
        for cyc in cycles_on_subset(S, tau):
            composite = list(range(q))
            for i in cyc:
                composite = [fiber[i][x] for x in composite]
            tr_U *= sum(composite[x] == x for x in range(q)) - 1
        total += orientation * tr_U * trace_link_C(m, S, tau, p - len(S))
    return total


def check_wreath_chain_characters():
    tests = 0
    for m in range(3, 11):
        for q in (2, 3):
            perms = [tuple(range(q)), tuple(reversed(range(q)))]
            if q == 3:
                perms.append((1, 2, 0))
            for variant in range(12):
                shift = (variant * 3 + 1) % m
                tau = [((i + shift) % m if variant % 2 == 0 else
                        (shift - i) % m) for i in range(m)]
                fiber = [perms[(i * i + i * variant + variant) % len(perms)]
                         for i in range(m)]
                for p in range(-1, (m + 1) // 2):
                    actual = trace_C(m, q, tau, fiber, p)
                    predicted = predicted_trace_C(m, q, tau, fiber, p)
                    assert actual == predicted, (m, q, variant, p, actual, predicted)
                    tests += 1
    print('FULL_WREATH_EQUIVARIANT_CHAIN_SPLITTING_VERIFIED', tests)

if __name__ == '__main__':
    check_wreath_chain_characters()
