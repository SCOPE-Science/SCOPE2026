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

# Reproducibility and limits

The displayed proof is analytic. Finite corroboration is supplied by `check.py`, which depends only on Python 3's standard library. Execute it from the directory holding this file and the script as `python3 check.py`. The script passed 5190 deterministic assertions: 2001-point evaluations of the polynomial factorization, exhaustive pair-constraint intersection checks against the proposed finite-grid optimizer for every modulus from 9 through 60, direct grid-positivity and positive dual-weight checks for 61 through 400, and convergence checks for the two nonzero-residue asymptotic constants.

A finite grid check is not an infinite proof. The rigorous justification of the exact divisibility criterion uses an explicit globally nonnegative polynomial and its precise zero set. The eventual two-contact theorem uses strictly positive second derivatives, separation of the nonzero portion of the continuous polynomial, nonzero determinant, and positive finite-grid dual weights for sufficiently large moduli. The limiting coefficients come from a second-order Taylor expansion with uniform third-order remainder along each fixed residue class.

Independent mathematical audit: not performed. No evidence of independent validation is asserted. Potential originality overlap with unexamined finite-grid extrema remains unresolved after bounded source comparisons.
