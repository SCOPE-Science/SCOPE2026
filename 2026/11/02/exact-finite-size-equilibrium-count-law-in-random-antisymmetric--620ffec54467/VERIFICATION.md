---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Every column has an independent uniformly random ordered distinct maximum/minimum pair (H_j,L_j). An equilibrium (i,j) is the simultaneous event H_j=i,L_i=j, so loops/two-cycles impossible. Each consistent prescribed arc set is a vertex-disjoint assembly of directed paths and cycles length >=3, of weight n^(-2k)(n/(n-1))^h. Labeled exponential path and cycle components give exactly n![x^n]exp(x+(x^2 t/n^2)/(1-xt/(n(n-1)))+sum_{m>=3}(xt/(n(n-1)))^m/m). The second factorial moment from disjoint arcs and 2-paths yields the variance; N=n requires all vertices in cycles of lengths >=3, including multiple cycles n>=6. Proof covers n=2 boundary with empty top tail. Independent exact-rational enumeration of all ordered column extrema at n=2,3,4 agrees; these finite computations corroborate but are not infinite proof.

## originality

PASS

Best-of-knowledge originality for complete stated claim, after explicit same-object and strong-theorem comparisons; known ingredients and limitations credited. Historical priority is not certified.

## value

PASS

An exact all-n counting distribution, variance and maximum-equilibrium tail in an established random strategic-game ensemble quantifies finite-population deviations missed by its known Poisson limit. Cycle partitions reveal rare events with multiple cyclic best-response components, a natural mathematical feature rather than an arbitrary finite numerical constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
