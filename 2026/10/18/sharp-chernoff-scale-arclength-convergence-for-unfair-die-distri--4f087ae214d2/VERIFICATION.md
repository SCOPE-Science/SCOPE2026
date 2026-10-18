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
# Verification and reproducibility

The proof's essential analytical checks are the exact finite-length formula, the exponential likelihood tilt, strict positivity of the subdivision gain, the relevant nonarithmetic/lattice local limit theorem, and the beta-integral evaluation. They establish an infinite-parameter theorem. The standard local limit theorem is invoked, not rederived.

Run `python3 CHECK.py` to verify the exact finite-length formula two ways (ordered digit words and multinomial occupancy counts) for two examples, monotonic refinement of arclength, numerical normalization and centering of the tilt, the beta coefficient by independent quadrature, and a positive arithmetic lattice profile sample. The program uses only the Python standard library and reports checks that genuinely ran. Numeric agreement is corroboration and cannot replace the infinite proof.

The cases with zero digit weights or a fair die are excluded by the assumptions. Neither independently certified results nor external expert review are claimed.
