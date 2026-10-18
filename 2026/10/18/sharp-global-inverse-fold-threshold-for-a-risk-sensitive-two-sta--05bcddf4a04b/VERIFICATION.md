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

The proof in `RESULT.md` establishes the exact inverse reduction, the full real-plane inverse-fiber count, and physical injectivity by monotonicity/continuity. The standalone checker `check_inverse_geometry.py` uses Python 3, SymPy, and SciPy and performs two symbolic validations plus 436 seeded finite numerical diagnostics. Execute `python check_inverse_geometry.py` from the package directory. These tests sample neither all parameters nor all roots at infinitely many levels; completeness is supplied by the analytic monotonicity proof.

The smooth global inverse is claimed only for \(B<4\); the \(B=4\) map is injective but singular at the critical line. The extended three-inverse image count is separate from admissible physical image multiplicity. No independent audit has been performed.
