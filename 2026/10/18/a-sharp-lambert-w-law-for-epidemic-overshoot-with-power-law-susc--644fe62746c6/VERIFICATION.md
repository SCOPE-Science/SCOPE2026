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

## Reproducibility

Run `python3 verify.py` using the supplied standard-library script. It computes finite-dimensional numerical maximizers from the exact final-size formula, tests the exact quadratic optimum, compares the cubic optimum to the previously published reference value, checks strict order at seven sampled exponents, tests the final-size identity on 196 grid pairs, and checks the Lambert-function asymptotic discrepancies at four large exponents.

Observed completion: `PASS: power-incidence overshoot checks`.

## Proven and unproved boundaries

The proof in RESULT.md applies to every real exponent \(p\ge2\) and gives a true asymptotic as \(p\to\infty\). Finite samples cannot certify either infinite quantifier. Numerical optimization is used only for supplementary consistency checks, not for the analytical theorem. The study does not establish universality for heterogeneous, stochastic, controlled, or finite-seed epidemics. Independent assessment has not been performed.
