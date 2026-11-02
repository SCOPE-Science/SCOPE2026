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

`RESULT.md` provides exact assumptions, a complete determinant-based threshold proof, the Markov match-process argument, and an exact positive-vector growth certificate. `check.py` requires only Python 3 standard-library `fractions` and can be run in the directory containing the files with `python3 check.py`.

The checker recomputes the exact two environmental matrices, four weighted matrix products, endpoint threshold fractions, and the growth-certificate product. It also verifies the determinant formulas on 77 rational triples. These tests independently detect arithmetic transcription errors but are not substitutes for the algebraic identities or infinite-time ergodic argument.

The random environment is specified by independent Bernoulli switch indicators, so the strong law applies to their frequency. In the two edge cases, an ergodic two-state chain supplies exact time averages of local multipliers. No simulation, finite enumeration or log output is presented as proof of those conclusions. Full historical priority remains subject to outside examination; no independent verification has been performed.
