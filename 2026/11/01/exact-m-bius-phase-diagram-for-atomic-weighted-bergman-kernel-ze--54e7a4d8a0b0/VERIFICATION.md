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

# Finite computational checks and proof boundaries

Execute `python check.py` with Python 3 and its standard library. A completed execution reported 2,491 deterministic assertions passed. The checks cover independent power-series reconstruction of the kernel, Möbius factorization at fractional exponents, scalar zero equations, complete index counts, selected contour winding numbers with safe sampling radius, strict crossings at entry thresholds, derivative estimates, and valid disk-pair realization.

The infinite claims are established analytically in `RESULT.md`: direct rank-one kernel calculation; conformal factorization; principal-logarithm branch exhaustion; strict disk-membership inequalities; and exact integer counting. Numerical winding tests do not establish the global count and do not substitute for the analytical proof. Independently certified proof or validation has not been supplied.
