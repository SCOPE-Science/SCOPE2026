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

# Verification and boundaries

The entire infinite proof is contained in `RESULT.md`, based on the verified coefficient identity in Rogers's Theorem 3.1, Equation (3.4), and the elementary binary form of Legendre's formula.

Execute `python3 verify.py` with Python 3.8+ and no external packages. This independently evaluates 80 complete Domb coefficients from both summation formulas, 9 Mersenne-index Domb terms, and 2,044 Rogers summands at precisions \(3\le r\le11\). It checks the exact digit-sum formula, reindexed summand valuations, endpoints, and uniqueness of the minimum. The observed terminal line is `VERIFY_OK identities 80 Domb Mersenne indices 9 summand comparisons 2044`.

Finite checks are not a proof for arbitrarily large indices. In particular, they do not establish complete database novelty or an unrelated statement about all indices. The exact symbolic proof handles all \(r\ge3\). The exceptional values at \(r=1,2\) are checked independently. No independent audit has been performed.
