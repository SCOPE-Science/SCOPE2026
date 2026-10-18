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

# Verification of the extremal-run census

The proof in RESULT.md establishes the infinite claims for each fixed integer base at least three. The finite checker verifies, independently of the claimed Fourier sum, all eight tested digit-length shells for each of ten bases, actual membership of tested consecutive integer blocks by computing all nonzero-digit products, and the necessity and sufficiency of predicted starts in the tested complete ranges.

Run `python verify.py` using only a standard Python 3 installation. The successful replay prints ten PASS entries and a final `VERIFIED 80 shell counts` line. Arithmetic membership and shell totals are exact integers; a floating-point bound check is merely a numerical consistency check, not the proof of the error estimate. The full universal error inequality follows instead from the explicit Fourier argument.

Known limits: no independent audit, no general count of shorter blocks, no uniformity as the base varies, and no claim of a global fixed leading constant. The underlying maximum-run boundary theorem is cited to Gohn et al. (2022) rather than reproved.
