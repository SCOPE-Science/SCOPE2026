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

# Reproducibility and verification

Run `python3 CHECK.py`. It uses Python's standard library only, with a fixed pseudorandom seed. The checker evaluates the stated closed forms for seven deposition parameters, verifies nonnegativity and normalization of all nine ordered-pair outcomes, verifies the one-site marginals and cavity total-density identity, and evaluates the strict covariance signs. It independently simulates direct sequential deposition on a 96-site periodic ring in 12,000 independent realizations per parameter pair. It also exhaustively enumerates all arrival permutations and species assignments on periodic rings with five, six, and seven sites, comparing their local probabilities against the infinite-line law with explicit tolerances. Those finite-size comparisons test limiting consistency; the random seed and deterministic code are included for replay.

Recorded output from the packaged checker is stored as `CHECK_OUTPUT.txt`; it reports 147 passed assertions and the maximum absolute pair-probability discrepancies for each test.

The analytic proof, including the existence of the infinite-volume process, the half-line cavity equations, joint accepted-pair factorization, all nine probabilities, and the strict covariance signs, appears in `RESULT.md`. Simulations and finite-volume enumeration do not establish infinite-volume results or scholarly priority. Independent audit is not performed.
