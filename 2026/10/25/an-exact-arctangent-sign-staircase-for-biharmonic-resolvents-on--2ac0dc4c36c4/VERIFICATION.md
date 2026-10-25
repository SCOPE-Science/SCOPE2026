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
# Verification record
The standalone `check.py` requires Python 3, NumPy and SciPy; run `python check.py`. It reconstructs \((I+tL_d^2)^{-1}\) from adjacency for dimensions two through six, compares the antipodal entry with the exact binomial spectral sum and phase product for rational parameters, checks all predicted phase roots and neighboring signs through dimension eighty, and inspects the asymptotic error scale. In the recorded run, **5,099 assertions passed**.

Finite enumeration and numerical root solving are only corroborative. The complete proof uses exact partial fractions and monotone phase geometry and does not depend on numerical accuracy. The matrix positivity of non-antipodal entries is not asserted or tested as a theorem. Independent external audit has not been performed.
