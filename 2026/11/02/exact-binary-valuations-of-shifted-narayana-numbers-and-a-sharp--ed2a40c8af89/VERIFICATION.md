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

# Reproducible checks and limitations

Run `python3 verify.py` with Python 3 and only the standard library. It checks the exact seventh and fourteenth companion-matrix powers, both odd increment coefficients, and a separate modulo-eight increment needed for the isolated residue class. The program computes 100001 terms of the recurrence modulo \(2^{24}\), compares their exact binary valuations with the proposed all-index formula, and cross-checks 101 matrix-powered indices. It then evaluates all residues of the finite counting-discrepancy periods with rational arithmetic and verifies nineteen higher-level congruence representatives.

Observed output:

`VERIFY_OK matrix_powers=2 recurrence_terms=100001 matrix_cross_checks=101 sharp_discrepancy_levels=3 higher_levels=19`

The all-index proof and uniform discrepancy theorem depend on the algebraic arguments in `RESULT.md`, not on finite extrapolation. Nothing here constitutes independent validation.
