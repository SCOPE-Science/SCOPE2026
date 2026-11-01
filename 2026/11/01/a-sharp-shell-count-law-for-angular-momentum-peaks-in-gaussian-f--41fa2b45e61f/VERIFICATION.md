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

## Analytical verification

The eigenvalues are the Gamma\((n+d,1)\) probabilities of a finite union of intervals. Their consecutive difference is exactly the signed endpoint exponential sum divided by \(\Gamma(n+d+1)\). The ordered endpoint coefficients alternate, and a generalized Descartes induction limits the number of real sign changes. The first sign is positive and the terminal sign negative, yielding the stated strict peak budget. The fixed-mass construction holds the Gamma\((d,1)\) probability exactly equal to any prescribed \(p\in(0,1)\), while shells at \(R\pm\sqrt R\) have strict degree peaks at \(n=R-d\) for sufficiently separated integer scales.

## Reproduction

Run `python check_shell_modes.py` with Python 3, NumPy and SciPy. In the reviewed version the script passed 422 finite integral, endpoint-difference, logarithmic-mean and fixed-mass peak assertions for sampled dimensions and shells. These finite checks corroborate, but do not certify, the universal analytic theorem.

## Limits

No independent audit or validation has been conducted. The proof addresses only analytic Gaussian Fock space and finitely many strictly separated positive-radius full annuli. The priority comparison does not establish global historical uniqueness, and does not extend to arbitrary radial, signed, or nonradial symbols.
