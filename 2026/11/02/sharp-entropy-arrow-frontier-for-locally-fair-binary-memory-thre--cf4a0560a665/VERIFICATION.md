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

# Verification of the stated sharp frontier

The proof uses four exact steps: the stationary three-word flow constraints and positive table parametrization; equality of the four nontrivial reversal differences; order-three path factorization; and a one-dimensional sign-definite derivative plus boundary continuity. These establish the entire infinite-parameter claim analytically.

Run `python verify.py` with Python 3 and its standard library. The checker uses a fixed seed, 32 positive exact-rational parameter systems, exact normalization and four-word flow arithmetic, independent summation of binary word probabilities up to length eight, numerical KL comparisons, five exact-rational minimizers, and a monotone sequence approaching a divergent endpoint. Its successful replay reported: `PASS 266 exact block normalization and finite-word checks; 32 rational parameter systems; sharp equality and divergence witnesses`.

The finite checks do not establish uniformity over all real parameters, prove strict positivity at singular boundaries, or certify physical heat. The main theorem is supported by the analytic calculations, and the exact marginal/conditional normalizations in the code guard against transcription and indexing errors.
