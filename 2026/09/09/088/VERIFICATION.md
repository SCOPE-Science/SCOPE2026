---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

For the repaired result, checked all 32 parameters are distinct per instance; in B only groups 3 and 4 (zero-based) overlap, by 3/50 with strict nesting. The frozen rational tables system_B_groups.json, narrow_groups.json and narrow_groups_v2.json agree. Rebuilt each divisor independently as a Plücker linear equation from the coefficient vectors of the vanishing quartic and its product by T. Reconstructed rational centers and inverses tested by a direct complex contraction certificate: the maximum Lipschitz upper bounds are below 0.000257 in A and 0.001403 in B, b+qr<r at r=10^−6, and the 14 balls in each are disjoint. Real centers certify real roots by conjugation and uniqueness; the two remaining B balls avoid the real locus. At the true roots the contraction estimate implies derivative invertibility. A separate norm conversion gives rigorous Euclidean alpha bounds, not floating norms or an upward-rounded critical threshold. For the global count, appending P_01=0 yields nine linear pivot columns modulo 1009; eliminating them gives a degree-four Macaulay row span of full rank 126 in six variables in both cases. These unit pivots and nonzero minors lift to characteristic zero. The projective intersection is contained in one affine chart and is therefore finite; its proper intersection length is the Grassmannian degree 14. The 14 simple certified roots exhaust it. The actual repair checker ran successfully for both instances.

## originality

PASS

Only the exactly certified single-nested geometry with 32 distinct rational parameters and the global 12-real-plus-pair count passes. The disjoint result is a known control; generic overlap-associated nonreality in this exact cell and even the same numerical overlap score are prior. The bounded comparison does not disclose a previously certified same-geometry witness.

## value

PASS

A single interacting pair is the smallest number of pairwise-disjointness violations possible. Showing that strict nesting alone suffices, even without a repeated point and with exhaustion and transversality proved, isolates a clear geometric failure mode not visible in a coarse empirical overlap score. The known disjoint instance is only a control. The exact rational witness can be used as a reproducible test of candidate weakenings of the divisor theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
