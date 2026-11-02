"""Exact-rational finite tests for three-project Pareto transfer theorem."""
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement


def simplexes(den):
    return [tuple(F(v, den) for v in (a, b, den-a-b))
            for a in range(den+1) for b in range(den+1-a)]


def boxes(profile, x):
    dim = len(x)
    radii = [max(abs(a-b) for a,b in zip(x,p)) for p in profile]
    low = [max(F(0), *(p[j]-r for p,r in zip(profile,radii))) for j in range(dim)]
    high = [min(F(1), *(p[j]+r for p,r in zip(profile,radii))) for j in range(dim)]
    return radii, low, high


def pair_certificate(profile, x):
    radius, low, high = boxes(profile, x)
    for j in range(3):
        for k in range(3):
            if j == k or not (x[j] > low[j] and x[k] < high[k]):
                continue
            for i, p in enumerate(profile):
                if radius[i] == 0:
                    continue
                active = [h for h in range(3) if abs(x[h]-p[h]) == radius[i]]
                if not all((h == j and x[h] > p[h]) or
                           (h == k and x[h] < p[h]) for h in active):
                    continue
                permitted = [x[j]-low[j], high[k]-x[k], radius[i]]
                for h in (j,k):
                    if h not in active:
                        permitted.append(radius[i]-abs(x[h]-p[h]))
                eps = min(permitted)/2
                y = list(x)
                y[j] -= eps
                y[k] += eps
                assert eps > 0 and all(v >= 0 for v in y)
                costs_x = [sum(abs(a-b) for a,b in zip(x,q)) for q in profile]
                costs_y = [sum(abs(a-b) for a,b in zip(y,q)) for q in profile]
                assert all(b <= a for a,b in zip(costs_x,costs_y))
                assert any(b < a for a,b in zip(costs_x,costs_y))
                return True
    return False


def independent_global_test(profile, x):
    """Minimum possible radius for each agent over the common weak-improvement box.

    Derivation: simplex intersects coordinate intervals iff all lowers sum
    <=1<=all uppers. Expanding each max/min into subset inequalities yields
    the exact minimum possible infinity radius, without transfer enumeration.
    """
    radii, lo, hi = boxes(profile, x)
    for i,p in enumerate(profile):
        if radii[i] == 0:
            continue
        needed = [F(0)]
        needed.extend(lo[j]-p[j] for j in range(3))
        needed.extend(p[j]-hi[j] for j in range(3))
        for size in range(1,4):
            for group in combinations(range(3), size):
                other = [j for j in range(3) if j not in group]
                needed.append((sum(p[j] for j in group)+sum(lo[j] for j in other)-1)/size)
                needed.append((1-sum(p[j] for j in group)-sum(hi[j] for j in other))/size)
        if max(needed) < radii[i]:
            return True
    return False


def run():
    total = positive = 0
    for d in (2,3,4,5):
        gg = simplexes(d)
        for profile in combinations_with_replacement(gg,3):
            for x in gg:
                a = pair_certificate(profile,x)
                b = independent_global_test(profile,x)
                assert a == b, (profile,x,a,b)
                total += 1
                positive += a
        print('three-project denominator', d, 'cumulative profiles/outcomes',total, 'dominated',positive,flush=True)
    p = [(F(3,10),F(3,10),F(3,10),F(1,10)),
         (F(3,10),F(3,10),F(1,5),F(1,5)),
         (F(3,10),F(1,5),F(3,10),F(1,5)),
         (F(1,5),F(3,10),F(1,5),F(3,10)),
         (F(1,5),F(1,5),F(3,10),F(3,10))]
    x = [F(1,4)]*4
    y = [F(6,25),F(13,50),F(13,50),F(6,25)]
    assert [sum(abs(a-b) for a,b in zip(x,v)) for v in p] == [F(3,10)]+[F(1,5)]*4
    assert [sum(abs(a-b) for a,b in zip(y,v)) for v in p] == [F(7,25)]+[F(1,5)]*4
    protective_pairs = 0
    for j in range(4):
        for k in range(4):
            if j == k:
                continue
            assert any(x[j] < v[j] and x[k] > v[k] for v in p), (j,k)
            protective_pairs += 1
    print('four-project boundary: all',protective_pairs,'ordered transfers blocked; strict grand improvement verified')
    print('PASS: exact rational all-case checks:',total)


if __name__ == '__main__':
    run()
