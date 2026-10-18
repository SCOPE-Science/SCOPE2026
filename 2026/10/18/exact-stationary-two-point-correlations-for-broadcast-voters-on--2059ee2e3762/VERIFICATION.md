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

# Analytical and finite verification

The infinite-state proof is the two-lineage generator/hitting-probability argument in `RESULT.md`. The key nonstandard point is the distance-two transition: direct joint coalescence has rate \(q\), and each exclusive inward move has rate \(1-q\), after normalizing total broadcast intensity. Those rates follow by applying the finite-subset generator to precisely two occupied neighboring sites of the same midpoint.

The independent exact-arithmetic program `verify.py` checks all local harmonic equations using Python `fractions.Fraction`, solves finite Dirichlet boundary-value systems by a separate tridiagonal elimination routine, and verifies the truncation inequality \(0\le h_k-h_k^{(K)}\le h_K\) as well as the classical uncoordinated limit and strict monotonicity in \(q\). Run `python verify.py`; expected output: `PASS: 2430 exact rational recurrence, finite-boundary and monotonicity checks`.

The analytical infinite-distance decay comes from gambler's ruin for an outward-drifting walk stopped at distance two. Finite truncation and sampled parameters cannot establish this limit or a literature novelty claim. No independent audit was performed.
