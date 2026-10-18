---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

The weighted cycle Lipschitz increments identify Lip₀(C_m(w)) isometrically with Y_w={u∈ℝ^m:∑w_i u_i=0}, sup norm, even when a long edge is redundant; finite duality preserves numerical index. If 2w_i≥W, eliminating u_i identifies Y_w isometrically with ℓ∞^(m−1). Otherwise the dual unit ball is conv of ±restricted coordinate functionals, each exposed by q_i=1, q_j=−w_i/(W−w_i), so McGregor tests cube-hyperplane vertices for a coordinate inside (−1,1). A cube-section vertex has at most one free coordinate. If all weights equal, parity gives precisely even m. For unequal positive weights in genuine-cycle region take maximal a, alternately sign all other weights equal a to residual 0 or a, then sequentially choose opposite sign for each remaining c<a so |r−c|<a; hence a free maximal-weight coordinate |u_i|<1 yields strict index<1. This handles ties, arbitrary positive reals and thresholds, without assuming finite enumeration proves the universal lemma. Independently checked the exact rational vertex predicate on all 1053 weight vectors m=4..6 each coefficient 1..3, 42302 vertices total; finite diagnostic only.

## originality

PASS

Best-of-knowledge novelty survives comparison with unit-edge graph bipartiteness, equal-unit-weight cycle parity, 3-point metric formulas, general numerical-index geometry, and separately published one-edge special case. The all-positive-weight central hyperplane theorem implies the contemporaneous one-weight result, not conversely. McGregor gives a general method but does not state the signed-sum classification for all positive weights. No found earlier source covers the complete all-real-weight m>=4 phase diagram. Residual historical polyhedral/transportation aliases remain explicit.

## value

PASS

A complete exact parameter classification of maximal numerical index for the natural positive-normal hyperplane sections of cubes (equivalently arbitrary weighted cycle metrics) captures a robust parity/metric redundancy phenomenon. It settles a genuine family not mechanically decided by the unweighted theorem, with a useful signed-sum structural lemma; no downstream paper-sized corollary is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
