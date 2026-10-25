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

# Reproducibility and scope of checks

`CHECK.py` uses only the Python standard library. Run `python3 CHECK.py` from the directory containing that source. It verifies four exact integer-exponent first-age-moment beta normalizations, four transformed numerical quadrature values at a selected small positive speed, and four comparisons with the three predicted asymptotic regimes. The exact output is captured in `CHECK_OUTPUT.txt`.

The quadrature is a transformed finite Simpson rule, not an exhaustive or interval-arithmetic certificate. The global uniqueness of speeds, necessary-and-sufficient third-moment criterion, all fractional and critical limits, and all general-parameter statements are established by the analytical proof in `RESULT.md`, not by extrapolating finite diagnostics.

The theorem assumes fixed nonnegative age weights with finite first moment and a Gaussian spatial imprint. It does not verify stability of translating states, global solutions from arbitrary pasts, or historical uniqueness. Independent mathematical or bibliographic assessment has not been performed.
