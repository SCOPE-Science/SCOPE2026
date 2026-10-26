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
# Verification notes

Run `python3 verify.py` with a Python 3 standard-library interpreter in the directory containing this note and the verifier. The checker exhaustively enumerates all \(46{,}232\) permutations for \(2\le n\le8\), evaluates increasing subsequences through a dynamic recursion (without using the analytic hypergeometric proof), and checks exact local and global covariance formulas using `fractions.Fraction`. It also evaluates \(2{,}814\) comparison assertions including larger \(n\le35\) and beta-integral coefficients. Expected output: `PASS: 2814 exact comparisons, 46232 complete permutations, n=2..8 exhaustive; n<=35 symbolic identities.`

Finite enumerations test the formulas only on their stated ranges. The general covariance identity is proved by conditional image-set counting; the asymptotic formula is proved by a uniform fixed-length rank limit and a beta-integral evaluation. No automated proof assistant or independent audit is claimed.
