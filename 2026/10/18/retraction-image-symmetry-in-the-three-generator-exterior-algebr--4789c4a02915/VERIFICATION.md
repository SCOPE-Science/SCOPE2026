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

Exact exterior multiplication and algebra substitution were independently implemented in `artifacts/check_exterior_retractions.py`. The checker enumerates all higher-degree coefficients for the four standard tangent projections over \(\mathbb F_3\), rejects tuples that fail the exterior relations, and checks \(e^2=e\) on all three generators rather than merely checking the tangent projection. The observed fixed-projection counts \((1,27,81,1)\) match \((1,q^3,q^4,1)\) at \(q=3\).

Additional exact enumeration for a fixed tangent line/plane gives \(27\) distinct images in either intermediate rank over \(\mathbb F_3\), with \(27\) versus \(243\) normalized generating tuples; directly evaluated canonical image fibers are \(9\) and \(27\). Full parameter sweeps verify the rank-two normal form at \(q=5\) and \(q=7\). The script prints `ALL_EXACT_CHECKS_PASSED` when all tests succeed.

This is finite verification supporting, not replacing, the general symbolic proof. The equal number of embedded images, all-prime-power quantifiers, and uniform fiber counts rely on the algebraic normal forms, automorphism transitivity, and finite-field subspace counting supplied in the proof. The characteristic-two case is excluded. Independent audit has not been performed.
