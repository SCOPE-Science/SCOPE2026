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

Execute `python3 verify.py` using Python 3 and the standard library. Completed run: `VERIFY_OK: 4 quadrature pairs, 2000 matrix trace identities, convex-risk tests`.

The program checks moments by numerical integration, traces by direct rotated-matrix calculations, common median/quantile crossing and representative increasing convex penalties. It is a finite computational diagnostic, not a certificate of convex order on every function. The rigorous universal comparison uses the beta CDF sign pattern, the stop-loss convex-order criterion, and convexity of the residual map. The derivation also assumes independent standard circular complex Gaussian entries and exact arithmetic.

No independent scientific validation has been performed.
