---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The slice has a relative interior point c/2. A vertex can have at most one interior coordinate, since otherwise a two-coordinate transfer gives a feasible line segment, and cannot have zero interior coordinates by nonresonance. An isotropic Gaussian in the intrinsic space is obtained by subtracting the mean from iid Gaussian coefficients, which leaves all strict orders equiprobable. The transfer argument forces greedy saturation in that order. Exactly |H|!(n-|H|-1)! orders expose a given vertex (H,j), and uniform prefix subsets give the asserted tails including r=0,n. Half-quota nonresonance makes the crossing position reverse to n+1-T. A dominant coordinate makes its uniform position pivotal; without one the law is central for n=3,4, and n=2 must be dominant. Majorization cannot create a dominant coordinate under balancing, and comparing the extreme ranks to the nearer central ranks proves convex-order monotonicity there. For five coordinates without a dominant weight, winning pairs are intersecting, so they form a star of at most four edges or lie in a triangle. Hence only h=0,...,4 are possible and the two tails have mass h/10. All six witnesses avoid ties by even capacities and odd half-total. For the example c and d the sorted prefix sums are (6,12,14,16,18) and (6,10,14,16,18); h goes from 1 to 2, so E phi(T_d)-E phi(T_c)=(phi(2)+phi(4)-2phi(3))/10 and the variances are 1/5 and 2/5. Read the supplied code without executing it; fresh exact enumeration of 120 permutations per witness gave all six histograms (/tmp/opencode/frozen-review-replay.py, section 2). That is a check on the witnesses, not a proof of exhaustive real-capacity classification.

## originality

PASS

The supported distinct finding is the sharp majorization statement, including strict reversal of the whole convex order at five coordinates and the location of that witness in the exact six-law spectrum. The random permutation interpretation is classical, and the law spectrum alone is very close to prior voting-game enumeration: a complete table of the relevant winning-coalition families determines it automatically. No independent priority is assigned to the geometric greedy correspondence, basic counting construction, or game taxonomy. The actual comparably weighted representations and sharp convex-order theorem were not found in the inspected statements.

## value

PASS

The exposed-vertex rank is a canonical directional sampling statistic for a fixed central section, quite different from counting vertices or calculating a voter's influence. It is natural to expect balancing to concentrate it. The proof establishes exactly where that intuition first fails and supplies a reverse convex-order witness, not just a single variance comparison; the six-law spectrum explains the mechanism through changes in winning-pair counts. This is a useful small-dimensional boundary rather than an unmotivated finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
