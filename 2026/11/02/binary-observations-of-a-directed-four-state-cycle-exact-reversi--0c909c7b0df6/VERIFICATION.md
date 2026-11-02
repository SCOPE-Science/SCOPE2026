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

Run `python3 verify.py` with Python 3 standard library, with the script located beside this document and `RESULT.md`. The program tests the stationary cycle from exact fractions, builds the Taylor coefficients of sixteen four-frame word probabilities, verifies all six reversed-word identities through cubic order on sixty deterministic positive-rate quadruples, and independently computes finite-time probabilities using Poisson uniformization. It reports 1036 passing deterministic assertions.

These finite parameter tests are regression evidence, **not** exhaustive proofs for arbitrary positive real rates. The analytic proof of the reflection classification, the cubic leading coefficient and the KL remainder appears in `RESULT.md`. The reported likelihood information uses natural logarithms and the stationary four-snapshot joint law; it is neither an infinite-time entropy rate nor the microscopic thermodynamic dissipation. Independent audit has not been performed.
