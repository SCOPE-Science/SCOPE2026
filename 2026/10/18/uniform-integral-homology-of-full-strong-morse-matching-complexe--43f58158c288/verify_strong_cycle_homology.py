#!/usr/bin/env python3
"""Finite checks for the integral strong-cycle homology theorem.

No external packages; all indexing and algebra are explicitly finite.  The
published independence-complex theorems and Alexander duality are used only
in the accompanying mathematical proof, not asserted from finite tests.
"""
from collections import Counter, defaultdict
from itertools import permutations


def ind_faces(n, run_limit):
    """Faces of higher independence complex with no run of run_limit sites."""
    faces = []
    for m in range(1 << n):
        if not any(all((m >> ((i + j) % n)) & 1 for j in range(run_limit))
                   for i in range(n)):
            faces.append(m)
    return faces


def critical_faces(n, run_limit):
    faces = ind_faces(n, run_limit)
    remaining = bytearray(1 << n)
    for m in faces:
        remaining[m] = 1
    for v in range(n):
        bit = 1 << v
        for m in faces:
            if not (m & bit) and remaining[m] == remaining[m | bit] == 1:
                remaining[m] = remaining[m | bit] = 0
    return Counter(m.bit_count() - 1 for m in faces if remaining[m]), len(faces)


def ind_homology_prediction(n, r):
    if r == 1:
        q, z = divmod(n, 3)
        return (q - 1 if z in (0, 1) else q, 2 if z == 0 else 1)
    assert r == 2
    q, z = divmod(n, 4)
    return ((2*q-1 if z in (0, 1) else 2*q if z == 2 else 2*q+1),
            3 if z == 0 else 1)


def face_word_valid(w):
    n = len(w)
    if any(w[i] and w[(i+1) % n] and w[i] != w[(i+1) % n]
           for i in range(n)):
        return False
    nonzero = {x for x in w if x}
    return len(nonzero) != 1 or any(w[i] == w[(i+1) % n] == 0 for i in range(n))


def word_to_mask(w):
    n = len(w)
    return sum(1 << (i if w[i] == 1 else n+i) for i in range(n) if w[i])


def word_faces(n, require_strong):
    from itertools import product
    ans = set()
    for w in product((0, 1, -1), repeat=n):
        if require_strong and not face_word_valid(w):
            continue
        if not require_strong and any(w[i] and w[(i+1) % n]
                                       and w[i] != w[(i+1) % n]
                                       for i in range(n)):
            continue
        ans.add(word_to_mask(w))
    return ans


def filtration_faces(n):
    """Independent generator: enumerate all strict vertex orderings."""
    ans = {0}
    for order in permutations(range(n)):
        h = [0]*n
        for j,v in enumerate(order):
            h[v] = j
        s = [1 if h[i] < h[(i+1) % n] else -1 for i in range(n)]
        marks = [(i if s[i] == 1 else n+i) for i in range(n)
                 if s[i-1] == s[i]]
        for sub in range(1 << len(marks)):
            m = 0
            for j,mark in enumerate(marks):
                if (sub >> j) & 1:
                    m |= 1 << mark
            ans.add(m)
    return ans


def ranks_mod2(faces, nverts):
    bydim = defaultdict(list)
    for m in faces:
        bydim[m.bit_count()-1].append(m)
    if not bydim:
        return {}
    ranks = {}
    for d in sorted(k for k in bydim if k >= 1):
        low = {m:i for i,m in enumerate(bydim[d-1])}
        pivots = {}
        for m in bydim[d]:
            col = 0
            for i in range(nverts):
                if m & (1<<i):
                    col ^= 1 << low[m ^ (1<<i)]
            while col:
                pivot = col.bit_length()-1
                if pivot not in pivots:
                    pivots[pivot] = col
                    break
                col ^= pivots[pivot]
        ranks[d] = len(pivots)
    betti = {}
    for d in sorted(k for k in bydim if k >= 0):
        b = len(bydim[d]) - ranks.get(d,0) - ranks.get(d+1,0)
        if d == 0: b -= 1
        if b:
            betti[d] = b
    return betti


def predicted_homology(n):
    d1,a1 = ind_homology_prediction(n,1)
    d2,a2 = ind_homology_prediction(n,2)
    out = Counter()
    out[n-2-d2] += a2
    out[n-3-d1] += 2*a1
    return dict(sorted(out.items()))


def direct_model_check(n):
    strong = word_faces(n, True)
    loose = word_faces(n, False)
    assert strong <= loose
    missing = loose - strong
    xmask = (1<<n)-1
    for m in missing:
        assert not (m & xmask and m & (xmask<<n))
        t = (m & xmask) or (m>>n)
        assert all((t>>i)&1 or (t>>((i+1)%n))&1 for i in range(n))
    for m in strong:
        assert m in loose
    all_legal = filtration_faces(n)
    assert strong == all_legal, (n, len(strong), len(all_legal))
    return len(strong), len(missing)


def main():
    print('IND_1_AND_IND_2_ACYCLIC_MATCHING_CRITICAL_CELLS')
    for n in range(6, 23):
        pred = ind_homology_prediction(n, 2)
        critical,num = critical_faces(n,3)
        assert critical == Counter({pred[0]:pred[1]}), (n,critical,pred)
        print(f'Ind_2(C_{n}): faces={num} critical={dict(critical)}')
    for n in range(6, 17):
        pred = ind_homology_prediction(n,1)
        critical,_ = critical_faces(n,2)
        assert critical == Counter({pred[0]:pred[1]}), (n,critical,pred)
    print('INDEPENDENT_FILTRATION_AND_WORD_VALIDATION')
    for n in range(3,9):
        a,b = direct_model_check(n)
        print(f'n={n}: strong_faces={a} loose_only_faces={b}')
    print('DIRECT_MOD2_HOMOLOGY')
    for n in range(6,10):
        actual = ranks_mod2(word_faces(n,True),2*n)
        expected = predicted_homology(n)
        assert actual == expected, (n,actual,expected)
        print(f'n={n}: actual={actual}, predicted={expected}')
    published_table = {
        6:{2:5}, 7:{2:1,3:2}, 8:{3:5}, 9:{4:5},
        10:{4:1,5:2}, 11:{4:1,5:2}, 12:{5:3,6:4},
        13:{6:1,7:2}, 14:{6:1,7:2}, 15:{6:1,8:4},
        16:{7:3,9:2}, 17:{8:1,9:2}, 18:{8:1,10:4},
        19:{8:1,11:2}, 20:{9:3,11:2}, 21:{10:1,12:4},
    }
    for n, ranks in published_table.items():
        assert predicted_homology(n) == ranks, (n,predicted_homology(n),ranks)
    print('PUBLISHED_TABLE_1_CHECK_OK sizes=6..21')
    assert predicted_homology(22) == {10:1, 13:2}
    print('n=22: predicted integral reduced homology Z in degree 10 and Z^2 in degree 13')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
