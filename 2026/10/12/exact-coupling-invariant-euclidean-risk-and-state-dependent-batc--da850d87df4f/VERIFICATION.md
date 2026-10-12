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

# Reproduction and checks

The complete standalone Python 3 file `verify.py` is included in this package and uses only the standard library. Run `python3 verify.py` in the directory containing this file and the script. Expected output:

`PASS: 1024 exact rational objective/norm/optimality identities, horizons through 5 and 8`

The verifier uses `fractions.Fraction` to enumerate all nonzero-probability batch histories through five iterations for multiple rational correlation parameters, initial directions, and alternative fixed-size-two joint laws. It compares exact enumerated objective and squared-norm expectations with the formulas from `RESULT.md`. Exact endpoint inequalities and the unbounded-gap ratio formula are checked through eight iterations for additional rational correlations. The finite checks are diagnostic only: the all-horizon assertion is proved separately using the exact two-moment conditional recurrence and its closed-form solution. No theorem proving, independent validation, external certification, or infinite numerical enumeration is asserted. The scope excludes floating point errors and different update operators.
