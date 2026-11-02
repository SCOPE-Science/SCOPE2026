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

# Reproducibility

Run `python3 verify_tail_crossover.py` using Python 3 and the standard library. The delivered verifier checks the exactly derived renewal pole identities, strict growth of the reset-rate parametrization on sampled parameters, two separated asymptotic maxima, global objective dominance on broad finite grids, and the finite-separation coexistence shift. The fixed version reports 30,524 passing assertions and prints sample constants and coexistence data.

The source file is contained alongside this document and must be extracted as UTF-8 before execution. It has no third-party dependencies and does not download data. Numerical assertions are finite diagnostics and do not establish all-parameter uniqueness or large-distance asymptotic bounds. The full proof is in RESULT.md, including the key renewal theorem step and a uniform exclusion of competing intermediate scales.

# Verification state

Self-review: passed. Independent audit: not yet performed.
