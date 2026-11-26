---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

On the invariant centered subspace, comparing P_s for all s is equivalent to comparing A_t^{-2} in Loewner order, where A_t=H+tB. Order reversal under positive-definite inversion converts this to ordering A_t² in the opposite direction. For t₂>t₁ its change is (t₂−t₁)[HB+BH+(t₁+t₂)B²], proving sufficiency and necessity by t₁=0, t₂→0. Differentiating gives the stated congruence by A_t^{-2}, so a negative direction y at 0 gives s=H²y with positive initial derivative. Independently, put J=[e₁−e₂,e₂−e₃]; JᵀJ=[[2,−1],[−1,2]]. In Q=JCJᵀ the two diagonal entries of C are (2+4a)u and (2+4b)v; the off-diagonal is −(av+bu). Hence det C=Kuv−b²u²−a²v², and C has the same inertia as Q on the centered subspace. This gives the two positive distinct roots and a negative direction when either update alone is nonzero. Closed endpoints are safe; on a connected update path B² is positive definite on that subspace, which gives strictness for t>0, including relative to t=0. Independent exact evaluation via −2zᵀH⁻¹Bz, z=H⁻¹s, reproduced all three slopes 10/2197 in the example.

## originality

PASS

Passes for the exact two-edge path window with endpoints and two individually unsafe updates jointly safe for every opinion profile. The general anticommutator criterion is a short application of standard matrix order; the single-edge derivative and adverse individual updates already have prior coverage and are not separate novelty claims.

## value

PASS

All-profile safety is actionable when innate opinions are unknown. The weighted three-path is the smallest natural setting with two distinct connected update edges, not an arbitrarily selected example. The exact interval shows how to balance strengths and proves that combining two individually risky updates can protect every fixed profile, including at the sharp boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
