---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For d>=2,m>=3 the symmetric polarization of F=x0^(m-1)*x_(d-1)+x0^(m-2)*sum_(1<=i<=d-2) xi^2 has all d partial derivatives linearly independent: the first partial separates x_(d-1), the remaining monomial derivatives are independent, and the last coordinate derivative is x0^(m-1). Each mode flattening has rank d. Simultaneous determinant-one weights (d-1,-1,...,-1) give strictly positive weights (m-1)(d-1)-1 and (m-2)(d-1)-2 except d=m=3; at (3,3), (2,0,-2) gives weight 2 for both monomials. Thus T tends to zero under an SL_d^m one-parameter subgroup, forcing every positive-character semi-invariant to vanish: it is not central semistable. For m=2, invertible matrices lie in the GL_d x GL_d orbit of I_d, a balanced polystable representative. I independently recomputed flattening ranks and occupied-term 1PS weights for 42 finite formats; these checks corroborate and do not establish the universal quantifiers.

## originality

PASS

The d=2,m=3 W/GHZ separation is classical and explicitly excluded from the novelty claim. A uniform all-d, all-m algebraic full-rank nullcone witness distinguishes m=2 from all m>=3 and confronts a recent hyperquiver rank/semistability assertion. No matching all-format statement was located in the inspected relevant materials, but old invariant-theoretic tensor instability criteria could encode the same result implicitly. The closely targeted 2026 Bielawski manuscript itself was not available in full, so the exact formulation and central-character convention in its Proposition 3.3 remain a priority/interpretation risk.

## value

PASS

The boundary identifies exactly where the full-flattening-rank test ceases to characterize quotient semistability, and supplies a uniform algebraic obstruction even when generic stabilizers are finite. It is relevant to the actual GIT/Kähler quotient, not a cheap rank calculation. It does not classify the entire semistable locus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
