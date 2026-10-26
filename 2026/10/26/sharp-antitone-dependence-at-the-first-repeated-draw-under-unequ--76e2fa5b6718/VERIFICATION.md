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
# Verification evidence

The exact-rational verifier `collision_verifier.py` was run with Python 3 and completed successfully. It enumerates every ordered distinct initial sample followed by a matching draw, independently forms the generating-polynomial coefficients, checks the joint distribution, the optimal finite-support Newton coefficient and its equality behavior, all reverse-TP2 rectangles, and strict negative raw covariance.

The accompanying `verification_output.txt` records 140 passing weight vectors with \(2\le m\le6\). These checks are limited to enumerated finite cases and do **not** establish any universally quantified inequality by themselves. The general proof is the Stieltjes pole-interlacing, Newton inequality, and covariance argument in `RESULT.md`. Historical originality has not been independently confirmed.
