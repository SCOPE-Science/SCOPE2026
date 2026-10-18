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

# Reproducibility and evidence

Use Python 3.9 or later and run `python3 verification/circular_universality_check.py` from the package root. No third-party library or external data is required. The program directly enumerates all binary words of length \(1\) through \(16\); for each word, it independently evaluates the maximum linear arch count over all rotations, checks the cyclic transition-run condition, counts maximizing rotation classes, confirms the formula for labeled words, checks odd primitive maximizers, and compares the fixed-origin optimal count. It also checks 6,400 deterministic pseudorandom words at lengths \(17\)–\(80\). The actual run completed successfully and printed `ALL CHECKS PASSED`.

The all-length theorem is proved by an odd-cycle maximum-matching decomposition and a bijective rooted-run counting argument in RESULT.md. Finite enumeration cannot prove those general claims and was not used for that purpose. The 2021 circular-universality remainder paper's complete text was inaccessible, so its exact coverage is not certified. The mathematical review is same-model only; independent audit and validation are not performed.
