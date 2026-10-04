---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The final claim was checked from its definitions and from the published ball-gradient premises. For \(u=\sum_{j=1}^m a_j\mathbf 1_{B_{r_j}(c_j)}\), positivity and nesting determine \(u^*\) exactly. Linearity gives \(\nabla^s u=\sum_{j=1}^m a_jG_j\), and each \(G_j\) is \(L^1\), nonzero away from its center and sphere boundary, and radial with direction \(-(x-c_j)/|x-c_j|\).

For concentric balls, all nonzero summands have one direction almost everywhere, so the \(L^1\) norm is the sum of the individual \(L^1\) norms. For arbitrary centers, the triangle inequality gives the upper bound and subtraction gives the exact nonnegative deficit. If two centers differ, strictness holds on positive measure: outside their connecting affine line when \(N\ge2\), and between the centers when \(N=1\). This verifies the equality classification.

No finite computation is used as an infinite proof. No claim is made beyond finite towers or beyond the \(L^1\) endpoint. The central nonstandard analytic premises were checked against the primary fractional-gradient source, especially its equations (2.1)–(2.3).
