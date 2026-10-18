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

# Computational and analytical verification

Use `python verify.py` with Python 3, SymPy and mpmath. The standalone source verifies exact symbolic Gaussian posterior-mean variances for every feasible one- or two-sensor set; exact conditional second-reading variances; a closed Gaussian upper-tail formula against separately integrated high-precision quadrature; strict separation and sharp maximum across positive noise levels and competing goal coefficients; and the predicted derivative signs on both sides of the threshold. Results are deterministic.

The code is a finite consistency checker. The universal claims about every positive noise variance and amplitude, all measurable second-stage policies, strict inequalities and the unique sharp ratio follow instead from the proof's dynamic-programming exhaustion, conditional Gaussian independence, integration by parts and exact monotonicity identities. Neither a limited parameter grid nor a numerical calculation is an infinite proof. No independent scientific audit has been performed.
