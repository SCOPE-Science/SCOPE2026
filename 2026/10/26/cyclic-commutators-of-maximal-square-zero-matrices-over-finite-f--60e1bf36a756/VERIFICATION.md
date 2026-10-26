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

# Verification record

The exact mathematical claim, including its finite distribution and limiting probability, is proved in `RESULT.md`. The key external finite-field cycle-index identity is traceable to Fulman's general-linear conjugacy calculation (pp. 54–57). The opposite-polynomial factorization and character-Euler simplification are derived explicitly in the proof, with the nonzero-constant convention essential in both identities.

`checker.py` is a standalone Python 3 standard-library program. Running `python3 checker.py` exhaustively verifies nine general-linear prime-field configurations, comparing cyclicity of block commutators by span of matrix powers against independently calculated rational coefficients. It also enumerates three small square-zero pair families and tests invertibility directly. Its output is saved verbatim as `checker_output.txt`. Total tested general-linear matrices: 13,957; square-zero ordered pairs: 44,173. Tested finite data do not constitute proof for all field extensions or all dimensions.

Analytical boundaries: fixed field order, square-zero factors of exactly half ambient rank, and the condition of commutator invertibility. For the convergence of the conditional probability, the cycle-index quotient is analytic on a disk of radius greater than one, and a standard Cauchy coefficient bound supplies an exponentially decreasing error with no claimed uniform rate as the field order varies.
