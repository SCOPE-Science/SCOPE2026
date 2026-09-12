"""Independent certificate for lane-1275 emergent finding (p=3 case).

Verifies, by complete finite enumeration (no heuristics):
  T1: S16 (16 points in C9^2) contains NO 9-term zero-sum  =>  g(C9^2) >= 17.
  T2: every one-point extension of S16 (65 of them) DOES contain a 9-term
      zero-sum  =>  S16 is extension-maximal (maximal one-free along chains).
  T3: S20 (20 points) contains 9-term zero-sums but NO TWO DISJOINT ones
      =>  g^2(C9^2) >= 21.
  T4: every one-point extension of S20 (61 of them) DOES contain two disjoint
      9-term zero-sums  =>  S20 is extension-maximal two-free along chains.

Run: python3 certify.py   (deterministic; no randomness, no dependencies)
"""
import itertools

MOD = 9
K = 9

S16 = [(0,1),(0,2),(1,0),(1,1),(2,7),(3,4),(3,5),(4,2),(4,3),(5,0),
       (5,8),(6,7),(6,8),(7,5),(8,3),(8,4)]

S20 = [(0,1),(0,2),(0,3),(1,0),(1,1),(2,7),(3,4),(3,5),(4,2),(4,3),
       (5,0),(5,1),(5,8),(6,5),(6,7),(6,8),(7,2),(7,5),(8,3),(8,4)]

G = [(x, y) for x in range(MOD) for y in range(MOD)]


def zero_sum_masks(S):
    """Bitmasks (over positions of S) of all K-subsets summing to (0,0)."""
    out = []
    n = len(S)
    for T in itertools.combinations(range(n), K):
        sx = 0
        sy = 0
        for i in T:
            sx += S[i][0]
            sy += S[i][1]
        if sx % MOD == 0 and sy % MOD == 0:
            m = 0
            for i in T:
                m |= (1 << i)
            out.append(m)
    return out


def has_zero_sum(S):
    for T in itertools.combinations(range(len(S)), K):
        sx = 0
        sy = 0
        for i in T:
            sx += S[i][0]
            sy += S[i][1]
        if sx % MOD == 0 and sy % MOD == 0:
            return True
    return False


def has_disjoint_pair_new_point(S, g):
    """Does S+[g] contain two disjoint K zero-sums? Fast path: old zero-sums
    of S are pairwise intersecting (checked separately), so any disjoint pair
    must use a zero-sum containing the new point (position n)."""
    n = len(S)
    old = zero_sum_masks(S)
    # new zero-sums: (K-1)-subsets of S summing to -g
    tx = (-g[0]) % MOD
    ty = (-g[1]) % MOD
    new = []
    for T in itertools.combinations(range(n), K - 1):
        sx = 0
        sy = 0
        for i in T:
            sx += S[i][0]
            sy += S[i][1]
        if sx % MOD == tx and sy % MOD == ty:
            m = 0
            for i in T:
                m |= (1 << i)
            new.append(m)
    # A disjoint pair in S+[g] must use at least one zero-sum containing the
    # new point (old zero-sums are pairwise intersecting by T3). Two
    # zero-sums both containing the new point share it, so it suffices to
    # test each new zero-sum (a (K-1)-subset of S summing to -g) for
    # disjointness against the old zero-sums.
    for m in new:
        for o in old:
            if m & o == 0:
                return True
    return False


def main():
    assert len(S16) == 16 and len(set(S16)) == 16
    assert len(S20) == 16 + 4 and len(set(S20)) == 20
    assert set(S16) < set(S20)  # S20 extends S16

    # T1
    z16 = zero_sum_masks(S16)
    print("T1: #9-sums in S16 =", len(z16))
    assert len(z16) == 0, "S16 must be 9-sum-free"

    # T2
    rest16 = [g for g in G if g not in S16]
    assert len(rest16) == 65
    bad16 = [g for g in rest16 if not has_zero_sum(S16 + [g])]
    print("T2: one-free extensions of S16 =", len(bad16))
    assert len(bad16) == 0, bad16

    # T3
    z20 = zero_sum_masks(S20)
    print("T3: #9-sums in S20 =", len(z20))
    assert len(z20) > 0
    pair = any((z20[i] & z20[j]) == 0
               for i in range(len(z20)) for j in range(i + 1, len(z20)))
    print("T3: disjoint pair in S20 =", pair)
    assert not pair, "S20 must have no two disjoint 9-sums"

    # T4
    rest20 = [g for g in G if g not in S20]
    assert len(rest20) == 61
    bad20 = [g for g in rest20 if not has_disjoint_pair_new_point(S20, g)]
    print("T4: two-free extensions of S20 =", len(bad20))
    assert len(bad20) == 0, bad20

    print("ALL CERTIFICATES PASS: g(C9^2)>=17, g^2(C9^2)>=21, "
          "both extremals extension-maximal.")


if __name__ == "__main__":
    main()
