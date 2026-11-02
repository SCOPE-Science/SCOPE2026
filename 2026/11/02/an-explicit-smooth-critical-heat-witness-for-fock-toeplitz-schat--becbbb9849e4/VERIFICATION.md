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

# Verification of the constructive smooth endpoint witness

The accompanying `verify.py` passed 186 supplementary checks on finite rational moment arrays, numerical trace pairings, and the stated Schatten majorants. It deliberately uses a rational piecewise-uniform surrogate density to validate the moment algebra independently of the high derivatives in the chosen smooth bump. No exact smooth-bump derivative values or recursively huge centers are asserted to have been numerically computed.

The analytic proof in `RESULT.md` supplies the required infinite assertions: vanishing boundary terms for the fixed smooth bump, exact monomial moment formula, the \(\mathcal S_1\) tail bound, \(p>1\) summability for all real exponents, existence of every recursively selected center, coherent-state admissibility, Toeplitz covariance, exact heat peak formula, and off-center Gaussian separation. The final non-\(\mathcal S_1\) assertion uses the cited published trace-class endpoint estimate.

Run `python verify.py` with Python 3 standard library. The finite tests are supplementary consistency checks and not an independent audit or external certification. No higher-dimensional or optimal-growth claim is verified or made.
