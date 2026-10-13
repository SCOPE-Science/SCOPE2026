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

## Reproducible checks

Run `python3 checks/check_inversions.py` with the Python standard library. The script exhaustively checks the conditional inversion-count regression for each permutation with two through seven cards, and enumerates exact shuffle distributions for each deck size two through six and each step count zero through seven. At each such state it verifies the exact mean and an independently derived closed variance expression with rational arithmetic. These finite computations cross-check the sign of the increment, normalizations, and coefficients; they do not certify the infinite functional weak limit.

## Analytical basis and limits

The proof relies on the exchangeable uniform-prefix/increasing-tail decomposition, its empirical-measure weak law, explicit conditional increment-variance integral, uniformly convergent martingale predictable brackets, the standard functional martingale CLT, and an exact discrete Volterra map. These steps, not sampling or finite enumeration, cover every fixed compact time window. The independent scientific audit has not been performed and no rate of weak convergence is claimed.
