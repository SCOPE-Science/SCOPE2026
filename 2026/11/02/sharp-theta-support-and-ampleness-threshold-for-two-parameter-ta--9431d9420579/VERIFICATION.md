---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
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
Proof steps are the published Fourier recurrence, free theta normal form, algebraicity of the basis by rank and codimension-one regularity, two-sided adjacent integrality inequalities, special-fiber support, and the resulting obstruction to ampleness outside the strict chamber. In the strict chamber, the global section morphism is separated and quasi-finite, so ampleness follows by quasi-affine pullback. Finite cases are not a certificate of the general result. The degeneration and cocycle are fixed as stated in RESULT.md.
