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

# Reproducibility and verification

The analytic proof in `RESULT.md` establishes the exact support boundary for every integer \(n\ge3\), every budget \(B>0\), and every relative price \(r>0\). Finite numerical tests are supporting evidence only. The script `verify_cycle.py` uses NumPy, SciPy, and SymPy and is run with `python verify_cycle.py`; `VERIFICATION_OUTPUT.txt` records a successful run.

Checks independently evaluate Kirchhoff index by Laplacian inversion and by sum-over-pairs electrical series/parallel arc reduction; compare exact derivatives and critical-price formulas; confirm exact symbolic formulas at \(n=3,4\); compare constrained full-dimensional numerical optimizations at selected prices above and below the critical price; and inspect the asymptotic normalized threshold numerically. These tests are not exhaustive over the continuum of parameters and do not replace the strict-convexity proof, the zero-ordinary-edge exclusion, or the improper Riemann-sum argument.

The optimization comparisons use floating-point tolerances. No independent mathematical audit or external certification has been conducted.
