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

# Verification

The positive period-two exchange equations, the Floquet factorization via a coordinate interchange, the two exact quadratic Jury inequalities and the global monotonicity arguments are reconstructed in RESULT.md. They constitute the proof for the full parameter domain.

Run `python3 verify.py` with a standard Python 3 interpreter. The standalone script establishes exact rational inequalities for one orbit by bracketing the series for \(\log4\), verifies the exact swap log relations, and computes independent numerical consistency values for the unique critical coupling and several attraction windows. Numerical root finding and sampled stability checks only corroborate the analytical proof; they are not used to establish an infinite-parameter classification.

At a stability boundary, a unit-modulus multiplier prevents strict exponential attraction; the nonlinear stability and bifurcation type there have not been determined. A separate independent scientific audit has not been performed.
