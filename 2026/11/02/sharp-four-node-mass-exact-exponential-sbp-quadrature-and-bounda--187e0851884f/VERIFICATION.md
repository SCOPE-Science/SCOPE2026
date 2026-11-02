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

## Reproduction
Extract `verify.py` from the same record and run `python verify.py` with Python 3.11+ and the standard library. The program uses 95-digit `decimal` arithmetic, reconstructs the symmetric nodes/weights, evaluates all five moment conditions on nine scale parameters, solves the six-coefficient skew matrix extension system afresh on each, checks the exact differentiated basis and SBP matrix identity, tests positivity and mass discrepancy of the separate three-node derivative-product quadrature, then reports four large-frequency endpoint-layer diagnostics.

An executed run produced `PASS: exact-exponential moments, positive weights, four-point SBP matrices, three-point mass defect, asymptotic trends`. Across the nine frequencies the maximum displayed relative moment discrepancy was below \(2\times10^{-94}\); the skew-system residuals were below \(2\times10^{-90}\). Finite numerical computations cannot prove the theorem for all \(\lambda>0\); its proof is in `RESULT.md`.

## Exact proof components
The nonnegative exponential-polynomial witness proves the no-three-node claim for every interior node position, with or without positive weights. The strict variance identity guarantees the formulas are admissible for every real \(\lambda>0\); first/second moment matching establishes exactness, and the constructed skew extension establishes the FSBP matrix property. The endpoint-layer coefficient is obtained analytically from the leading hyperbolic moments, not estimated by finite regression.

## Limits
No external or independent audit has been performed. The checks do not certify numerical conditioning, arbitrary precision implementations, unknown prior art, or broader PDE behavior.
