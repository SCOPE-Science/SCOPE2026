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

The result follows analytically from the circular arc-gap bijection and binomial mixing. The independent `checker.py` enumerates all Bernoulli-relocation patterns and all possible uniform destinations for cycle sizes 2 through 7, checks conditional non-repetition probabilities exactly, and separately compares the closed formula against a rational-state dynamic program. Further exact checks cover normalization of the first-repeat distribution and monotonicity in relocation probability on a rational grid.

The checker was run in Python 3 and returned `PASS: 438 exact comparisons`. Its output is finite test evidence, not a proof of the asymptotic assertions. For the latter, tight Poisson relocation counts give the finite-frequency limit; concentration and a uniform logarithmic expansion give the many-relocation limit. No independent mathematical audit has been performed.

Reproduction: extract `checker.py` alongside this document and execute `python3 checker.py`.
