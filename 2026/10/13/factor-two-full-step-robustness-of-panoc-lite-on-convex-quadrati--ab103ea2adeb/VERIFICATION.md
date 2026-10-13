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

The proof in `RESULT.md` is analytic.

`artifacts/verify_panoc_lite_quadratic.py` uses exact rational arithmetic to check a two-dimensional example with noncommuting positive-semidefinite smooth and nonsmooth Hessians. The tested stepsize lies strictly above \(1/L_f\). The script verifies the affine normal residual, exact Newton displacement, the scaled-candidate identity, and the PANOC-lite full-step inequality for \(\theta\in\{0,1/2,1,3/2,2\}\).

The same script checks legal scalar source parameters for which \(\theta=-1/2\) and \(\theta=5/2\) both fail the full-step test.

These computations support the proof; the universal interval and its sharpness follow from the symbolic identities in `RESULT.md`.
