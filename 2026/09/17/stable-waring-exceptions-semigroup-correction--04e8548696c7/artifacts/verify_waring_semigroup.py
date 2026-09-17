#!/usr/bin/env python3
"""Verifier for a correction/generalization of a stable Waring-exception bound.

The stable offset set B^k is identified in the accompanying proof with the gap set
of S_k=<a^k-1 : a>=2>.  This script checks small exact cases from
Benfield--Lippard, the p=3 counterexample to their Theorem 10.7, and the explicit
modular gap families used in the corrected proof.

No network access or third-party packages are used.
"""

KNOWN = {2: (7, 13), 4: (1321, 2641), 6: (355825, 711649), 8: (945121, 1890241)}


def semigroup_gaps(k: int, claimed_max_gap: int):
    """Return all gaps through a certified conductor using the known max as target."""
    multiplicity = 2**k - 1
    cap = claimed_max_gap + multiplicity
    gens = []
    a = 2
    while a**k - 1 <= cap:
        gens.append(a**k - 1)
        a += 1
    reachable = bytearray(cap + 1)
    reachable[0] = 1
    for n in range(1, cap + 1):
        reachable[n] = any(n >= g and reachable[n - g] for g in gens)
    # multiplicity consecutive reachable values imply every later value is reachable.
    assert all(reachable[n] for n in range(claimed_max_gap + 1, cap + 1))
    return [n for n in range(1, cap + 1) if not reachable[n]], gens


def carmichael_prime_power(p: int, e: int) -> int:
    return 2 ** (e - 2) if p == 2 and e >= 3 else (p - 1) * p ** (e - 1)


def modular_gap_family(k: int, p: int, e: int):
    """Explicit gaps from q=p^e when lambda(q)|k and e<=k."""
    q = p**e
    lam = carmichael_prime_power(p, e)
    assert k >= e and k % lam == 0
    M = p**k // q
    gaps = set()
    for r in range(1, q):
        for t in range(1, r * M):
            gaps.add(q * t - r)
    formula = p**k * (q - 1) // 2 - (q - 1)
    assert len(gaps) == formula
    return gaps, formula


def main():
    computed = {}
    for k, (known_count, known_max) in KNOWN.items():
        gaps, gens = semigroup_gaps(k, known_max)
        assert len(gaps) == known_count
        assert max(gaps) == known_max
        computed[k] = set(gaps)
        print(f"k={k}: |B^k|={len(gaps)}, max={max(gaps)}, first generators={gens[:5]}")

    # Theorem 10.7 says 9 for p=3, while B^2 has exactly seven elements.
    claimed_p3 = 3**2 * (3 - 1) // 2
    assert claimed_p3 == 9 and len(computed[2]) == 7
    assert computed[2] == {1, 2, 4, 5, 7, 10, 13}
    print(f"p=3: published claimed lower bound={claimed_p3}, exact |B^2|={len(computed[2])}")

    # Correct modular family in representative prime and prime-power cases.
    tests = [(2, 3, 1), (4, 5, 1), (4, 2, 3), (6, 7, 1), (8, 5, 1)]
    for k, p, e in tests:
        explicit, formula = modular_gap_family(k, p, e)
        assert explicit <= computed[k]
        print(f"k={k}, q={p**e}: modular family has {formula} certified gaps")

    # A non-minimal-exponent example: p=5 also applies to k=8, since 4|8.
    # Here 5*4 < 2^8-1, so adding four small multiples of 5 yields 5^8*2 gaps.
    mod58, count58 = modular_gap_family(8, 5, 1)
    extra58 = {5, 10, 15, 20}
    assert extra58 <= computed[8] and mod58.isdisjoint(extra58)
    assert count58 + 4 == 5**8 * 2 == 781250
    print("k=8, p=5: repaired/generalized lower bound=781250")

    # Repair of the original lower bound for p=5: four residue-0 gaps supplement
    # the modular family of size 1246.
    mod5, count5 = modular_gap_family(4, 5, 1)
    extra5 = {5, 10, 20, 25}
    assert extra5 <= computed[4] and mod5.isdisjoint(extra5)
    assert count5 + len(extra5) == 5**4 * (5 - 1) // 2 == 1250
    print("p=5: modular 1246 + gaps {5,10,20,25} = 1250")

    # For p>=7, p,2p,...,(p-1)p lie below 2^(p-1)-1, hence are extra gaps.
    for p in (7, 11, 13, 17, 19):
        assert p * (p - 1) < 2 ** (p - 1) - 1
    mod7, count7 = modular_gap_family(6, 7, 1)
    extra7 = {7 * m for m in range(1, 7)}
    assert extra7 <= computed[6] and mod7.isdisjoint(extra7)
    assert count7 + 6 == 7**6 * 3 == 352947
    print("p=7: modular 352941 + six small residue-0 gaps = 352947")

    # p=11 corollary: the repaired p>=7 argument retains the published number.
    p = 11
    k = 10
    repaired = p**k * (p - 1) // 2
    modular_only = repaired - (p - 1)
    assert repaired == 129_687_123_005
    assert modular_only == 129_687_122_995
    assert p * (p - 1) < 2**k - 1
    print(f"p=11: repaired lower bound={repaired}; modular family alone={modular_only}")


if __name__ == "__main__":
    main()
