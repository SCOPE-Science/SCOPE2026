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

# Reproducibility and limitations

Run `python3 verify_robust_book.py` using Python 3. The script uses standard-library exact rational arithmetic to compute all edge-deleted Laplacian cofactors and compare them to both symbolic closed forms, checks all three price regimes at rational parameters, and tests strict losses under budget-preserving asymmetric edge changes. It prints its total number of successful assertions and raises an exception on failure.

The universal theorem is proved in `RESULT.md`, including symmetry reduction, boundary derivatives, strict concavity, and uniqueness. Finite determinant checks alone cannot certify assertions for all integers or all positive real prices and budgets; no independent external mathematical validation has been performed.
