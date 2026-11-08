---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Let G=K_m x K_n with adjacency when both coordinates differ, m,n>=3. Reconstructed classification: disconnected survivors with an isolate lie in one row/column cross; without isolates an edge in one component forces every vertex of the other into the two cross corners, so exactly a 2x2 rectangle. These four disjoint forms yield D(t)=m[(1+t)^n-1-nt]+n[(1+t)^m-1-mt]+mn t[(1+t)^(m-1)-1][(1+t)^(n-1)-1]+C(m,2)C(n,2)t^4. Maximal disconnected survivor sets are full crosses and 2x2 rectangles; complements are all inclusion-minimal cuts of sizes (m-1)(n-1), mn-4. Independent exhaustive graph search over every labeled survivor subset for 3x3, 3x4, 3x5, 4x4 (sum 2144 disconnected subsets) matched all coefficients and both maximal-cut types; graph proof covers unbounded m,n. Reliability subtraction is exact for independent p survival with nonempty-connected convention.

## originality

PASS

Best-of-knowledge qualified originality: the exact published model/theorem comparisons below do not establish an earlier dominating theorem for the narrow stated new remainder. Related prior methods and components explicitly credited; uninspected specialized literature risks remain.

## value

PASS

The complete labeled disconnected-subset polynomial and all inclusion-minimal vertex-cut sizes refine previously known minimum cut and super-connectivity into a full reliability invariant, useful for exact residual node-failure distributions in categorical-product networks. Both tiers have natural cut interpretation and an unbounded separation, not a random small graph computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
