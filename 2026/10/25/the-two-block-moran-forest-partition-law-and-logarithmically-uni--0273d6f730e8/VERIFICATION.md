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

# Reproducibility of the two-component Moran-forest law

Run `python verify.py` with Python 3. The script uses only standard-library integer arithmetic, `fractions.Fraction`, and exhaustive enumeration of each independent mother-choice vector. It checks the full two-component size-frequency law for \(n=3,4,5,6,7\), meaning respectively \(8,81,1024,15625,279936\) equiprobable vectors, and verifies the closed normalization in exact rational arithmetic through \(n=100\).

Expected successful ending: `EXACT_NORMALIZATION_PASS n=3..100` followed by `VERIFY_OK`.

Analytical boundaries: Enumeration through order seven does not prove unrestricted correctness; the all-order identity follows from blockwise parent counting and averaging interleavings. The conditional weak limit follows from the uniform asymptotic comparison of the exact weights with harmonic weights. No external independent audit has been performed.
