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

Analytic proof ingredients: eigenvalue simplicity for irreducible symmetric tridiagonal paths; reflection parity continuity; tensor-product rung spectrum; two-input PBH rank evaluation at simple and double eigenvalues; disjointness of exact gap sets for unit paths with two through five rungs and simultaneous even/odd gaps at six rungs. None of these general steps relies on finite experiments.

Run the included `verify.py` with Python 3 and SymPy. It independently computes controllable ranks by translated characteristic-polynomial gcds and by full Kalman matrices, and checks exact small-path gap sets. Replaying the included source produced: `PASS: 42 exact-rational predicted-versus-Kalman rank comparisons; four boundary assertions; five exhaustive exact small-path gap-set checks.`

These computations are exhaustive only for the explicitly stated finite check ranges; the proof provides the arbitrary-dimensional conclusion. Uninspected specialized historical literature remains a possible originality limitation. No independent mathematical audit has been performed.
