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
# Verification record

The analytical polynomial identities were reconstructed with exact rational arithmetic. The unique root enclosure \(53/10<w_\star<11/2\) follows from exact signed polynomial evaluations and strict monotonicity on \(w>3\). The residual exponent bound is proved by pointwise positivity of the normalized logarithmic integrand and integration; no finite set of exponent tests substitutes for that quantifier.

The accompanying `verify.py` rechecks the Runge–Kutta polynomial and derivative identities, the unit-circle polynomial, the algebraic lower bound for \(\mu\), and illustrative quadrature/finite-difference consistency for \(p=1,2,4\). Run `python3 verify.py`. Tests at finitely many exponents and gains are not exhaustive; the written proof establishes the general statement.

The scientific comparison credits the original central Hermite estimator, special analytic \(L^2\) formula, and numerical instability results. Previously unknown equivalent literature cannot be excluded by finite literature searches. Independent audit has not been performed.
