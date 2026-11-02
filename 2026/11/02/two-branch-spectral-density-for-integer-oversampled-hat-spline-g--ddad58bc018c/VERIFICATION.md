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
# Reproducibility and verification

`verify.py` uses only the Python standard library. Execute `python3 verify.py` alongside this package. The completed run printed `PASS: 4068 exact/algebraic and numerical checks`.

Exact rational arithmetic checks the quadratic overlap formula and the partition identity on numerous test cells for \(1\le q\le20\). Numerical integration checks density normalization and its two moments for \(q\in\{2,3,4,5,8,16,32\}\), with changes of variables resolving the square-root boundary behavior. Sample symbol and continuity values are checked. All identities for infinitely many parameters and the spectral-type assertion require the derivation in `RESULT.md`; finite checking alone does not establish them.

The source review examined the accessible 2018, 2023 and 2026 mathematical material described in `RESULT.md`. The full September 2026 Zak-zero manuscript could not be read, so its abstract-only comparison does not justify a strong noncoverage claim. Independent audit is unperformed.
