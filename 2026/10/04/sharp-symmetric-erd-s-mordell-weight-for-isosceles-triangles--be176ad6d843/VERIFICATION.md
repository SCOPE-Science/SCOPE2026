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
The analytic verification checks the full quantified claim: symmetry and strict convexity reduce to the axis; differentiating the quotient \(B_h(y)\) gives a unique phase transition at \(h=1\); substitution yields both exact coefficient branches; and the median-to-bisector comparison factors into an explicitly nonnegative polynomial.

The bundled `verify.py` independently replayed the central algebraic factorization with exact integer polynomial arithmetic, checked 20,000 deterministic parameter values, and ran 60,000 deterministic interior-point stress tests. It returned `VERIFY_OK`; the smallest sampled sharp-inequality defect was `1.7688941511551093e-07`, the smallest sampled Liu-specialization defect was `0.0017469132115603969`, and the maximum residual on tested exact interior equality points was `3.5527136788005009e-15`. These finite checks are supplemental and do not replace the analytic proof.

Unproved limits: no statement is made for scalene triangles, and no claim of absolute literature uniqueness is made beyond the recorded searches and source comparisons.
