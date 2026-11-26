---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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
# Verification and reproducibility
`RESULT.md` gives the thin-QR reduction, the sharp dimension-free scalar bound, and an explicit extremizer of rank one when the budget is positive. At zero budget the only permissible perturbation is zero. The scalar replay in `RESULT.md` checks the rank distinction and the normalized loss directly.

Run `python3 checks/verify.py` with Python 3 and its standard library. The script uses orthonormal coordinates and computes errors from the normal equations by partial-pivot Gaussian elimination. The 48 scalar cases consist of 42 positive-budget rank-one examples and six zero-budget examples, followed by 1,200 feasible randomized matrices. The corrected expected marker is `PASS: 42 sharp rank-one cases; 6 zero-budget cases; 1200 randomized feasible matrices`. The original recorded marker lumped all 48 scalar cases into its rank-one count; the numerical loss tests are unchanged. These are finite numerical stress tests, not proofs of the theorem or evidence of originality.

The original result also reported a separate numerical suite using QR factorizations, least-squares solves, condition numbers up to \(10^6\), and 120 extremizer/1,200 feasible random perturbation instances. The separate suite is not required for the proof or the furnished replay.
