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

The standard-library script `check.py` performs three separate comparisons: (1) twenty exact rational checks of the Fourier digit-congruence sum against the two-state carry matrix; (2) thirty-five direct finite-group trigonometric averages against the same matrix; (3) four subcritical energy series and Perron-eigenvalue asymptotic checks. It also verifies the Haar and point-mass endpoint formulas. Execution command: `python3 check.py` from the directory containing the script. Observed result: all checks passed.

The exact rational portion includes amplitudes \(1/4\), \(1/2\), \(3/4\), and \(1\), at levels \(1\) through \(5\). The trigonometric portion uses five amplitudes and levels \(1\) through \(7\). The energy checks use the parameter range \(1/8\) through \(3/4\), at a subcritical exponent.

The proof of the global assertions does not depend on floating-point checks. Character orthogonality proves the finite-level matrix for all levels and real \(0<a<1\); Cayley–Hamilton and positivity prove its asymptotics; Tonelli and a geometric series prove convergence, divergence and the exact critical coefficient. No exhaustive infinite computation or external validation is claimed. Scientific priority is limited by incomplete access to an earlier dyadic Riesz-product manuscript.
