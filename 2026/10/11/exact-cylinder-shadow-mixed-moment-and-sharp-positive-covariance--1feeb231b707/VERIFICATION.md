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

# Reproducibility and limits

Run `python3 verify.py` from the extracted directory. Only the Python standard library is needed. The checker independently generates rational bounds for \(\pi\) by Machin's identity and alternating arctangent partial sums, constructs \(S_{144}\) exactly, applies the proved coefficient and tail estimates, and verifies strict inequalities guaranteeing a negative discriminant. Thus the positivity proof is an exact finite certificate plus elementary analytic bounds, not a numerical experiment.

The same script checks the first and mixed moments by numerical quadrature for multiple aspect ratios and compares fifteen actual convex hulls of projected finite polygonal cylinder approximations with the continuous shadow formulas. Those finite checks independently test geometry and normalization but are not proofs for the continuum of shapes or directions. The printed minimizer and minimum are quadrature approximations, not part of the exact rational sign certificate; the analytic expressions provide their definitions. Independent audit has not been performed.
