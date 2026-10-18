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
# Reproducibility

Run `python verify_cactus_na.py` using the Python standard library. The included program constructs the finite random-cluster law by direct component counting, checks exact rational factorization for a two-cycle cactus (two triangles sharing a vertex and one bridge), checks discrete monotone observables and the predicted rank-one covariance, and enumerates monotone Boolean tests on a four-edge cycle.

Observed output in the current analysis: `PASS: 33908 exact rational assertions for two-cycle cactus and rank-one covariance`.

The calculation is a finite consistency check, not an exhaustive proof for all graphs, sizes, edge weights, external fields, or pinning patterns. Those are treated by the algebraic block decomposition and covariance identity in `RESULT.md`. In the strong-Rayleigh comparison, the upper-half-plane zero is an explicit symbolic witness, not a floating-point inference. Independent mathematical validation was not performed.
