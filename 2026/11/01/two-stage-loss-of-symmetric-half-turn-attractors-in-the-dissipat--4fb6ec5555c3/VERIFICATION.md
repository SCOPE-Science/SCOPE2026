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

# Reproducible verification

Execute `python verify.py` with Python 3, SymPy and NumPy. The script was executed directly from the candidate package before acceptance and checked six symbolic algebra families plus 48 two-cycle orbits for representative parameter cases. The assertions recompute both iterates and their full Jacobians. All assertions passed.

Analytic coverage, not supplied by finite tests, consists of exact symmetry reduction, a cubic forcing maximum, Schur inequalities for a two-by-two return matrix, monotonicity of a rational function in the squared phase sine, and a strict algebraic ordering identity. Each of these steps is written and justified in RESULT.md.

The checks do not certify global dynamics, off-symmetry periodic orbits, or independent validation.
