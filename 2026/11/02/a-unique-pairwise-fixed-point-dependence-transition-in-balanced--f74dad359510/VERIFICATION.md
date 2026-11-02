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

Run `python3 verify.py` with Python 3 (standard library only), after extracting the file alongside this document. The executed verifier reported `passed 633 exact-integer/rational assertions`.

The verifier exhaustively enumerates all permutations at balanced block sizes 2, 3, and 4. It checks the exact number of permutations in each block-count class, one- and two-tag conditional probabilities, and the unconditional rational covariance at five rational bias parameters. It separately checks the transformed Legendre recurrence through size 18, endpoint polynomial coefficients and signs through size 17, and exact rational sign brackets for thresholds through size 13.

The general proof for every integer block size at least two and every strictly positive bias is analytic: conditional combinatorial enumeration, Legendre orthogonality and root monotonicity, and a parameter-uniform Gaussian Laplace expansion of a closed integral. Finite enumeration does not establish the infinite theorem. The transition at the critical parameter is defined implicitly for block sizes greater than two; no unsupported exact elementary expression is claimed.

Scientific literature comparisons include Ottolini--Starr (arXiv:2605.25274), Duan--Lyu--Powell (arXiv:2610.14616), Johnson--Leader--Long (arXiv:1909.03770) and the classical Fisher noncentral hypergeometric mass law. Definitive historical-priority assessment has not been performed. Independent audit status is not performed.
