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

# Verification notes

The proof uses exact finite-group combinatorics, not numerical approximation. The critical points checked in `check_signatures.py` are the phase-to-permutation bijection, the alternative full-signature construction, the complete row-matching reconstruction, and the maximal prime-power fibre for \(n\in\{4,8,9,16,25\}\). Every verification run uses the standalone script in this package. Exhaustive cycle counts additionally cover \(n\in\{4,6,8,9\}\), with a distinct phase-order enumeration at \(n=9\). The script reports `ALL_CHECKS_PASSED`.

No finite experiment proves the theorem at arbitrary length. That scope is covered by the analytic stabilizer argument, the nested-subgroup suffix-translation construction, and the mixed-prime obstruction in `RESULT.md`. No exact mixed-prime extremal formula or classification of all realizable signature tables is asserted. External independent verification has not been performed.
