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

# Reproducibility and limits

Run `python3 verify.py` (Python 3 standard library, no third-party dependencies) from the directory containing these files. The script constructs rank/order congruence classes, enumerates all gcd values over each candidate period, tests every proper period divisor for a discrepancy, and compares exact Möbius fractions with observed counts. It covers all 22 shifts \(a\in\{-12,\ldots,-2,2,\ldots,12\}\), and terminates with `VERIFY_OK: 22 signed shifts, complete least-period and density replay`.

The verification checks the finite test domain exactly; it is not an exhaustive proof for all shifts or indices. The general infinite claims rest instead on the matrix, divisibility, residue-period and Möbius arguments in `RESULT.md`. The available inspection included original 2018 and both relevant 2022 full texts; the 2016 Spilker chapter was assessed via its abstract and published restatements, without an accessible full text. No external independent audit or certification was performed.
