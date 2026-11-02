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

# Reproduction and scope

Run `python verify6harvest.py` with SymPy installed. The script independently constructs all three six-step projective matrices, checks the exact determinant, trace-difference polynomial identities, zero-harvest baseline, and the two-consecutive-low extinction bound. It then verifies exact rational brackets for a concrete parameter triple. This is a finite reproducibility and symbolic-identity check, not an independent scientific audit or a proof of historical priority.

The all-positive-parameter result is established mathematically in `RESULT.md`. Numeric brackets illustrate the theorem; no exhaustive parameter enumeration is asserted. The model ignores demographic noise and larger environmental periods.
