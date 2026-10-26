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

# Verification and reproducibility

The continuum theorem is proved in `RESULT.md`; the optional standalone `verify.py` checks its formulas numerically with deterministic pseudorandom samples. It uses Python 3 with NumPy and SciPy, and can be run from a folder containing the extracted files by executing:

```sh
python verify.py
```

Actual check output:

```text
PASS: 826 fixed-wavenumber, 681 full-optimum, 400 height-order families, 6 limit checks (some extreme parameter samples skipped for conditioning).
```

In detail, the checker compares (i) the closed optimum denominator and heavy-layer depth against direct two-fluid cotangent values and one-dimensional bounded minimization; (ii) the analytic unique fastest wavenumber against a separate bounded scalar maximization of the unoptimized physical dispersion; (iii) the strict equal-depth deficit, the location interval, and the variation of the optimum with total height; and (iv) the leading shallow and deep asymptotic limits for a specified asymmetric density pair.

Extreme random draws with dimensionless height–wavenumber product outside the well-conditioned numerical comparison range are not counted as tests. The checker suppresses the common positive surface-tension factor in growth rates and works with the normalized cutoff parameter; this does not change any maximizer. Numerical sampling does not prove the all-parameter inequalities or uniqueness, which follow from the written analytic arguments.

Scientific limitation: results describe a linear inviscid two-fluid problem between rigid parallel walls, not viscous, finite-width, or nonlinear physical systems. The source-priority comparison remains historically incomplete for the 1990 parent paper.
