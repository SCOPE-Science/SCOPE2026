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

The submitted `verify.py` uses only the Python standard library. From the extracted package directory, run `python3 verify.py`.

Expected exact output:

`VERIFY_OK width_length_cases=288 base_support_cases=6 matrix_rank_identities=4 direct_assignments=74954`

The check computes all binary first-column seeds at widths one through four and lengths one through 72, verifies the recurrence-based weight counts and each vertex's closed-neighborhood parity equation, enumerates every finite-base subcode through independent span generation and deduplication, and checks prime patterns. A separate brute-force method enumerates all \(74{,}954\) binary arrays in the sixteen grids of dimensions at most \(4\times4\) to compare parity equation counts directly.

The general proof uses the identity \(F_p(B)=0\), invertibility of \(F_{p-1}(B)\), and reflection about all-zero separator columns, so no infinite-length claim is inferred from finite testing. The 2002 primary reference was not completely accessible, leaving historical-priority uncertainty; no independent audit has been performed.
