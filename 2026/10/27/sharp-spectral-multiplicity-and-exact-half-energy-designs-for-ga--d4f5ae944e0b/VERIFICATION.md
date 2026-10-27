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

The core analytic certificates are: (i) exact radial diagonalization, (ii) the endpoint integration-by-parts formula, (iii) the Rolle-induction zero count for distinct real exponentials, (iv) existence and sign orthogonality of the monic weighted \(L^1\) minimizer, (v) its exactly \(2m\) distinct positive roots, (vi) strict tail negativity after exhausting every possible zero of the endpoint exponential sum, and (vii) uniqueness by equality in the \(L^1\) triangle inequality. All are proved in `RESULT.md` without relying on finite searches.

Execute `python checker.py` using Python with NumPy and SciPy. The checker independently solves the truncated-gamma half-moment equations for the one-annulus and two-annulus cases. Its successful execution reported:

`VERIFY_OK cases=2 half_moment_checks=6 strict_tail_steps=26 difference_checks=28`

This evaluates six half-moment identities, 26 strict later-mode inequalities, and 28 instances of the exact difference formula. It does **not** numerically test every number of annuli, every spectral level, or all mode indices. No formal proof assistant, independent audit, or external certification has been used. No historical-priority claim is inferred from the numerical checks.
