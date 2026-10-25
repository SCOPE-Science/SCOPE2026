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
# Reproducibility and boundaries

Run `python verify.py` with SymPy. The symbolic characteristic polynomial is evaluated exactly as a polynomial identity over the rational function field in two edge-cosine variables. Direct test configurations at six couplings verify the sine-flow equations and winding closure for all four mixed inverse-sine orientation choices at thirty interior parameter values, as well as the sink and source. The script checks the admissible singleton at the threshold. Its tests passed.

The proof's universal parameter claim depends on explicit sixteen-case branch exhaustiveness, the inverse-sine range bounds, and exact Jacobian algebra, not on the finite numerical test grid. No external independent mathematical audit has been performed.
