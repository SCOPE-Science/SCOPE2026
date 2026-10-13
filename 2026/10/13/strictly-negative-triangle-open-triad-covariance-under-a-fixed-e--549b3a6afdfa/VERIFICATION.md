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

# Reproducible mathematical checks

Run `python3 verify.py` with Python 3 and no third-party packages. The checker constructs exact rational mixed moments from triangle/two-star overlap classes and compares them to the factored formula, including edge-count degeneracies. It independently exhausts all labeled graphs on four through six vertices, groups by edge count, and compares the empirical exact-rational covariances. Further exact-rational evaluations confirm the independent-edge identity by binomial mixtures and check the predicted sign for parameter grids.

The universal proof is the combinatorial overlap identity and a finite algebraic simplification combined with a positivity argument; exhaustive graph enumeration through six vertices cannot prove universal correctness. The dense limiting statement is established by asymptotic analysis, not by numeric convergence checks. The code contains no third-party works or scientific claims of independence beyond its own finite calculations.
