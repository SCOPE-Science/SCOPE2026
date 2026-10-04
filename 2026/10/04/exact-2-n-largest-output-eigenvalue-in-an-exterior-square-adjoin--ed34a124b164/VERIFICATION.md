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
The all-\(n\) theorem is established by the analytic proof in `RESULT.md`. The bundled `artifacts/verify.py` was replayed from the packaged bytes and returned `VERIFY_OK`.

The checker uses exact rational arithmetic to verify, for \(5\le n\le12\), the sharp diagonal witness ratio \(2/n\), the Hilbert--Schmidt scale factor \(n-2\), the coherent partial-isometry ratio \(1/(n-2)\), the positive gap, and the Slater transition-matrix projection norm. It also checks representative rational instances of the sum-of-squares identity in the transition estimate. These checks do not exhaust infinitely many dimensions or replace the proof.

Independent audit has not been performed.
