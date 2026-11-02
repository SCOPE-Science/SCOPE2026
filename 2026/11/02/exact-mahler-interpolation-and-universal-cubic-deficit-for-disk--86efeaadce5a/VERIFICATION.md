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

Run `python3 check.py` with the Python 3 standard library. In the recorded execution the checker printed `PASS 417 independent area/polar, monotonicity, endpoints and large-n comparisons`.

The checker constructs polygon-plus-circle convex hulls numerically, integrates a radial area independently, and compares these with the exact formulas. It also checks endpoint and large-sided expansions for representative parameters. Geometric circle discretization introduces controlled approximation error in the checks; it is not part of the analytical proof.

The complete proof is contained in `RESULT.md`; checking a finite sample does not verify a universal quantified statement. The priority comparison does not constitute independent historical certification. No independent audit has been performed.
