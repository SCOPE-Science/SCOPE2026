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

# Reproducible verification

Run `python verify.py` with Python 3.10 or newer. It uses only the Python standard library. It directly evaluates the finite-atomic optimizers, Chebyshev recurrence, and concave envelope for sizes \(2\le n\le40\), multiple endpoint and interior calibrations, and randomized finite-support phase laws. It checks that the sampled rates never lie below the stated sharp bound and confirms the quadratic activation coefficient and the QFI expression on the effective GHZ two-level state.

The verification is finite and subject to floating-point tolerance. It cannot certify Jensen's inequality for every Borel measure, the global quantum Fisher-information formula beyond the specified GHZ subspace, or novelty. The exact analytic proof in `RESULT.md` supplies the universal argument. No external independent audit has been performed.
