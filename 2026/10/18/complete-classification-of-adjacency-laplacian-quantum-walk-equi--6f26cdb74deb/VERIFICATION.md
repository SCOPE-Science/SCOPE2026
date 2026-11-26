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

Verified the repaired clique-return theorem directly, independently of the three-cell moment multiplication. For clique v, shift L up by a+b−1 times the identity, which does not affect probabilities. The shifted matrix B=A+(b−1)P_I, with P_I the coordinate projection onto I, has Be_v=Ae_v and zero diagonal at v. The second moments coincide, so the difference of the fourth-order return coefficients is (||A²e_v||²−||B²e_v||²)/12. Now B²e_v=A²e_v+(b−1)1_I and each I-component of A²e_v is a−1. This gives exactly −b(b−1)(2a+b−3)/12, including a=1, and the probabilities are even in t. The coefficient is strictly negative for b≥2. For the full classification retained as a corollary, on the real normalized part vectors the off-diagonal coupling is √(ab) for both matrices and the diagonal differences are a−1 and b−a up to sign. The cross-part single-vertex transition probabilities have fourth-order terms −[(a−1)²+4ab]/12 and −[(a−b)²+4ab]/12, forcing b=1 or 2a−1. In the complete case the degree is scalar. In the irregular candidate case the bright block identity L_B+aI=−RA_BR (R=diag(1,−1) in I,C order) and the independent dark eigenvalues 0 and −a verify the signed, conjugated amplitude relation for a localized independent source. No clique-dark component occurs for such a start. Thus the retained classification and its boundaries are correct.

## originality

PASS

Pass for the repaired claim only. The frozen text treated the all-size proof for the independent-start family as distinct from numerical observations, overlooking an indexed stronger theorem that already proves the exterior-start iff criterion. The repair credits that coverage and foregrounds the universal quartic clique-return obstruction. The full source classification remains as an explicit corollary combining the two, with the exterior amplitude identity as context. The compared weighted finding and primary papers do not give this clique-return difference or exclude every irregular clique start by it.

## value

PASS

The result distinguishes the two source orbits of a natural graph family: a single local measurement, the return probability to the clique start, rules out every irregular clique case. Knowing the exterior-start equivalence does not answer this other orbit's question. The strict coefficient explains the obstruction for all sizes, including cones, and fills the precise gap needed for the complete source classification rather than repeating the known positive family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
