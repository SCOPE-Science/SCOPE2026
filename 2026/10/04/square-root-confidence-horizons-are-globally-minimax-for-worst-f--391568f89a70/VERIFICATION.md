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

The analytic verification is the event inclusion in RESULT.md. For any admissible boundary \(g\), its worst fixed-time-relative ratio \(K\) implies the deterministic pointwise envelope \(g(s)\le K z_\alpha\sqrt{s}\). Therefore simultaneous coverage by \(g\) cannot exceed that of its square-root envelope, which forces the stated quantile lower bound. The square-root boundary attains that lower bound by construction.

`verify_boundary.py` checks the pointwise envelope and constant-relative-width identities on representative power and non-power shapes. It is a finite arithmetic sanity check only. No finite grid or simulation is used as proof of the continuous Brownian statement.

Scientific limits: Brownian/asymptotic calibration; deterministic pre-specified boundaries; worst fixed-time-relative half-width criterion; no finite-sample or uniqueness assertion.
