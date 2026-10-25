"""Independent finite tests for fixed-content ternary Parikh-matrix spectra.

Usage: python3 checker.py
Requires only Python 3 standard library. Finite tests supplement, not replace,
the all-parameter proof in RESULT.md.
"""
from itertools import combinations
from collections import defaultdict
from random import Random


def direct_spectra(m):
    n = m + 4
    out = defaultdict(set)
    instances = 0
    for apos in combinations(range(n), 2):
        unused = [i for i in range(n) if i not in apos]
        for cpos in combinations(unused, 2):
            w = ['b'] * n
            for i in apos:
                w[i] = 'a'
            for i in cpos:
                w[i] = 'c'
            aa = bb = ab = bc = abc = 0
            for ch in w:
                if ch == 'a':
                    aa += 1
                elif ch == 'b':
                    bb += 1
                    ab += aa
                else:
                    bc += bb
                    abc += ab
            out[ab, bc].add(abc)
            instances += 1
    return out, instances


def cut_spectra(m, u, v):
    vals = set()
    for x in range((u + 1) // 2, min(u, m) + 1):
        y = u - x
        if y < 0 or y > m:
            continue
        for p in range(max(0, v-m), v // 2 + 1):
            q = v-p
            if q > m:
                continue
            vals.add(sum(max(0, s+t-m) for s in (x,y) for t in (p,q)))
    return vals


def proposed(m, u, v):
    assert 0 <= u <= 2*m and 0 <= v <= 2*m
    if u > m:
        # Reverse the word: (u,v,z) maps to
        # (2m-u,2m-v,4m-2u-2v+z).
        up, vp = 2*m-u, 2*m-v
        return {z-(4*m-2*u-2*v) for z in proposed(m,up,vp)}
    s = u+v
    if s < 2*m:
        return set(range(min(u,max(0,s-m))+1))
    if s == 2*m:
        return set(range(u%2,u+1,2))
    h = s-2*m
    return set(range(2*h,u+h+1))


def run():
    nwords = 0
    pairs = 0
    for m in range(16):
        by, instances = direct_spectra(m)
        nwords += instances
        expected = (m+1)*(m+2)*(2*m+1)//2
        actual = sum(map(len,by.values()))
        assert actual == expected, (m,actual,expected)
        for u in range(2*m+1):
            for v in range(2*m+1):
                have = by.get((u,v),set())
                want = proposed(m,u,v)
                assert have == want, ('direct',m,u,v,have,want)
                cut = cut_spectra(m,u,v)
                assert cut == want, ('cut',m,u,v,cut,want)
                pairs += 1
    rng = Random(2048)
    random_checks = 0
    for _ in range(2500):
        m = rng.randint(0,90)
        u = rng.randint(0,2*m)
        v = rng.randint(0,2*m)
        assert cut_spectra(m,u,v) == proposed(m,u,v), (m,u,v)
        random_checks += 1
    print(f'CHECK_OK direct_words={nwords} complete_slices={pairs} random_slices={random_checks}')

if __name__=='__main__':
    run()
