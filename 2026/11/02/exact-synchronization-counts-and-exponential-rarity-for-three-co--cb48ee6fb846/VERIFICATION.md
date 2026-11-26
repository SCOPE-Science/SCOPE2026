---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the stated synchronous three-color rule, let e(v) be the advance indicator. The new signed edge increment is the old one plus e(v)-e(u): it cannot leave [-1,1], since at old increment +1 the tail advances, and at -1 the head advances. Thus cycle sums persist. If they vanish, integrate to integer heights; updates take the maximum over the closed neighborhood and after two steps the diameter-two rook graph is constant. Minimum-zero heights are confined to {0,1,2}, and the three root phases give distinct colorings. Of these arrays, 2^(mn)-1 use no two. Otherwise the exact row and column supports of zeros determine a full-support binary rectangle (inclusion–exclusion E), and twos occupy an arbitrary nonempty subset of its complementary rectangle. For two rows E(1,u)=1; the binomial sum simplifies to the stated closed form. Inner sums of size O(ru) give O(m²n²) arithmetic, with binomial and power tables precomputed, not a bit bound. For m<=n, each fixed zero/two row typing permits at most 2^r+2^s-1 options per column. Apart from at most 2m extreme typings the bound is 2^(m-2)+3, by r+s<=m and convexity. For m>=6 the normalized contribution is at most 2n(33/64)^n+(57/64)^n; for m<=5 it is at most 3^5(3/4)^n. This proves the uniform asymptotic. An independent spanning-tree exact-lift count and direct binary support check gave 57, 261, 1065, 4149, 2289, 17757 for (2,2),(2,3),(2,4),(2,5),(3,3),(3,4). Replay: python3 /workspace/branches/reproduce_frozen_math.py 4.

## originality

PASS

Credit the general synchronization theorem, the diameter-two homomorphism identity and its generic Widom–Rowlinson partition function, as well as covered tiny members. The distinct all-size result is the polynomial-arithmetic evaluation by zero row/column supports, the entire two-row formula, and the uniform leading term even when the short side stays bounded. No dominating result for those claims was established by the inspected evidence.

## value

PASS

Labelled rook graphs are a natural infinite diameter-two test family, and basin size is a natural dynamical invariant. The support evaluation gives an exact usable count rather than an exponential state or vacancy census, and shows that short graph distances and fast synchronization conditional on success coexist with an exponentially small basin. The leading constant holds even for arbitrarily thin families with the short dimension at least two.

The dated certificate retains the supplied scientific assessment, sources and limitations.
