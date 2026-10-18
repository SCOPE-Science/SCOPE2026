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

# Reproducibility and scope

Run `python verify_light_birth_covariance.py` in a standard Python environment. It computes the one-birth integrals exactly using `fractions.Fraction` for four finite-support lifetime laws, checks the directional overlap symmetry and verifies coefficients of \(\mathbb E T\), \(\mathbb E S\), \(\mathbb E(TS)\), and their covariance. Expected completion line: `PASS: all finite-support checks match the theorem exactly.`

The symbolic proof establishes the result for every positive bounded lifetime distribution with mean one, including laws not supported on finitely many points. The dominant quadratic-error bound uses total-progeny domination by Poisson-\(\lambda B\) offspring and does not follow from the finite tests. The result does not assert an exact formula at finite nonzero birth rate, nor does it establish statistical confidence intervals for data. Independent audit has not been performed.
