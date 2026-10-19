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

`verify.py` is a standalone Python 3 script using only the standard library, with 85-digit `decimal.Decimal` arithmetic. Execute `python3 verify.py`. The deterministic checks cover the original Gram equations, positive side weights, the unique sign threshold at varied bandwidths, the natural scaled Gauss–Hermite radius, the auxiliary node-scaling crossover, tensor-product norm identities, and the near-coalescence asymptotic. The observed run completed 441 checks successfully.

The universality claims are **proved analytically** in `RESULT.md`: explicit three-point inversion, derivative sign for the unique boundary, two-case natural-node inequality, exact tensor norm, and formal Taylor coefficients for coalescence. Numerical samples and finite checks do not prove all-parameter assertions. The claim does not apply to the approximate Mercer weights, to Gaussian measures altered with the auxiliary scale, to an unrestricted Gauss–Hermite node count, or to RKHS worst-case errors for the normalized functional. Independent scientific audit has not been performed.
