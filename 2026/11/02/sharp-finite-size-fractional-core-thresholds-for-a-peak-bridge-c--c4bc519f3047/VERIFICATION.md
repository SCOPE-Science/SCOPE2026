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

The exact expressions are proved by explicit primal constructions, positive normalized dual weights, and a decomposition of any coalition into contiguous blocks. The checker `verification/check_path_frontier.py` is included for reproducibility.

Executed checks: `python verification/check_path_frontier.py` returned `VERIFY_OK exact_primal_dual=80 numerical_coalition_LPs=2505`. The exact-rational portion verifies candidate caps, budget equality, every voter's attained utility, the dual inequalities, and monotonicity on populations up to sixteen across five rational bridge values. SciPy's HiGHS routine independently evaluates every coalition for population sizes two through eight at the same five values. This finite verification cannot establish a statement over all real values; the analytical proof establishes that.

Requirements: Python 3 and SciPy for the finite linear-programming cross-check. The exact fraction checks use only the Python standard library. The bridge utilities in the cross-check are rational approximations, not the full real domain.

No external independent audit has been performed.
