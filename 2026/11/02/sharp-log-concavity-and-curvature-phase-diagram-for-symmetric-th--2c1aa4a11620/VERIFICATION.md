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

# Reproducibility and verification scope

The included `verification.py` is a standalone Python program using SymPy and mpmath. Running `python verification.py` on the packaged file reproduces `verification_output.txt` (283 passing symbolic and finite numerical checks). Tests include the exact derivative factorization, both global optimizer formulas, equality of curvature branches at the transition, principal Lambert-boundary identities for twelve weight ratios, exact branch-range checks, strictly positive and negative perturbations about the threshold, attainment of calculated curvature maxima at 180 sampled parameter pairs, and the unimodal/non-log-concave witness. All symbolic identities are verified algebraically; decimal comparisons and finite parameter grids serve only as corroboration.

The proof in `RESULT.md` establishes the exact one-dimensional and finite-dimensional statements directly. The checker is not an exhaustive parameter search and does not replace analytic proofs of unique phase transitions or monotonicity. External independent mathematical audit and historical-priority evaluation have not been performed.
