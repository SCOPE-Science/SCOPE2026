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
Run `python3 verify.py` using Python 3 with no third-party packages. It checks all generated patterns with concrete nonnegative-start, positive-step arithmetic progressions for lengths 1 through 40, including the high-exponent witnesses. It compares the language against every tested small arithmetic progression at lengths through 17 and deterministic large-progression samples at lengths 19, 24, 31 and 40. It independently checks the output cardinality bounds and selected histograms. A finite test alone cannot certify all lengths or exclude all equivalent publications; those are addressed by proof and scholarly comparison.
