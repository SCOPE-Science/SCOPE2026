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

`verify.py` enumerates RREF subspaces of the nilpotent ideal in selected prime-characteristic examples and tests closure under its actual multiplication. It compares the resulting coefficient counts against the counting inputs and separately checks isotropic subspace numbers. The finite test is a check of the counting inputs, not of the large-dimension probability statements.

The orthogonal quotient recurrence in `RESULT.md` supplies the counts for every odd prime power. The rarity estimate and dimension limits follow from uniform product bounds and discrete-Gaussian summation at fixed \(q\); no scale extrapolation from the finite checks is used.
