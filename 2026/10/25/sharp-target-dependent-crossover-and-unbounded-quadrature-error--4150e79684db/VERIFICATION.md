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

The complete proof is contained in `RESULT.md`. The separate `verify.py` program reproduces the sample-set laws and their target-dependent optimal-weight RKHS squared risks using exact rational arithmetic. Execute `python3 verify.py` in the directory containing this file and `verify.py`; no third-party packages are required.

The implementation enumerates every distinct ordered pivot path and every fixed-size determinant subset for finite parameters \(2\le m\le5\), \(2\le k\le m\), and five rational contrast values, testing three rational targets per case. It additionally checks an exact two-pivot specialization and high-contrast ratios. The output observed was `VERIFY_OK: exact subset enumeration, optimal quadrature risks, crossover and high-contrast limit; 150 integrand checks`.

These tests do not certify the infinite family or asymptotic limit; the formulas and limits are established by the proof. No independent audit has been performed.
