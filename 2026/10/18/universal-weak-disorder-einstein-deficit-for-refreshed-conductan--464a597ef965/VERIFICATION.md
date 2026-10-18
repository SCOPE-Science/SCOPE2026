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

The proof derives the two response coefficients from the spectral-gap resolvent, the stationary-environment density, and a martingale corrector with both walker and refresh jumps. The Fourier cancellations reduce the result to the exact one-dimensional lattice Green integral.

`verify.py` executes independent high-precision quadratures and solves finite-state linear systems for the dynamic environment on a periodic lattice. It tests the normalization and second-order approximation but does not by itself certify any infinite-lattice limit. Its only nonstandard dependencies are listed in `requirements.txt`.

The claim assumes bounded symmetric marks and fixed positive refresh rate. No independent audit or expert certification has been performed.
