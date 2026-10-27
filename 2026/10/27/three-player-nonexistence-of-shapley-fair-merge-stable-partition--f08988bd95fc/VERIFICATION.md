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

# Verification

Run `python3 verify_sfms.py` from the extracted package directory. The checker has no external dependencies; it enumerates all three-person coalitions and all five partitions, independently computes their exact Shapley payoffs through the permutation definition, tests all SFMS conditions, and checks the split-merge update and decrease of \((-\Psi,\Phi)\). All checks completed successfully in exact rational arithmetic in the preparation environment.

The universal one/two-player assertion is a symbolic two-case proof in `RESULT.md`, not an extrapolation from finite enumeration. The game is nonmonotone, so the evidence does not extend to monotone characteristic functions. No independent scientific audit has been performed.
