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

# Verification and limitations

The analytical certificate is the six-step proof in `RESULT.md`: mass conservation, direct interval solution, exact decomposition of order dependence, strict cumulative-hazard comparisons, two signed threshold-gap identities, and the two-stage minimality calculation. It covers the continuous positive parameter domain and both equality boundaries. No computational enumeration is claimed to prove the continuum theorem.

The self-contained Python 3 standard-library checker `verify.py` computes all six stagewise solutions directly and reconstructs the simplified permutation score independently for 2,200 deterministic parameter choices. It also checks exact rational values at and across both sharp loading thresholds. Running `python verify.py` from the extracted package prints `VERIFY_OK assertions=22058`. The exact illustrative rates, \(h=\log2\), and sample masses are specified in `RESULT.md`.

These tests verify only the simple linear, single-stock, equal-stage-duration model and the explicitly defined integrated accumulating-pool mass proxy. They do not establish empirical stormwater suitability, correctness of unknown external documents, historical uniqueness, or a third-party audit. Full historical priority remains subject to independent literature review.
