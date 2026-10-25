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

Execute `python verify.py` with Python 3 and `mpmath`. The program sets 90 decimal digits, brackets and bisects the strictly positive crossover, independently evaluates the cosh ratio and addition-law form, checks equality to the zero-reset queue boundary, checks nearby signs, and verifies dimensionless invariance for matched physical parameters. It passed all 13 root cases (server counts \(1\) through \(10^{10}\)) and eight physical-unit rescalings at four server counts. These finite checks are corroboration only and cannot prove a limit as \(c	o\infty\).

The exact analytical proof is in `RESULT.md`: the first nonzero Taylor term provides a negative sign, the exponential tail gives a positive sign, and every root is shown to lie on the same diverging branch before asymptotic inversion. Numerical root values are deliberately not extrapolated into a uniqueness assertion.

Scope: finite reflecting interval, single absorbing endpoint, independent Poisson resets to the starting point, instantaneous captures, positive fixed physical coefficients and increasing integer server count. Any uninspected prior work on uniform moving-boundary high-reset asymptotics is a residual priority risk.
