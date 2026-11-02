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

The mathematical proof is provided in `RESULT.md`; no numerical program is invoked as a substitute for the infinite-limit or central-limit arguments. Reproduce the finite checks by running `python3 checker.py` with a standard Python 3 interpreter and comparing its output to `checker_output.txt`.

The checker independently enumerates the small independent-Bernoulli laws as exact rational numbers and tests their mean/variance identities. It then evaluates, using finite sums and bisection, nine deterministic critical-Zipf profiles over three population sizes and three quorum fractions. It reports the mean-root correction, the normalized discovered-mass variance, and the mean slope. There were 72 assertions in the recorded execution; all passed.

The theoretical facts needing scrutiny independently are the uniform harmonic-sum remainder, the mean-root inversion, the triangular-array Lindeberg bound, and the time-threshold inversion. The proofs and hypotheses for each appear explicitly in `RESULT.md`. The small-population calculations are neither exhaustive evidence for all \(N\) nor an independent proof of the Gaussian limit. External historical-priority assessment and independent mathematical audit are not performed.
