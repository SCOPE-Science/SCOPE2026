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

Use the standard Euclidean norm on \(\mathbb C^2\), the bi-infinite supremum norm on the forcing and orbit sequence spaces, and the definitions in `RESULT.md`. To reproduce the finite rational coefficient checks, execute `python3 verify_bounds.py` with Python 3. The script prints `RATIONAL_BOUNDS_OK` after verifying the concavity sign, both endpoint products, the exact \(56/39\) finite lower bound and its strict squared comparison with \(2\). That execution succeeded on the included script.

The following assertions are proved analytically, not certified by this finite checker: absolute convergence and uniqueness of the Green inverse, the two-sided bound on its operator norm, the unit-circle resolvent bound for all \(K>0\), and the asymptotic ratio \(2-\varepsilon\) for fixed \(\varepsilon\). The bounds and proof steps are reproduced in `RESULT.md` without external dependencies. An exact finite-\(K\) shadowability value is neither computed nor required; universal optimality among nonnormal operators is not claimed. The publisher preview for one earlier quantitative-shadowing source did not provide its complete body, which remains a specific literature risk.
