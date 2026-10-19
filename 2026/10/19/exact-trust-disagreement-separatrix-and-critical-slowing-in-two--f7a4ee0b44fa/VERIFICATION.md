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

# Verification and boundaries

The complete proof derives the exact planar reduction, conserved \(\operatorname{artanh}(w)-F(d)\), monotone potential geometry, endpoint classification, and the critical Taylor expansion. The decisive argument is analytical; sampling the dynamics would not prove an infinite-time theorem.

Run `python verify.py` using Python 3 with the standard library only. The script checks the exact rational-kernel potential against the vector field at multiple rational states; integrates three explicit basins; checks conservation, the implicit disagreement limit, the critical asymptotic coefficients, and the exponential rates at finite large time. Reported finite-time residuals and explicit tolerances are numerical diagnostics, not independent proof.

The mathematical domain is two reciprocal agents with strictly positive initial tie, unit self weights, a smooth strictly decreasing positive kernel with a transverse half-strength crossing, and no external forcing. It excludes larger networks, nontransverse crossings, and alternate edge normalizations. No independent audit has been performed.
