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

The standalone `verification.py` uses Python's standard library `fractions.Fraction` and `math.factorial`. Run `python verification.py` to reproduce 670 assertions using exact rational arithmetic: the first six coefficients of the characteristic function, both trace normalizations, a rigorous tail bound and sign bracket for its first positive root, the negative derivative on the first unit interval, exact row and column Gram identities for four rational parameter values, and continuous-limit trace moments.

The analytic theorem requires the written Hilbert–Schmidt step-kernel estimate, the compact singular-value perturbation inequality, and the fourth-order eigenvalue/entire-determinant boundary equivalence. The finite checker does not replace those infinite-dimensional arguments. The bracket for the first zero is certified only at four decimal places; the longer decimal in the text is approximate.

The relevant recent primary manuscript was accessible only in part, and the priority comparison is therefore qualified. No independently conducted mathematical audit is claimed. The characteristic equation does not separately assert equality of analytic zero multiplicity with singular eigenspace dimension, and no sharp large-index root asymptotic is claimed.
