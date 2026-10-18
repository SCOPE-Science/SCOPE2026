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
# Reproduction and proof-boundary checks

Run `python3 verify.py` with a standard Python 3 installation. The expected exact output is `VERIFY_OK 2716 finite scores/integral/argmax comparisons`. Tests independently validate the hopping-matrix eigenvector residuals, recalculate normalized finite-chain positional moments for multiple biases and modes, compare independently summed Fisher scores, check endpoint-mode reflection, compare Riemann and oscillatory limits, and verify a dense range of mode-order inequalities.

Analytical verification requires: direct differentiation of the normalized right eigenstate, the three weighted Riemann moments, a uniform Abel/summation-by-parts bound for nonzero discrete frequencies, exact evaluation of the partition integral, differentiation of its logarithm, and strict maximizer comparison. Every one of these steps is shown in RESULT.md. Finite checks do not prove convergence for arbitrary modes or the exact eventual argmax; that conclusion is analytically established. The mode-location assertion at equality is deliberately not made. External independent validation was not performed.
