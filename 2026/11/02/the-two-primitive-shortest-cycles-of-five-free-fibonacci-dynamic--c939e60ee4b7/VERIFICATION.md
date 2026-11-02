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

# Reproducibility and verification

Execute `python3 verify.py` in the directory containing the extracted package. The program uses only the Python 3 standard library and exact integer or rational arithmetic. It checks the full signed determinant expansion over all \(720\) permutations, the \(17\) nonempty independent sets on a six-cycle, the twelve modulo-five division supports, the equality at the minimal possible positive exponents, the strict one-step monotonicity inequality for each divided coordinate, and the rank-five rational recurrence matrices for each surviving support. It independently verifies both primitive cycles, their valuations, and that their twelve rotations produce all candidate signatures.

Expected terminal prefix: `VERIFY_OK signed_determinant_terms=20 division_supports=12 primitive_rotation_classes=2 kernel_rank=5`.

The checker does not search all unbounded initial pairs or all arbitrarily large valuation exponents. Those are handled mathematically by modulo-five reduction and strict monotonicity; the finite checker validates the critical symbolic identity and the finite support case analysis. No independent audit or formal-machine certification has been performed.
