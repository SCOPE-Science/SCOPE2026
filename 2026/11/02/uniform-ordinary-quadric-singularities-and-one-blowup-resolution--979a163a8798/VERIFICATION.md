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

# Reproducibility and scope

Run `python3 verify_pencil_normal_forms.py` using the included standalone file. The Python standard library suffices. The script computes exact integer-polynomial identities for 432 choices of block partitions, pivot blocks and dual coordinate charts, checking the original two-equation ideal reduces to the split quadratic and that the proposed triangular coordinate inverses are exact. It additionally exhaustively checks points and Jacobian ranks over \(\mathbb F_3\) for the seven partitions \((2),(1,1),(3),(1,2),(1,1,1),(4),(2,2)\), with corresponding scroll counts \(4,16,4,16,52,4,16\). The successful final line is `ALL_CANONICAL_PENCIL_TESTS_PASS`.

These are genuinely finite verifications. The all-ranks/all-partitions result follows instead from the variable-elimination and inverse-coordinate proof in RESULT.md. In particular, characteristic zero is the scope of the singularity classification and discrepancy assertions; the \(\mathbb F_3\) checks are supplementary examples rather than an extension of the stated theorem. The resolution and terminality deductions use standard blowup and adjunction formulas, not machine certification. Independent validation is not performed.
