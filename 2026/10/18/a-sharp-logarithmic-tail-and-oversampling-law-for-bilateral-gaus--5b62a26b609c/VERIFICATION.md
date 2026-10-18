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

# Reproduction checks and scope

The standalone script `verify.py` uses only the Python standard library, with fixed random seeds and no external data. Execute `python3 verify.py` from a directory containing that file. It checks finite-rank identities and the almost-sure weak-gap limit for six pairs of sketch dimensions, gamma-function and exact mean-square constants, and the limiting logarithmic-tail coefficient by one-dimensional quadrature. Expected output begins with `PASS: 1520 checks`.

The analysis establishing the distribution, infinite moment thresholds, and asymptotic tail coefficients is contained in `RESULT.md`. Finite checks do not verify an infinite limit, mathematical priority, or the validity of unrelated practical rank estimators. No independent audit has been performed.
