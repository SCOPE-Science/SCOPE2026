"""Exact integer verification of majority-error counts for exact-three substitutions.

Uses two independent finite binomial-product expansions for prescribed bad
coordinates, plus the derived one- and two-coordinate closed sums.
No third-party dependencies are required.
"""
from itertools import combinations
from math import comb
import random


def C(n, r):
    return comb(n, r) if 0 <= r <= n else 0


def model(k):
    return 2 * C(k - 2, 2) + 1, C(k - 2, 2) + 1


def single_formula(k):
    n, threshold = model(k)
    incident = C(k - 1, 2)
    outside = C(k - 1, 3)
    return sum(C(incident, d) * C(outside, n-d)
               for d in range(threshold, incident + 1))


def double_formula(k):
    b = C(k-2, 2)
    a = k-2
    c = C(k-2, 3)
    ans = 0
    for x in range(1, a+1):
        for i in range(x):
            for j in range(x):
                ans += C(a, x) * C(b, i) * C(b, j) * C(c, 1-x+i+j)
    return ans


def prescribed_bad(k, r, selected):
    """Coefficient DP: selected edge counts or complementary omitted edge counts.

    The two variants accumulate entirely different degree statistics and
    require different threshold inequalities. State compression in selected
    mode is legitimate because degrees only increase.
    """
    n, threshold = model(k)
    total = C(k, 3)
    lim = n if selected else total-n
    cap = threshold if selected else C(k-1, 2)-threshold
    categories = []
    for mask in range(1 << r):
        m = C(k-r, 3-mask.bit_count())
        if m:
            categories.append((mask, m))
    states = {(0, (0,)*r): 1}
    for mask, m in categories:
        new = {}
        for (count, degrees), ways in states.items():
            for take in range(min(m, lim-count)+1):
                new_degs = tuple(
                    (min(cap, degrees[i]+take) if selected else degrees[i]+take)
                    if mask >> i & 1 else degrees[i]
                    for i in range(r))
                if not selected and any(d > cap for d in new_degs):
                    continue
                key = (count+take, new_degs)
                new[key] = new.get(key, 0) + ways * C(m, take)
        states = new
    return sum(ways for (count, degs), ways in states.items()
               if count == lim and all(
                   d >= threshold if selected else d <= cap for d in degs))


def complete_distribution(k, use_dp=False):
    n, threshold = model(k)
    maximum = 4 if k == 7 else 3 if k == 8 else 2
    F = [None, single_formula(k), double_formula(k)]
    if maximum >= 3:
        F.append(prescribed_bad(k, 3, selected=use_dp))
    if maximum >= 4:
        F.append(prescribed_bad(k, 4, selected=use_dp))
    I = [C(C(k, 3),n)] + [C(k, j)*F[j] for j in range(1, maximum+1)]
    dist = [sum((-1)**(j-r)*C(j,r)*I[j] for j in range(r,maximum+1))
            for r in range(maximum+1)]
    assert min(dist) >= 0 and sum(dist) == I[0]
    return F, dist


def random_check(k, count, seed):
    rng = random.Random(seed)
    triples = list(combinations(range(k), 3))
    n, threshold = model(k)
    max_allowed = 4 if k == 7 else 3 if k == 8 else 2
    max_seen = 0
    for _ in range(count):
        Y = rng.sample(triples, n)
        deg = [0]*k
        for e in Y:
            for v in e:
                deg[v] += 1
        bad = sum(x >= threshold for x in deg)
        assert bad <= max_allowed
        max_seen = max(bad, max_seen)
    return max_seen


def witness_7():
    k=7
    all_edges=set(combinations(range(k),3))
    removed={(4,5,6)}
    for v in range(4):
        for ab in combinations((4,5,6),2):
            removed.add(tuple(sorted((v,)+ab)))
    removed.add((0,1,4))
    assert len(removed)==14
    remaining=all_edges-removed
    assert len(remaining)==21
    degrees=[sum(v in e for e in remaining) for v in range(k)]
    assert degrees[:4]==[11,11,12,12]
    return degrees


def witness_8():
    k=8
    out=range(3,8)
    chosen={tuple((0,1,2))}
    for p in combinations(range(3), 2):
        for v in out:
            chosen.add(tuple(sorted(p+(v,))))
    for v in range(3):
        for ab in list(combinations(out,2))[:5]:
            chosen.add(tuple(sorted((v,)+ab)))
    assert len(chosen)==31
    degrees=[sum(v in e for e in chosen) for v in range(k)]
    assert degrees[:3]==[16,16,16]
    return degrees


def main():
    assert witness_7()[:4] == [11,11,12,12]
    assert witness_8()[:3] == [16,16,16]
    cases=0
    for k in range(7, 12):
        F, distribution = complete_distribution(k)
        for j in range(1, min(2, len(F)-1)+1):
            assert F[j]==prescribed_bad(k,j,False)
            assert F[j]==prescribed_bad(k,j,True)
            cases+=2
        if k in (7,8):
            for j in range(3,len(F)):
                assert F[j]==prescribed_bad(k,j,True)
                cases+=1
        if k==7:
            assert F[3:]==[951125,4531]
            assert sum(distribution[1:]) == 1819700190
        if k==8:
            assert F[3]==C(10,5)**3==16003008
            assert sum(distribution[1:])==649938525134752
        if k==9:
            assert sum(distribution[1:])==5345935937652753076536
        print('k',k,'N',model(k)[0],'intersection_counts',F[1:],
              'majority_error_distribution',distribution)
    assert random_check(7, 1500, seed=73) <= 4
    assert random_check(8, 1500, seed=83) <= 3
    assert random_check(9, 1500, seed=93) <= 2
    assert all((k-3)*(k-8)>0 for k in range(9,200))
    print('EXACT_THREE_MAJORITY_VERIFY_OK',cases,'cross-expansions and 4500 direct samples')

if __name__=='__main__':
    main()
