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

# Analytic and computational checks

Run `python3 check_entropy_series.py` using Python 3 (standard library only). The program creates local directed-neighbor weights with exact `fractions.Fraction` coefficients in the asymmetry variable, computes off-diagonal stationary pair-correlation Taylor coefficients as common-input path sums, computes the zero-coupling cubic contractions, and independently reconstructs the resulting entropy-production coefficients. The current execution passed 207 exact assertions for every integer circumference from 3 through 25, including both the four-periodic exception and several rational values outside the physical parameter interval as an additional algebraic cross-check.

The analytic proof, not these finite checks, establishes that no new two-step wrapping types occur beyond circumference four. Finite-state stationary transition-matrix calculations for the 3-by-3 lattice were separately performed at coupling strengths 0.08, 0.04, and 0.02 and three asymmetry values, with sixth-order-scaled deviations remaining bounded. The numerical experiment is corroborative and not part of the proof of any universal statement. The expansion does not control convergence uniformly in volume or near criticality.
