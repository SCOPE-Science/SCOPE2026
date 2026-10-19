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

# Reproduction and limits

Run `python verify.py` under Python 3 with SymPy installed. The code checks 12,334 exact rational trajectories, symbolic generating-function normalizations and means, and finite-law Taylor coefficients. The implementation is the signed-error representation of the cited Algorithm 1 for normalized singleton coordinate sketches and its stipulated `0/0=0` convention. The mathematical proof, rather than the finite tests, establishes the statements for all sample paths, all positive-definite two-by-two normal matrices, all sampling probabilities in `(0,1)`, and unbounded stopping horizons.

No independent audit, hardware-precision certification or finite-tolerance convergence verification has been performed.
