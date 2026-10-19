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

# Verification and reproducibility

Run `python3 verify_correlation.py` using standard Python. The script checks exact rational equality for the first 25 covariance coefficients computed by two constructions: (i) the algebraic Green-function power series and (ii) a reflected-walk binomial sum, including its infinite-level geometric tail evaluated symbolically. It also checks representative asymptotic magnitudes for both parities at lags 300, 301, 800, 801. These finite checks support identities and constants, not the infinite-time theorem.

The proof of the infinite assertion is in RESULT.md, specifically the exact reduced transfer on the central coordinate, the binary Rademacher action, a summable resolvent recurrence with a killed boundary, and singularity transfer at both points on the unit circle. Boundary points of the affine map have no effect on Lebesgue correlations.

The structural input P0 and the equality of physical central-only correlations with reduced-operator correlations come from Takahasi--Tsujii, arXiv:2408.16618v1, Sections 2.3 and 3.5. No independent mathematical audit has been carried out.
