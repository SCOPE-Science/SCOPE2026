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
# Verification

The theorem is proved analytically by bounded permutation-sign prefixes, discrete summation by parts, telescoping total variation, and an absolutely convergent Rademacher series. `verify.py` independently computes exact rational finite identities for small sign patterns, simulates sample permutation histories within the quadratic sign cell, and checks the harmonic identities numerically. No finite computation is presented as proof of infinite-time convergence or global literature uniqueness.

The main mathematical assumptions are componentwise sign constancy on an open neighborhood, zero sum of component sign vectors, a globally nonincreasing positive vanishing step sequence, and a ball-containment condition. For the strongly convex witness, the full gradient at every limit point is at least one in magnitude. For the random law, epoch shuffles must be independent and uniform. External audit and independent validation have not been performed.
