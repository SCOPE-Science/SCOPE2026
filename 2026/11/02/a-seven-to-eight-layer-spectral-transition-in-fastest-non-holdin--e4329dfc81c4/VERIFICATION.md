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

The exact infinite-family result follows from group averaging, an explicit two-factor Fourier decomposition, and minimization of the maximum of three affine functions; no empirical enumeration is used as a substitute for these steps. A checker is included as `verify_cyclic_layers.py`. Execute `python verify_cyclic_layers.py` in an environment with NumPy and SciPy.

The checked run reported `VERIFY_OK: 1716 scalar optimizations; 48 full matrix spectra; 225 asymmetric feasible perturbations; exact small rational values.` The scalar sweep tests all integer pairs with \(3\leq n\leq80\) and \(2\leq m\leq23\); the full-matrix spectrum checks cover \(3\leq n\leq10\), \(2\leq m\leq7\). Asymmetric perturbations are constructed in the nullspace of every row-sum constraint, so they preserve the zero diagonal, symmetric support and row sums; nonnegativity is checked. A small test evaluates the exact rational case \((n,m)=(3,6)\), and another checks the \((3,3)\) plateau boundaries.

Computations run in floating point except for the rational assertions; their finite coverage and tolerance are explicit in the script. They do not independently verify the group-averaging theorem or originality priority. Theoretical formulas, hypotheses, and proof are in `RESULT.md`.
