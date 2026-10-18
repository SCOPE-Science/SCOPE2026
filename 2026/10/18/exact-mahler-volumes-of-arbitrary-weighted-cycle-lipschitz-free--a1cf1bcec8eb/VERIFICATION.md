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
# Reproducibility

Run `python check_cycle.py` with Python 3, NumPy, and SciPy installed. The file includes eleven specified rational edge-length lists of sizes 3 through 6. It constructs primal signed edge-molecule points and dual feasible-gradient intersection vertices, uses convex-hull triangulations, and evaluates simplex determinants with rational arithmetic. It then checks both formula volumes separately against the resulting triangulated volumes and prints `ALL EXACT WEIGHTED CYCLE MAHLER TESTS PASSED` when every comparison succeeds.

This confirms eleven finite test cases. It does not establish the formulas in arbitrary dimension, does not rely on a rigorous exact-predicate hull algorithm, and is not an independent scientific audit. The general proof, including the simultaneous-resonance limit and uniform-cycle asymptotic, is presented in RESULT.md.
