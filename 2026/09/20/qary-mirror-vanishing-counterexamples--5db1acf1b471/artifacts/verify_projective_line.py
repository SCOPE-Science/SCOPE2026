from itertools import combinations
from math import ceil


def compositions(total, parts):
    for cuts in combinations(range(total + parts - 1), parts - 1):
        prev = -1
        out = []
        for c in cuts + (total + parts - 1,):
            out.append(c - prev - 1)
            prev = c
        yield tuple(out)


def projective_points_prime(q):
    return [(1, a) for a in range(q)] + [(0, 1)]


def construct(q, d, t):
    cap = d - t
    assert d <= (q - 1) * cap
    pts = projective_points_prime(q)
    mult = [0] * (q + 1)
    mult[0] = d + 1
    remaining = d
    for i in range(1, q):
        x = min(cap, remaining)
        mult[i] = x
        remaining -= x
    assert remaining == 0
    columns = []
    for p, m in zip(pts, mult):
        columns.extend([p] * m)
    G = (
        [c[0] for c in columns],
        [c[1] for c in columns],
    )
    return G, mult


def weight_distribution(G, q):
    n = len(G[0])
    A = [0] * (n + 1)
    for a in range(q):
        for b in range(q):
            w = 0
            for j in range(n):
                if (a * G[0][j] + b * G[1][j]) % q:
                    w += 1
            A[w] += 1
    return A


def direct_construction_checks():
    cases = 0
    for q in [3, 5, 7, 11, 13]:
        for d in range(2, 13):
            for t in range(1, d):
                feasible = d <= (q - 1) * (d - t)
                if not feasible:
                    continue
                G, mult = construct(q, d, t)
                A = weight_distribution(G, q)
                assert len(G[0]) == 2 * d + 1
                assert min(i for i in range(1, len(A)) if A[i]) == d
                assert all(A[d + j] == 0 for j in range(1, t + 1))
                assert A[2 * d + 1] > 0
                assert max(mult) == d + 1
                assert min(mult) == 0
                cases += 1
    return cases


def sharpness_checks():
    checked = 0
    for q in [3, 5]:
        for d in range(2, 8):
            n = 2 * d + 1
            all_mult = list(compositions(n, q + 1))
            for t in range(1, d):
                predicted = d <= (q - 1) * (d - t)
                found = False
                forbidden = set(range(d + 1 - t, d + 1))
                for m in all_mult:
                    if max(m) != d + 1:
                        continue
                    if 0 not in m:
                        continue
                    if any(x in forbidden for x in m):
                        continue
                    found = True
                    break
                assert found == predicted, (q, d, t, found, predicted)
                checked += 1
    return checked


if __name__ == '__main__':
    c1 = direct_construction_checks()
    c2 = sharpness_checks()
    print('PASS')
    print(f'constructed_parameter_cases={c1}')
    print(f'exhaustive_sharpness_cases={c2}')
    print('prime_fields_checked=3,5,7,11,13')
    print('general_prime-power theorem is proved geometrically over PG(1,q)')
