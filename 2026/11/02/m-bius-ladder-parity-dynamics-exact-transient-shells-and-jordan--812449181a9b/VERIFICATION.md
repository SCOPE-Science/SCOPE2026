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

The standalone standard-library Python script `verify_mobius_xor.py` was executed and produced `verification_output.txt`. It builds direct finite graph updates and checks matrix ranks of powers against the predicted nilpotent kernel dimensions, independently compares fixed-state ranks against binary polynomial-gcd computations, and separately checks the twisted-versus-untwisted prism dimensions. An exhaustive functional-graph analysis computes first-periodic-entry times for every labelled binary configuration on Möbius ladders with half-lengths 3 through 8.

Observed checks: 1,115 matrix-kernel and polynomial-gcd cases, 429 prism comparison matrix cases, and 87,360 complete labelled-state classifications. The executable has no external dependencies. Results are numerical checks of finitely many instances; the general formulas are justified by the polynomial factorization and local Jordan arguments in `RESULT.md`. No external or independent scientific review has been conducted.
