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

# Verification notes

The analytical proof computes **both** two-step quadratic-form expectations with exact angular integrals. In the scaled Hessian eigenbasis, the pair-to-independent coefficient ratio is \(((r^2-1)/(r^2+1))^2\), where \(r=\sqrt\kappa\). Both coefficients of the independent expectation are positive. Reflection parity eliminates mixed terms.

The accompanying `verify.py` directly integrates the conditional two-step energy losses by uniform-angle midpoint quadrature and checks all four coefficient formulas at seven anisotropy parameters. Run `python verify.py` from the directory containing that file; a successful run prints `VERIFY_OK`. Midpoint quadrature at finitely many angles is a consistency test, not an independent proof of all-angle integral equalities, and neither test establishes novelty.

The result is limited to planar exact positive-definite quadratics with sequential exact minimizations. Safeguarded, approximate, noisy, and higher-dimensional analogues remain unproved.
