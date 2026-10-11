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

# Verification and scope
The analytic checks are: (i) product covariogram of the square; (ii) a convergent Mellin moment for every \(p>-1\); (iii) exact factorization of the reduced radial derivative; (iv) logarithmic monotonicity for the axis/diagonal comparison; and (v) explicit substitution at the phase boundary \(p=2\). The standalone `verify.py` recomputes the moment identity using rational arithmetic, checks the derivative factorization, and numerically surveys directions for selected parameters on both sides of the transitions. The recorded numerical checks support only the finite test cases. The proof in `RESULT.md` is the justification for the all-real-parameter theorem.

The negative-parameter formula is the integration-by-parts form of the covariogram representation in Langharst, arXiv:2603.14134v4, Proposition 10. The finding does not claim independent external validation or any general sharp parameter optimization for other convex bodies.
