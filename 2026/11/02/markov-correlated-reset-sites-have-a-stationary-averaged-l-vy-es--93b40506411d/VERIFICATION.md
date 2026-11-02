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

The standalone `verification/markov_reset_check.py` passes 30 numerical sanity assertions for a three-state nonreversible reset-site chain: stationary weights, stable jump intensities, exact finite-state killed-generator resolvents for four scales and three Laplace arguments, first and second moments, and a distinct reset transition kernel with the same stationary law. Reproduce using `python verification/markov_reset_check.py` (NumPy required).

The executable checks the Markov-modulated **rare-jump analogue** only. It does not simulate a path of an infinite-activity Lévy process, cannot prove convergence, and does not establish publication novelty. The analytical proof of the stable result uses the marked small-time interval-exit theorem, exact self-similarity, the reset-renewal matrix, Perron stationary projection, and the exponential-moment bound described in RESULT.md.

No independent audit has been performed.
