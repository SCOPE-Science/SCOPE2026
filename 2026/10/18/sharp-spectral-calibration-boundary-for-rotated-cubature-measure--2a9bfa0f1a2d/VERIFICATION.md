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

## Reproducible checks

The attached standalone `verify.py` requires NumPy and invokes sign-paired cubature directly on random symmetric quadratic sensors for state dimensions two through eight. It checks predicted means, innovation and cross covariances, conditional-error-free **unconditional** actual-minus-reported covariance identities, extremal constant-diagonal frames, eigenframe upper bounds, and strict/boundary/impossible calibration examples.

Run `python verify.py`. On the accompanying tested environment it passed **2,210** assertions or grouped checks, and a replay after extraction should produce the same reported check total. The finite checker is evidence of consistency, not an infinite classification proof; that proof is contained in `RESULT.md`.

No independent scientific audit or external certification has been performed.
