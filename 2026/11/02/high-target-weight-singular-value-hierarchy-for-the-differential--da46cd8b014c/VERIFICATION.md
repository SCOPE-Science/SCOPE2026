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

# Verification

The executable `check_spectral.py` uses only Python's standard library (Python 3.9 or newer). From this directory, run `python check_spectral.py`. The verified run returned `EXACT_BERG_SPECTRAL_OK 4240`.

The program checks finite Cauchy determinants, the exact finite Cauchy--Binet identity for the lowest compound row, positivity of the associated finite moment Gram matrices, and rational monotonicity/log-convexity tests for normalized row weights. In particular, these are exact rational computations, with no tolerance-based acceptance. Additional exploratory singular-value calculations on finite matrices used numerical software, but are not required for replay or the mathematical argument.

The passage to infinite-dimensional compound operators and the sharp fixed-rank singular-value asymptotics are proved analytically in `RESULT.md`, using the cited compactness theorem, strong convergence of bounded diagonal multipliers, positivity of Cauchy minors, and Cauchy--Binet. Finite enumeration neither replaces these arguments nor establishes novelty. Independent mathematical review remains unperformed.
