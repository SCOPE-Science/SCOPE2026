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

# Verification of mathematical claim

The analytic proof in `RESULT.md` is the basis for the infinite-parameter statement. To repeat the standalone finite arithmetic diagnostics, run `python3 verify.py` with Python 3.9 or later; it requires only Python's standard library. The script uses exact `fractions.Fraction` arithmetic for all discrete probe expectations and one-spike sign formulas, and separates those tests from explicitly approximate Gaussian Monte Carlo and deterministic beta-integral comparisons.

Observed execution from the packaged script: `PASS: 621 exact and numerical check groups`.

The finite code does not establish universal distributional optimality, almost-sure equality classifications or asymptotic rates. Those follow from the swap-symmetrization argument, strict positivity of the pair denominators, the chi-square/beta identity and the dominated-convergence proof in the result. The results are not independently audited.
