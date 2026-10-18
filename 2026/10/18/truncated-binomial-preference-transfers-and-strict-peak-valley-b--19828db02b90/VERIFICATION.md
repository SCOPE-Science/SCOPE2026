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

Run `python3 verify.py` in the same directory as this document. Python's standard library suffices. The script independently enumerates feasible occupancy profiles, weighted by their multinomial number of realizing preference words, through size seven. It checks the precise conditional truncation support, binomial relative weights, pairwise rearrangement inequalities, and the exact cubic occupancy statistic. It independently enumerates all preference words for sizes three through six and checks strict-peak and strict-valley frequencies against the moment identity and the independent-uniform mean. A finite dynamic program verifies exact counts and positivity through size forty.

All checks use Python arbitrary-precision integers or exact fractions, not floating-point comparisons. The combinatorial arguments in the report are required for general \(n\): no finite enumerator establishes them by itself. The Pollak cyclic-rotation correspondence is a cited classical input rather than an independently mechanized theorem. Historical priority cannot be certified by computational tests. Independent mathematical auditing has not been performed.
