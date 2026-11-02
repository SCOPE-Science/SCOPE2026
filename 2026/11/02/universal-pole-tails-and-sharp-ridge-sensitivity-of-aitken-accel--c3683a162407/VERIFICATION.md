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

# Reproducibility

Run `python3 verify.py` with Python 3.9 or newer and the standard library only. The test verifies all three exact mean-to-Aitken algebraic reductions at positive sample points, exact rational polynomial integrations for powers two and four, and exact constants for the \(\chi^2_2\) probe law.

A fixed-seed Monte Carlo calculation samples the \(\chi^2_2\) energies as exponential random variables and compares \(t\Pr\{|T-2|>t\}\) with \(27/128\) at a moderate threshold. It also confirms the broad approach of \(\delta\mathbb E[(T_\delta-2)^2]\) toward \(243\pi/512\). Monte Carlo cannot establish either distributional limit: those follow from the density and approximate-identity proof in RESULT.md.

The general theorem assumes a nonzero fixed positive-semidefinite matrix and four independent standard Gaussian vectors. The exact constants and verification scripts are reproducible independently of any external data set. Uncertainties about publication priority are separately discussed in REVIEW.md.
