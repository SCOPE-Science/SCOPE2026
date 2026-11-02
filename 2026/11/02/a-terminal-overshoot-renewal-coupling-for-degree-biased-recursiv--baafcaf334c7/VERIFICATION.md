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

Run `python3 verify.py` in the directory containing this file and the other embedded package files. The script requires Python 3 and no external packages. It uses exact `fractions.Fraction` arithmetic to check the harmonic-tail identity, normalization and full-deletion atom, the conditional overshoot mixture, and independent recursive probability distributions for the cutting and renewal counts for finite state sizes.

The analytic proof, especially the terminal-residual bound, the infinite-mean lattice renewal theorem and the weak law from truncated increments, is presented in `RESULT.md`. Exact finite checks support the algebra but do not prove the all-size statements. This package does not supply an independent mathematical audit, a quantitative total-variation convergence rate, an expectation asymptotic or a second-order fluctuation law.
