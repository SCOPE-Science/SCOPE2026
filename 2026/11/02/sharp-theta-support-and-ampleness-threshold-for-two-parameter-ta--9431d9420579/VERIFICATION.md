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

## Computational reproduction
Run `python3 theta_checker13.py` with a Python 3 interpreter. It checks the simultaneous minimum of the exact valuation quadratics in all 2,268 parameter cases with \(1\le d\le7\), \(-4\le e,f\le4\), and \(1\le N\le4\). Expected output: `VERIFY_OK: 2,268 parameter quadruples, all exact integer valuation calculations`.

## Mathematical verification and limitations
Proof steps are the published Fourier recurrence, free theta normal form, two-sided adjacent integrality inequalities, special-fiber support, obstruction to ampleness and a fiberwise projective immersion in the strict chamber. Finite cases are not a certificate of the general result. No external independent audit or formal verification has been performed. The degeneration and cocycle are fixed as stated in RESULT.md.
